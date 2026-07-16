from __future__ import annotations

import html
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from PySide6.QtCore import QEvent, QObject, QRectF, QRunnable, Qt, QThreadPool, QTimer, QUrl, Signal, Slot
from PySide6.QtGui import QColor, QBrush, QFont, QIcon, QKeySequence, QLinearGradient, QPainter, QPen, QPixmap, QRadialGradient, QShortcut
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings, QWebEnginePage
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QFormLayout,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from raggg.config import Settings, application_root, config_env_path, load_settings
from raggg.desktop.image_cache import ImageDataUriCache
from raggg.desktop.session_manager import SessionManager
from raggg.i18n import get_text, get_language, set_language, get_welcome_text
from raggg.pipeline.builder import BuildReport, build_knowledge_base
from raggg.pipeline.ingestion import IngestReport, ingest_document
from raggg.pipeline.rag_pipeline import RAGAnswer, RAGPipeline
from raggg.pipeline.source_watch import SourceSnapshot, scan_source_tree, snapshot_changed
from raggg.retrieval.retriever import SearchResult
from raggg.theme import get_theme, set_theme, get_colors, build_style, get_chat_bubble_colors, THEMES

# ── 动态主题 ──
COLORS = get_colors()
APP_STYLE = build_style()



class SourceViewer(QDialog):
    """独立的源文档查看窗口"""

    def __init__(self, title: str, html_content: str, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle(f"{title} — {get_text('source_viewer_title')}")
        self.resize(960, 680)
        self.setMinimumSize(600, 400)
        self.setAttribute(Qt.WA_DeleteOnClose)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.viewer = QWebEngineView()
        self.viewer.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        self.viewer.setHtml(html_content)

        # Bottom bar with close button
        bar = QHBoxLayout()
        bar.setContentsMargins(12, 8, 12, 8)
        bar.addStretch()
        close_btn = QPushButton(get_text("btn_close"))
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.clicked.connect(self.close)
        bar.addWidget(close_btn)

        layout.addWidget(self.viewer, stretch=1)
        layout.addLayout(bar)


