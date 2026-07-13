import unittest
from unittest.mock import Mock

from raggg.pipeline.rag_pipeline import RAGPipeline


class RAGPipelineStreamingTests(unittest.TestCase):
    def make_pipeline(self) -> RAGPipeline:
        pipeline = RAGPipeline.__new__(RAGPipeline)
        pipeline.client = Mock()
        return pipeline

    def test_forwards_stream_chunks_and_joins_answer(self) -> None:
        pipeline = self.make_pipeline()
        pipeline.client.complete_stream.return_value = iter(["波端口", "设置"])
        received: list[str] = []

        answer, warning = pipeline._complete_streaming(
            "prompt",
            "question",
            [],
            received.append,
        )

        self.assertEqual(answer, "波端口设置")
        self.assertEqual(received, ["波端口", "设置"])
        self.assertIsNone(warning)

    def test_falls_back_to_complete_when_streaming_is_rejected(self) -> None:
        pipeline = self.make_pipeline()
        pipeline.client.complete_stream.side_effect = RuntimeError("stream unsupported")
        pipeline.client.complete.return_value = "完整回答"
        received: list[str] = []

        answer, warning = pipeline._complete_streaming(
            "prompt",
            "question",
            [],
            received.append,
        )

        self.assertEqual(answer, "完整回答")
        self.assertEqual(received, ["完整回答"])
        self.assertIsNone(warning)


if __name__ == "__main__":
    unittest.main()
