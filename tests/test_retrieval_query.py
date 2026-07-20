import unittest

from raggg.pipeline.rag_pipeline import RAGPipeline
from raggg.retrieval.retriever import SearchResult


def make_result(bm25_raw: float) -> SearchResult:
    return SearchResult(
        chunk=None,  # 过滤逻辑只看 bm25_raw，不触碰 chunk
        score=1.0,
        vector_score=0.5,
        lexical_score=0.5,
        bm25_raw=bm25_raw,
    )


class BuildRetrievalQueryTests(unittest.TestCase):
    """A5：只有追问才拼接历史，独立问题不被历史污染。"""

    def test_standalone_question_ignores_history(self) -> None:
        history = [("怎么设置波端口？", "……"), ("PML 边界怎么配？", "……")]
        query = RAGPipeline._build_retrieval_query("怎么创建一个棱柱？", history)
        self.assertEqual(query, "怎么创建一个棱柱？")

    def test_followup_includes_previous_question(self) -> None:
        history = [("怎么设置波端口？", "……")]
        query = RAGPipeline._build_retrieval_query("那这个和集总端口有什么区别？", history)
        self.assertEqual(query, "怎么设置波端口？\n那这个和集总端口有什么区别？")

    def test_very_short_followup_includes_previous_question(self) -> None:
        history = [("怎么设置波端口？", "……")]
        query = RAGPipeline._build_retrieval_query("为什么？", history)
        self.assertEqual(query, "怎么设置波端口？\n为什么？")

    def test_empty_history_returns_question(self) -> None:
        query = RAGPipeline._build_retrieval_query("那怎么办？", [])
        self.assertEqual(query, "那怎么办？")


class Bm25FloorFilterTests(unittest.TestCase):
    """A6：BM25 原始分门槛过滤不可靠命中。"""

    def test_below_floor_are_dropped(self) -> None:
        sources = [make_result(35.0), make_result(8.0), make_result(22.0)]
        kept = RAGPipeline._filter_by_bm25_floor(sources, 20.0)
        self.assertEqual([s.bm25_raw for s in kept], [35.0, 22.0])

    def test_zero_floor_disables_filter(self) -> None:
        sources = [make_result(0.0), make_result(1.0)]
        kept = RAGPipeline._filter_by_bm25_floor(sources, 0.0)
        self.assertEqual(len(kept), 2)

    def test_all_below_floor_returns_empty(self) -> None:
        sources = [make_result(3.0), make_result(1.5)]
        kept = RAGPipeline._filter_by_bm25_floor(sources, 20.0)
        self.assertEqual(kept, [])


if __name__ == "__main__":
    unittest.main()
