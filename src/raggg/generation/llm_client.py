from __future__ import annotations

import json
from collections.abc import Iterator
import urllib.error
import urllib.request


class OpenAICompatibleClient:
    def __init__(self, base_url: str, api_key: str, model: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.model = model

    @property
    def is_configured(self) -> bool:
        return bool(self.base_url and self.api_key and self.model)

    def complete(self, prompt: str, timeout: int = 60) -> str:
        if not self.is_configured:
            raise RuntimeError("LLM API is not configured.")
        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
        }
        request = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                data = json.loads(response.read().decode("utf-8"))
        except urllib.error.URLError as exc:
            raise RuntimeError(f"LLM request failed: {exc}") from exc
        return data["choices"][0]["message"]["content"]

    def complete_stream(self, prompt: str, timeout: int = 60) -> Iterator[str]:
        """Yield text deltas from an OpenAI-compatible SSE response."""
        if not self.is_configured:
            raise RuntimeError("LLM API is not configured.")
        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
            "stream": True,
        }
        request = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "Accept": "text/event-stream",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                raw_lines: list[str] = []
                saw_sse_event = False
                for raw_line in response:
                    line = raw_line.decode("utf-8").strip()
                    if not line:
                        continue
                    raw_lines.append(line)
                    if not line.startswith("data:"):
                        continue
                    saw_sse_event = True
                    event_data = line[5:].strip()
                    if event_data == "[DONE]":
                        break
                    event = json.loads(event_data)
                    choices = event.get("choices") or []
                    if not choices:
                        continue
                    choice = choices[0]
                    content = choice.get("delta", {}).get("content")
                    if not content:
                        content = choice.get("message", {}).get("content")
                    if isinstance(content, str) and content:
                        yield content

                # A few compatible providers ignore stream=true and return
                # one ordinary JSON response. Treat that as a single chunk.
                if not saw_sse_event and raw_lines:
                    data = json.loads("".join(raw_lines))
                    content = data["choices"][0]["message"]["content"]
                    if content:
                        yield content
        except (
            urllib.error.URLError,
            UnicodeDecodeError,
            json.JSONDecodeError,
            KeyError,
            IndexError,
        ) as exc:
            raise RuntimeError(f"LLM streaming request failed: {exc}") from exc
