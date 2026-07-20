from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from raggg.config import Settings
from raggg.generation.llm_client import (
    LLMAuthError,
    LLMConnectionError,
    LLMRateLimitError,
    LLMServerError,
    LLMTimeoutError,
    OpenAICompatibleClient,
)
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
        on_chunk: Callable[[str], None] | None = None,
    ) -> RAGAnswer:
        history = conversation_history or []
        sources = self.retriever.search(self._build_retrieval_query(question, history), top_k=top_k)
        prompt = build_prompt(question, sources, conversation_history=history)
        warning = None
        if self.client.is_configured:
            if on_chunk is not None:
                answer, warning = self._complete_streaming(prompt, question, sources, on_chunk)
            else:
                try:
                    answer = self.client.complete(prompt)
                except Exception as exc:
                    answer = build_local_answer(question, sources)
                    warning = self._friendly_llm_warning(exc)
        else:
            answer = build_local_answer(question, sources)
            if on_chunk is not None:
                on_chunk(answer)
        return RAGAnswer(question=question, answer=answer, sources=sources, warning=warning)

    def _complete_streaming(
        self,
        prompt: str,
        question: str,
        sources: list[SearchResult],
        on_chunk: Callable[[str], None],
    ) -> tuple[str, str | None]:
        parts: list[str] = []
        try:
            for chunk in self.client.complete_stream(prompt):
                parts.append(chunk)
                on_chunk(chunk)
            if not parts:
                raise RuntimeError("The model returned an empty streaming response.")
            return "".join(parts), None
        except RuntimeError as stream_error:
            if parts:
                return "".join(parts), self._friendly_llm_warning(stream_error)

            try:
                answer = self.client.complete(prompt)
                on_chunk(answer)
                return answer, None
            except Exception as fallback_error:
                answer = build_local_answer(question, sources)
                on_chunk(answer)
                return answer, self._friendly_llm_warning(fallback_error)

    @staticmethod
    def _build_retrieval_query(question: str, conversation_history: ConversationHistory) -> str:
        recent_questions = [item[0] for item in conversation_history[-3:] if item[0].strip()]
        if not recent_questions:
            return question
        return "\n".join([*recent_questions, question])

    @staticmethod
    def _friendly_llm_warning(error: Exception) -> str:
        if isinstance(error, LLMAuthError):
            return get_text("error_llm_auth")
        if isinstance(error, LLMRateLimitError):
            return get_text("error_llm_rate_limit")
        if isinstance(error, LLMServerError):
            return get_text("error_llm_server")
        if isinstance(error, LLMTimeoutError):
            return get_text("error_llm_timeout")
        if isinstance(error, LLMConnectionError):
            return get_text("error_llm_connection")
        return get_text("error_llm_unavailable")
