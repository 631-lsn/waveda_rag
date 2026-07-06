from __future__ import annotations

import html
import re
from dataclasses import dataclass
from typing import Callable

from PySide6.QtCore import QObject, QRunnable, Qt, QThreadPool, Signal, Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from raggg.config import Settings, load_settings
from raggg.pipeline.builder import BuildReport, build_knowledge_base
from raggg.pipeline.rag_pipeline import RAGAnswer, RAGPipeline
from raggg.retrieval.retriever import SearchResult


COLORS = {
    "bg": "#07111f",
    "surface": "#0d1726",
    "surface2": "#121f32",
    "surface3": "#18263b",
    "border": "#26364c",
    "text": "#e6edf7",
    "muted": "#92a2b8",
    "subtle": "#607087",
    "accent": "#31d0aa",
    "accent2": "#7dd3fc",
    "warning": "#f5c26b",
    "danger": "#f87171",
    "input": "#0a1322",
}


APP_STYLE = f"""
QWidget {{
    background: {COLORS["bg"]};
    color: {COLORS["text"]};
    font-family: "Microsoft YaHei UI", "Segoe UI";
    font-size: 13px;
}}
QFrame#panel {{
    background: {COLORS["surface"]};
    border: 1px solid {COLORS["border"]};
    border-radius: 12px;
}}
QFrame#metricCard, QFrame#sourceCard {{
    background: {COLORS["surface2"]};
    border: 1px solid {COLORS["border"]};
    border-radius: 10px;
}}
QLabel#title {{
    color: #f8fbff;
    font-size: 24px;
    font-weight: 700;
}}
QLabel#subtitle, QLabel#muted {{
    color: {COLORS["muted"]};
}}
QLabel#section {{
    color: #f8fbff;
    font-size: 14px;
    font-weight: 700;
}}
QLabel#metricLabel {{
    color: {COLORS["muted"]};
    font-size: 12px;
}}
QLabel#metricValue {{
    color: {COLORS["accent"]};
    font-size: 18px;
    font-weight: 700;
}}
QLabel#badge {{
    background: #103430;
    color: {COLORS["accent"]};
    border: 1px solid #1f6b5e;
    border-radius: 12px;
    padding: 8px 14px;
    font-weight: 700;
}}
QPushButton {{
    background: {COLORS["surface3"]};
    color: {COLORS["text"]};
    border: 1px solid {COLORS["border"]};
    border-radius: 9px;
    padding: 10px 12px;
}}
QPushButton:hover {{
    background: #21324a;
    border-color: #3a506d;
}}
QPushButton#primary {{
    background: {COLORS["accent"]};
    color: #041514;
    border: 0;
    font-weight: 700;
}}
QPushButton#primary:hover {{
    background: #5eead4;
}}
QPushButton:disabled {{
    background: #1b2433;
    color: {COLORS["subtle"]};
}}
QLineEdit {{
    background: {COLORS["input"]};
    color: {COLORS["text"]};
    border: 1px solid {COLORS["border"]};
    border-radius: 12px;
    padding: 13px 14px;
    selection-background-color: {COLORS["accent"]};
}}
QTextBrowser {{
    background: {COLORS["input"]};
    border: 1px solid {COLORS["border"]};
    border-radius: 12px;
    padding: 12px;
}}
QScrollBar:vertical {{
    background: transparent;
    width: 10px;
}}
QScrollBar::handle:vertical {{
    background: #26364c;
    border-radius: 5px;
}}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0;
}}
"""


@dataclass(frozen=True)
class AskResult:
    question: str
    answer: RAGAnswer


class WorkerSignals(QObject):
    result = Signal(object)
    error = Signal(str)
    finished = Signal()


class Worker(QRunnable):
    def __init__(self, fn: Callable[[], object]) -> None:
        super().__init__()
        self.fn = fn
        self.signals = WorkerSignals()

    @Slot()
    def run(self) -> None:
        try:
            self.signals.result.emit(self.fn())
        except Exception as exc:
            self.signals.error.emit(str(exc))
        finally:
            self.signals.finished.emit()


INLINE_BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
ORDERED_RE = re.compile(r"^\s*(\d+)\.\s+(.+)$")
UNORDERED_RE = re.compile(r"^\s*[-*]\s+(.+)$")
INLINE_MATH_RE = re.compile(r"\\\((.+?)\\\)")
DISPLAY_MATH_RE = re.compile(r"\\\[(.+?)\\\]|\$\$(.+?)\$\$", re.DOTALL)
FRAC_RE = re.compile(r"\\frac\{([^{}]+)\}\{([^{}]+)\}")


