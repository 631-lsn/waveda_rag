from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from raggg.indexing.embeddings import HashedEmbeddingModel
from raggg.models import Chunk


@dataclass
class VectorStore:
    chunks: list[Chunk]
    vectors: np.ndarray
    embedding_model: HashedEmbeddingModel

    @classmethod
    def from_chunks(
        cls,
        chunks: list[Chunk],
        embedding_model: HashedEmbeddingModel | None = None,
    ) -> "VectorStore":
        model = embedding_model or HashedEmbeddingModel()
        vectors = model.embed_many([chunk.content for chunk in chunks])
        return cls(chunks=chunks, vectors=vectors, embedding_model=model)

    def save(self, index_dir: Path) -> None:
        index_dir.mkdir(parents=True, exist_ok=True)
        (index_dir / "chunks.json").write_text(
            json.dumps([chunk.to_dict() for chunk in self.chunks], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        np.save(index_dir / "vectors.npy", self.vectors)

    @classmethod
    def load(
        cls,
        index_dir: Path,
        embedding_model: HashedEmbeddingModel | None = None,
    ) -> "VectorStore":
        model = embedding_model or HashedEmbeddingModel()
        chunks_data = json.loads((index_dir / "chunks.json").read_text(encoding="utf-8"))
        chunks = [Chunk.from_dict(item) for item in chunks_data]
        vectors = np.load(index_dir / "vectors.npy")
        return cls(chunks=chunks, vectors=vectors, embedding_model=model)
