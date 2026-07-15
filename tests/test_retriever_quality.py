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


if __name__ == "__main__":
    unittest.main()
