from pathlib import Path
import unittest

from raggg.indexing.vector_store import VectorStore
from raggg.models import Chunk
from raggg.retrieval.retriever import Retriever


def make_chunk(index: int, relative_path: str) -> Chunk:
    return Chunk(
        id=str(index),
        source_type="obsidian_note",
        source_path=str(Path(relative_path)),
        relative_path=relative_path,
        title="波端口",
        section=f"设置 {index}",
        content="波端口 设置 方向",
        metadata={"priority": 4},
    )


class RetrieverQualityTests(unittest.TestCase):
    def test_reordered_mixed_language_query_keeps_same_lexical_coverage(self) -> None:
        chunks = [
            Chunk(
                id="export",
                source_type="waveda_help",
                source_path="faq.md",
                relative_path="faq.md",
                title="WavEDA FAQ",
                section="S 参数怎么导出？",
                content="生成端口结果后，可以右键数据图导出 txt 或 csv 文件。",
                metadata={"priority": 4},
            )
        ]
        retriever = Retriever(VectorStore.from_chunks(chunks))

        forward = retriever.search("S参数如何导出", top_k=1)[0]
        reversed_query = retriever.search("如何导出S参数", top_k=1)[0]

        self.assertEqual(forward.chunk.id, "export")
        self.assertEqual(reversed_query.chunk.id, "export")
        self.assertAlmostEqual(forward.lexical_score, reversed_query.lexical_score)

    def test_limits_repeated_chunks_from_the_same_document(self) -> None:
        chunks = [
            make_chunk(1, "manual.md"),
            make_chunk(2, "manual.md"),
            make_chunk(3, "manual.md"),
            make_chunk(4, "tutorial.md"),
        ]
        retriever = Retriever(VectorStore.from_chunks(chunks))

        results = retriever.search("波端口怎么设置方向", top_k=3)
        paths = [result.chunk.relative_path for result in results]

        self.assertEqual(paths.count("manual.md"), 2)
        self.assertIn("tutorial.md", paths)


if __name__ == "__main__":
    unittest.main()
