from __future__ import annotations

import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from raggg.config import Settings
from raggg.desktop.store import DesktopStore
from raggg.desktop.web_bridge import DesktopBridge
from raggg.pipeline.rag_pipeline import RAGAnswer, RAGPipeline


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


class FakeRetriever:
    def search(self, _query: str, top_k: int = 6):
        return []


class FakeClient:
    is_configured = False


class FakePipeline:
    def ask(self, question, conversation_history=None, progress=None):
        if progress:
            progress("retrieving")
            progress("generating")
        return RAGAnswer(question=question, answer="这是回答", sources=[], warning=None)


def run_immediately(operation, done, failed) -> None:
    try:
        done(operation())
    except Exception as exc:  # pragma: no cover - asserted through bridge output
        failed(str(exc))


class WebBridgeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "data").mkdir(parents=True)
        (self.root / "config").mkdir(parents=True)
        self.settings = make_settings(self.root)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_rag_pipeline_reports_retrieval_then_generation(self) -> None:
        pipeline = RAGPipeline.__new__(RAGPipeline)
        pipeline.retriever = FakeRetriever()
        pipeline.client = FakeClient()
        phases: list[str] = []

        pipeline.ask("波端口怎么设置？", progress=phases.append)

        self.assertEqual(phases, ["retrieving", "generating"])

    def test_bridge_bootstrap_is_sanitized(self) -> None:
        bridge = DesktopBridge(
            self.settings,
            pipeline=FakePipeline(),
            store=DesktopStore(self.settings),
            task_runner=run_immediately,
        )

        payload = json.loads(bridge.bootstrap("{}"))

        self.assertNotIn("apiKey", payload)
        self.assertEqual(payload["theme"], "dark")

    def test_bridge_answer_emits_progress_and_terminal_event(self) -> None:
        bridge = DesktopBridge(
            self.settings,
            pipeline=FakePipeline(),
            store=DesktopStore(self.settings),
            task_runner=run_immediately,
        )
        events: list[dict] = []
        bridge.event_json.connect(lambda encoded: events.append(json.loads(encoded)))

        accepted = json.loads(
            bridge.ask(
                json.dumps(
                    {
                        "requestId": "request-1",
                        "question": "波端口怎么设置？",
                        "conversationId": None,
                    }
                )
            )
        )

        self.assertTrue(accepted["accepted"])
        self.assertEqual(
            [event["phase"] for event in events if event["type"] == "answer_progress"],
            ["retrieving", "generating"],
        )
        terminal = events[-1]
        self.assertEqual(terminal["type"], "answer_completed")
        self.assertEqual(terminal["answer"], "这是回答")
        self.assertTrue(terminal["conversation"]["id"])


if __name__ == "__main__":
    unittest.main()
