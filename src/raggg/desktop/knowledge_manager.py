"""
知识库管理界面 — 查看/编辑知识结构、导入PDF/PPT并AI辅助分类
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Callable

from PySide6.QtCore import Qt, QThreadPool
from PySide6.QtWidgets import (
    QComboBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QSplitter,
    QTextEdit,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from raggg.config import Settings
from raggg.i18n import get_text
from raggg.theme import get_colors

COLORS = get_colors()


class KnowledgeManager(QWidget):
    """知识库管理面板：树形浏览 + 编辑 + 导入"""

    def __init__(self, settings: Settings, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.settings = settings
        self._kb_root = Path(__file__).resolve().parents[3] / "knowledge_base"
        self._current_file: Path | None = None
        self._build_ui()
        self._load_tree()

    # ─── UI ─────────────────────────────────────
    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        # ── 顶部说明 ──
        desc = QLabel(get_text("kbm_desc"))
        desc.setStyleSheet(f"color:{COLORS['muted']};font-size:12px;")
        desc.setWordWrap(True)
        layout.addWidget(desc)

        # ── 左右分栏 ──
        splitter = QSplitter(Qt.Horizontal)

        # 左侧：树
        left = QWidget()
        left_layout = QVBoxLayout(left)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(6)

        tree_label = QLabel(get_text("kbm_tree_title"))
        tree_label.setStyleSheet(f"color:{COLORS['text']};font-weight:700;")
        left_layout.addWidget(tree_label)

        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.tree.itemClicked.connect(self._on_tree_select)
        left_layout.addWidget(self.tree)

        splitter.addWidget(left)

        # 右侧：编辑区
        right = QWidget()
        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(6)

        # 文件信息栏
        info_bar = QHBoxLayout()
        self.file_label = QLabel(get_text("kbm_select_hint"))
        self.file_label.setStyleSheet(f"color:{COLORS['muted']};font-size:11px;")
        info_bar.addWidget(self.file_label, stretch=1)

        save_btn = QPushButton(get_text("kbm_save"))
        save_btn.clicked.connect(self._save_current)
        info_bar.addWidget(save_btn)

        right_layout.addLayout(info_bar)

        self.editor = QTextEdit()
        self.editor.setPlaceholderText(get_text("kbm_editor_placeholder"))
        right_layout.addWidget(self.editor)

        splitter.addWidget(right)
        splitter.setSizes([280, 480])
        layout.addWidget(splitter, stretch=1)

        # ── 导入区 ──
        import_section = QWidget()
        import_layout = QVBoxLayout(import_section)
        import_layout.setContentsMargins(0, 0, 0, 0)
        import_layout.setSpacing(6)

        import_label = QLabel(get_text("kbm_import_title"))
        import_label.setStyleSheet(f"color:{COLORS['text']};font-weight:700;")
        import_layout.addWidget(import_label)

        import_controls = QHBoxLayout()
        import_controls.setSpacing(8)

        pdf_btn = QPushButton(get_text("kbm_import_pdf"))
        pdf_btn.clicked.connect(self._import_pdf)
        import_controls.addWidget(pdf_btn)

        ppt_btn = QPushButton(get_text("kbm_import_ppt"))
        ppt_btn.clicked.connect(self._import_ppt)
        import_controls.addWidget(ppt_btn)

        import_controls.addWidget(QLabel(get_text("kbm_import_target") + ":"))
        self.category_combo = QComboBox()
        self._populate_categories()
        self.category_combo.currentIndexChanged.connect(self._on_category_changed)
        import_controls.addWidget(self.category_combo)

        import_controls.addWidget(QLabel(get_text("kbm_import_subdir") + ":"))
        self.subdir_combo = QComboBox()
        self._populate_subdirs()
        import_controls.addWidget(self.subdir_combo)

        import_controls.addWidget(QLabel(get_text("kbm_priority_label") + ":"))
        self.priority_combo = QComboBox()
        for i in range(1, 6):
            self.priority_combo.addItem(get_text(f"kbm_priority_{i}"), i)
        self.priority_combo.setCurrentIndex(2)
        import_controls.addWidget(self.priority_combo)

        import_controls.addWidget(QLabel(get_text("kbm_import_desc_label") + ":"))
        self.desc_edit = QLineEdit()
        self.desc_edit.setPlaceholderText(get_text("kbm_import_desc_placeholder"))
        import_controls.addWidget(self.desc_edit, stretch=1)

        import_controls.addStretch()
        import_layout.addLayout(import_controls)
        layout.addWidget(import_section)

    # ─── Tree ──────────────────────────────────
    def _load_tree(self) -> None:
        self.tree.clear()
        if not self._kb_root.exists():
            return
        self._add_tree_items(self.tree.invisibleRootItem(), self._kb_root)

    # 目录名 → i18n key 映射
    _CAT_I18N = {
        "01_team_tutorials": "kbm_cat_01",
        "02_software_manual": "kbm_cat_02",
        "03_examples": "kbm_cat_03",
        "04_error_cases": "kbm_cat_04",
        "05_reference": "kbm_cat_05",
        "06_theory_notes": "kbm_cat_06",
        "tutorials": "kbm_sub_tutorials",
        "Circuit": "kbm_example_circuit",
        "EM": "kbm_example_em",
        "Mech": "kbm_example_mech",
        "Multi-Physics": "kbm_example_multi",
        "Thermal": "kbm_example_thermal",
    }

    def _add_tree_items(self, parent: QTreeWidgetItem, path: Path) -> None:
        for entry in sorted(path.iterdir()):
            if entry.name.startswith("."):
                continue
            if entry.is_dir():
                display_name = get_text(self._CAT_I18N.get(entry.name, "")) or entry.name
                item = QTreeWidgetItem(parent, [display_name])
                item.setData(0, Qt.UserRole, str(entry))
                md_count = sum(1 for _ in entry.rglob("*.md"))
                item.setToolTip(0, f"{md_count} documents")
                self._add_tree_items(item, entry)
            elif entry.suffix == ".md":
                item = QTreeWidgetItem(parent, [entry.stem])
                item.setData(0, Qt.UserRole, str(entry))
                item.setToolTip(0, str(entry))

        # Expand first level
        if parent == self.tree.invisibleRootItem():
            self.tree.expandAll()

    def _on_tree_select(self, item: QTreeWidgetItem, _column: int) -> None:
        filepath = item.data(0, Qt.UserRole)
        if not filepath:
            return
        path = Path(filepath)
        if path.is_file() and path.suffix == ".md":
            self._load_file(path)

    def _load_file(self, path: Path) -> None:
        self._current_file = path
        self.file_label.setText(str(path.relative_to(self._kb_root.parent)))
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            text = path.read_text(encoding="utf-8", errors="ignore")
        self.editor.setPlainText(text)

    def _save_current(self) -> None:
        if not self._current_file:
            QMessageBox.information(self, get_text("kbm_save"), get_text("kbm_no_file_selected"))
            return
        self._current_file.write_text(self.editor.toPlainText(), encoding="utf-8")
        QMessageBox.information(self, get_text("kbm_save"), get_text("kbm_save_ok"))

    # ─── Import ────────────────────────────────
    def _populate_categories(self) -> None:
        cats = [
            ("01_team_tutorials", get_text("kbm_cat_01")),
            ("02_software_manual", get_text("kbm_cat_02")),
            ("03_examples", get_text("kbm_cat_03")),
            ("04_error_cases", get_text("kbm_cat_04")),
            ("05_reference", get_text("kbm_cat_05")),
            ("06_theory_notes", get_text("kbm_cat_06")),
        ]
        self.category_combo.clear()
        for cat_id, cat_label in cats:
            self.category_combo.addItem(cat_label, cat_id)

    def _on_category_changed(self, _index: int) -> None:
        self._populate_subdirs()

    def _populate_subdirs(self) -> None:
        """根据选中的大分类，列出所有子目录，外加 AI 自动推荐选项"""
        cat_id = self.category_combo.currentData()
        cat_path = self._kb_root / cat_id
        self.subdir_combo.clear()
        # 首选项：AI 自动推荐
        self.subdir_combo.addItem(get_text("kbm_subdir_auto"), "__AUTO__")
        # 根目录
        self.subdir_combo.addItem(get_text("kbm_subdir_root"), "")
        if cat_path.exists():
            for entry in sorted(cat_path.iterdir()):
                if entry.is_dir() and not entry.name.startswith("."):
                    display = self._CAT_I18N.get(entry.name, entry.name)
                    self.subdir_combo.addItem(f"  {display}", entry.name)
        self.subdir_combo.setCurrentIndex(0)

    def _import_pdf(self) -> None:
        path, _ = QFileDialog.getOpenFileName(
            self, get_text("kbm_import_pdf_title"), "", "PDF (*.pdf)"
        )
        if path:
            self._import_file(path, "pdf")

    def _import_ppt(self) -> None:
        path, _ = QFileDialog.getOpenFileName(
            self, get_text("kbm_import_ppt_title"), "", "PowerPoint (*.pptx)"
        )
        if path:
            self._import_file(path, "pptx")

    def _import_file(self, filepath: str, filetype: str) -> None:
        """转换 PDF/PPT → MD，用 LLM 建议分类，然后写入知识库"""
        filepath = Path(filepath)

        # 1. 提取文本
        if filetype == "pdf":
            try:
                from raggg.pipeline.ingestion import _extract_pdf_text
                text = _extract_pdf_text(filepath)
            except ImportError:
                text = f"[PDF: {filepath.name}]\n\n(需要安装 pypdf 来提取PDF文本)"
        elif filetype == "pptx":
            text = self._extract_pptx_text(filepath)
        else:
            return

        if not text.strip():
            QMessageBox.warning(self, get_text("kbm_import_failed"), get_text("kbm_import_empty"))
            return

        # 2. 生成 Markdown
        markdown = self._build_markdown(filepath, text)

        # 3. 获取目标路径（大分类 + 子目录）
        cat_id = self.category_combo.currentData()
        base_dir = self._kb_root / cat_id
        user_desc = self.desc_edit.text().strip()

        # 确定子目录（手动选择 或 AI 自动推荐）
        subdir_choice = self.subdir_combo.currentData()
        if subdir_choice == "__AUTO__":
            # 列出可选子目录让 AI 从中选择
            avaialble_subdirs = self._list_subdirs(base_dir)
            chosen_subdir = self._ai_suggest_subdir(text, filepath.stem, user_desc, avaialble_subdirs)
            target_dir = base_dir / chosen_subdir if chosen_subdir else base_dir
        elif subdir_choice:
            target_dir = base_dir / subdir_choice
        else:
            target_dir = base_dir

        # 4. 调用 LLM 辅助分析
        suggestion = self._ai_analyze(text, filepath.stem, user_desc)

        # 5. 预览并确认
        preview = (
            f"{get_text('kbm_preview_file')}: {filepath.name}\n"
            f"{get_text('kbm_preview_target')}: {target_dir.relative_to(self._kb_root.parent)}\n"
            f"{get_text('kbm_preview_suggestion')}:\n{suggestion}\n\n"
            f"---\n{markdown[:500]}...\n"
        )
        reply = QMessageBox.question(
            self,
            get_text("kbm_confirm_import"),
            preview,
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply != QMessageBox.Yes:
            return

        # 6. 写入文件
        target_dir.mkdir(parents=True, exist_ok=True)
        safe_name = re.sub(r"[^\w\-.]", "_", filepath.stem)
        out_path = target_dir / f"{safe_name}.md"
        out_path.write_text(markdown, encoding="utf-8")
        self._load_tree()

        # 7. 重建索引使新内容可检索
        from raggg.pipeline.builder import build_knowledge_base
        try:
            report = build_knowledge_base(self.settings)
            msg = f"{get_text('kbm_import_ok_msg')}: {out_path.relative_to(self._kb_root.parent)}\nChunks: {report.chunk_count}"
        except Exception:
            msg = f"{get_text('kbm_import_ok_msg')}: {out_path.relative_to(self._kb_root.parent)}\n(索引重建失败，请手动重建)"
        QMessageBox.information(self, get_text("kbm_import_done"), msg)

    def _build_markdown(self, filepath: Path, text: str) -> str:
        """构建带 YAML 头部的 md 文件"""
        cat_id = self.category_combo.currentData()
        priority = self.priority_combo.currentData()
        return (
            "---\n"
            f"title: \"{filepath.stem}\"\n"
            f"content_kind: \"imported\"\n"
            f"source_file: \"{filepath.name}\"\n"
            f"imported_at: \"2026-07-09\"\n"
            f"category: \"{cat_id}\"\n"
            f"priority: {priority}\n"
            "---\n\n"
            f"# {filepath.stem}\n\n"
            f"{text}\n"
        )

    @staticmethod
    def _list_subdirs(base_dir: Path) -> list[str]:
        """列出某大分类下的所有子目录名"""
        subdirs = []
        if base_dir.exists():
            for entry in sorted(base_dir.iterdir()):
                if entry.is_dir() and not entry.name.startswith("."):
                    subdirs.append(entry.name)
        return subdirs

    def _ai_suggest_subdir(
        self, text: str, filename: str, user_desc: str, subdirs: list[str]
    ) -> str:
        """让 AI 从可用子目录中推荐最匹配的一个"""
        if not subdirs:
            return ""
        prompt = (
            f"分析以下文档内容，从候选子目录中选择最合适的一个。\n"
            f"文档名：{filename}\n"
            f"候选子目录：{', '.join(subdirs)}\n"
            f"内容片段：{text[:1200]}\n"
        )
        if user_desc:
            prompt += f"管理员备注：{user_desc}\n"
        prompt += "只回答子目录名，不要解释。如果不确定，回答 ROOT。"

        if self.settings.llm_api_key:
            try:
                from raggg.generation.llm_client import OpenAICompatibleClient
                client = OpenAICompatibleClient(
                    self.settings.llm_base_url,
                    self.settings.llm_api_key,
                    self.settings.llm_model,
                )
                response = client.complete(prompt).strip()
                if response in subdirs:
                    return response
            except Exception:
                pass

        # 本地匹配回退
        keyword_map = {}
        for sub in subdirs:
            lower = sub.lower()
            if "em" in lower or "project" in lower:
                keyword_map.update({"端口": sub, "激励": sub, "边界": sub, "远场": sub, "pml": sub})
            if "modeling" in lower:
                keyword_map.update({"建模": sub, "几何": sub, "面": sub, "曲线": sub, "拉伸": sub})
            if "mesh" in lower:
                keyword_map.update({"网格": sub, "mesh": sub})
            if "antenna" in lower:
                keyword_map.update({"天线": sub})
            if "filter" in lower:
                keyword_map.update({"滤波器": sub})
            if "circuit" in lower:
                keyword_map.update({"电路": sub})
        for kw, sub in keyword_map.items():
            if kw in text.lower() or kw in filename.lower():
                return sub
        return ""

    def _ai_analyze(self, text: str, filename: str, user_desc: str) -> str:
        """调用 LLM 分析内容，给出分类建议"""
        prompt = (
            f"你是知识库管理助手。分析以下文档内容，给出：\n"
            f"1. 建议的分类节点（从：教程/软件手册/案例/错误排查/参考资料/理论笔记 中选一个）\n"
            f"2. 3-5 个关键词\n"
            f"3. 一句话摘要\n\n"
        )
        if user_desc:
            prompt += f"管理员备注：{user_desc}\n\n"
        prompt += f"文档名：{filename}\n内容片段：{text[:1500]}\n"
        prompt += "\n请用中文简洁回答，格式：分类: xxx | 关键词: a,b,c | 摘要: xxx"

        if self.settings.llm_api_key:
            try:
                from raggg.generation.llm_client import OpenAICompatibleClient
                client = OpenAICompatibleClient(
                    self.settings.llm_base_url,
                    self.settings.llm_api_key,
                    self.settings.llm_model,
                )
                response = client.complete(prompt)
                return response.strip()
            except Exception:
                pass

        # LLM 不可用时用关键词匹配
        keywords_map = {
            "端口": "02_software_manual", "激励": "02", "边界": "02", "求解器": "02",
            "案例": "03_examples", "仿真": "03", "错误": "04_error_cases",
            "教程": "01_team_tutorials", "FAQ": "01",
            "材料": "05_reference", "理论": "06_theory_notes",
        }
        for kw, cat in keywords_map.items():
            if kw in text or kw in filename:
                return f"分类: {cat} | 关键词: {kw} | 摘要: (本地匹配，安装API Key后可使用AI分析)"
        return "分类: 02_software_manual | 关键词: 待补充 | 摘要: (本地匹配)"

    @staticmethod
    def _extract_pptx_text(filepath: Path) -> str:
        """从 PPTX 提取文本"""
        try:
            from pptx import Presentation
        except ImportError:
            return f"[PPT: {filepath.name}]\n\n(需要安装 python-pptx: pip install python-pptx)"

        prs = Presentation(str(filepath))
        slides = []
        for i, slide in enumerate(prs.slides, 1):
            slide_lines = [f"## Slide {i}"]
            for shape in slide.shapes:
                if shape.has_text_frame:
                    for para in shape.text_frame.paragraphs:
                        t = para.text.strip()
                        if t:
                            slide_lines.append(t)
                if shape.has_table:
                    table = shape.table
                    rows = []
                    for row in table.rows:
                        cells = [cell.text.strip() for cell in row.cells]
                        rows.append(" | ".join(cells))
                    if rows:
                        slide_lines.append("\n| " + " |\n| ".join(rows) + " |")
            if len(slide_lines) > 1:
                slides.append("\n".join(slide_lines))
        return "\n\n".join(slides) if slides else f"[PPT: {filepath.name} - 无可提取文本]"
