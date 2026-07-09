"""
i18n 国际化模块 — 中/英文切换
语言偏好保存到 config/.env (RAG_LANGUAGE=zh/en)
"""
from __future__ import annotations

import os
from pathlib import Path

# ── 当前语言（模块级缓存） ──────────────────────────────────
_current_lang: str = "zh"

TEXTS: dict[str, dict[str, str]] = {
    # ── 窗口标题 ──────────────────────────────────
    "window_title": {
        "zh": "WavEDA Knowledge Workbench",
        "en": "WavEDA Knowledge Workbench",
    },
    "settings_title": {
        "zh": "设置",
        "en": "Settings",
    },

    # ── 侧边栏 ──────────────────────────────────
    "app_subtitle": {
        "zh": "WavEDA 仿真软件知识问答助手",
        "en": "WavEDA Simulation Knowledge Assistant",
    },
    "badge_waveda_first": {
        "zh": "WavEDA 优先",
        "en": "WavEDA First",
    },
    "sidebar_status": {
        "zh": "工作台状态",
        "en": "Workspace Status",
    },
    "card_knowledge_base": {
        "zh": "知识库",
        "en": "Knowledge Base",
    },
    "card_chunks": {
        "zh": "知识块",
        "en": "Chunks",
    },
    "card_model": {
        "zh": "模型",
        "en": "Model",
    },

    # ── 按钮 ──────────────────────────────────
    "btn_reload_index": {
        "zh": "重新载入索引",
        "en": "Reload Index",
    },
    "btn_api_settings": {
        "zh": "设置",
        "en": "Settings",
    },
    "btn_favorites": {
        "zh": "收藏夹",
        "en": "Favorites",
    },
    "btn_ask": {
        "zh": "提问",
        "en": "Ask",
    },
    "btn_back_to_sources": {
        "zh": "← 返回来源列表",
        "en": "← Back to Sources",
    },
    "btn_delete": {
        "zh": "删除",
        "en": "Delete",
    },
    "btn_copy": {
        "zh": "复制",
        "en": "Copy",
    },
    "btn_copied": {
        "zh": "已复制!",
        "en": "Copied!",
    },
    "btn_fav": {
        "zh": "收藏",
        "en": "Save",
    },
    "btn_faved": {
        "zh": "已收藏",
        "en": "Saved",
    },

    # ── 快捷问题 ──────────────────────────────────
    "quick_questions_label": {
        "zh": "快捷问题",
        "en": "Quick Questions",
    },
    "quick_q1": {
        "zh": "波端口怎么设置？",
        "en": "How to set up a wave port?",
    },
    "quick_q2": {
        "zh": "PML 和吸收边界有什么关系？",
        "en": "What is the relationship between PML and absorbing boundary?",
    },
    "quick_q3": {
        "zh": "如何设置平面波激励？",
        "en": "How to configure plane wave excitation?",
    },
    "search_note": {
        "zh": "优先检索 WavEDA 帮助文档和团队教程，理论笔记作为补充。",
        "en": "Prioritizes WavEDA help docs and team tutorials, supplemented by theory notes.",
    },

    # ── 问答区 ──────────────────────────────────
    "section_qa": {
        "zh": "问答",
        "en": "Q&A",
    },
    "status_ready": {
        "zh": "就绪",
        "en": "Ready",
    },
    "status_loading_index": {
        "zh": "正在载入",
        "en": "Loading",
    },
    "status_building": {
        "zh": "正在重建知识库",
        "en": "Rebuilding knowledge base",
    },
    "status_searching": {
        "zh": "正在检索与生成",
        "en": "Searching & generating",
    },
    "kb_not_built": {
        "zh": "未构建",
        "en": "Not built",
    },
    "kb_loaded": {
        "zh": "已载入",
        "en": "Loaded",
    },
    "model_local": {
        "zh": "本地片段",
        "en": "Local snippets",
    },
    "placeholder_input": {
        "zh": "输入WavEDA问题，如：波端口怎么设置？| PML和吸收边界的关系？",
        "en": "Ask about WavEDA, e.g. How to set up a wave port? | What is PML?",
    },

    # ── 来源面板 ──────────────────────────────────
    "section_sources": {
        "zh": "来源证据",
        "en": "Source Evidence",
    },
    "sources_subtitle": {
        "zh": "按相关性排序，帮助文档和团队教程优先",
        "en": "Sorted by relevance, help docs & team tutorials first",
    },
    "sources_empty": {
        "zh": "提出问题后，这里会显示可追溯的来源证据。",
        "en": "After asking a question, traceable source evidence will appear here.",
    },
    "sources_not_built": {
        "zh": "知识库尚未构建。",
        "en": "Knowledge base not yet built.",
    },
    "you_label": {
        "zh": "你",
        "en": "You",
    },

    # ── 来源标签 ──────────────────────────────────
    "badge_waveda_help": {
        "zh": "WavEDA 帮助",
        "en": "WavEDA Help",
    },
    "badge_team_tutorial": {
        "zh": "团队教程",
        "en": "Team Tutorial",
    },
    "badge_theory_notes": {
        "zh": "理论笔记",
        "en": "Theory Notes",
    },

    # ── 来源匹配度 ──────────────────────────────────
    "match_score": {
        "zh": "匹配度",
        "en": "Match",
    },

    # ── 图片/截图 ──────────────────────────────────
    "screenshot_label": {
        "zh": "操作截图",
        "en": "Screenshots",
    },

    # ── 启动页 ──────────────────────────────────
    "startup_brand_subtitle": {
        "zh": "WavEDA 仿真软件知识问答助手",
        "en": "WavEDA Simulation Knowledge Assistant",
    },
    "startup_chunks_label": {
        "zh": "知识块",
        "en": "Chunks",
    },
    "startup_strategy_label": {
        "zh": "检索策略",
        "en": "Strategy",
    },
    "startup_llm_label": {
        "zh": "大模型",
        "en": "LLM",
    },
    "startup_hint": {
        "zh": "在下方输入 WavEDA 相关问题开始",
        "en": "Enter a WavEDA question below to get started",
    },

    # ── 错误/提示消息 ──────────────────────────────────
    "error_rebuild_title": {
        "zh": "重建失败",
        "en": "Rebuild Failed",
    },
    "error_no_kb_title": {
        "zh": "未载入知识库",
        "en": "Knowledge Base Not Loaded",
    },
    "error_no_kb_msg": {
        "zh": "请先重建或载入知识库。",
        "en": "Please rebuild or load the knowledge base first.",
    },
    "msg_generation_failed": {
        "zh": "生成失败：",
        "en": "Generation failed: ",
    },
    "msg_favorites_empty": {
        "zh": "还没有收藏任何问答。",
        "en": "No saved Q&A yet.",
    },
    "msg_api_saved": {
        "zh": "设置已更新，重启应用后生效。",
        "en": "Settings updated. Restart the app for changes to take effect.",
    },

    # ── 设置：主题 Tab ──────────────────────────────────
    "settings_theme_tab": {
        "zh": "主题",
        "en": "Theme",
    },
    "settings_theme_label": {
        "zh": "界面主题",
        "en": "Interface Theme",
    },
    "settings_theme_desc": {
        "zh": "切换主题后需要重启应用生效。",
        "en": "Restart the app after changing theme for it to take effect.",
    },
    "settings_theme_light": {
        "zh": "浅色",
        "en": "Light",
    },
    "settings_theme_dark": {
        "zh": "深色",
        "en": "Dark",
    },

    # ── 设置：API Tab ──────────────────────────────────
    "settings_api_tab": {
        "zh": "API 设置",
        "en": "API",
    },
    "settings_api_desc": {
        "zh": "选择大模型提供商，输入你的 API Key 即可。\nBase URL 和模型名称会自动填写。",
        "en": "Select your LLM provider and enter your API Key.\nBase URL and model name will be filled automatically.",
    },
    "settings_api_provider": {
        "zh": "大模型",
        "en": "Provider",
    },
    "settings_api_key": {
        "zh": "API Key",
        "en": "API Key",
    },

    # ── 设置：WavEDA 路径 Tab ─────────────────────────
    "settings_waveda_paths_tab": {
        "zh": "WavEDA 路径",
        "en": "WavEDA Paths",
    },
    "settings_waveda_paths_desc": {
        "zh": "填写本机 WavEDA 的绝对路径后，agent 可以在回答中调用你电脑上的帮助文档和案例图片。推荐只填写 WavEDA 安装根目录。",
        "en": "Set local WavEDA paths so the agent can use help and example images from this computer. Usually only the WavEDA install root is needed.",
    },
    "settings_waveda_root": {
        "zh": "WavEDA 安装根目录",
        "en": "WavEDA install root",
    },
    "settings_waveda_help_root": {
        "zh": "帮助文档目录",
        "en": "Help docs folder",
    },
    "settings_waveda_example_root": {
        "zh": "案例目录",
        "en": "Example folder",
    },
    "settings_waveda_paths_hint": {
        "zh": "示例：D:\\Program Files\\WavEDA。保存后请重启应用，新的图片路径索引会自动生效。帮助文档和案例目录可留空，除非你的安装结构比较特殊。",
        "en": "Example: D:\\Program Files\\WavEDA. Restart the app after saving; image paths will be re-indexed automatically. Help and Example folders can stay empty unless your install layout is unusual.",
    },

    # ── 设置：语言 Tab ──────────────────────────────────
    "settings_lang_tab": {
        "zh": "语言",
        "en": "Language",
    },
    "settings_lang_label": {
        "zh": "界面语言",
        "en": "Interface Language",
    },
    "settings_lang_desc": {
        "zh": "切换语言后需要重启应用生效。",
        "en": "Restart the app after changing language for it to take effect.",
    },
    "settings_lang_zh": {
        "zh": "中文",
        "en": "Chinese",
    },
    "settings_lang_en": {
        "zh": "English",
        "en": "English",
    },

    # ── Prompt 模板 ──────────────────────────────────
    "prompt_role": {
        "zh": "你是一个中文 RAG 助手，帮助用户解决 WavEDA 仿真软件的使用问题。",
        "en": "You are an English RAG assistant. Help users solve problems with WavEDA simulation software.",
    },
    "prompt_context_label": {
        "zh": "资料",
        "en": "Reference",
    },
    "prompt_context_instruction": {
        "zh": "请优先使用资料中的内容回答，资料不足时用自己的知识补充。",
        "en": "Prioritize content from the references. Supplement with your own knowledge when references are insufficient.",
    },
    "prompt_history_label": {
        "zh": "最近对话",
        "en": "Recent conversation",
    },
    "prompt_history_instruction": {
        "zh": "如果当前问题使用了“这个、它、上一步、下一步、刚才”等指代，请结合最近对话理解用户真实意图；但事实依据仍以资料为准。",
        "en": "If the current question uses references such as this, it, previous step, next step, or just now, use the recent conversation to understand the intent; factual grounding should still come from the references.",
    },
    "prompt_history_user": {
        "zh": "用户",
        "en": "User",
    },
    "prompt_history_assistant": {
        "zh": "助手",
        "en": "Assistant",
    },
    "prompt_no_context": {
        "zh": "（知识库中暂无相关文档）\n\n请用自己的知识回答这个问题，给出简洁、可操作的建议。",
        "en": "(No relevant documents found in the knowledge base)\n\nPlease answer this question using your own knowledge. Give concise, actionable advice.",
    },
    "prompt_question_prefix": {
        "zh": "问题",
        "en": "Question",
    },
    "prompt_final_instruction": {
        "zh": "请给出简洁、可操作的回答，如果引用了资料请标注来源。",
        "en": "Give concise, actionable answers. Cite sources when referencing materials.",
    },

    # ── 本地答案模板 ──────────────────────────────────
    "local_answer_title": {
        "zh": "根据当前知识库，先给出可确认的信息。",
        "en": "Based on the current knowledge base, here is what can be confirmed.",
    },
    "local_answer_points": {
        "zh": "要点",
        "en": "Key Points",
    },
    "local_answer_sources": {
        "zh": "引用来源",
        "en": "Sources",
    },
    "local_answer_no_sources": {
        "zh": "资料中没有足够依据回答这个问题。",
        "en": "Insufficient evidence in the knowledge base to answer this question.",
    },

    # ── LLM 错误 ──────────────────────────────────
    "error_llm_auth": {
        "zh": "模型暂不可用：API 认证失败，已使用本地知识库回答。请检查 API key。",
        "en": "LLM unavailable: API authentication failed. Using local knowledge base. Please check your API key.",
    },
    "error_llm_unavailable": {
        "zh": "模型暂不可用，已使用本地知识库回答。",
        "en": "LLM temporarily unavailable. Using local knowledge base.",
    },

    # ── 收藏夹对话框 ──────────────────────────────────
    "favorites_title": {
        "zh": "收藏夹",
        "en": "Favorites",
    },
    "favorites_saved": {
        "zh": "已收藏",
        "en": "Saved",
    },
}