def latex_formula_to_html(formula: str) -> str:
    replacements = {
        r"\partial": "∂",
        r"\nabla": "∇",
        r"\cdot": "·",
        r"\times": "×",
        r"\oiint": "∯",
        r"\iiint": "∭",
        r"\iint": "∬",
        r"\oint": "∮",
        r"\int": "∫",
        r"\rho": "ρ",
        r"\mu": "μ",
        r"\epsilon": "ε",
        r"\omega": "ω",
        r"\alpha": "α",
        r"\beta": "β",
        r"\theta": "θ",
        r"\phi": "φ",
        r"\mathbf": "",
        r"\mathrm": "",
        r"\left": "",
        r"\right": "",
        r"\,": " ",
    }

    converted = formula
    while True:
        updated = FRAC_RE.sub(r"(\1)/(\2)", converted)
        if updated == converted:
            break
        converted = updated
    for src, dst in replacements.items():
        converted = converted.replace(src, dst)
    converted = re.sub(r"\{([^{}]+)\}", r"\1", converted)
    converted = re.sub(r"_\{([^{}]+)\}", r"<sub>\1</sub>", converted)
    converted = re.sub(r"_([A-Za-z0-9])", r"<sub>\1</sub>", converted)
    converted = converted.replace("\\", "")
    converted = converted.replace(",", " ")
    converted = re.sub(r"\s+", " ", converted).strip()
    converted = re.sub(r"∂\s+([A-Za-z\u4e00-\u9fff])", r"∂\1", converted)
    converted = re.sub(r"∇\s+", "∇", converted)
    converted = converted.replace("· ", " · ")
    converted = re.sub(r"\s+", " ", converted).strip()
    return html.escape(converted, quote=False).replace("&lt;sub&gt;", "<sub>").replace("&lt;/sub&gt;", "</sub>")


def latex_to_readable(text: str) -> str:
    def formula_span(rendered: str) -> str:
        style = (
            "background:#0b1e2e;"
            f"border:1px solid {COLORS['border']};"
            "border-radius:6px;"
            "padding:2px 6px;"
            "font-family:'Cambria Math','Times New Roman','Consolas';"
            "font-size:14px;"
            f"color:{COLORS['text']};"
            "white-space:nowrap;"
        )
        return f"<span style=\"{style}\">{rendered}</span>"

    def inline_repl(match: re.Match[str]) -> str:
        return formula_span(latex_formula_to_html(match.group(1)))

    def display_repl(match: re.Match[str]) -> str:
        return formula_span(latex_formula_to_html(match.group(1) or match.group(2) or ""))

    text = DISPLAY_MATH_RE.sub(display_repl, text)
    return INLINE_MATH_RE.sub(inline_repl, text)


def render_inline_markdown(text: str) -> str:
    escaped = html.escape(latex_to_readable(text), quote=False)
    escaped = re.sub(r"&lt;span style=\"(.+?)\"&gt;", r'<span style="\1">', escaped)
    escaped = re.sub(r"&lt;span style=&quot;(.+?)&quot;&gt;", r'<span style="\1">', escaped)
    escaped = escaped.replace("&lt;/span&gt;", "</span>")
    escaped = escaped.replace("&lt;sub&gt;", "<sub>").replace("&lt;/sub&gt;", "</sub>")
    return INLINE_BOLD_RE.sub(r"<strong>\1</strong>", escaped)


def markdown_to_html(text: str) -> str:
    lines = text.strip().splitlines()
    output: list[str] = []
    list_mode: str | None = None

    def close_list() -> None:
        nonlocal list_mode
        if list_mode:
            output.append(f"</{list_mode}>")
            list_mode = None

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            close_list()
            output.append("<div style='height:8px;'></div>")
            continue

        ordered = ORDERED_RE.match(line)
        unordered = UNORDERED_RE.match(line)
        if ordered:
            if list_mode != "ol":
                close_list()
                output.append("<ol>")
                list_mode = "ol"
            output.append(f"<li>{render_inline_markdown(ordered.group(2))}</li>")
            continue
        if unordered:
            if list_mode != "ul":
                close_list()
                output.append("<ul>")
                list_mode = "ul"
            output.append(f"<li>{render_inline_markdown(unordered.group(1))}</li>")
            continue

        close_list()
        if line.startswith(">"):
            output.append(
                f"<blockquote style='margin:8px 0;padding:8px 12px;border-left:3px solid {COLORS['accent']};color:{COLORS['muted']};'>"
                f"{render_inline_markdown(line.lstrip('> ').strip())}</blockquote>"
            )
        elif line.startswith("#"):
            heading = line.lstrip("#").strip()
            output.append(
                f"<div style='margin:12px 0 6px 0;color:{COLORS['accent']};font-weight:700;'>"
                f"{render_inline_markdown(heading)}</div>"
            )
        else:
            output.append(f"<p style='margin:7px 0;line-height:1.58;'>{render_inline_markdown(line)}</p>")

    close_list()
    return "\n".join(output)


