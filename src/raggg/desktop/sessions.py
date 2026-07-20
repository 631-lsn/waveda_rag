from __future__ import annotations

import html

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)

from raggg.desktop.rendering import markdown_to_html, web_wrapper
from raggg.i18n import get_text
from raggg.theme import get_chat_bubble_colors, get_colors


COLORS = get_colors()


class SessionPanel(QFrame):
    """Dedicated widget type for the desktop session sidebar."""

    new_requested = Signal()
    switched = Signal(int)
    delete_requested = Signal()

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("panel")
        self.setFixedWidth(210)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 12, 10, 12)
        layout.setSpacing(6)

        header = QHBoxLayout()
        title = QLabel(get_text("session_panel_title"))
        title.setStyleSheet(
            f"color:{COLORS['text']};font-weight:700;font-size:12px;"
        )
        header.addWidget(title, stretch=1)
        new_button = QPushButton("+")
        new_button.setObjectName("iconButton")
        new_button.setToolTip(f"{get_text('session_new')} (Ctrl+N)")
        new_button.clicked.connect(self.new_requested.emit)
        header.addWidget(new_button)
        layout.addLayout(header)

        self.session_list = QListWidget()
        self.session_list.setStyleSheet(
            "QListWidget { background:transparent;border:0; }"
            f"QListWidget::item {{ padding:7px 10px;color:{COLORS['muted']}; }}"
            f"QListWidget::item:selected {{ color:{COLORS['accent']};font-weight:600; }}"
        )
        self.session_list.currentRowChanged.connect(self.switched.emit)
        layout.addWidget(self.session_list, stretch=1)

        delete_button = QPushButton(get_text("session_delete"))
        delete_button.clicked.connect(self.delete_requested.emit)
        layout.addWidget(delete_button)


class SessionsMixin:
    def _clear_sources_for_session_change(self) -> None:
        self._source_paths.clear()
        self.sources.setHtml(
            self._empty_sources_html(get_text("sources_empty"))
        )

    def _build_session_panel(self) -> QFrame:
        panel = SessionPanel(self)
        self.session_list = panel.session_list
        panel.new_requested.connect(self._new_session)
        panel.switched.connect(self._on_session_switched)
        panel.delete_requested.connect(self._delete_session)
        return panel

    def _refresh_session_list(self) -> None:
        self.session_list.blockSignals(True)
        self.session_list.clear()
        sessions = sorted(
            self._session_manager.sessions.values(),
            key=lambda session: session.created_at,
            reverse=True,
        )
        for session in sessions:
            prefix = "● " if session.id == self._session_manager.current_id else "○ "
            item = QListWidgetItem(f"{prefix}{session.title}")
            item.setData(Qt.UserRole, session.id)
            self.session_list.addItem(item)
            if session.id == self._session_manager.current_id:
                self.session_list.setCurrentItem(item)
        self.session_list.blockSignals(False)

    def _new_session(self) -> None:
        self._session_manager.new_session()
        self._conversation_history = []
        self._clear_sources_for_session_change()
        self.chat.setHtml(
            self._welcome_html(
                chunk_count=(
                    str(len(self.pipeline.store.chunks)) if self.pipeline else "-"
                ),
                model_name=(
                    self.settings.llm_model
                    if self.settings.llm_api_key
                    else get_text("model_local")
                ),
            )
        )
        self._refresh_session_list()

    def _on_session_switched(self, _row: int) -> None:
        item = self.session_list.currentItem()
        if not item:
            return
        session_id = item.data(Qt.UserRole)
        if session_id == self._session_manager.current_id:
            return
        self._session_manager.switch_to(session_id)
        self._clear_sources_for_session_change()
        history = self._session_manager.get_history()
        self._conversation_history = history
        if history:
            self._show_session_content(history)
        else:
            self.chat.setHtml(self._welcome_html())
        self._refresh_session_list()

    def _show_session_content(self, history: list[tuple[str, str]]) -> None:
        bubbles = get_chat_bubble_colors()
        parts = []
        for question, answer in history:
            parts.append(
                "<div style='margin:16px 26px;display:flex;justify-content:flex-end;'>"
                f"<div style='max-width:76%;padding:12px 15px;border-radius:18px;"
                f"background:{bubbles['user_bg']};color:{bubbles['text']};'>"
                f"{html.escape(question)}</div></div>"
            )
            parts.append(
                "<div style='margin:16px 26px;display:flex;justify-content:flex-start;'>"
                f"<div style='max-width:82%;padding:15px 17px;border-radius:18px;"
                f"background:{bubbles['assistant_bg']};color:{bubbles['text']};'>"
                f"{markdown_to_html(answer, citations_clickable=False)}</div></div>"
            )
        self.chat.setHtml(web_wrapper("\n".join(parts)))

    def _delete_session(self) -> None:
        current = self._session_manager.current
        name = current.title if current else ""
        reply = QMessageBox.question(
            self,
            get_text("session_delete_confirm"),
            get_text("session_delete_msg").replace("{name}", name),
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply != QMessageBox.Yes:
            return
        if self._session_manager.delete(self._session_manager.current_id):
            self._conversation_history = self._session_manager.get_history()
            self._clear_sources_for_session_change()
            self.chat.setHtml(self._welcome_html())
            self._refresh_session_list()

    def _toggle_session_panel(self) -> None:
        self.session_panel.setVisible(not self.session_panel.isVisible())
