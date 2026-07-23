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
from raggg.indexing.semantic_embeddings import create_embedding_model
from raggg.indexing.vector_store import VectorStore
from raggg.retrieval.retriever import Retriever, SearchResult

ConversationHistory = list[tuple[str, str]]

# 追问信号：指代词/承上启下的说法。命中才认为当前问题依赖上文（A5）
FOLLOWUP_HINTS = (
    "这个",
    "这种",
    "这里",
    "这次",
    "这样",
    "那个",
    "那种",
    "那里",
    "上面",
    "刚才",
    "接着",
    "继续",
    "还有",
    "它",
)


@dataclass(frozen=True)
class RAGAnswer:
    question: str
    answer: str
    sources: list[SearchResult]
    warning: str | None = None


class RAGPipeline:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.store = VectorStore.load(
            settings.data_dir / "index",
            embedding_model=create_embedding_model(settings.embedding_model),
        )
        self.retriever = Retriever(self.store)
        self.client = OpenAICompatibleClient(
            settings.llm_base_url,
            settings.llm_api_key,
            settings.llm_model,
        )

    def ask(
        self,
        question: str,
        top_k: int = 8,
        conversation_history: ConversationHistory | None = None,
        on_chunk: Callable[[str], None] | None = None,
    ) -> RAGAnswer:
        history = conversation_history or []
        sources = self.retriever.search(self._build_retrieval_query(question, history), top_k=top_k)
        sources = self._filter_by_bm25_floor(sources, self.settings.retrieval_min_score)
        if not sources:
            # A6：检索无可靠命中时明说"没找到"，不让 LLM 凭参数知识编造答案
            answer = build_local_answer(question, sources)
            if on_chunk is not None:
                on_chunk(answer)
            return RAGAnswer(question=question, answer=answer, sources=sources)
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
    def _filter_by_bm25_floor(
        sources: list[SearchResult], min_score: float
    ) -> list[SearchResult]:
        """A6 分数门槛：按 BM25 原始分过滤不可靠命中。

        混合分/min-max 归一化分会被"每查询必有最优文档"的地板效应抬高，
        只有 BM25 原始分（稀有词 IDF 求和）能区分"真命中"和"词表完全不沾边"。
        阈值标定（2026-07，41+3 题）：in-scope 最低 34.8，out-of-scope 最高 33.5，
        默认取保守值 20——只拦最明显的无关问题，real 问题留足 40% 余量。
        """
        if min_score <= 0:
            return sources
        return [s for s in sources if s.bm25_raw >= min_score]

    @staticmethod
    def _build_retrieval_query(question: str, conversation_history: ConversationHistory) -> str:
        # 只有追问（指代上文或极短）才带上一条问题一起检索；
        # 否则历史问题会污染检索向量，把新话题带偏（A5）
        if not conversation_history:
            return question
        stripped = question.strip()
        is_followup = len(stripped) <= 6 or any(
            hint in stripped for hint in FOLLOWUP_HINTS
        )
        if not is_followup:
            return question
        previous = next(
            (q for q, _answer in reversed(conversation_history) if q.strip()), ""
        )
        return f"{previous}\n{question}" if previous else question

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
