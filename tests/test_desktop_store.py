from __future__ import annotations

import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from raggg.config import Settings
from raggg.desktop.store import DesktopStore


def make_settings(root: Path, api_key: str = "secret-value") -> Settings:
    return Settings(
        project_root=root,
        waveda_root=None,
        waveda_help_root=root / "wavEDA_docs" / "helpHtml" / "helpHtml",
        waveda_example_root=None,
        obsidian_vault_root=root / "knowledge_base",
        data_dir=root / "data",
        embedding_model="local-hashed-vectors",
        llm_base_url="https://api.deepseek.com",
        llm_api_key=api_key,
        llm_model="deepseek-chat",
    )


class DesktopStoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "data").mkdir(parents=True)
        (self.root / "config").mkdir(parents=True)
        self.settings = make_settings(self.root)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_bootstrap_never_returns_api_key(self) -> None:
        store = DesktopStore(self.settings)

        payload = store.bootstrap_payload()

        self.assertTrue(payload["apiConfigured"])
        self.assertEqual(payload["theme"], "dark")
        self.assertNotIn("apiKey", payload)
        self.assertNotIn("secret-value", json.dumps(payload))

    def test_conversation_lifecycle_changes_only_selected_record(self) -> None:
        store = DesktopStore(self.settings)
        first = store.save_turn(None, "第一个问题", "第一个回答", [])
        second = store.save_turn(None, "第二个问题", "第二个回答", [])

        renamed = store.rename_conversation(first["id"], "端口设置讨论")
        deleted = store.delete_conversation(second["id"])

        self.assertEqual(renamed["title"], "端口设置讨论")
        self.assertTrue(deleted)
        conversations = store.list_conversations()
        self.assertEqual([item["id"] for item in conversations], [first["id"]])
        self.assertEqual(len(conversations[0]["messages"]), 2)

    def test_migrates_legacy_favorites_and_deletes_one(self) -> None:
        favorites_path = self.root / "data" / "favorites.json"
        original = json.dumps(
            [
                {"question": "Q1", "answer": "A1", "time": "2026-07-01 09:00"},
                {"question": "Q2", "answer": "A2", "time": "2026-07-02 09:00"},
            ],
            ensure_ascii=False,
        )
        favorites_path.write_text(original, encoding="utf-8")
        store = DesktopStore(self.settings)

        favorites = store.list_favorites()
        self.assertEqual(favorites_path.read_text(encoding="utf-8"), original)
        deleted = store.delete_favorite(favorites[0]["id"])

        self.assertTrue(deleted)
        remaining = store.list_favorites()
        self.assertEqual(len(remaining), 1)
        self.assertEqual(remaining[0]["question"], "Q2")
        self.assertIn("createdAt", remaining[0])

    def test_saving_settings_preserves_unsubmitted_api_key(self) -> None:
        env_path = self.root / "config" / ".env"
        env_path.write_text(
            "RAG_LLM_API_KEY=secret-value\nRAG_LLM_MODEL=deepseek-chat\n",
            encoding="utf-8",
        )
        store = DesktopStore(self.settings)

        payload = store.save_settings({"theme": "light", "locale": "en"})

        saved = env_path.read_text(encoding="utf-8")
        self.assertIn("RAG_LLM_API_KEY=secret-value", saved)
        self.assertNotIn("apiKey", payload)
        self.assertEqual(payload["theme"], "light")
        self.assertEqual(payload["locale"], "en")


if __name__ == "__main__":
    unittest.main()
