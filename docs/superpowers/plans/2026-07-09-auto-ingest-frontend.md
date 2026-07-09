# Auto Ingest Frontend Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a desktop UI button that imports one supported document into the knowledge base, rebuilds the local index, and reloads the RAG pipeline.

**Architecture:** Add a focused ingestion service for file validation and safe copying. Keep the PySide6 UI thin: select a file, run ingestion plus existing full rebuild in a worker, and refresh the pipeline on success.

**Tech Stack:** Python 3, PySide6, existing `raggg.pipeline.builder.build_knowledge_base`, local hashed embeddings, unittest-compatible pytest tests.

## Global Constraints

- Do not batch delete files or directories.
- Do not use `del /s`, `rd /s`, `rmdir /s`, `Remove-Item -Recurse`, or `rm -rf`.
- Only support one selected file per import in this version.
- Imported files must live under `knowledge_base/05_reference/imported/`.
- Do not rely on `scripts/add_document.py` for the frontend path.
- Follow TDD: write failing tests before production code.

---

### Task 1: Ingestion Service

**Files:**
- Create: `src/raggg/pipeline/ingestion.py`
- Create: `tests/test_ingestion.py`

**Interfaces:**
- Consumes: `Settings.project_root`
- Produces: `IngestReport(original_path: Path, imported_path: Path, source_format: str)` and `ingest_document(settings: Settings, source_path: Path | str) -> IngestReport`

- [ ] **Step 1: Write failing tests**

Create `tests/test_ingestion.py` with tests that:

```python
from pathlib import Path

import pytest

from raggg.config import Settings
from raggg.pipeline.ingestion import ingest_document


def make_settings(root: Path) -> Settings:
    return Settings(
        project_root=root,
        waveda_help_root=root / "wavEDA_docs" / "helpHtml" / "helpHtml",
        obsidian_vault_root=root / "knowledge_base",
        data_dir=root / "data",
        embedding_model="local-hashed-vectors",
        llm_base_url="https://api.deepseek.com",
        llm_api_key="",
        llm_model="deepseek-chat",
    )


def test_imports_markdown_into_imported_folder(tmp_path: Path) -> None:
    source = tmp_path / "new guide.md"
    source.write_text("# New Guide\n\ncontent", encoding="utf-8")

    report = ingest_document(make_settings(tmp_path), source)

    assert report.imported_path == tmp_path / "knowledge_base" / "05_reference" / "imported" / "new guide.md"
    assert report.imported_path.read_text(encoding="utf-8") == "# New Guide\n\ncontent"
    assert report.source_format == "markdown"


def test_converts_text_file_to_markdown(tmp_path: Path) -> None:
    source = tmp_path / "notes.txt"
    source.write_text("plain notes", encoding="utf-8")

    report = ingest_document(make_settings(tmp_path), source)

    assert report.imported_path.name == "notes.md"
    assert report.imported_path.read_text(encoding="utf-8") == "# notes\n\nplain notes\n"
    assert report.source_format == "text"


def test_rejects_unsupported_extension(tmp_path: Path) -> None:
    source = tmp_path / "table.xlsx"
    source.write_bytes(b"not supported")

    with pytest.raises(ValueError, match="不支持"):
        ingest_document(make_settings(tmp_path), source)


def test_avoids_overwriting_existing_import(tmp_path: Path) -> None:
    imported = tmp_path / "knowledge_base" / "05_reference" / "imported"
    imported.mkdir(parents=True)
    (imported / "guide.md").write_text("old", encoding="utf-8")
    source = tmp_path / "guide.md"
    source.write_text("new", encoding="utf-8")

    report = ingest_document(make_settings(tmp_path), source)

    assert report.imported_path.name == "guide-2.md"
    assert report.imported_path.read_text(encoding="utf-8") == "new"
    assert (imported / "guide.md").read_text(encoding="utf-8") == "old"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_ingestion.py -q`

Expected: import failure because `raggg.pipeline.ingestion` does not exist.

- [ ] **Step 3: Implement minimal ingestion service**

Create `src/raggg/pipeline/ingestion.py` with validation, unique destination naming, copying Markdown/HTML files, and `.txt` to `.md` conversion.

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_ingestion.py -q`

Expected: `4 passed`.

### Task 2: Desktop UI Wiring

**Files:**
- Modify: `src/raggg/desktop/main_window.py`

**Interfaces:**
- Consumes: `ingest_document(settings, selected_path)`
- Produces: `WorkbenchWindow._import_document()` and `WorkbenchWindow._import_and_rebuild(path: str)`

- [ ] **Step 1: Add UI imports and button**

Add `QFileDialog` to imports and add an `import_button` in `_left_panel()` before `reload_button`.

- [ ] **Step 2: Add import worker methods**

Add `_import_document()`, `_import_and_rebuild(path: str)`, and `_on_import_done(result: tuple[IngestReport, BuildReport])`.

- [ ] **Step 3: Reuse existing busy handling**

Disable ask, reload, and import buttons while work is active.

- [ ] **Step 4: Run syntax and import checks**

Run: `python -m py_compile src/raggg/desktop/main_window.py src/raggg/pipeline/ingestion.py`

Expected: exit code 0.

### Task 3: Real Index Verification

**Files:**
- No source changes expected.

**Interfaces:**
- Consumes: existing `scripts/build_knowledge_base.py` and `scripts/smoke_test.py`
- Produces: a valid `data/index/chunks.json` and `data/index/vectors.npy`

- [ ] **Step 1: Build the index**

Run: `python -B scripts/build_knowledge_base.py`

Expected: prints document and chunk counts and exits 0.

- [ ] **Step 2: Run smoke test**

Run: `python -B scripts/smoke_test.py`

Expected: exits 0 and prints sources for each sample question.
