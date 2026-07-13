import json
import unittest
from unittest.mock import patch

from raggg.generation.llm_client import OpenAICompatibleClient


class FakeResponse:
    def __init__(self, lines: list[bytes]) -> None:
        self.lines = lines

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback) -> None:
        return None

    def __iter__(self):
        return iter(self.lines)


class LLMClientStreamingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.client = OpenAICompatibleClient("https://example.com", "secret", "test-model")

    def test_yields_sse_content_deltas(self) -> None:
        response = FakeResponse([
            b'data: {"choices":[{"delta":{"content":"Hello"}}]}\n',
            b'data: {"choices":[{"delta":{"content":" world"}}]}\n',
            b'data: [DONE]\n',
        ])

        with patch("urllib.request.urlopen", return_value=response) as urlopen:
            chunks = list(self.client.complete_stream("question"))

        self.assertEqual(chunks, ["Hello", " world"])
        request = urlopen.call_args.args[0]
        payload = json.loads(request.data.decode("utf-8"))
        self.assertTrue(payload["stream"])

    def test_accepts_non_streaming_json_from_compatible_provider(self) -> None:
        response = FakeResponse([
            b'{"choices":[{"message":{"content":"Complete answer"}}]}',
        ])

        with patch("urllib.request.urlopen", return_value=response):
            chunks = list(self.client.complete_stream("question"))

        self.assertEqual(chunks, ["Complete answer"])


if __name__ == "__main__":
    unittest.main()
