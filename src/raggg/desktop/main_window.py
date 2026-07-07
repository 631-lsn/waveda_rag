from __future__ import annotations

import base64
import html
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from PySide6.QtCore import QObject, QRunnable, Qt, QThreadPool, QUrl, Signal, Slot
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings, QWebEnginePage
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QDialogButtonBox,
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

from raggg.config import Settings, load_settings
from raggg.pipeline.builder import BuildReport, build_knowledge_base
from raggg.pipeline.rag_pipeline import RAGAnswer, RAGPipeline
from raggg.retrieval.retriever import SearchResult


COLORS = {
    "bg": "#07111f",
    "surface": "#0d1726",
    "surface2": "#1a2a43",
    "surface3": "#2F4564",
    "border": "#475a75",
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


IMAGE_MD_RE = re.compile(r">?\s*图片:\s*`\.?/(images/[^`)]+\.(?:png|jpg|jpeg|gif|svg))`")
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
    converted = re.sub(r"∂\s+([A-Za-z一-鿿])", r"∂\1", converted)
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
    list_prefix: str = ""  # 缓存列表项间空白

    def close_list() -> None:
        nonlocal list_mode, list_prefix
        if list_mode:
            output.append(f"</{list_mode}>")
        list_mode = None
        list_prefix = ""

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            list_prefix += "<div style='height:4px;'></div>"
            continue

        ordered = ORDERED_RE.match(line)
        unordered = UNORDERED_RE.match(line)
        if ordered:
            if list_mode != "ol":
                close_list()
                output.append(list_prefix + "<ol>")
                list_prefix = ""
                list_mode = "ol"
            output.append(f"<li>{render_inline_markdown(ordered.group(2))}</li>")
            continue
        if unordered:
            if list_mode == "ol":
                # 有序列表内不嵌套无序列表，当作文本追加到上一个<li>
                if output:
                    last = output[-1]
                    if last.endswith("</li>"):
                        output[-1] = last[:-5] + "<br>" + render_inline_markdown(unordered.group(1)) + "</li>"
                continue
            if list_mode != "ul":
                close_list()
                output.append(list_prefix + "<ul>")
                list_prefix = ""
                list_mode = "ul"
            output.append(f"<li>{render_inline_markdown(unordered.group(1))}</li>")
            continue

        close_list()
        if list_prefix:
            output.append(list_prefix)
            list_prefix = ""
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
    if list_prefix:
        output.append(list_prefix)
    result = "\n".join(output)
    # Merge broken ordered lists: </ol>...<ol> -> nothing
    result = re.sub(r"</ol>(<div[^>]*></div>)<ol>", r"\1", result)
    # Convert image markdown to actual <img> tags pointing to helpHtml
    result = _convert_image_refs(result)
    return result


IMAGE_PATH_RE = re.compile(r"[`\"]?(\.?/?images/[^`\"\s)]+\.(?:png|jpg|jpeg|gif|svg))[`\"]?", re.IGNORECASE)

MIME_MAP = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
            ".gif": "image/gif", ".svg": "image/svg+xml"}


_data_uri_cache: dict[str, str] = {}


def _path_to_data_uri(filepath: str) -> str:
    """将本地图片文件转为 base64 data URI，带缓存"""
    if filepath in _data_uri_cache:
        return _data_uri_cache[filepath]
    try:
        with open(filepath, "rb") as f:
            data = f.read()
        ext = os.path.splitext(filepath)[1].lower()
        mime = MIME_MAP.get(ext, "image/png")
        b64 = base64.b64encode(data).decode("ascii")
        result = f"data:{mime};base64,{b64}"
        _data_uri_cache[filepath] = result
        return result
    except Exception:
        return ""


def _preload_all_images(image_index: dict[str, str]) -> None:
    """后台线程：预编码所有图片为data URI"""
    for path in image_index.values():
        _path_to_data_uri(path)


def _extract_images_from_sources(sources: list, image_index: dict[str, str],
                                  min_score: float = 0.75) -> list[tuple[str, str]]:
    """从检索到的来源chunk中提取图片路径, 过滤低分来源, 返回 [(绝对路径, 标题), ...]"""
    seen = set()
    results = []
    for src in sources:
        if src.score < min_score:
            continue
        content = src.chunk.content
        title = src.chunk.title
        for match in IMAGE_PATH_RE.finditer(content):
            img_name = os.path.basename(match.group(1))
            if img_name in seen or img_name not in image_index:
                continue
            seen.add(img_name)
            results.append((image_index[img_name], title))
    return results


