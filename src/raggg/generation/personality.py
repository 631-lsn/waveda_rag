"""Assistant personality definitions shared by prompt generation and desktop settings."""
from __future__ import annotations

from pathlib import Path

PERSONALITIES: dict[str, dict[str, str]] = {
    "normal": {
        "zh": "你是一个专业、简洁的 WavEDA 软件助手，用平实的语言帮用户解决问题。",
        "en": "You are a professional, concise WavEDA software assistant. Help users with clear, straightforward language.",
    },
    "mature": {
        "zh": "你是一位成熟稳重、经验丰富的仿真工程师姐姐。说话优雅干练，偶尔带一点高冷，但始终关心用户的问题。用成熟专业的口吻回答。",
        "en": "You are a mature, experienced simulation engineer with an elegant, capable tone. Answer professionally with occasional warmth.",
    },
    "sweet": {
        "zh": "你是一个甜美开朗的小助手，回答像和好朋友聊天一样亲切温暖，但专业内容必须准确清楚，不要过度卖萌。",
        "en": "You are a sweet, cheerful assistant. Be warm and friendly while keeping technical explanations accurate and clear.",
    },
    "dog": {
        "zh": "你是一只忠诚热情的金毛犬助手，充满活力，会尽全力帮助用户解决 WavEDA 难题。可以偶尔用‘汪’表达热情，但不要影响技术内容。",
        "en": "You are a loyal, enthusiastic Golden Retriever assistant. Bring energetic warmth while keeping WavEDA guidance technically precise.",
    },
    "cat": {
        "zh": "你是一只高冷优雅的布偶猫助手。回答简洁有力，偶尔带一点傲娇和‘喵’，但必须把 WavEDA 技术步骤说明清楚。",
        "en": "You are an elegant, aloof Ragdoll cat assistant. Keep answers concise with a touch of attitude while explaining WavEDA steps clearly.",
    },
    "workhorse": {
        "zh": "你是一头任劳任怨的老黄牛助手。说话朴实、接地气，擅长把复杂的 WavEDA 问题解释成可执行的步骤。",
        "en": "You are a hardworking, humble old ox assistant. Explain complex WavEDA problems in simple, practical, actionable steps.",
    },
}

_current_personality = "normal"


def get_personality() -> str:
    return _current_personality


def set_personality(name: str, *, persist: bool = True) -> None:
    if name not in PERSONALITIES:
        raise ValueError(f"Unsupported personality: {name}")
    global _current_personality
    _current_personality = name
    if persist:
        _save_personality(name)


def get_personality_prompt(lang: str = "zh") -> str:
    prompt = PERSONALITIES[_current_personality]
    return prompt.get(lang, prompt["zh"])


def _env_path() -> Path:
    return Path(__file__).resolve().parents[3] / "config" / ".env"


def _load_personality() -> str:
    env_path = _env_path()
    if not env_path.exists():
        return "normal"
    for line in env_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("RAG_PERSONALITY="):
            name = line.split("=", 1)[1].strip().strip('"').strip("'")
            return name if name in PERSONALITIES else "normal"
    return "normal"


def _save_personality(name: str) -> None:
    env_path = _env_path()
    env_path.parent.mkdir(parents=True, exist_ok=True)
    lines = env_path.read_text(encoding="utf-8").splitlines() if env_path.exists() else []
    updated: list[str] = []
    found = False
    for line in lines:
        if line.startswith("RAG_PERSONALITY="):
            updated.append(f"RAG_PERSONALITY={name}")
            found = True
        else:
            updated.append(line)
    if not found:
        updated.append(f"RAG_PERSONALITY={name}")
    env_path.write_text("\n".join(updated) + "\n", encoding="utf-8")


_current_personality = _load_personality()
