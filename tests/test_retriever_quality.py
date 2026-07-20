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

    def test_bm25_prefers_rare_term_match(self) -> None:
        """A4：BM25 的 IDF 应让稀有词命中的文档排在泛用词命中之前。"""
        common_doc = Chunk(
            id="c1",
            source_type="obsidian_note",
            source_path="common.md",
            relative_path="common.md",
            title="仿真",
            section="仿真",
            content="仿真 " * 200,
            metadata={},
        )
        rare_doc = Chunk(
            id="c2",
            source_type="obsidian_note",
            source_path="rare.md",
            relative_path="rare.md",
            title="色散",
            section="色散",
            content="磁色散 材料 设置",
            metadata={},
        )
        # 语料里塞满“仿真”，让“仿真”成为泛用词、“磁色散”保持稀有
        filler = [
            Chunk(
                id=f"f{index}",
                source_type="obsidian_note",
                source_path=f"filler{index}.md",
                relative_path=f"filler{index}.md",
                title="仿真",
                section="仿真",
                content="仿真 仿真 仿真",
                metadata={},
            )
            for index in range(20)
        ]
        retriever = Retriever(VectorStore.from_chunks([common_doc, rare_doc, *filler]))

        results = retriever.search("磁色散 仿真", top_k=5)

        self.assertEqual(results[0].chunk.relative_path, "rare.md")


if __name__ == "__main__":
    unittest.main()