def _convert_image_refs(html_text: str) -> str:
    """把 图片: `./images/xxx.png` 换成实际可显示的 <img> 标签"""
    def _img_repl(match: re.Match[str]) -> str:
        img_rel = match.group(1)  # images/xxx.png
        # Find actual image in helpHtml
        project_root = Path(__file__).resolve().parents[3]
        help_base = project_root / "wavEDA_docs" / "helpHtml" / "helpHtml"
        # Search recursively for the image
        for root, dirs, files in os.walk(help_base):
            if "images" in dirs:
                candidate = os.path.join(root, img_rel.replace("/", os.sep))
                if os.path.exists(candidate):
                    data_uri = _path_to_data_uri(candidate)
                    if data_uri:
                        return f'<p style="margin:8px 0;"><img src="{data_uri}" style="max-width:100%;border-radius:8px;border:1px solid {COLORS["border"]};" alt="示意图"></p>'
                    return match.group(0)
        return match.group(0)  # fallback: leave as text
    return IMAGE_MD_RE.sub(_img_repl, html_text)


WEBVIEW_BG = COLORS["input"]
WEBVIEW_TEXT = COLORS["text"]


def web_wrapper(body_html: str, extra_css: str = "") -> str:
    return f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><style>
body {{
    font-family: "Microsoft YaHei UI", "Segoe UI", sans-serif;
    font-size: 14px;
    background: {WEBVIEW_BG};
    color: {WEBVIEW_TEXT};
    margin: 0;
    padding: 0;
}}
p {{ margin: 7px 0; line-height: 1.58; }}
ol, ul {{ margin: 8px 0; padding-left: 24px; }}
li {{ margin: 4px 0; }}
strong {{ color: {COLORS["accent"]}; }}
blockquote {{ margin: 8px 0; padding: 8px 12px; border-left: 3px solid {COLORS["accent"]}; color: {COLORS["muted"]}; }}
a {{ color: {COLORS["accent2"]}; }}
{extra_css}
</style></head><body>{body_html}</body></html>"""


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


LLM_PROVIDERS = [
    ("DeepSeek",      "https://api.deepseek.com",                       "deepseek-chat"),
    ("Kimi (Moonshot)", "https://api.moonshot.cn/v1",                    "moonshot-v1-8k"),
    ("千问 (通义)",     "https://dashscope.aliyuncs.com/compatible-mode/v1", "qwen-plus"),
    ("百炼 (阿里云)",   "https://dashscope.aliyuncs.com/compatible-mode/v1", "qwen-plus"),
    ("OpenAI",        "https://api.openai.com/v1",                      "gpt-4o-mini"),
]


class ApiSettingsDialog(QDialog):
    def __init__(self, settings: Settings, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.settings = settings
        self.setWindowTitle("API 设置 — 选择大模型")
        self.setMinimumWidth(400)
        layout = QVBoxLayout(self)
        layout.setSpacing(14)

        desc = QLabel("选择大模型提供商，输入你的 API Key 即可。\nBase URL 和模型名称会自动填写。")
        desc.setStyleSheet(f"color:{COLORS['muted']};font-size:12px;")
        desc.setWordWrap(True)
        layout.addWidget(desc)

        form = QFormLayout()
        form.setSpacing(10)

        self.provider_combo = QComboBox()
        for name, _, _ in LLM_PROVIDERS:
            self.provider_combo.addItem(name)
        current_url = settings.llm_base_url.rstrip("/")
        current_idx = 0
        for i, (_, url, _) in enumerate(LLM_PROVIDERS):
            if url == current_url:
                current_idx = i; break
        self.provider_combo.setCurrentIndex(current_idx)
        self.provider_combo.currentIndexChanged.connect(self._on_provider_changed)
        form.addRow("大模型:", self.provider_combo)

        self.key_edit = QLineEdit(settings.llm_api_key)
        self.key_edit.setPlaceholderText("sk-...")
        self.key_edit.setEchoMode(QLineEdit.Password)
        form.addRow("API Key:", self.key_edit)

        self.info_label = QLabel()
        self.info_label.setStyleSheet(f"color:{COLORS['subtle']};font-size:11px;")
        self._on_provider_changed(current_idx)
        form.addRow(self.info_label)

        layout.addLayout(form)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self._save_and_accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def _on_provider_changed(self, index: int) -> None:
        _, url, model = LLM_PROVIDERS[index]
        self.info_label.setText(f"URL: {url}   |   Model: {model}")

    def _save_and_accept(self) -> None:
        _, url, model = LLM_PROVIDERS[self.provider_combo.currentIndex()]
        env_path = Path(__file__).resolve().parents[3] / "config" / ".env"
        lines = []
        if env_path.exists():
            lines = env_path.read_text(encoding="utf-8").splitlines()
        new_lines = []
        for line in lines:
            if not any(line.startswith(k + "=") for k in ("RAG_LLM_BASE_URL", "RAG_LLM_API_KEY", "RAG_LLM_MODEL")):
                new_lines.append(line)
        new_lines.append(f"RAG_LLM_BASE_URL={url}")
        new_lines.append(f"RAG_LLM_API_KEY={self.key_edit.text().strip()}")
        new_lines.append(f"RAG_LLM_MODEL={model}")
        env_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
        self.accept()


class WorkbenchWindow(QMainWindow):
    def __init__(self, settings: Settings) -> None:
        super().__init__()
        self.settings = settings
        self.pipeline: RAGPipeline | None = None
        self.thread_pool = QThreadPool.globalInstance()
        self._active_workers: list[Worker] = []
        self.is_busy = False
        self._last_qa: tuple[str, str] = ("", "")  # (question, answer)
        self._fav_file = settings.data_dir / "favorites.json"
        self._project_root = Path(__file__).resolve().parents[3]
        self.setWindowTitle("WavEDA Knowledge Workbench")
        icon_path = self._project_root / "wavEDA_docs" / "helpHtml" / "image" / "waveda.png"
        if icon_path.exists():
            self.setWindowIcon(QIcon(str(icon_path)))
        self.resize(1360, 840)
        self.setMinimumSize(1120, 720)
        self._image_index: dict[str, str] = {}  # filename -> absolute_path
        self._build_image_index()
        self._build_ui()
        self._load_pipeline_if_ready()
        # 后台预编码所有图片，用户第一次问就不慢了
        self._preload_images()

    def _preload_images(self) -> None:
        """后台异步预编码所有图片到缓存，用户第一次提问时不再等待"""
        from functools import partial
        worker = Worker(partial(_preload_all_images, self._image_index))
        worker.signals.finished.connect(lambda: print("Image preload complete"))
        self.thread_pool.start(worker)

    def _build_image_index(self) -> None:
        """预建图片索引: 文件名 -> 绝对路径"""
        help_base = self._project_root / "wavEDA_docs" / "helpHtml" / "helpHtml"
        if not help_base.exists():
            return
        for root, dirs, files in os.walk(str(help_base)):
            if os.path.basename(root) == "images":
                for fname in files:
                    if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
                        self._image_index[fname] = os.path.join(root, fname).replace(os.sep, "/")
        print(f"Image index: {len(self._image_index)} images loaded")

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
        title_row = QHBoxLayout()
        icon_label = QLabel()
        icon_label.setPixmap(QPixmap(str(self._project_root / "wavEDA_docs" / "helpHtml" / "image" / "waveda.png"))
                             .scaled(36, 36, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        icon_label.setFixedSize(42, 42)
        title_row.addWidget(icon_label)
        title = QLabel("WavEDA Knowledge Workbench")
        title.setObjectName("title")
        title_row.addWidget(title, stretch=1)
        titles.addLayout(title_row)
        subtitle = QLabel("WavEDA 仿真软件知识问答助手")
        subtitle.setObjectName("subtitle")
        titles.addWidget(subtitle)
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

        self.api_button = self._button("API 设置")
        self.api_button.clicked.connect(self._open_api_settings)
        layout.addWidget(self.api_button)

        self.fav_button = self._button("收藏夹")
        self.fav_button.clicked.connect(self._open_favorites)
        layout.addWidget(self.fav_button)

        prompt_label = QLabel("快捷问题")
        prompt_label.setObjectName("section")
        layout.addSpacing(10)
        layout.addWidget(prompt_label)
        for prompt in ("波端口怎么设置？", "PML 和吸收边界有什么关系？", "如何设置平面波激励？"):
            button = self._button(prompt)
            button.clicked.connect(lambda _checked=False, text=prompt: self._ask(text))
            layout.addWidget(button)

        note = QLabel("优先检索 WavEDA 帮助文档和团队教程，理论笔记作为补充。")
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

        self.chat = QWebEngineView()
        self.chat.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        self.chat.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, False)
        self.chat.setHtml(self._welcome_html())
        self.chat.setMinimumHeight(300)
        self.chat.page().setProperty("_workbench", self)  # 让页面能找回窗口引用
        layout.addWidget(self.chat, stretch=1)

        # 自定义 console 消息拦截：JS 中 console.log('RAGGG_XXX') 触发 Python 回调
        class _FavPage(QWebEnginePage):
            def javaScriptConsoleMessage(self, level, msg, line, source):
                if msg == "RAGGG_FAV":
                    wb = self.parent().findChild(WorkbenchWindow)
                    if wb is None:
                        wb = self.property("_workbench")
                    if wb:
                        wb._do_fav()
                elif msg.startswith("RAGGG_FAVDEL:"):
                    idx = int(msg.split(":")[1])
                    wb = self.parent().findChild(WorkbenchWindow)
                    if wb is None:
                        wb = self.property("_workbench")
                    if wb and hasattr(wb, '_fav_dialog'):
                        wb._do_fav_del(idx)
        self.chat.setPage(_FavPage(self.chat))

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
        subtitle = QLabel("按相关性排序，帮助文档和团队教程优先")
        subtitle.setObjectName("muted")
        self.sources = QWebEngineView()
        self.sources.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
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
            self.sources.setHtml(self._empty_sources_html("知识库尚未构建。"))
            return
        self.pipeline = RAGPipeline(self.settings)
        self.status_card.set_value("已载入", COLORS["accent"])
        self.chunk_card.set_value(str(len(self.pipeline.store.chunks)), COLORS["warning"])
        model_name = self.settings.llm_model if self.settings.llm_api_key else "本地片段"
        model_color = COLORS["accent"] if self.settings.llm_api_key else COLORS["warning"]
        self.model_card.set_value(model_name, model_color)
        self.sources.setHtml(self._empty_sources_html())

    def _do_fav(self) -> None:
        q, a = self._last_qa
        if q and a:
            favs = self._load_favs()
            favs.append({"question": q, "answer": a, "time": __import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M")})
            with open(self._fav_file, "w", encoding="utf-8") as f:
                import json as _json; _json.dump(favs, f, ensure_ascii=False, indent=2)
            self.status_card.set_value("已收藏", COLORS["accent"])

    def _load_favs(self) -> list:
        import json as _json
        if self._fav_file.exists():
            with open(self._fav_file, "r", encoding="utf-8") as f:
                return _json.load(f)
        return []


    def _open_favorites(self) -> None:
        favs = self._load_favs()
        if not favs:
            QMessageBox.information(self, "收藏夹", "还没有收藏任何问答。")
            return
        dialog = QDialog(self)
        dialog.setWindowTitle("收藏夹")
        dialog.resize(750, 550)
        layout = QVBoxLayout(dialog)
        from PySide6.QtWidgets import QScrollArea
        scroll = QWidget()
        scroll_layout = QVBoxLayout(scroll)
        for i, f in enumerate(reversed(favs)):
            card = QFrame()
            card.setObjectName("metricCard")
            card_layout = QVBoxLayout(card)
            q_label = QLabel(f"Q: {f['question']}")
            q_label.setStyleSheet(f"color:{COLORS['accent']};font-weight:700;")
            time_label = QLabel(f.get('time', ''))
            time_label.setStyleSheet(f"color:{COLORS['subtle']};font-size:11px;")
            hdr = QHBoxLayout()
            hdr.addWidget(q_label, stretch=1)
            hdr.addWidget(time_label)
            card_layout.addLayout(hdr)
            a_label = QLabel(f['answer'][:500])
            a_label.setWordWrap(True)
            a_label.setStyleSheet(f"color:{COLORS['text']};margin-top:6px;")
            card_layout.addWidget(a_label)
            del_btn = QPushButton("删除")
            del_btn.setStyleSheet(f"background:{COLORS['danger']};color:#fff;border:0;padding:2px 8px;font-size:11px;")
            real_idx = len(favs) - 1 - i
            del_btn.clicked.connect(lambda ch=False, idx=real_idx: self._do_fav_del(idx, dialog))
            card_layout.addWidget(del_btn)
            scroll_layout.addWidget(card)
        scroll_layout.addStretch(1)
        area = QScrollArea()
        area.setWidgetResizable(True)
        area.setWidget(scroll)
        layout.addWidget(area)
        dialog.exec()

    def _do_fav_del(self, idx: int, dialog: QDialog) -> None:
        favs = self._load_favs()
        if 0 <= idx < len(favs):
            del favs[idx]
            with open(self._fav_file, "w", encoding="utf-8") as f:
                import json as _json; _json.dump(favs, f, ensure_ascii=False, indent=2)
        dialog.accept()
        self._open_favorites()

    def _open_api_settings(self) -> None:
        dialog = ApiSettingsDialog(self.settings, self)
        if dialog.exec() == QDialog.Accepted:
            self.settings = load_settings()
            self._load_pipeline_if_ready()
            QMessageBox.information(self, "已保存", "API 设置已更新，重启应用后生效。")

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
        # ---- 追加来源中的图片 ----
        all_images = _extract_images_from_sources(result.answer.sources, self._image_index)
        if all_images:
            img_html = '<div style="margin:12px 0 8px 0;"><div style="color:' + COLORS["accent2"] + ';font-weight:700;margin-bottom:8px;">操作截图</div>'
            for img_path, title in all_images[:6]:
                abs_path = img_path.replace(os.sep, "/")
                data_uri = _path_to_data_uri(abs_path)
            if data_uri:
                img_html += f'<p style="margin:6px 0;"><span style="color:{COLORS["muted"]};font-size:12px;">{html.escape(title)}</span><br><img src="{data_uri}" style="max-width:100%;max-height:400px;border-radius:8px;border:1px solid {COLORS["border"]};margin-top:4px;"></p>'
            img_html += '</div>'
            self._append_html(web_wrapper(img_html))
        self.sources.setHtml(self._sources_html(result.answer.sources))

    def _set_busy(self, busy: bool, text: str) -> None:
        self.is_busy = busy
        self.activity_label.setText(text)
        self.activity_label.setStyleSheet(f"color: {COLORS['warning' if busy else 'accent']};")
        for button in (self.ask_button, self.reload_button):
            button.setDisabled(busy)

    def _append_user(self, question: str) -> None:
        self._last_qa = (question, "")  # 记住问题，等回答来了配对
        msg_html = web_wrapper(
            f"""<div style="margin:16px 0 8px 0;">
              <div style="color:{COLORS['accent']};font-weight:700;font-size:13px;">你</div>
              <div style="margin-top:6px;padding:12px 14px;border-radius:12px;background:#102033;color:{COLORS['text']};">
                {html.escape(question)}
              </div>
            </div>"""
        )
        self._append_html(msg_html)

    def _append_assistant(self, answer: str) -> None:
        self._last_qa = (self._last_qa[0], answer)  # 配对完成
        rendered = markdown_to_html(answer)
        msg_html = web_wrapper(
            f"""<div style="margin:16px 0 18px 0;">
              <div style="display:flex;align-items:center;gap:8px;">
                <div style="color:{COLORS['warning']};font-weight:700;font-size:13px;">RAG</div>
                <button onclick="var p=this.parentElement.nextElementSibling;var t=document.createElement('textarea');t.value=p.innerText;document.body.appendChild(t);t.select();document.execCommand('copy');document.body.removeChild(t);var s=this.innerHTML;this.innerHTML='已复制!';setTimeout(function(){{this.innerHTML=s;}}.bind(this),1000)"
                  style="background:{COLORS['surface3']};color:{COLORS['muted']};border:1px solid {COLORS['border']};border-radius:6px;padding:2px 10px;font-size:11px;cursor:pointer;"
                  onmouseover="this.style.color='{COLORS['accent']}'" onmouseout="this.style.color='{COLORS['muted']}'">复制</button>
                <button onclick="console.log('RAGGG_FAV')"
                  style="background:{COLORS['surface3']};color:{COLORS['muted']};border:1px solid {COLORS['border']};border-radius:6px;padding:2px 10px;font-size:11px;cursor:pointer;"
                  onmouseover="this.style.color='{COLORS['accent']}'" onmouseout="this.style.color='{COLORS['muted']}'">收藏</button>
              </div>
              <div style="margin-top:6px;padding:14px 16px;border-radius:12px;background:#111c2f;color:{COLORS['text']};line-height:1.55;">
                {rendered}
              </div>
            </div>"""
        )
        self._append_html(msg_html)

    def _append_html(self, html_content: str) -> None:
        """Append HTML content to the chat WebView, preserving existing content."""
        self.chat.page().runJavaScript(
            f"""var div=document.createElement('div');
