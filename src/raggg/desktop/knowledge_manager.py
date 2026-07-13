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
        import_controls.addWidget(self.category_combo)

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

    def _add_tree_items(self, parent: QTreeWidgetItem, path: Path) -> None:
        for entry in sorted(path.iterdir()):
            if entry.name.startswith("."):
                continue
            if entry.is_dir():
                item = QTreeWidgetItem(parent, [entry.name])
                item.setData(0, Qt.UserRole, str(entry))
                # Count md files inside
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

        # 3. 获取用户指定的分类和目标文件夹
        cat_id = self.category_combo.currentData()
        target_dir = self._kb_root / cat_id
        user_desc = self.desc_edit.text().strip()

        # 4. 调用 LLM 辅助分析（异步和简化处理）
        suggestion = self._ai_analyze(text, filepath.stem, user_desc)

        # 5. 预览并确认
        preview = (
            f"{get_text('kbm_preview_file')}: {filepath.name}\n"
            f"{get_text('kbm_preview_target')}: {target_dir}\n"
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
        safe_name = re.sub(r"[^\w\-.]", "_", filepath.stem)
        out_path = target_dir / f"{safe_name}.md"
        out_path.write_text(markdown, encoding="utf-8")
        self._load_tree()
        QMessageBox.information(
            self,
            get_text("kbm_import_done"),
            f"{get_text('kbm_import_ok_msg')}: {out_path.relative_to(self._kb_root.parent)}",
        )

    def _build_markdown(self, filepath: Path, text: str) -> str:
        """构建带 YAML 头部的 md 文件"""
        cat_id = self.category_combo.currentData()
        return (
            "---\n"
            f"title: \"{filepath.stem}\"\n"
            f"content_kind: \"imported\"\n"
            f"source_file: \"{filepath.name}\"\n"
            f"imported_at: \"2026-07-09\"\n"
            f"category: \"{cat_id}\"\n"
            "---\n\n"
            f"# {filepath.stem}\n\n"
            f"{text}\n"
        )

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
