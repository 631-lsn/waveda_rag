"""C4: Prompt 构建测试 — 验证格式、包含来源、正确处理空结果"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from raggg.generation.prompt_builder import build_local_answer, build_prompt
from raggg.retrieval.retriever import SearchResult


class _FakeChunk:
    def __init__(self, title: str, content: str, path: str = "test/doc.md",
                 source_type: str = "waveda_help") -> None:
        self.title = title
        self.content = content
        self.relative_path = path
        self.source_type = source_type
        self.section = title


def _make_result(title: str, content: str, score: float = 0.8) -> SearchResult:
    return SearchResult(
        chunk=_FakeChunk(title, content),
        score=score,
        vector_score=0.5,
        lexical_score=0.3,
    )


class PromptBuildingTests(unittest.TestCase):
    def test_prompt_with_sources_contains_reference_label(self) -> None:
        sources = [_make_result("端口设置", "端口设置的详细步骤...")]
        prompt = build_prompt("端口怎么设置？", sources)
        self.assertIn("端口设置", prompt)
        self.assertIn("端口怎么设置？", prompt)

    def test_prompt_without_sources_graceful(self) -> None:
        prompt = build_prompt("端口怎么设置？", [])
        self.assertIsInstance(prompt, str)
        self.assertIn("端口怎么设置？", prompt)

    def test_prompt_contains_citation_instruction(self) -> None:
        prompt = build_prompt("问题", [_make_result("T", "C")])
        self.assertIn("[1]", prompt)
        self.assertIn("不得编造", prompt)

    def test_prompt_sources_are_numbered(self) -> None:
        results = [
            _make_result("DocA", "Content A"),
            _make_result("DocB", "Content B"),
        ]
        prompt = build_prompt("Q", results)
        self.assertIn("[1]", prompt)
        self.assertIn("[2]", prompt)

    def test_local_answer_with_sources(self) -> None:
        sources = [_make_result("端口指南", "步骤一：打开界面...步骤二：设置参数...")]
        answer = build_local_answer("端口怎么设置？", sources)
        self.assertIn("端口指南", answer)
        self.assertIn("引用来源", answer)

    def test_local_answer_empty(self) -> None:
        answer = build_local_answer("问题", [])
        self.assertIn("没有足够依据", answer)


if __name__ == "__main__":
    unittest.main()
