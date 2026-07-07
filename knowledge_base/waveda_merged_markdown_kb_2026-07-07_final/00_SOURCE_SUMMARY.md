# Source and Packaging Notes

## Strategy

- Original source folders were not modified.
- Existing Markdown was preserved as Markdown, with normalized source metadata added at the top.
- CSV, JSON, JSONL, PDF, DOCX, XLSX, TXT, and HTML user-dropbox files were converted to Markdown text where present.
- The current user dropbox is included as `current_user_dropbox`.
- The output is intentionally placed under `exports/` instead of `knowledge_sources/` to avoid duplicate ingestion by the active RAG index.

## Layout

```text
waveda_merged_markdown_kb_2026-07-07_final/
  00_INDEX.md
  00_SOURCE_SUMMARY.md
  WavEDA_Merged_Knowledge_Base_single_file.md
  sources/
```
