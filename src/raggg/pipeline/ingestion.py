from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

from raggg.config import Settings


MARKDOWN_EXTENSIONS = {".md", ".markdown"}
HTML_EXTENSIONS = {".html", ".htm"}
TEXT_EXTENSIONS = {".txt"}
SUPPORTED_EXTENSIONS = MARKDOWN_EXTENSIONS | HTML_EXTENSIONS | TEXT_EXTENSIONS


@dataclass(frozen=True)
class IngestReport:
    original_path: Path
    imported_path: Path
    source_format: str


def _source_format(suffix: str) -> str:
    if suffix in MARKDOWN_EXTENSIONS:
        return "markdown"
    if suffix in HTML_EXTENSIONS:
        return "html"
    if suffix in TEXT_EXTENSIONS:
        return "text"
    raise ValueError(f"不支持的文件类型: {suffix or '(无扩展名)'}")


def _unique_destination(directory: Path, name: str) -> Path:
    candidate = directory / name
    if not candidate.exists():
        return candidate

    stem = candidate.stem
    suffix = candidate.suffix
    counter = 2
    while True:
        candidate = directory / f"{stem}-{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def ingest_document(settings: Settings, source_path: Path | str) -> IngestReport:
    source = Path(source_path)
    if not source.exists():
        raise FileNotFoundError(f"文件不存在: {source}")
    if not source.is_file():
        raise ValueError(f"请选择一个文件: {source}")

    suffix = source.suffix.lower()
    source_format = _source_format(suffix)
    import_dir = settings.project_root / "knowledge_base" / "05_reference" / "imported"
    import_dir.mkdir(parents=True, exist_ok=True)

    if source_format == "text":
        destination = _unique_destination(import_dir, f"{source.stem}.md")
        text = source.read_text(encoding="utf-8", errors="ignore")
        destination.write_text(f"# {source.stem}\n\n{text}\n", encoding="utf-8")
    else:
        destination = _unique_destination(import_dir, source.name)
        shutil.copy2(source, destination)

    return IngestReport(
        original_path=source,
        imported_path=destination,
        source_format=source_format,
    )