class MetricCard(QFrame):
    def __init__(self, label: str, value: str, color: str = COLORS["accent"]) -> None:
        super().__init__()
        self.setObjectName("metricCard")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 12, 14, 12)
        layout.setSpacing(4)
        title = QLabel(label)
        title.setObjectName("metricLabel")
        self.value_label = QLabel(value)
        self.value_label.setObjectName("metricValue")
        self.value_label.setStyleSheet(f"color: {color};")
        layout.addWidget(title)
        layout.addWidget(self.value_label)

    def set_value(self, value: str, color: str | None = None) -> None:
        self.value_label.setText(value)
        if color:
            self.value_label.setStyleSheet(f"color: {color};")


class WorkbenchWindow(QMainWindow):
    def __init__(self, settings: Settings) -> None:
        super().__init__()
        self.settings = settings
        self.pipeline: RAGPipeline | None = None
        self.thread_pool = QThreadPool.globalInstance()
        self._active_workers: list[Worker] = []
        self.is_busy = False
        self.setWindowTitle("WavEDA Knowledge Workbench")
        self.resize(1360, 840)
        self.setMinimumSize(1120, 720)
        self._build_ui()
        self._load_pipeline_if_ready()

    def _build_ui(self) -> None:
        root = QWidget()
        root.setObjectName("root")
        root.setStyleSheet(APP_STYLE)
        self.setCentralWidget(root)

        shell = QGridLayout(root)
        shell.setContentsMargins(22, 20, 22, 20)
        shell.setHorizontalSpacing(16)
        shell.setVerticalSpacing(16)
        shell.setColumnStretch(0, 0)
        shell.setColumnStretch(1, 1)
        shell.setColumnStretch(2, 0)
        shell.setRowStretch(1, 1)

        shell.addLayout(self._header(), 0, 0, 1, 3)
        shell.addWidget(self._left_panel(), 1, 0)
        shell.addWidget(self._chat_panel(), 1, 1)
        shell.addWidget(self._source_panel(), 1, 2)

    def _header(self) -> QHBoxLayout:
        header = QHBoxLayout()
        header.setContentsMargins(2, 0, 2, 0)
        titles = QVBoxLayout()
        title = QLabel("WavEDA Knowledge Workbench")
        title.setObjectName("title")
        subtitle = QLabel("软件帮助优先的仿真知识检索与问答工作台")
        subtitle.setObjectName("subtitle")
        titles.addWidget(title)
        titles.addWidget(subtitle)
        header.addLayout(titles)
        header.addStretch(1)
        badge = QLabel("WavEDA 优先")
        badge.setObjectName("badge")
        header.addWidget(badge, alignment=Qt.AlignRight | Qt.AlignVCenter)
        return header

    def _left_panel(self) -> QFrame:
        panel = self._panel(270)
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        section = QLabel("工作台状态")
        section.setObjectName("section")
        layout.addWidget(section)

        self.status_card = MetricCard("知识库", "正在载入")
        self.chunk_card = MetricCard("知识块", "-", COLORS["warning"])
        self.model_card = MetricCard("模型", "DeepSeek")
        layout.addWidget(self.status_card)
        layout.addWidget(self.chunk_card)
        layout.addWidget(self.model_card)

        # 重建知识库按钮已移除 — 改用 scripts/add_document.py 追加文档
        self.reload_button = self._button("重新载入索引")
        self.reload_button.clicked.connect(self._load_pipeline_if_ready)
        layout.addWidget(self.reload_button)

        prompt_label = QLabel("快捷问题")
        prompt_label.setObjectName("section")
        layout.addSpacing(10)
        layout.addWidget(prompt_label)
        for prompt in ("波端口怎么设置？", "PML 和吸收边界有什么关系？", "如何设置平面波激励？"):
            button = self._button(prompt)
            button.clicked.connect(lambda _checked=False, text=prompt: self._ask(text))
            layout.addWidget(button)

        note = QLabel("涉及 WavEDA 的问题会优先检索软件帮助文档，理论笔记作为补充。")
        note.setObjectName("muted")
        note.setWordWrap(True)
        layout.addStretch(1)
        layout.addWidget(note)
        return panel

    def _chat_panel(self) -> QFrame:
        panel = self._panel()
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        top = QHBoxLayout()
        section = QLabel("问答")
        section.setObjectName("section")
        self.activity_label = QLabel("就绪")
        self.activity_label.setStyleSheet(f"color: {COLORS['accent']};")
        top.addWidget(section)
        top.addStretch(1)
        top.addWidget(self.activity_label)
        layout.addLayout(top)

        self.chat = QTextBrowser()
        self.chat.setOpenExternalLinks(False)
        self.chat.setHtml(self._welcome_html())
        layout.addWidget(self.chat, stretch=1)

        composer = QHBoxLayout()
        composer.setSpacing(10)
        self.question = QLineEdit()
        self.question.setPlaceholderText("输入WavEDA问题，如：波端口怎么设置？| PML和吸收边界的关系？")
        self.question.returnPressed.connect(self._ask)
        self.ask_button = self._button("提问", primary=True)
        self.ask_button.clicked.connect(self._ask)
        composer.addWidget(self.question, stretch=1)
        composer.addWidget(self.ask_button)
        layout.addLayout(composer)
        return panel

    def _source_panel(self) -> QFrame:
        panel = self._panel(360)
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)
        title = QLabel("来源证据")
        title.setObjectName("section")
        subtitle = QLabel("按相关性排序，WavEDA 文档优先")
        subtitle.setObjectName("muted")
        self.sources = QTextBrowser()
        self.sources.setHtml(self._empty_sources_html())
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.sources, stretch=1)
        return panel

    def _panel(self, fixed_width: int | None = None) -> QFrame:
        panel = QFrame()
        panel.setObjectName("panel")
        if fixed_width:
            panel.setFixedWidth(fixed_width)
        else:
            panel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        return panel

    def _button(self, text: str, primary: bool = False) -> QPushButton:
        button = QPushButton(text)
        if primary:
            button.setObjectName("primary")
        button.setCursor(Qt.PointingHandCursor)
        return button

    def _load_pipeline_if_ready(self) -> None:
        index_dir = self.settings.data_dir / "index"
        if not (index_dir / "chunks.json").exists() or not (index_dir / "vectors.npy").exists():
            self.pipeline = None
            self.status_card.set_value("未构建", COLORS["danger"])
            self.chunk_card.set_value("-", COLORS["warning"])
            self.sources.setHtml(self._empty_sources_html("知识库尚未构建。请点击左侧“重建知识库”。"))
            return
        self.pipeline = RAGPipeline(self.settings)
        self.status_card.set_value("已载入", COLORS["accent"])
        self.chunk_card.set_value(str(len(self.pipeline.store.chunks)), COLORS["warning"])
        model_name = self.settings.llm_model if self.settings.llm_api_key else "本地片段"
        model_color = COLORS["accent"] if self.settings.llm_api_key else COLORS["warning"]
        self.model_card.set_value(model_name, model_color)
        self.sources.setHtml(self._empty_sources_html())

    def _rebuild_async(self) -> None:
        if self.is_busy:
            return
        self._set_busy(True, "正在重建知识库")
        worker = Worker(lambda: build_knowledge_base(self.settings))
        worker.signals.result.connect(self._on_rebuild_done)
        worker.signals.error.connect(lambda message: self._show_error("重建失败", message))
        worker.signals.finished.connect(lambda: self._set_busy(False, "就绪"))
        self._start_worker(worker)

    def _on_rebuild_done(self, report: BuildReport) -> None:
        self.chunk_card.set_value(str(report.chunk_count), COLORS["warning"])
        self._load_pipeline_if_ready()

    def _ask(self, question: str | None = None) -> None:
        if self.is_busy:
            return
        text = (question or self.question.text()).strip()
        if not text:
            return
        if self.pipeline is None:
            QMessageBox.information(self, "未载入知识库", "请先重建或载入知识库。")
            return
        self.question.clear()
        self._append_user(text)
        self._set_busy(True, "正在检索与生成")
        worker = Worker(lambda: AskResult(text, self.pipeline.ask(text)))
        worker.signals.result.connect(self._on_answer_done)
        worker.signals.error.connect(lambda message: self._append_assistant(f"生成失败：{message}"))
        worker.signals.finished.connect(lambda: self._set_busy(False, "就绪"))
        self._start_worker(worker)

    def _start_worker(self, worker: Worker) -> None:
        self._active_workers.append(worker)
        worker.signals.finished.connect(lambda: self._forget_worker(worker))
        self.thread_pool.start(worker)

    def _forget_worker(self, worker: Worker) -> None:
        if worker in self._active_workers:
            self._active_workers.remove(worker)

    def _on_answer_done(self, result: AskResult) -> None:
        self._append_assistant(result.answer.answer)
        self.sources.setHtml(self._sources_html(result.answer.sources))

    def _set_busy(self, busy: bool, text: str) -> None:
        self.is_busy = busy
        self.activity_label.setText(text)
        self.activity_label.setStyleSheet(f"color: {COLORS['warning' if busy else 'accent']};")
        for button in (self.ask_button, self.rebuild_button, self.reload_button):
            button.setDisabled(busy)

    def _append_user(self, question: str) -> None:
        self.chat.append(
            f"""
            <div style="margin:16px 0 8px 0;">
              <div style="color:{COLORS['accent']};font-weight:700;">你</div>
              <div style="margin-top:6px;padding:12px 14px;border-radius:12px;background:#102033;color:{COLORS['text']};">
                {html.escape(question)}
              </div>
            </div>
            """
        )

    def _append_assistant(self, answer: str) -> None:
        rendered = markdown_to_html(answer)
        self.chat.append(
            f"""
            <div style="margin:16px 0 18px 0;">
              <div style="color:{COLORS['warning']};font-weight:700;">RAG</div>
              <div style="margin-top:6px;padding:14px 16px;border-radius:12px;background:#111c2f;color:{COLORS['text']};line-height:1.55;">
                {rendered}
              </div>
            </div>
            """
        )

    def _sources_html(self, sources: list[SearchResult]) -> str:
        cards: list[str] = []
        seen: set[str] = set()
        for source in sources:
            chunk = source.chunk
            key = f"{chunk.relative_path}:{chunk.section}"
            if key in seen:
                continue
            seen.add(key)
            label = "WavEDA 帮助文档" if chunk.source_type == "waveda_help" else "理论笔记"
            label_color = COLORS["accent"] if chunk.source_type == "waveda_help" else COLORS["accent2"]
            snippet = html.escape(chunk.content[:560]).replace("\n", " ")
            cards.append(
                f"""
                <div style="margin:0 0 14px 0;padding:14px;border-radius:12px;background:{COLORS['surface2']};border:1px solid {COLORS['border']};">
                  <div style="color:{COLORS['text']};font-weight:700;font-size:14px;">{html.escape(chunk.title)}</div>
                  <div style="margin-top:6px;color:{label_color};font-size:12px;">{label} | 分数 {source.score:.3f}</div>
                  <div style="margin-top:4px;color:{COLORS['muted']};font-size:12px;">{html.escape(chunk.relative_path)}</div>
                  <div style="margin-top:10px;color:{COLORS['text']};line-height:1.45;">{snippet}</div>
                </div>
                """
            )
            if len(cards) >= 6:
                break
        return self._html_page("".join(cards) or self._empty_sources_html())

    def _welcome_html(self) -> str:
        return self._html_page(
            f"""
            <div style="padding:4px 2px 14px 2px;">
              <div style="color:{COLORS['accent']};font-weight:700;font-size:16px;">就绪</div>
              <div style="margin-top:8px;color:{COLORS['muted']};line-height:1.6;">
                询问 WavEDA 的端口、边界、PML、网格、激励设置，或用理论笔记补充解释电磁概念。
              </div>
            </div>
            """
        )

    def _empty_sources_html(self, message: str = "提出问题后，这里会显示可追溯的来源证据。") -> str:
        return self._html_page(
            f"""
            <div style="padding:16px;border-radius:12px;background:{COLORS['surface2']};border:1px solid {COLORS['border']};color:{COLORS['muted']};line-height:1.6;">
              {html.escape(message)}
            </div>
            """
        )

    def _html_page(self, body: str) -> str:
        return f"""
        <html>
        <body style="background:{COLORS['input']};color:{COLORS['text']};font-family:'Microsoft YaHei UI','Segoe UI';font-size:13px;">
        {body}
        </body>
        </html>
        """

    def _show_error(self, title: str, message: str) -> None:
        QMessageBox.critical(self, title, message)


class RAGDesktopApp:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or load_settings()

    def run(self) -> int:
        app = QApplication.instance() or QApplication([])
        app.setStyleSheet(APP_STYLE)
        window = WorkbenchWindow(self.settings)
        window.show()
        self.window = window
        return app.exec()


def run_desktop_app() -> int:
    return RAGDesktopApp().run()
