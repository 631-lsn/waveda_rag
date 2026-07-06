from __future__ import annotations

from dataclasses import dataclass

from raggg.config import Settings
from raggg.generation.llm_client import OpenAICompatibleClient
from raggg.generation.prompt_builder import build_local_answer, build_prompt
from raggg.indexing.vector_store import VectorStore
from raggg.retrieval.retriever import Retriever, SearchResult


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

    def ask(self, question: str, top_k: int = 6) -> RAGAnswer:
        sources = self.retriever.search(question, top_k=top_k)
        prompt = build_prompt(question, sources)
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
    def _friendly_llm_warning(error_message: str) -> str:
        if "401" in error_message or "Authorization" in error_message:
            return "模型暂不可用：API 认证失败，已使用本地知识库回答。请检查 DeepSeek API key。"
        return "模型暂不可用，已使用本地知识库回答。"
