from __future__ import annotations

from dataclasses import dataclass

from raggg.config import Settings
from raggg.generation.llm_client import OpenAICompatibleClient
from raggg.generation.prompt_builder import build_local_answer, build_prompt
from raggg.i18n import get_text
from raggg.indexing.vector_store import VectorStore
from raggg.retrieval.retriever import Retriever, SearchResult

ConversationHistory = list[tuple[str, str]]


@dataclass(frozen=True)
class RAGAnswer:
    question: str
    answer: str
    sources: list[SearchResult]
    warning: str | None = None


class RAGPipeline:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.store = VectorStore.load(settings.data_dir / "index")
        self.retriever = Retriever(self.store)
        self.client = OpenAICompatibleClient(
            settings.llm_base_url,
            settings.llm_api_key,
            settings.llm_model,
        )

    def ask(
        self,
        question: str,
        top_k: int = 6,
        conversation_history: ConversationHistory | None = None,
    ) -> RAGAnswer:
        history = conversation_history or []
        sources = self.retriever.search(self._build_retrieval_query(question, history), top_k=top_k)
        prompt = build_prompt(question, sources, conversation_history=history)
        warning = None
        if self.client.is_configured:
            try:
                answer = self.client.complete(prompt)
            except RuntimeError as exc:
                answer = build_local_answer(question, sources)
                warning = self._friendly_llm_warning(str(exc))
        else:
            answer = build_local_answer(question, sources)
        return RAGAnswer(question=question, answer=answer, sources=sources, warning=warning)

    @staticmethod
    def _build_retrieval_query(question: str, conversation_history: ConversationHistory) -> str:
        recent_questions = [item[0] for item in conversation_history[-3:] if item[0].strip()]
        if not recent_questions:
            return question
        return "\n".join([*recent_questions, question])

    @staticmethod
    def _friendly_llm_warning(error_message: str) -> str:
        if "401" in error_message or "Authorization" in error_message:
            return get_text("error_llm_auth")
        return get_text("error_llm_unavailable")
