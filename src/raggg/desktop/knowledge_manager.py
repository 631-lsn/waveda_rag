"""
知识库管理界面 — 查看/编辑知识结构、导入PDF/PPT并AI辅助分类
"""
from __future__ import annotations

import re
from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QComboBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMenu,
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
from raggg.pipeline.knowledge_import import (
    analyze_document,
    build_import_markdown,
    extract_pptx_text,
    list_all_subdirs,
    suggest_subdir,
)
from raggg.theme import get_colors

COLORS = get_colors()


class KnowledgeManager(QWidget):
    knowledge_changed = Signal()

    def __init__(self, settings: Settings, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.settings = settings
        self._kb_root = settings.obsidian_vault_root
        self._current_file: Path | None = None
        self._pending_import_path: str = ""
        self._pending_import_type: str = ""
        self._build_ui()
        self._load_tree()

    # ─── UI ─────────────────────────────────────
    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        desc = QLabel(get_text("kbm_desc"))
        desc.setStyleSheet(f"color:{COLORS['muted']};font-size:12px;")
        desc.setWordWrap(True)
        layout.addWidget(desc)

        splitter = QSplitter(Qt.Horizontal)

        # 左侧：树 + 右键菜单
        left = QWidget()
        left_layout = QVBoxLayout(left)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(6)

        tree_label = QLabel(get_text("kbm_tree_title"))
        tree_label.setStyleSheet(f"color:{COLORS['text']};font-weight:700;")
        left_layout.addWidget(tree_label)

        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.itemClicked.connect(self._on_tree_select)
        self.tree.customContextMenuRequested.connect(self._on_tree_context_menu)
        left_layout.addWidget(self.tree)

        splitter.addWidget(left)

        # 右侧：编辑区
        right = QWidget()
        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(6)

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

        # Row 1: 选择文件
        row1 = QHBoxLayout(); row1.setSpacing(8)
        self.file_select_btn = QPushButton(get_text("kbm_select_file"))
        self.file_select_btn.clicked.connect(self._select_file)
        row1.addWidget(self.file_select_btn)
        self.file_status = QLabel(get_text("kbm_no_file"))
        self.file_status.setStyleSheet(f"color:{COLORS['muted']};font-size:11px;")
        row1.addWidget(self.file_status, stretch=1)
        import_layout.addLayout(row1)

        # Row 2: 分类 + 子目录 + 重要度
        row2 = QHBoxLayout(); row2.setSpacing(8)
        row2.addWidget(QLabel(get_text("kbm_import_target") + ":"))
        self.category_combo = QComboBox()
        self._populate_categories()
        self.category_combo.currentIndexChanged.connect(self._on_category_changed)
        row2.addWidget(self.category_combo)

        row2.addWidget(QLabel(get_text("kbm_import_subdir") + ":"))
        self.subdir_btn = QPushButton(get_text("kbm_subdir_auto"))
        self.subdir_btn.clicked.connect(self._popup_subdir_menu)
        self._subdir_value = "__AUTO__"
        row2.addWidget(self.subdir_btn)

        row2.addWidget(QLabel(get_text("kbm_priority_label") + ":"))
        self.priority_combo = QComboBox()
        for i in range(1, 6):
            self.priority_combo.addItem(get_text(f"kbm_priority_{i}"), i)
        self.priority_combo.setCurrentIndex(2)
        row2.addWidget(self.priority_combo)
        import_layout.addLayout(row2)

        # Row 3: 备注 + 确认导入
        row3 = QHBoxLayout(); row3.setSpacing(8)
        row3.addWidget(QLabel(get_text("kbm_import_desc_label") + " *:"))
        self.desc_edit = QLineEdit()
        self.desc_edit.setPlaceholderText(get_text("kbm_import_desc_placeholder"))
        row3.addWidget(self.desc_edit, stretch=1)

        self.confirm_btn = QPushButton(get_text("kbm_confirm_import_btn"))
        self.confirm_btn.clicked.connect(self._confirm_import)
        row3.addWidget(self.confirm_btn)
        import_layout.addLayout(row3)

        layout.addWidget(import_section)

    # ─── Tree ──────────────────────────────────
    _CAT_I18N = {
        "01_team_tutorials": "kbm_cat_01", "02_software_manual": "kbm_cat_02",
        "03_examples": "kbm_cat_03", "04_error_cases": "kbm_cat_04",
        "05_reference": "kbm_cat_05", "06_theory_notes": "kbm_cat_06",
        "tutorials": "kbm_sub_tutorials", "Circuit": "kbm_example_circuit",
        "EM": "kbm_example_em", "Mech": "kbm_example_mech",
        "Multi-Physics": "kbm_example_multi", "Thermal": "kbm_example_thermal",
    }

    def _load_tree(self) -> None:
        self.tree.clear()
        if self._kb_root.exists():
            self._add_tree_items(self.tree.invisibleRootItem(), self._kb_root)

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
        self.knowledge_changed.emit()
        QMessageBox.information(self, get_text("kbm_save"), get_text("kbm_save_ok"))

    # ─── 右键菜单：删除文件 ─────────────────────
    def _on_tree_context_menu(self, pos) -> None:
        item = self.tree.itemAt(pos)
        if not item:
            return
        filepath = item.data(0, Qt.UserRole)
        if not filepath:
            return
        path = Path(filepath)
        if not path.is_file():
            return

        menu = QMenu(self)
        del_action = QAction(get_text("kbm_delete_file"), self)
        del_action.triggered.connect(lambda: self._delete_file(path, item))
        menu.addAction(del_action)
        menu.exec(self.tree.viewport().mapToGlobal(pos))

    def _delete_file(self, path: Path, item: QTreeWidgetItem) -> None:
        name = path.name
        reply = QMessageBox.question(
            self,
            get_text("kbm_delete_confirm_title"),
            get_text("kbm_delete_confirm_msg").replace("{name}", name),
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply != QMessageBox.Yes:
            return
        try:
            path.unlink()
            parent = item.parent() or self.tree.invisibleRootItem()
            parent.removeChild(item)
            if self._current_file and str(self._current_file) == str(path):
                self._current_file = None
                self.editor.clear()
                self.file_label.setText(get_text("kbm_select_hint"))
            # 移除空目录
            parent_path = Path(path.parent)
            if parent_path != self._kb_root and not any(parent_path.iterdir()):
                parent_path.rmdir()
                self._load_tree()
            self.knowledge_changed.emit()
        except Exception as e:
            QMessageBox.warning(self, get_text("kbm_delete_error"), str(e))

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
        self._subdir_value = "__AUTO__"
        self.subdir_btn.setText(get_text("kbm_subdir_auto"))

    def _popup_subdir_menu(self) -> None:
        """弹出级联子目录菜单，鼠标悬停自动展开子级"""
        cat_id = self.category_combo.currentData()
        cat_path = self._kb_root / cat_id
        menu = QMenu(self)

        # 首选项
        auto_action = menu.addAction(get_text("kbm_subdir_auto"))
        auto_action.triggered.connect(lambda: self._set_subdir("__AUTO__", get_text("kbm_subdir_auto")))
        menu.addAction(get_text("kbm_subdir_root")).triggered.connect(
            lambda: self._set_subdir("", get_text("kbm_subdir_root")))
        menu.addSeparator()

        if cat_path.exists():
            self._build_subdir_menu(menu, cat_path, "")

        menu.exec(self.subdir_btn.mapToGlobal(self.subdir_btn.rect().bottomLeft()))

    def _build_subdir_menu(self, parent_menu: QMenu, base: Path, prefix: str) -> None:
        """递归构建级联菜单，深层目录作为子菜单悬停展开"""
        for entry in sorted(base.iterdir()):
            if not entry.is_dir() or entry.name.startswith("."):
                continue
            display = self._CAT_I18N.get(entry.name, entry.name)
            rel_path = (prefix + "/" + entry.name).lstrip("/")
            subdirs = [d for d in entry.iterdir() if d.is_dir() and not d.name.startswith(".")]

            if subdirs:
                submenu = QMenu(display, parent_menu)
                parent_menu.addMenu(submenu)
                # 子菜单里也加一个"选此目录"的选项
                pick_action = submenu.addAction(f"[{display}]")
                pick_action.triggered.connect(lambda checked=False, rp=rel_path, d=display: self._set_subdir(rp, d))
                submenu.addSeparator()
                self._build_subdir_menu(submenu, entry, rel_path)
            else:
                action = parent_menu.addAction(display)
                action.triggered.connect(lambda checked=False, rp=rel_path, d=display: self._set_subdir(rp, d))

    def _set_subdir(self, value: str, display: str) -> None:
        self._subdir_value = value
        self.subdir_btn.setText(display)

    # ── 文件选择 ────────────────────────────────
    def _select_file(self) -> None:
        path, _ = QFileDialog.getOpenFileName(
            self, get_text("kbm_select_file_title"), "",
            "Documents (*.pdf *.pptx)"
        )
        if not path:
            return
        self._pending_import_path = path
        self._pending_import_type = "pdf" if path.lower().endswith(".pdf") else "pptx"
        self.file_status.setText(f"📎 {Path(path).name}")
        self.file_status.setStyleSheet(f"color:{COLORS['accent']};font-size:11px;")

    # ── 确认导入（强制备注） ─────────────────────
    def _confirm_import(self) -> None:
        if not self._pending_import_path:
            QMessageBox.information(self, get_text("kbm_no_file"), get_text("kbm_no_file_msg"))
            return
        user_desc = self.desc_edit.text().strip()
        if not user_desc:
            QMessageBox.information(self, get_text("kbm_notes_required"), get_text("kbm_notes_required_msg"))
            return
        self._import_file(self._pending_import_path, self._pending_import_type)
        self._pending_import_path = ""
        self._pending_import_type = ""
        self.file_status.setText(get_text("kbm_no_file"))
        self.file_status.setStyleSheet(f"color:{COLORS['muted']};font-size:11px;")

    def _import_file(self, filepath: str, filetype: str) -> None:
        filepath = Path(filepath)

        # 1. 提取文本
        if filetype == "pdf":
            try:
                from raggg.pipeline.ingestion import _extract_pdf_text
                text = _extract_pdf_text(filepath)
            except ImportError:
                text = f"[PDF: {filepath.name}]\n\n(需要安装 pypdf)"
        else:
            text = extract_pptx_text(filepath)

        if not text.strip():
            QMessageBox.warning(self, get_text("kbm_import_failed"), get_text("kbm_import_empty"))
            return

        # 2. 生成 Markdown
        cat_id = self.category_combo.currentData()
        priority = int(self.priority_combo.currentData())
        markdown = build_import_markdown(filepath, text, cat_id, priority)

        # 3. 目标路径（大分类 + AI/手动子目录，支持多级深度）
        base_dir = self._kb_root / cat_id
        user_desc = self.desc_edit.text().strip()
        subdir_choice = self._subdir_value

        if subdir_choice == "__AUTO__":
            all_subdirs = list_all_subdirs(base_dir)
            chosen_subdir = suggest_subdir(
                self.settings, text, filepath.stem, user_desc, all_subdirs
            )
            target_dir = base_dir / chosen_subdir if chosen_subdir else base_dir
        elif subdir_choice:
            target_dir = base_dir / subdir_choice
        else:
            target_dir = base_dir

        # 4. AI 分析
        suggestion = analyze_document(self.settings, text, filepath.stem, user_desc)

        # 5. 预览并确认
        preview = (
            f"{get_text('kbm_preview_file')}: {filepath.name}\n"
            f"{get_text('kbm_preview_target')}: {target_dir.relative_to(self._kb_root.parent)}\n"
            f"{get_text('kbm_preview_suggestion')}:\n{suggestion}\n\n"
            f"---\n{markdown[:500]}...\n"
        )
        reply = QMessageBox.question(
            self, get_text("kbm_confirm_import"), preview,
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply != QMessageBox.Yes:
            return

        # 6. 写入
        target_dir.mkdir(parents=True, exist_ok=True)
        safe_name = re.sub(r"[^\w\-.]", "_", filepath.stem)
        out_path = target_dir / f"{safe_name}.md"
        out_path.write_text(markdown, encoding="utf-8")
        self._load_tree()
        self.knowledge_changed.emit()

        # 7. 主窗口收到信号后在后台增量更新索引
        msg = (
            f"{get_text('kbm_import_ok_msg')}: "
            f"{out_path.relative_to(self._kb_root.parent)}\n"
            f"{get_text('kbm_index_update_queued')}"
        )
        QMessageBox.information(self, get_text("kbm_import_done"), msg)
