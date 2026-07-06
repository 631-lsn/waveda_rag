from __future__ import annotations

import hashlib
import re

from raggg.models import Chunk, Document
from raggg.preprocessing.cleaner import clean_text


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$")
FORMULA_MARKERS = ("$$", "\\nabla", "\\partial", "\\cdot", "\\times", "∇", "∮", "∫")


def _chunk_id(source_type: str, relative_path: str, index: int, content: str) -> str:
    digest = hashlib.sha1(content.encode("utf-8")).hexdigest()[:12]
    return f"{source_type}:{relative_path}:{index}:{digest}"


def _paragraphs(text: str) -> list[str]:
    parts = re.split(r"\n\s*\n", text)
    paragraphs: list[str] = []
    for part in parts:
        lines = [line.strip() for line in part.splitlines() if line.strip()]
        paragraphs.extend(lines)
    return paragraphs


def chunk_document(document: Document, target_chars: int = 800) -> list[Chunk]:
    text = clean_text(document.text)
    paragraphs = _paragraphs(text)
    if not paragraphs:
        return []

    chunks: list[Chunk] = []
    current: list[str] = []
    current_section = document.title

    def flush() -> None:
        if not current:
            return
        content = "\n\n".join(current).strip()
        index = len(chunks)
        metadata = dict(document.metadata)
        metadata["has_formula"] = any(marker in content for marker in FORMULA_MARKERS)
        metadata["has_wikilink"] = "[[" in content and "]]" in content
        chunks.append(
            Chunk(
                id=_chunk_id(document.source_type, document.relative_path, index, content),
                source_type=document.source_type,
                source_path=str(document.source_path),
                relative_path=document.relative_path,
                title=document.title,
                section=current_section,
                content=content,
                links=list(document.links),
                images=list(document.images),
                metadata=metadata,
            )
        )
        current.clear()

    for paragraph in paragraphs:
        heading = HEADING_RE.match(paragraph)
        if heading:
            flush()
            current_section = heading.group(2).strip()
            current.append(paragraph)
            continue

        current_len = sum(len(item) for item in current)
        current_text = "\n".join(current)
        formula_nearby = "$$" in current_text or "$$" in paragraph
        if current and current_len + len(paragraph) > target_chars and not formula_nearby:
            flush()
        current.append(paragraph)

    flush()
    return chunks


def chunk_documents(documents: list[Document], target_chars: int = 800) -> list[Chunk]:
    chunks: list[Chunk] = []
    for document in documents:
        chunks.extend(chunk_document(document, target_chars=target_chars))
    return chunks
