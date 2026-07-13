from __future__ import annotations

from dataclasses import replace
import json
from pathlib import Path
from typing import Any, Callable

from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal, Slot
from PySide6.QtWidgets import QApplication, QFileDialog

from raggg.config import Settings, load_dotenv_file
from raggg.pipeline.builder import build_knowledge_base
from raggg.pipeline.ingestion import ingest_document
from raggg.pipeline.rag_pipeline import RAGPipeline
from raggg.retrieval.retriever import SearchResult
from raggg.desktop.store import DesktopStore
from raggg.generation.personality import set_personality
from raggg.i18n import set_language


TaskRunner = Callable[
    [Callable[[], Any], Callable[[Any], None], Callable[[str], None]],
    None,
]


class _TaskSignals(QObject):
    result = Signal(object)
    error = Signal(str)


class _Task(QRunnable):
    def __init__(self, operation: Callable[[], Any]) -> None:
        super().__init__()
        self.operation = operation
        self.signals = _TaskSignals()

    @Slot()
    def run(self) -> None:
        try:
            result = self.operation()
        except Exception as exc:  # noqa: BLE001 - emitted to the frontend safely
            self.signals.error.emit(str(exc))
            return
        self.signals.result.emit(result)


def _encode(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False)


def _decode(payload: str) -> dict[str, Any]:
    try:
        value = json.loads(payload or "{}")
    except ValueError as exc:
        raise ValueError("Invalid JSON request.") from exc
    if not isinstance(value, dict):
        raise ValueError("Request payload must be an object.")
    return value


