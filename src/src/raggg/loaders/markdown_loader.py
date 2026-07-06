from __future__ import annotations

import re
from pathlib import Path

from raggg.models import Document


WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")


def _relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _title_from_markdown(text: str, fallback: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return fallback


def load_markdown_document(path: Path, root: Path) -> Document:
    text = path.read_text(encoding="utf-8", errors="ignore")
    links = WIKILINK_RE.findall(text)
    has_formula = any(token in text for token in ("$$", "\\nabla", "\\partial", "∇", "∮", "∫"))
    return Document(
        source_type="obsidian_note",
        source_path=path,
        relative_path=_relative(path, root),
        title=_title_from_markdown(text, path.stem),
        text=text,
        links=links,
        images=re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text),
        metadata={
            "domain": "multiphysics",
            "content_type": "note",
            "has_formula": has_formula,
            "has_wikilink": bool(links),
        },
    )


def iter_markdown_documents(root: Path) -> list[Document]:
    if not root.exists():
        return []
    docs: list[Document] = []
    for path in sorted(root.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        docs.append(load_markdown_document(path, root))
    return docs
