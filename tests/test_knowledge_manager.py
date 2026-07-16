import os
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication

from raggg.config import Settings
from raggg.desktop.knowledge_manager import KnowledgeManager


def make_settings(root: Path) -> Settings:
    return Settings(
        project_root=root,
        waveda_root=None,
        waveda_help_root=root / "wavEDA_docs",
        waveda_example_root=None,
        obsidian_vault_root=root / "knowledge_base",
        data_dir=root / "data",
        embedding_model="local-hashed-vectors",
        llm_base_url="https://api.deepseek.com",
        llm_api_key="",
        llm_model="deepseek-chat",
    )


class KnowledgeManagerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.app = QApplication.instance() or QApplication([])

    def test_category_selects_recommended_default_priority(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "knowledge_base").mkdir()
            manager = KnowledgeManager(make_settings(root))

            theory_index = manager.category_combo.findData("06_theory_notes")
            manager.category_combo.setCurrentIndex(theory_index)

            self.assertEqual(manager.priority_combo.currentData(), 1)


if __name__ == "__main__":
    unittest.main()