class DesktopBridge(QObject):
    """JSON QWebChannel API for the React desktop client."""

    event_json = Signal(str)

    def __init__(
        self,
        settings: Settings,
        parent: QObject | None = None,
        *,
        pipeline: RAGPipeline | Any | None = None,
        store: DesktopStore | None = None,
        task_runner: TaskRunner | None = None,
        file_picker: Callable[[], str] | None = None,
    ) -> None:
        super().__init__(parent)
        self.settings = settings
        self.store = store or DesktopStore(settings)
        self.pipeline = pipeline if pipeline is not None else self._load_pipeline()
        self._task_runner = task_runner or self._queue_task
        self._file_picker = file_picker or self._pick_document
        self._detached_requests: set[str] = set()
        self._active_tasks: list[_Task] = []

    @Slot(str, result=str)
    def bootstrap(self, _payload: str) -> str:
        return _encode(self.store.bootstrap_payload())

    @Slot(str, result=str)
    def ask(self, payload: str) -> str:
        try:
            request = _decode(payload)
            request_id = self._required_text(request, "requestId")
            question = self._required_text(request, "question")
            conversation_id = request.get("conversationId") or None
            if self.pipeline is None:
                raise RuntimeError("Knowledge index is not ready.")
        except (ValueError, RuntimeError) as exc:
            return _encode({"error": str(exc)})

        self._detached_requests.discard(request_id)
        history = self._conversation_pairs(conversation_id)

        def progress(phase: str) -> None:
            if request_id not in self._detached_requests:
                self._emit(
                    {
                        "type": "answer_progress",
                        "requestId": request_id,
                        "phase": phase,
                    }
                )

        def operation():
            return self.pipeline.ask(
                question,
                conversation_history=history,
                progress=progress,
            )

        def done(answer) -> None:
            if request_id in self._detached_requests:
                return
            sources = [self._serialize_source(item) for item in answer.sources]
            conversation = self.store.save_turn(
                conversation_id,
                question,
                answer.answer,
                sources,
                answer.warning,
            )
            self._emit(
                {
                    "type": "answer_completed",
                    "requestId": request_id,
                    "conversation": conversation,
                    "answer": answer.answer,
                    "sources": sources,
                    "warning": answer.warning,
                }
            )

        def failed(message: str) -> None:
            if request_id not in self._detached_requests:
                self._emit(
                    {
                        "type": "answer_failed",
                        "requestId": request_id,
                        "message": message,
                    }
                )

        self._task_runner(operation, done, failed)
        return _encode({"accepted": True})

    @Slot(str, result=str)
    def stop_answer(self, payload: str) -> str:
        try:
            request_id = self._required_text(_decode(payload), "requestId")
        except ValueError as exc:
            return _encode({"error": str(exc)})
        self._detached_requests.add(request_id)
        return _encode({"stopped": True})

    @Slot(str, result=str)
    def select_and_import_document(self, payload: str) -> str:
        try:
            request_id = self._required_text(_decode(payload), "requestId")
        except ValueError as exc:
            return _encode({"error": str(exc)})
        self._emit({"type": "import_progress", "requestId": request_id, "phase": "selecting"})
        path = self._file_picker()
        if not path:
            self._emit({"type": "import_cancelled", "requestId": request_id})
            return _encode({"accepted": False})
        self._emit({"type": "import_progress", "requestId": request_id, "phase": "importing"})

        def operation():
            report = ingest_document(self.settings, path)
            self._emit({"type": "import_progress", "requestId": request_id, "phase": "rebuilding"})
            build_report = build_knowledge_base(self.settings)
            return report, build_report

        def done(result) -> None:
            report, build_report = result
            self.pipeline = self._load_pipeline()
            self._emit(
                {
                    "type": "import_completed",
                    "requestId": request_id,
                    "fileName": report.imported_path.name,
                    "chunkCount": build_report.chunk_count,
                }
            )
            self._emit(
                {
                    "type": "index_changed",
                    "status": "ready",
                    "chunkCount": build_report.chunk_count,
                }
            )

        self._task_runner(
            operation,
            done,
            lambda message: self._emit(
                {"type": "import_failed", "requestId": request_id, "message": message}
            ),
        )
        return _encode({"accepted": True})

    @Slot(str, result=str)
    def list_history(self, _payload: str) -> str:
        return _encode(self.store.list_conversations())

    @Slot(str, result=str)
    def get_conversation(self, payload: str) -> str:
        return self._store_call(payload, "id", self.store.get_conversation)

    @Slot(str, result=str)
    def rename_history(self, payload: str) -> str:
        try:
            request = _decode(payload)
            result = self.store.rename_conversation(
                self._required_text(request, "id"),
                self._required_text(request, "title"),
            )
            return _encode(result)
        except (ValueError, KeyError) as exc:
            return _encode({"error": str(exc)})

    @Slot(str, result=str)
    def delete_history(self, payload: str) -> str:
        return self._delete_call(payload, self.store.delete_conversation)

    @Slot(str, result=str)
    def list_favorites(self, _payload: str) -> str:
        return _encode(self.store.list_favorites())

    @Slot(str, result=str)
    def save_favorite(self, payload: str) -> str:
        try:
            request = _decode(payload)
            result = self.store.save_favorite(
                self._required_text(request, "question"),
                self._required_text(request, "answer"),
            )
            return _encode(result)
        except ValueError as exc:
            return _encode({"error": str(exc)})

    @Slot(str, result=str)
    def delete_favorite(self, payload: str) -> str:
        return self._delete_call(payload, self.store.delete_favorite)

    @Slot(str, result=str)
    def save_settings(self, payload: str) -> str:
        try:
            update = _decode(payload)
            result = self.store.save_settings(update)
            self._refresh_runtime_settings(update)
            return _encode(result)
        except (ValueError, OSError) as exc:
            return _encode({"error": str(exc)})

    @Slot(str, result=str)
    def select_provider(self, payload: str) -> str:
        try:
            request = _decode(payload)
            provider_id = self._required_text(request, "providerId")
            result = self.store.select_provider(provider_id)
            self._refresh_runtime_settings(
                {
                    "providerId": result["providerId"],
                    "baseUrl": result["baseUrl"],
                    "model": result["model"],
                }
            )
            return _encode(result)
        except (ValueError, OSError) as exc:
            return _encode({"error": str(exc)})

    @Slot(str, result=str)
    def rebuild_index(self, payload: str) -> str:
        try:
            request_id = self._required_text(_decode(payload), "requestId")
        except ValueError as exc:
            return _encode({"error": str(exc)})

        def done(report) -> None:
            self.pipeline = self._load_pipeline()
            self._emit(
                {
                    "type": "index_changed",
                    "requestId": request_id,
                    "status": "ready",
                    "chunkCount": report.chunk_count,
                }
            )

        self._task_runner(
            lambda: build_knowledge_base(self.settings),
            done,
            lambda message: self._emit(
                {"type": "index_failed", "requestId": request_id, "message": message}
            ),
        )
        return _encode({"accepted": True})

    def _load_pipeline(self) -> RAGPipeline | None:
        index_dir = self.settings.data_dir / "index"
        if not (index_dir / "chunks.json").exists() or not (index_dir / "vectors.npy").exists():
            return None
        return RAGPipeline(self.settings)

    def _queue_task(
        self,
        operation: Callable[[], Any],
        done: Callable[[Any], None],
        failed: Callable[[str], None],
    ) -> None:
        task = _Task(operation)
        self._active_tasks.append(task)
        task.signals.result.connect(done)
        task.signals.error.connect(failed)
        task.signals.result.connect(lambda _result: self._forget_task(task))
        task.signals.error.connect(lambda _message: self._forget_task(task))
        QThreadPool.globalInstance().start(task)

    def _forget_task(self, task: _Task) -> None:
        if task in self._active_tasks:
            self._active_tasks.remove(task)

    def _pick_document(self) -> str:
        path, _ = QFileDialog.getOpenFileName(
            QApplication.activeWindow(),
            "导入资料",
            str(self.settings.project_root),
            "Documents (*.md *.markdown *.html *.htm *.txt *.pdf *.docx)",
        )
        return path

    def _conversation_pairs(self, conversation_id: str | None) -> list[tuple[str, str]]:
        if not conversation_id:
            return []
        try:
            conversation = self.store.get_conversation(conversation_id)
        except KeyError:
            return []
        messages = conversation.get("messages", [])
        pairs: list[tuple[str, str]] = []
        pending_question: str | None = None
        for message in messages:
            if message.get("role") == "user":
                pending_question = str(message.get("content", ""))
            elif message.get("role") == "assistant" and pending_question:
                pairs.append((pending_question, str(message.get("content", ""))))
                pending_question = None
        return pairs[-5:]

    @staticmethod
    def _serialize_source(source: SearchResult) -> dict[str, Any]:
        chunk = source.chunk
        return {
            "id": chunk.id,
            "title": chunk.title,
            "section": chunk.section,
            "path": chunk.relative_path or chunk.source_path,
            "sourceType": chunk.source_type,
            "score": source.score,
            "excerpt": chunk.content[:260],
            "content": chunk.content,
            "images": [],
        }

    def _refresh_runtime_settings(self, update: dict[str, Any]) -> None:
        env = load_dotenv_file(self.store.env_path)
        root = self.settings.project_root
        set_personality(env.get("RAG_PERSONALITY", "normal"), persist=False)
        set_language(env.get("RAG_LANGUAGE", "zh"))

        def optional_path(name: str, current: Path | None) -> Path | None:
            raw = env.get(name)
            if raw is None:
                return current
            if not raw:
                return None
            path = Path(raw)
            return path if path.is_absolute() else root / path

        self.settings = replace(
            self.settings,
            llm_base_url=env.get("RAG_LLM_BASE_URL", self.settings.llm_base_url),
            llm_api_key=env.get("RAG_LLM_API_KEY", self.settings.llm_api_key),
            llm_model=env.get("RAG_LLM_MODEL", self.settings.llm_model),
            waveda_root=optional_path("WAVEDA_ROOT", self.settings.waveda_root),
            waveda_help_root=optional_path("WAVEDA_HELP_ROOT", self.settings.waveda_help_root)
            or self.settings.waveda_help_root,
            waveda_example_root=optional_path(
                "WAVEDA_EXAMPLE_ROOT", self.settings.waveda_example_root
            ),
        )
        self.store = DesktopStore(self.settings)
        self.pipeline = self._load_pipeline()

    def _store_call(
        self,
        payload: str,
        field: str,
        operation: Callable[[str], Any],
    ) -> str:
        try:
            value = self._required_text(_decode(payload), field)
            return _encode(operation(value))
        except (ValueError, KeyError) as exc:
            return _encode({"error": str(exc)})

    def _delete_call(self, payload: str, operation: Callable[[str], bool]) -> str:
        try:
            record_id = self._required_text(_decode(payload), "id")
            return _encode({"deleted": operation(record_id)})
        except ValueError as exc:
            return _encode({"error": str(exc)})

    @staticmethod
    def _required_text(payload: dict[str, Any], field: str) -> str:
        value = payload.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Missing required field: {field}.")
        return value.strip()

    def _emit(self, payload: dict[str, Any]) -> None:
        self.event_json.emit(_encode(payload))
