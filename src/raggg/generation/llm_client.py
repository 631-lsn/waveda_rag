from __future__ import annotations

import json
from collections.abc import Iterator
import urllib.error
import urllib.request


# ── 异常类型：按错误原因分类，调用方可据此给出不同提示 ──

class LLMError(RuntimeError):
    """LLM 请求失败的基类异常"""


class LLMAuthError(LLMError):
    """API Key 无效或鉴权失败（401/403）"""


class LLMRateLimitError(LLMError):
    """API 额度用尽或频率限制（429）"""


class LLMServerError(LLMError):
    """服务端错误或模型过载（5xx）"""


class LLMTimeoutError(LLMError):
    """请求超时"""


class LLMConnectionError(LLMError):
    """网络连接失败（DNS/代理/断网）"""


def _classify_http_error(exc: urllib.error.HTTPError) -> LLMError:
    code = exc.code
    msg = str(exc)
    if code in (401, 403):
        return LLMAuthError(f"[{code}] API Key 无效或鉴权失败。请检查设置中的 API Key 是否正确。")
    if code == 429:
        return LLMRateLimitError(f"[429] API 额度用尽或请求频率过高，请稍后重试或检查余额。")
    if 500 <= code < 600:
        return LLMServerError(f"[{code}] 模型服务暂时不可用，请稍后重试。")
    return LLMError(f"[{code}] {msg}")


def _classify_url_error(exc: urllib.error.URLError) -> LLMError:
    reason = str(exc.reason).lower() if exc.reason else ""
    if "timeout" in reason or "timed out" in reason:
        return LLMTimeoutError("请求超时：网络不稳定或模型响应过慢，已重试一次。")
    return LLMConnectionError(f"网络连接失败：请检查网络或 API 地址设置。({exc.reason})")


class OpenAICompatibleClient:
    def __init__(self, base_url: str, api_key: str, model: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.model = model

    @property
    def is_configured(self) -> bool:
        return bool(self.base_url and self.api_key and self.model)

    # ── 非流式请求 ─────────────────────────────────

    def complete(self, prompt: str, timeout: int = 60) -> str:
        if not self.is_configured:
            raise LLMError("LLM API 未配置。请在设置中填写 API Key。")
        return self._complete(prompt, timeout)

    def _complete(self, prompt: str, timeout: int) -> str:
        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
        }
        try:
            return self._do_request(url, payload, timeout)
        except LLMTimeoutError:
            # 超时重试一次
            return self._do_request(url, payload, timeout)

    def _do_request(self, url: str, payload: dict, timeout: int) -> str:
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
        except urllib.error.HTTPError as exc:
            raise _classify_http_error(exc) from exc
        except urllib.error.URLError as exc:
            raise _classify_url_error(exc) from exc
        except OSError as exc:
            raise LLMConnectionError(f"网络连接失败：{exc}") from exc

        return data["choices"][0]["message"]["content"]

    # ── 流式请求 ───────────────────────────────────

    def complete_stream(self, prompt: str, timeout: int = 60) -> Iterator[str]:
        if not self.is_configured:
            raise LLMError("LLM API 未配置。请在设置中填写 API Key。")
        try:
            yield from self._complete_stream(prompt, timeout)
        except LLMTimeoutError:
            yield from self._complete_stream(prompt, timeout)

    def _complete_stream(self, prompt: str, timeout: int) -> Iterator[str]:
        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
            "stream": True,
        }
        try:
            yield from self._do_stream_request(url, payload, timeout)
        except (LLMTimeoutError, LLMConnectionError):
            raise
        except urllib.error.HTTPError as exc:
            raise _classify_http_error(exc) from exc
        except urllib.error.URLError as exc:
            raise _classify_url_error(exc) from exc
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, IndexError) as exc:
            raise LLMError(f"模型返回格式异常：{exc}") from exc
        except OSError as exc:
            raise LLMConnectionError(f"网络连接失败：{exc}") from exc

    def _do_stream_request(self, url: str, payload: dict, timeout: int) -> Iterator[str]:
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

            if not saw_sse_event and raw_lines:
                data = json.loads("".join(raw_lines))
                content = data["choices"][0]["message"]["content"]
                if content:
                    yield content