def get_text(key: str, lang: str | None = None) -> str:
    """获取翻译文本"""
    if lang is None:
        lang = get_language()
    entry = TEXTS.get(key, {})
    return entry.get(lang, entry.get("zh", key))


def get_language() -> str:
    """获取当前语言设置"""
    global _current_lang
    return _current_lang


def set_language(lang: str) -> None:
    """设置语言 (zh/en) 并持久化"""
    global _current_lang
    _current_lang = lang
    _save_language(lang)


def _language_env_path() -> Path:
    """config/.env 路径"""
    return Path(__file__).resolve().parents[2] / "config" / ".env"


def _load_language() -> str:
    """从 config/.env 加载语言设置"""
    env_path = _language_env_path()
    if not env_path.exists():
        return "zh"
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("RAG_LANGUAGE="):
            lang = line.split("=", 1)[1].strip().strip('"').strip("'")
            if lang in ("zh", "en"):
                return lang
    return "zh"


def _save_language(lang: str) -> None:
    """保存语言设置到 config/.env"""
    env_path = _language_env_path()
    lines: list[str] = []
    if env_path.exists():
        lines = env_path.read_text(encoding="utf-8").splitlines()
    new_lines: list[str] = []
    found = False
    for line in lines:
        if line.startswith("RAG_LANGUAGE="):
            new_lines.append(f"RAG_LANGUAGE={lang}")
            found = True
        else:
            new_lines.append(line)
    if not found:
        new_lines.append(f"RAG_LANGUAGE={lang}")
    env_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


# ── 模块导入时自动加载语言 ──────────────────────────
_current_lang = _load_language()