div.innerHTML=`{html_content}`;
document.body.appendChild(div);
window.scrollTo(0, document.body.scrollHeight);
"""
        )

    def _sources_html(self, sources: list[SearchResult]) -> str:
        cards: list[str] = []
        for rank, result in enumerate(sources[:10], start=1):
            chunk = result.chunk
            score_pct = min(1.0, result.score)
            color = COLORS["accent"] if score_pct > 0.8 else (COLORS["warning"] if score_pct > 0.5 else COLORS["muted"])
            badge_label = "WavEDA 帮助" if chunk.source_type == "waveda_help" else "理论笔记"
            badge_color = "#103430" if chunk.source_type == "waveda_help" else "#1f2937"
            source_link = chunk.relative_path

            # If there's an HTML source, link to it
            if chunk.source_type == "waveda_help" and chunk.relative_path:
                source_link = f"<a href='file:///{str(self._project_root / chunk.relative_path).replace(chr(92), '/')}'>{html.escape(chunk.relative_path)}</a>"

            cards.append(
                f"""<div style="background:{COLORS['surface2']};border:1px solid {COLORS['border']};border-radius:8px;padding:10px 12px;margin-bottom:8px;">
                  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
                    <span style="font-weight:700;color:{COLORS['text']};">[{rank}] {html.escape(chunk.title)}</span>
                    <span style="background:{badge_color};color:{color};border-radius:8px;padding:2px 10px;font-size:11px;font-weight:600;">{badge_label}</span>
                  </div>
                  <div style="color:{COLORS['muted']};font-size:11px;margin-bottom:4px;">{source_link}</div>
                  <div style="color:{color};font-size:11px;">匹配度 {score_pct:.1%}</div>
                </div>"""
            )
        return web_wrapper("\n".join(cards))

    def _welcome_html(self) -> str:
        return web_wrapper(
            f"""<div style="text-align:center;padding:60px 20px;">
            <div style="font-size:22px;font-weight:700;color:{COLORS['accent']};margin-bottom:12px;">WavEDA Knowledge Workbench</div>
            <div style="color:{COLORS['muted']};margin-bottom:24px;">WavEDA 仿真软件知识问答助手</div>
            <div style="display:flex;justify-content:center;gap:12px;flex-wrap:wrap;">
              <div style="background:{COLORS['surface2']};border-radius:10px;padding:14px 18px;text-align:center;min-width:100px;">
                <div style="font-size:20px;font-weight:700;color:{COLORS['accent']};">1,908</div>
                <div style="color:{COLORS['muted']};font-size:12px;">知识块</div>
              </div>
              <div style="background:{COLORS['surface2']};border-radius:10px;padding:14px 18px;text-align:center;min-width:100px;">
                <div style="font-size:20px;font-weight:700;color:{COLORS['accent2']};">WavEDA优先</div>
                <div style="color:{COLORS['muted']};font-size:12px;">检索策略</div>
              </div>
              <div style="background:{COLORS['surface2']};border-radius:10px;padding:14px 18px;text-align:center;min-width:100px;">
                <div style="font-size:20px;font-weight:700;color:{COLORS['warning']};">DeepSeek</div>
                <div style="color:{COLORS['muted']};font-size:12px;">大模型</div>
              </div>
            </div>
            <div style="margin-top:28px;color:{COLORS['subtle']};font-size:13px;">在下方输入 WavEDA 相关问题开始</div>
          </div>"""
        )

    def _empty_sources_html(self, message: str = "提出问题后，这里会显示可追溯的来源证据。") -> str:
        return web_wrapper(
            f"""<div style="text-align:center;padding:40px 16px;">
            <div style="color:{COLORS['subtle']};font-size:13px;">{html.escape(message)}</div>
          </div>"""
        )

    def _show_error(self, title: str, message: str) -> None:
        QMessageBox.warning(self, title, message)


def run_desktop_app() -> int:
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    settings = load_settings()
    window = WorkbenchWindow(settings)
    window.show()
    return app.exec()
