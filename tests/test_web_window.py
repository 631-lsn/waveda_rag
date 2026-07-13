from __future__ import annotations

import os
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
os.environ.setdefault("QTWEBENGINE_DISABLE_SANDBOX", "1")

from PySide6.QtWidgets import QApplication

from raggg.config import Settings
from raggg.desktop.web_window import WebWorkbenchWindow


def make_settings(root: Path) -> Settings:
    return Settings(
        project_root=root,
        waveda_root=None,
        waveda_help_root=root / "wavEDA_docs" / "helpHtml" / "helpHtml",
        waveda_example_root=None,
        obsidian_vault_root=root / "knowledge_base",
        data_dir=root / "data",
        embedding_model="local-hashed-vectors",
        llm_base_url="https://api.deepseek.com",
        llm_api_key="",
        llm_model="deepseek-chat",
    )


class WebWindowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.app = QApplication.instance() or QApplication([])

    def test_window_loads_production_frontend_and_registers_bridge(self) -> None:
        project_root = Path(__file__).resolve().parents[1]
        window = WebWorkbenchWindow(make_settings(project_root), start_watcher=False)
        self.addCleanup(window.close)

        self.assertEqual((window.width(), window.height()), (1280, 820))
        self.assertEqual((window.minimumWidth(), window.minimumHeight()), (960, 640))
        self.assertTrue(window.frontend_available)
        self.assertEqual(
            Path(window.view.url().toLocalFile()).resolve(),
            (project_root / "frontend" / "dist" / "index.html").resolve(),
        )
        self.assertIsNotNone(window.bridge)
        self.assertIsNotNone(window.channel)

    def test_window_exposes_missing_frontend_state(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "data").mkdir()
            window = WebWorkbenchWindow(make_settings(root), start_watcher=False)
            self.addCleanup(window.close)

        self.assertFalse(window.frontend_available)
        self.assertIn("frontend/dist/index.html", window.frontend_error)


if __name__ == "__main__":
    unittest.main()
