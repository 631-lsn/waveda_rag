from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from raggg.config import Settings
from raggg.indexing.embeddings import HashedEmbeddingModel
from raggg.indexing.vector_store import VectorStore
from raggg.loaders.html_loader import iter_html_documents
from raggg.loaders.markdown_loader import iter_markdown_documents
from raggg.models import Chunk, Document
from raggg.pipeline.ingestion import _extract_docx_text, _extract_pdf_text
from raggg.preprocessing.chunker import chunk_documents


@dataclass(frozen=True)
class BuildReport:
    document_count: int
    chunk_count: int
    waveda_document_count: int
    obsidian_document_count: int
    data_dir: Path


def _document_manifest(documents: list[Document]) -> list[dict[str, str]]:
    return [
        {
            "source_type": doc.source_type,
            "source_path": str(doc.source_path),
            "relative_path": doc.relative_path,
            "title": doc.title,
        }
        for doc in documents
    ]


def _write_chunks(path: Path, chunks: list[Chunk]) -> None:
    path.write_text(
        json.dumps([chunk.to_dict() for chunk in chunks], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def _iter_knowledge_base_documents(root: Path) -> list[Document]:
    documents = list(iter_markdown_documents(root))
    if not root.exists():
        return documents

    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        relative_parts = path.relative_to(root).parts
        if any(part.startswith(".") for part in relative_parts):
            continue
        suffix = path.suffix.lower()
        if suffix == ".pdf":
            text = _extract_pdf_text(path)
        elif suffix == ".docx":
            text = _extract_docx_text(path)
        else:
            continue
        documents.append(
            Document(
                source_type="obsidian_note",
                source_path=path,
                relative_path=path.relative_to(root).as_posix(),
                title=path.stem,
                text=text,
                metadata={
                    "domain": "multiphysics",
                    "content_type": "document",
                    "has_formula": any(token in text for token in ("$$", "\\nabla", "\\partial")),
                    "has_wikilink": False,
                },
            )
        )
    return documents


def build_knowledge_base(settings: Settings) -> BuildReport:
    settings.data_dir.mkdir(parents=True, exist_ok=True)
    documents = []
    waveda_docs = iter_html_documents(settings.waveda_help_root)
    obsidian_docs = _iter_knowledge_base_documents(settings.obsidian_vault_root)
    documents.extend(waveda_docs)
    documents.extend(obsidian_docs)

    chunks = chunk_documents(documents)
    (settings.data_dir / "raw_manifest.json").write_text(
        json.dumps(_document_manifest(documents), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    _write_chunks(settings.data_dir / "processed_chunks.json", chunks)
    store = VectorStore.from_chunks(chunks, HashedEmbeddingModel())
    store.save(settings.data_dir / "index")

    return BuildReport(
        document_count=len(documents),
        chunk_count=len(chunks),
        waveda_document_count=len(waveda_docs),
        obsidian_document_count=len(obsidian_docs),
        data_dir=settings.data_dir,
    )
