from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class LLMProvider:
    id: str
    label: str
    base_url: str
    model: str

    def payload(self) -> dict[str, str]:
        return {
            "id": self.id,
            "label": self.label,
            "baseUrl": self.base_url,
            "model": self.model,
        }


LLM_PROVIDERS = (
    LLMProvider("deepseek", "DeepSeek", "https://api.deepseek.com", "deepseek-chat"),
    LLMProvider("kimi", "Kimi (Moonshot)", "https://api.moonshot.cn/v1", "moonshot-v1-8k"),
    LLMProvider(
        "qwen",
        "通义千问",
        "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "qwen-plus",
    ),
    LLMProvider(
        "bailian",
        "阿里云百炼",
        "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "qwen-plus",
    ),
    LLMProvider("openai", "OpenAI", "https://api.openai.com/v1", "gpt-4o-mini"),
)


def provider_payloads() -> list[dict[str, str]]:
    return [provider.payload() for provider in LLM_PROVIDERS]


def get_provider(provider_id: str) -> LLMProvider:
    for provider in LLM_PROVIDERS:
        if provider.id == provider_id:
            return provider
    raise ValueError(f"Unknown provider: {provider_id}")


def infer_provider_id(base_url: str, model: str) -> str:
    normalized_url = base_url.rstrip("/")
    for provider in LLM_PROVIDERS:
        if provider.base_url.rstrip("/") == normalized_url and provider.model == model:
            return provider.id
    return LLM_PROVIDERS[0].id
