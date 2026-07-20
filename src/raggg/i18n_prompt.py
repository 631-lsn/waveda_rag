"""Prompt / LLM 翻译词条"""
from __future__ import annotations

TEXTS_PROMPT: dict[str, dict[str, str]] = {
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
        "zh": "API Key 无效或已过期，请打开设置检查并更新。已使用本地知识库回答。",
        "en": "Invalid or expired API Key. Please check your settings. Using local knowledge base.",
    },
    "error_llm_rate_limit": {
        "zh": "API 额度用尽或请求太频繁，请稍后重试或检查余额。已使用本地知识库回答。",
        "en": "API quota exhausted or rate limited. Please retry later or check your balance. Using local knowledge base.",
    },
    "error_llm_server": {
        "zh": "模型服务暂时不可用，请稍后重试。已使用本地知识库回答。",
        "en": "Model service temporarily unavailable. Please retry later. Using local knowledge base.",
    },
    "error_llm_timeout": {
        "zh": "请求超时（已自动重试），请检查网络或切换模型。已使用本地知识库回答。",
        "en": "Request timed out (auto-retried). Please check your network or switch models. Using local knowledge base.",
    },
    "error_llm_connection": {
        "zh": "网络连接失败，请检查网络或 API 地址。已使用本地知识库回答。",
        "en": "Network connection failed. Please check your network or API address. Using local knowledge base.",
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
