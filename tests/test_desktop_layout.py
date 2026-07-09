from pathlib import Path
from tempfile import TemporaryDirectory
import os
import unittest
from unittest.mock import patch

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
os.environ.setdefault("QTWEBENGINE_DISABLE_SANDBOX", "1")

from PySide6.QtWidgets import QApplication

from raggg.config import Settings
from raggg.desktop.main_window import WorkbenchWindow


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


class DesktopLayoutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.app = QApplication.instance() or QApplication([])

    def test_minimal_gui_starts_with_hidden_sidebar(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(WorkbenchWindow, "_build_image_index"), \
                 patch.object(WorkbenchWindow, "_preload_images"), \
                 patch.object(WorkbenchWindow, "_load_pipeline_if_ready"), \
                 patch.object(WorkbenchWindow, "_start_source_watcher"):
                window = WorkbenchWindow(make_settings(root))

            self.assertTrue(window.sidebar_container.isHidden())
            self.assertEqual(window.sidebar_toggle_button.text(), "◧")
            self.assertEqual(window.import_button.text(), "+")
            self.assertEqual(window.ask_button.text(), "↑")

    def test_sidebar_toggle_shows_and_hides_sidebar(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(WorkbenchWindow, "_build_image_index"), \
                 patch.object(WorkbenchWindow, "_preload_images"), \
                 patch.object(WorkbenchWindow, "_load_pipeline_if_ready"), \
                 patch.object(WorkbenchWindow, "_start_source_watcher"):
                window = WorkbenchWindow(make_settings(root))

            window.sidebar_toggle_button.click()
            self.assertFalse(window.sidebar_container.isHidden())

            window.sidebar_toggle_button.click()
            self.assertTrue(window.sidebar_container.isHidden())


if __name__ == "__main__":
    unittest.main()
