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
        "zh": "慢慢说，我听着",
        "en": "Take your time, I am listening",
    },

    # ── 监听模块 ──────────────────────────────────
    "watch_label": {
        "zh": "监听",
        "en": "Watch",
    },
    "watch_starting": {
        "zh": "启动中",
        "en": "Starting",
    },
    "watch_active": {
        "zh": "监听中",
        "en": "Watching",
    },
    "watch_changed": {
        "zh": "检测到变化",
        "en": "Changes detected",
    },
    "watch_idle": {
        "zh": "等待空闲",
        "en": "Waiting idle",
    },
    "watch_rebuilding": {
        "zh": "自动重建",
        "en": "Rebuilding",
    },
    "watch_busy_msg": {
        "zh": "知识库变化，正在自动重建",
        "en": "Knowledge base changed, auto-rebuilding",
    },
    "watch_rebuild_error": {
        "zh": "自动重建失败",
        "en": "Auto-rebuild failed",
    },
    "watch_waiting_stable": {
        "zh": "检测到知识库变化，等待文件稳定",
        "en": "Knowledge base changes detected, waiting for files to stabilize",
    },

    # ── 导入模块 ──────────────────────────────────
    "import_button": {
        "zh": "导入资料入库",
        "en": "Import Documents",
    },
    "import_tooltip": {
        "zh": "导入资料入库",
        "en": "Import documents to knowledge base",
    },
    "import_dialog_title": {
        "zh": "选择要导入的资料",
        "en": "Select documents to import",
    },
    "import_busy_msg": {
        "zh": "正在导入资料并重建知识库",
        "en": "Importing documents and rebuilding knowledge base",
    },
    "import_failed": {
        "zh": "导入失败",
        "en": "Import failed",
    },
    "import_done": {
        "zh": "导入完成",
        "en": "Import complete",
    },
    "import_result": {
        "zh": "已导入: {name}\n知识块: {count}",
        "en": "Imported: {name}\nChunks: {count}",
    },

    # ── 侧边栏 ──────────────────────────────────
    "sidebar_toggle_tooltip": {
        "zh": "显示/隐藏侧边栏",
        "en": "Show/Hide Sidebar",
    },
    "sidebar_hide_tooltip": {
        "zh": "隐藏侧边栏",
        "en": "Hide Sidebar",
    },
    "section_data_status": {
        "zh": "资料与状态",
        "en": "Data &amp; Status",
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
    "welcome_title": {
        "zh": "您好！我是 WavEDA 仿真软件助手",
        "en": "Hello! I am your WavEDA simulation assistant",
    },
    "welcome_intro": {
        "zh": "我可以根据官方帮助、团队教程和错误案例，为您解答建模操作、仿真设置、错误排查和结果后处理等问题。",
        "en": "I can use the official help, team tutorials, and error cases to answer questions about modeling, simulation settings, troubleshooting, and result post-processing.",
    },
    "welcome_detail": {
        "zh": "请直接描述您正在做什么、卡在哪一步，或贴出具体报错。我会尽量给出简洁、可操作的步骤，并附上相关资料来源。",
        "en": "Describe what you are doing, where you are stuck, or provide the exact error. I will give concise, actionable steps with relevant sources.",
    },
    "welcome_examples_title": {
        "zh": "例如，您可以这样问：",
        "en": "For example, you can ask:",
    },
    "welcome_example_1": {
        "zh": "波端口怎么设置，为什么预览方向要朝外？",
        "en": "How do I configure a wave port, and why should its preview direction point outward?",
    },
    "welcome_example_2": {
        "zh": "仿真提示材料未设置，应该怎么排查？",
        "en": "How should I troubleshoot a missing-material simulation error?",
    },
    "welcome_example_3": {
        "zh": "如何导出 S 参数，或者找到工程生成的 snp 文件？",
        "en": "How do I export S-parameters or find the generated SNP file?",
    },
    "welcome_click_hint": {
        "zh": "点击示例即可开始提问",
        "en": "Click an example to start",
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

    # ── 知识库管理 ──────────────────────────────────
    "kbm_desc": {
        "zh": "浏览、编辑知识库文件，导入 PDF/PPT 并自动转换。LLM 会辅助分析内容建议分类。",
        "en": "Browse and edit knowledge base files. Import PDF/PPT with auto-conversion. LLM assists with content classification.",
    },
    "kbm_tree_title": {
        "zh": "知识结构",
        "en": "Knowledge Tree",
    },
    "kbm_select_hint": {
        "zh": "点击左侧文件进行编辑",
        "en": "Click a file on the left to edit",
    },
    "kbm_save": {
        "zh": "保存",
        "en": "Save",
    },
    "kbm_editor_placeholder": {
        "zh": "选择文件后在此编辑 Markdown...",
        "en": "Select a file to edit Markdown here...",
    },
    "kbm_import_title": {
        "zh": "导入文档（PDF / PPT → MD）",
        "en": "Import Documents (PDF / PPT to MD)",
    },
    "kbm_import_pdf": {
        "zh": "导入 PDF",
        "en": "Import PDF",
    },
    "kbm_import_ppt": {
        "zh": "导入 PPT",
        "en": "Import PPT",
    },
    "kbm_priority_label": {
        "zh": "重要度",
        "en": "Priority",
    },
    "kbm_priority_1": {
        "zh": "1 - 最低",
        "en": "1 - Lowest",
    },
    "kbm_priority_2": {
        "zh": "2 - 较低",
        "en": "2 - Low",
    },
    "kbm_priority_3": {
        "zh": "3 - 普通",
        "en": "3 - Normal",
    },
    "kbm_priority_4": {
        "zh": "4 - 较高",
        "en": "4 - High",
    },
    "kbm_priority_5": {
        "zh": "5 - 最高",
        "en": "5 - Highest",
    },
    "kbm_import_subdir": {
        "zh": "子目录",
        "en": "Sub-directory",
    },
    "kbm_subdir_auto": {
        "zh": "🤖 AI 自动推荐",
        "en": "AI Auto-Suggest",
    },
    "kbm_subdir_root": {
        "zh": "(根目录)",
        "en": "(Root)",
    },
    "kbm_import_target": {
        "zh": "目标节点",
        "en": "Target Node",
    },
    "kbm_import_desc_label": {
        "zh": "备注",
        "en": "Notes",
    },
    "kbm_import_desc_placeholder": {
        "zh": "简要描述文档内容，帮助AI分类...",
        "en": "Briefly describe the document to help AI classification...",
    },
    "kbm_import_pdf_title": {
        "zh": "选择 PDF 文件",
        "en": "Select PDF File",
    },
    "kbm_import_ppt_title": {
        "zh": "选择 PPT 文件",
        "en": "Select PPT File",
    },
    "kbm_import_failed": {
        "zh": "导入失败",
        "en": "Import Failed",
    },
    "kbm_import_empty": {
        "zh": "无法从文件中提取文本内容。",
        "en": "Could not extract text content from the file.",
    },
    "kbm_preview_file": {
        "zh": "文件",
        "en": "File",
    },
    "kbm_preview_target": {
        "zh": "目标位置",
        "en": "Target",
    },
    "kbm_preview_suggestion": {
        "zh": "AI 分析建议",
        "en": "AI Analysis",
    },
    "kbm_confirm_import": {
        "zh": "确认导入",
        "en": "Confirm Import",
    },
    "kbm_import_done": {
        "zh": "导入完成",
        "en": "Import Complete",
    },
    "kbm_import_ok_msg": {
        "zh": "文件已导入",
        "en": "File imported",
    },
    "kbm_no_file_selected": {
        "zh": "请先选择要编辑的文件。",
        "en": "Please select a file to edit first.",
    },
    "kbm_save_ok": {
        "zh": "文件已保存。",
        "en": "File saved.",
    },
    "kbm_cat_01": {
        "zh": "01 团队教程",
        "en": "01 Team Tutorials",
    },
    "kbm_cat_02": {
        "zh": "02 软件手册",
        "en": "02 Software Manual",
    },
    "kbm_cat_03": {
        "zh": "03 仿真案例",
        "en": "03 Examples",
    },
    "kbm_cat_04": {
        "zh": "04 错误排查",
        "en": "04 Error Cases",
    },
    "kbm_cat_05": {
        "zh": "05 参考资料",
        "en": "05 Reference",
    },
    "kbm_cat_06": {
        "zh": "06 理论笔记",
        "en": "06 Theory Notes",
    },
    "kbm_sub_tutorials": {
        "zh": "tutorials",
        "en": "Tutorials",
    },
    "kbm_example_circuit": {
        "zh": "Circuit",
        "en": "Circuit",
    },
    "kbm_example_em": {
        "zh": "EM",
        "en": "EM",
    },
    "kbm_example_mech": {
        "zh": "Mech",
        "en": "Mech",
    },
    "kbm_example_multi": {
        "zh": "Multi-Physics",
        "en": "Multi-Physics",
    },
    "kbm_example_thermal": {
        "zh": "Thermal",
        "en": "Thermal",
    },
    "kbm_tab": {
        "zh": "知识库",
        "en": "Knowledge Base",
    },

    # ── 临时文件上传 ──────────────────────────────────
    "upload_tooltip": {
        "zh": "上传文件提问（PDF/PPT/DOCX）",
        "en": "Upload file to ask (PDF/PPT/DOCX)",
    },
    "upload_dialog_title": {
        "zh": "选择要提问的文件",
        "en": "Select file to ask about",
    },
    "upload_attached": {
        "zh": "已附加: {name}",
        "en": "Attached: {name}",
    },
    "upload_clear": {
        "zh": "移除附件",
        "en": "Remove attachment",
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
