"""知识库管理翻译词条"""
from __future__ import annotations

TEXTS_KB: dict[str, dict[str, str]] = {
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
    "kbm_select_file": {
        "zh": "选择文件",
        "en": "Select File",
    },
    "kbm_no_file": {
        "zh": "未选择文件",
        "en": "No file selected",
    },
    "kbm_no_file_msg": {
        "zh": "请先点击\"选择文件\"上传要导入的 PDF 或 PPT。",
        "en": "Please click \"Select File\" first to upload a PDF or PPT.",
    },
    "kbm_select_file_title": {
        "zh": "选择要导入的文件",
        "en": "Select file to import",
    },
    "kbm_notes_required": {
        "zh": "需要填写备注",
        "en": "Notes Required",
    },
    "kbm_notes_required_msg": {
        "zh": "请务必在备注栏填写文档内容描述，LLM将以此作为判据的一部分。",
        "en": "Please describe the document content — the LLM will use this as part of its classification judgment.",
    },
    "kbm_confirm_import_btn": {
        "zh": "确认导入",
        "en": "Confirm Import",
    },
    "kbm_delete_file": {
        "zh": "删除文件",
        "en": "Delete File",
    },
    "kbm_delete_confirm_title": {
        "zh": "确认删除",
        "en": "Confirm Delete",
    },
    "kbm_delete_confirm_msg": {
        "zh": "确定要删除 {name} 吗？此操作不可撤销。",
        "en": "Are you sure you want to delete {name}? This cannot be undone.",
    },
    "kbm_delete_error": {
        "zh": "删除失败",
        "en": "Delete Failed",
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
    "kbm_index_update_queued": {
        "zh": "知识库索引将在后台自动更新。",
        "en": "The knowledge index will update automatically in the background.",
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
    "session_panel_title": {"zh": "对话", "en": "Chats"},
    "session_new": {"zh": "新建对话", "en": "New Chat"},
    "session_toggle": {"zh": "显示/隐藏对话列表", "en": "Show/Hide Chats"},
    "session_delete": {"zh": "删除当前对话", "en": "Delete Chat"},
    "session_delete_confirm": {"zh": "确认删除", "en": "Confirm Delete"},
    "session_delete_msg": {"zh": "确定要删除「{name}」吗？", "en": "Delete \"{name}\"?"},
    "upload_image_title": {
        "zh": "上传图片",
        "en": "Upload Image",
    },
    "upload_image_no_vision": {
        "zh": "当前模型不支持图片识别。请切换到 GPT-4o、Claude 或千问 VL 等多模态模型后再上传图片。",
        "en": "Current model does not support image recognition. Please switch to GPT-4o, Claude, or Qwen VL to upload images.",
    },
    "upload_image_hint": {
        "zh": "图片已附加。请在输入框中描述你想了解的问题，AI 将根据图片内容回答。",
        "en": "Image attached. Describe what you want to know and AI will answer based on the image.",
    },
}
