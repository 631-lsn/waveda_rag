from pathlib import Path
from tempfile import TemporaryDirectory
import json
import os
import unittest
from unittest.mock import patch

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
os.environ.setdefault("QTWEBENGINE_DISABLE_SANDBOX", "1")

from PySide6.QtWidgets import QApplication, QDialog, QFrame, QLabel, QLineEdit

from raggg.config import Settings
from raggg.desktop.main_window import AILoaderOverlay, WorkbenchWindow, favorite_matches


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

    def test_startup_loader_is_visible_with_initial_message(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(WorkbenchWindow, "_build_image_index"), \
                 patch.object(WorkbenchWindow, "_preload_images"), \
                 patch.object(WorkbenchWindow, "_load_pipeline_if_ready"), \
                 patch.object(WorkbenchWindow, "_start_source_watcher"):
                window = WorkbenchWindow(make_settings(root))

            self.assertFalse(window.loader_overlay.isHidden())
            self.assertEqual(window.loader_overlay.text, "正在载入")

    def test_busy_state_reuses_loader_overlay(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(WorkbenchWindow, "_build_image_index"), \
                 patch.object(WorkbenchWindow, "_preload_images"), \
                 patch.object(WorkbenchWindow, "_load_pipeline_if_ready"), \
                 patch.object(WorkbenchWindow, "_start_source_watcher"):
                window = WorkbenchWindow(make_settings(root))

            window.loader_overlay.hide()
            window._set_busy(True, "正在检索")

            self.assertFalse(window.loader_overlay.isHidden())
            self.assertEqual(window.loader_overlay.text, "正在检索")

    def test_loader_uses_orbital_glow_animation_contract(self) -> None:
        overlay = AILoaderOverlay(text="生成中")

        self.assertEqual(overlay.visual_mode, "orbital-glow")
        self.assertGreater(overlay._letter_intensity(18), overlay._letter_intensity(60))
        self.assertGreaterEqual(overlay._letter_lift(18), 2)

    def test_favorite_search_matches_question_and_answer_case_insensitively(self) -> None:
        favorite = {
            "question": "How do I set a Wave Port?",
            "answer": "在边界设置中选择端口截面。",
        }
        self.assertTrue(favorite_matches(favorite, "wave port"))
        self.assertTrue(favorite_matches(favorite, "端口截面"))
        self.assertTrue(favorite_matches(favorite, ""))
        self.assertFalse(favorite_matches(favorite, "PML"))

    def test_favorites_dialog_filters_question_and_answer_content(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            root.joinpath("data").mkdir()
            root.joinpath("data", "favorites.json").write_text(
                json.dumps([
                    {"question": "如何设置波端口？", "answer": "选择端口截面", "time": "2026-07-15 10:00"},
                    {"question": "网格怎么划分？", "answer": "使用自适应网格", "time": "2026-07-15 11:00"},
                ], ensure_ascii=False),
                encoding="utf-8",
            )
            with patch.object(WorkbenchWindow, "_build_image_index"), \
                 patch.object(WorkbenchWindow, "_preload_images"), \
                 patch.object(WorkbenchWindow, "_load_pipeline_if_ready"), \
                 patch.object(WorkbenchWindow, "_start_source_watcher"):
                window = WorkbenchWindow(make_settings(root))

            def inspect_dialog(dialog: QDialog) -> int:
                search_input = dialog.findChild(QLineEdit, "favoritesSearchInput")
                self.assertIsNotNone(search_input)
                search_input.setText("自适应网格")
                cards = dialog.findChildren(QFrame, "metricCard")
                self.assertEqual(len(cards), 2)
                self.assertEqual(sum(not card.isHidden() for card in cards), 1)
                self.assertTrue(dialog.findChild(QLabel, "favoritesNoResults").isHidden())
                search_input.setText("不存在的内容")
                self.assertTrue(all(card.isHidden() for card in cards))
                self.assertFalse(dialog.findChild(QLabel, "favoritesNoResults").isHidden())
                search_input.clear()
                self.assertTrue(all(not card.isHidden() for card in cards))
                return QDialog.Rejected

            with patch.object(QDialog, "exec", new=inspect_dialog):
                window._open_favorites()


if __name__ == "__main__":
    unittest.main()
