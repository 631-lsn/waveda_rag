from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from raggg.indexing.embeddings import tokenize
from raggg.indexing.vector_store import VectorStore
from raggg.models import Chunk


WAVEDA_TERMS = {"waveda", "端口", "边界", "pml", "网格", "仿真", "菜单", "设置", "波端口", "集总端口"}
FORMULA_TERMS = {"公式", "方程", "maxwell", "麦克斯韦", "推导", "积分", "微分", "边界条件"}
DEFINITION_TERMS = {"什么是", "是什么", "定义"}
GENERIC_TITLES = {
    "设置",
    "设计设置",
    "建模",
    "工具",
    "选项",
    "视图",
    "文件",
    "仿真",
    "电磁结果",
}


@dataclass(frozen=True)
class SearchResult:
    chunk: Chunk
    score: float
    vector_score: float
    lexical_score: float


def _lexical_overlap(query_tokens: set[str], content: str) -> float:
    if not query_tokens:
        return 0.0
    content_tokens = set(tokenize(content))
    if not content_tokens:
        return 0.0
    return len(query_tokens & content_tokens) / len(query_tokens)


class Retriever:
    def __init__(self, store: VectorStore) -> None:
        self.store = store

    def search(self, query: str, top_k: int = 6) -> list[SearchResult]:
        if not self.store.chunks:
            return []
        query_vector = self.store.embedding_model.embed_text(query)
        vector_scores = self.store.vectors @ query_vector
        query_tokens = set(tokenize(query))
        query_lower = query.lower()

        results: list[SearchResult] = []
        for index, chunk in enumerate(self.store.chunks):
            vector_score = float(vector_scores[index]) if len(vector_scores) else 0.0
            lexical_score = _lexical_overlap(query_tokens, f"{chunk.title} {chunk.section} {chunk.content}")
            score = 0.65 * vector_score + 0.35 * lexical_score

            # 优先级加权 (1-5, 默认3) — 高优先级文档获得额外得分
            priority = int(chunk.metadata.get("priority", 3))
            score *= 0.9 + 0.07 * priority  # priority=3 → 1.11x, priority=5 → 1.25x

            chunk_text_lower = f"{chunk.title} {chunk.section} {chunk.content}".lower()
            is_helpful = chunk.source_type in ("waveda_help", "user_tutorial")
            if is_helpful and any(term in query_lower for term in WAVEDA_TERMS):
                score += 0.08
            compact_query = query_lower.replace(" ", "").replace("？", "").replace("?", "")
            compact_title = chunk.title.lower().replace(" ", "")
            if (
                is_helpful
                and len(compact_title) >= 2
                and compact_title not in GENERIC_TITLES
                and compact_title in compact_query
            ):
                score += 0.85
            matched_special_terms = [
                term
                for term in WAVEDA_TERMS | FORMULA_TERMS
                if term in query_lower and term in chunk_text_lower
            ]
            score += 0.14 * len(matched_special_terms)
            if "pml" in query_lower and "pml" in chunk_text_lower:
                score += 0.3
            if "吸收边界" in query_lower and "吸收边界" in chunk_text_lower:
                score += 0.25
            if any(term in query_lower for term in DEFINITION_TERMS):
                if "是什么" in compact_title or compact_title in compact_query or compact_query in compact_title:
                    score += 0.45
            if chunk.metadata.get("has_formula") and any(term in query_lower for term in FORMULA_TERMS):
                score += 0.5
            if chunk.source_type == "obsidian_note" and any(term in query_lower for term in FORMULA_TERMS):
                score += 0.08

            results.append(
                SearchResult(
                    chunk=chunk,
                    score=score,
                    vector_score=vector_score,
                    lexical_score=lexical_score,
                )
            )

        results.sort(key=lambda item: item.score, reverse=True)
        return results[:top_k]
