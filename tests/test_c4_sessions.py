"""C4: 会话管理测试 — 创建/切换/删除/持久化"""
import json
import tempfile
import unittest
from pathlib import Path

from raggg.desktop.session_manager import SessionManager


class SessionManagerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = tempfile.TemporaryDirectory()
        self.data_dir = Path(self.tmpdir.name)

    def tearDown(self) -> None:
        self.tmpdir.cleanup()

    def test_new_session_creates_non_empty(self) -> None:
        sm = SessionManager(self.data_dir)
        self.assertIsNotNone(sm.current)
        self.assertTrue(sm.current_id)

    def test_new_session_is_idle(self) -> None:
        sm = SessionManager(self.data_dir)
        self.assertEqual(len(sm.current.messages), 0)
        self.assertEqual(sm.current.title, "新对话")

    def test_add_message_persists(self) -> None:
        sm = SessionManager(self.data_dir)
        sm.add_message("测试问题", "测试回答")
        self.assertEqual(len(sm.current.messages), 1)
        self.assertEqual(sm.current.messages[0], ("测试问题", "测试回答"))

        # 重新加载应保持
        sm2 = SessionManager(self.data_dir)
        self.assertEqual(len(sm2.current.messages), 1)

    def test_set_title(self) -> None:
        sm = SessionManager(self.data_dir)
        sm.set_title("新标题")
        self.assertEqual(sm.current.title, "新标题")

    def test_switch_session_preserves_history(self) -> None:
        sm = SessionManager(self.data_dir)
        sid1 = sm.current_id
        sm.add_message("Q1", "A1")

        sm.new_session()
        sid2 = sm.current_id
        sm.add_message("Q2", "A2")

        sm.switch_to(sid1)
        self.assertEqual(len(sm.get_history()), 1)
        self.assertEqual(sm.get_history()[0][0], "Q1")

        sm.switch_to(sid2)
        self.assertEqual(len(sm.get_history()), 1)
        self.assertEqual(sm.get_history()[0][0], "Q2")

    def test_delete_session_keeps_at_least_one(self) -> None:
        sm = SessionManager(self.data_dir)
        sid = sm.current_id
        sm.delete(sid)
        # 只有一个时会拒绝删除
        self.assertIsNotNone(sm.current)
        self.assertIn(sm.current_id, sm.sessions)

    def test_delete_non_current_session(self) -> None:
        sm = SessionManager(self.data_dir)
        _ = sm.current_id
        sm.new_session()  # 现在有两个
        sid2 = sm.current_id
        sm.new_session()  # 有三个
        self.assertTrue(sm.delete(sid2))
        self.assertNotIn(sid2, sm.sessions)

    def test_history_capped(self) -> None:
        sm = SessionManager(self.data_dir)
        for i in range(15):  # MAX_HISTORY_TURNS = 5
            sm.add_message(f"Q{i}", f"A{i}")
        self.assertLessEqual(len(sm.current.messages), 5)

    def test_persistence_across_reload(self) -> None:
        sm = SessionManager(self.data_dir)
        sm.add_message("持久化测试", "持久化回答")
        sm.set_title("持久化标题")
        sid = sm.current_id

        sm2 = SessionManager(self.data_dir)
        self.assertIn(sid, sm2.sessions)
        self.assertEqual(sm2.get_history(sid), [("持久化测试", "持久化回答")])
        self.assertEqual(sm2.sessions[sid].title, "持久化标题")

    def test_file_format_is_valid_json(self) -> None:
        sm = SessionManager(self.data_dir)
        sm.add_message("Q", "A")
        file_path = self.data_dir / "conversations.json"
        self.assertTrue(file_path.exists())
        data = json.loads(file_path.read_text(encoding="utf-8"))
        self.assertIsInstance(data, dict)
        self.assertGreater(len(data), 0)


if __name__ == "__main__":
    unittest.main()
