from __future__ import annotations

import json
from pathlib import Path
import sys
from uuid import uuid4

from PySide6.QtCore import QTimer, QUrl, Qt
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow

from raggg.config import Settings, load_settings
from raggg.desktop.web_bridge import DesktopBridge
from raggg.pipeline.source_watch import SourceSnapshot, scan_source_tree, snapshot_changed


class WebWorkbenchWindow(QMainWindow):
    """Thin PySide6 shell for the production React workbench."""

    def __init__(self, settings: Settings, *, start_watcher: bool = True) -> None:
        super().__init__()
        self.settings = settings
        self.project_root = settings.project_root
        self.frontend_path = self.project_root / "frontend" / "dist" / "index.html"
        self.frontend_available = self.frontend_path.exists()
        self.frontend_error = ""
        self._source_snapshot: SourceSnapshot = {}
        self._pending_snapshot: SourceSnapshot | None = None

        self.setWindowTitle("WavEDA Knowledge Workbench")
        self.resize(1280, 820)
        self.setMinimumSize(960, 640)
        icon_path = self.project_root / "wavEDA_docs" / "helpHtml" / "image" / "waveda.png"
        if icon_path.exists():
            self.setWindowIcon(QIcon(str(icon_path)))

        self.view = QWebEngineView(self)
        self.view.setContextMenuPolicy(Qt.NoContextMenu)
        self.view.page().setBackgroundColor(QColor("#071019"))
        self.view.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        self.view.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, False)
        self.setCentralWidget(self.view)

        self.bridge = DesktopBridge(settings, parent=self)
        self.channel = QWebChannel(self.view.page())
        self.channel.registerObject("backend", self.bridge)
        self.view.page().setWebChannel(self.channel)
        self.bridge.event_json.connect(self._handle_bridge_event)

        if self.frontend_available:
            self.view.setUrl(QUrl.fromLocalFile(str(self.frontend_path.resolve())))
        else:
            self.frontend_error = f"Missing frontend build: {self.frontend_path.as_posix()}"
            self.view.setHtml(self._missing_frontend_html())

        if start_watcher:
            self._start_source_watcher()

    def _missing_frontend_html(self) -> str:
        escaped = self.frontend_error.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return f"""<!doctype html><html><meta charset='utf-8'><style>
        body{{margin:0;display:grid;place-items:center;height:100vh;background:#071019;color:#e7f0f5;font:14px 'Segoe UI',sans-serif}}
        main{{max-width:620px;border:1px solid #234052;border-radius:18px;background:#0d1925;padding:28px;box-shadow:0 24px 80px #0008}}
        h1{{font-size:22px}}code{{display:block;margin-top:16px;padding:12px;border-radius:10px;background:#071019;color:#fda4af;overflow-wrap:anywhere}}
        </style><main><h1>Frontend build is missing</h1><p>Run setup_env.bat or scripts\\build_frontend.ps1, then start the app again.</p><code>{escaped}</code></main></html>"""

    def _start_source_watcher(self) -> None:
        self._source_snapshot = scan_source_tree(self.settings.obsidian_vault_root)
        self._watch_timer = QTimer(self)
        self._watch_timer.setInterval(5000)
        self._watch_timer.timeout.connect(self._check_source_changes)
        self._watch_timer.start()

        self._watch_debounce = QTimer(self)
        self._watch_debounce.setSingleShot(True)
        self._watch_debounce.setInterval(2000)
        self._watch_debounce.timeout.connect(self._trigger_watch_rebuild)

    def _check_source_changes(self) -> None:
        current = scan_source_tree(self.settings.obsidian_vault_root)
        if not snapshot_changed(self._source_snapshot, current):
            return
        self._pending_snapshot = current
        self.bridge.event_json.emit(
            json.dumps({"type": "watcher_changed", "status": "changed"}, ensure_ascii=False)
        )
        self._watch_debounce.start()

    def _trigger_watch_rebuild(self) -> None:
        if self._pending_snapshot is None:
            return
        self.bridge.event_json.emit(
            json.dumps({"type": "watcher_changed", "status": "rebuilding"}, ensure_ascii=False)
        )
        self.bridge.rebuild_index(json.dumps({"requestId": f"watch-{uuid4()}"}))

    def _handle_bridge_event(self, encoded: str) -> None:
        try:
            event = json.loads(encoded)
        except ValueError:
            return
        if event.get("type") == "index_changed" and event.get("status") == "ready":
            self._source_snapshot = self._pending_snapshot or scan_source_tree(
                self.settings.obsidian_vault_root
            )
            self._pending_snapshot = None
            self.bridge.event_json.emit(
                json.dumps({"type": "watcher_changed", "status": "active"}, ensure_ascii=False)
            )


def run_desktop_app() -> int:
    app = QApplication.instance() or QApplication(sys.argv)
    app.setApplicationName("WavEDA Knowledge Workbench")
    app.setStyle("Fusion")
    window = WebWorkbenchWindow(load_settings())
    window.show()
    return app.exec()
