# Auto Ingest Frontend Design

## Goal

Add a conservative data-ingestion entry point to the existing WavEDA Knowledge Workbench so a user can select one supported document from the desktop UI and make it searchable without running scripts manually.

## Scope

The first version supports importing one file at a time with these extensions: `.md`, `.markdown`, `.html`, `.htm`, and `.txt`.

Imported files are copied into `knowledge_base/05_reference/imported/`. Existing knowledge-base source files are not deleted, moved, or renamed. The import flow then rebuilds the existing local index through `build_knowledge_base()` and reloads the desktop pipeline when rebuild finishes.

This design intentionally avoids batch deletion and batch import. It also avoids depending on `scripts/add_document.py`, because that script is not aligned with the current `Chunk` and `VectorStore` APIs.

## Architecture

Create a small ingestion service under `src/raggg/pipeline/ingestion.py`. It owns file validation, destination naming, text conversion for `.txt`, and copying/writing the imported source file. It returns an `IngestReport` that the UI can display and that tests can assert against.

The desktop window imports this service and adds a left-panel button named `导入资料入库`. The button opens `QFileDialog.getOpenFileName`, starts a background worker, calls the ingestion service, runs `build_knowledge_base()`, then calls `_load_pipeline_if_ready()` after success.

## Data Flow

1. User clicks `导入资料入库`.
2. UI prompts for one file.
3. Worker calls `ingest_document(settings, selected_path)`.
4. The service validates extension and file existence.
5. The service writes a safe, unique destination file in `knowledge_base/05_reference/imported/`.
6. Worker calls `build_knowledge_base(settings)`.
7. UI reloads the `RAGPipeline` and updates the chunk count.

## Error Handling

Unsupported extensions raise `ValueError` with a user-readable message.

Missing files raise `FileNotFoundError`.

Name collisions are handled by appending `-2`, `-3`, and so on before the extension. No existing imported file is overwritten.

If index rebuilding fails, the UI shows the existing warning dialog and keeps the current loaded pipeline state.

## Testing

Unit tests cover importing Markdown, converting `.txt` to Markdown, rejecting unsupported files, and avoiding filename collisions.

Desktop UI wiring is kept thin and uses the existing `Worker` pattern. It is verified by running the unit tests and then rebuilding the real project index followed by the smoke test.
