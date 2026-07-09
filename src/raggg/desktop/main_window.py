from __future__ import annotations

import base64
import html
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from PySide6.QtCore import QObject, QRunnable, Qt, QThreadPool, QTimer, QUrl, Signal, Slot
from PySide6.QtGui import QFont, QIcon, QPixmap
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

from raggg.config import Settings, load_settings
from raggg.i18n import get_text, get_language, set_language
from raggg.pipeline.builder import BuildReport, build_knowledge_base
from raggg.pipeline.ingestion import IngestReport, ingest_document
from raggg.pipeline.rag_pipeline import RAGAnswer, RAGPipeline
from raggg.pipeline.source_watch import SourceSnapshot, scan_source_tree, snapshot_changed
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


IMAGE_MD_RE = re.compile(r">?\s*[^:\n]{0,16}:\s*`?\.?/([^`)]+\.(?:png|jpg|jpeg|gif|svg))`?", re.IGNORECASE)
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


IMAGE_PATH_RE = re.compile(
    r"[`\"]?((?:[A-Za-z0-9_. -]+[\\/])*(?:(?:images|res)[\\/])?[A-Za-z0-9_. -]+\.(?:png|jpg|jpeg|gif|svg))[`\"]?",
    re.IGNORECASE,
)
IMAGE_PATH_PREFIXES = (
    "waveda_docs/helphtml/helphtml/",
    "waveda_docs/helphtml/",
    "knowledge_base/assets/images/",
    "assets/images/",
)
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif", ".svg")

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
    for path in set(image_index.values()):
        _path_to_data_uri(path)



def _normalize_image_key(value: str) -> str:
    key = value.strip().strip("`\"'<>|,;").replace("\\", "/")
    key = re.sub(r"^\./+", "", key)
    key = key.lstrip("/")
    lower = key.lower()
    for prefix in IMAGE_PATH_PREFIXES:
        if lower.startswith(prefix):
            key = key[len(prefix):]
            lower = key.lower()
            break
    marker = "helphtml/helphtml/"
    marker_index = lower.find(marker)
    if marker_index >= 0:
        key = key[marker_index + len(marker):]
    return key.lower()


def _extract_images_from_sources(sources: list, image_index: dict[str, str],
                                  min_score: float = 0.45) -> list[tuple[str, str]]:
    """从检索到的来源chunk中提取图片路径, 过滤低分来源, 返回 [(绝对路径, 标题), ...]"""
    seen = set()
    results = []
    for src in sources:
        if src.score < min_score:
            continue
        content = src.chunk.content
        title = src.chunk.title
        for match in IMAGE_PATH_RE.finditer(content):
            raw_ref = match.group(1)
            candidates = [
                _normalize_image_key(raw_ref),
                os.path.basename(raw_ref).lower(),
            ]
            normalized = candidates[0]
            if normalized.startswith("example/"):
                candidates.append(normalized[len("example/"):])
            img_path = next((image_index[key] for key in candidates if key in image_index), "")
            if not img_path or img_path in seen:
                continue
            seen.add(img_path)
            results.append((img_path, title))
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
        self.setMinimumHeight(72)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 10, 14, 10)
        layout.setSpacing(6)
        title = QLabel(label)
        title.setObjectName("metricLabel")
        title.setMinimumHeight(18)
        title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.value_label = QLabel(value)
        self.value_label.setObjectName("metricValue")
        self.value_label.setStyleSheet(f"color: {color};")
        self.value_label.setMinimumHeight(26)
        self.value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
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


class SettingsDialog(QDialog):
    """统一设置窗口，使用标签页组织：API + 语言（可扩展）"""

    def __init__(self, settings: Settings, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.settings = settings
        self.setWindowTitle(get_text("settings_title"))
        self.setMinimumWidth(480)
        self.setMinimumHeight(360)

        main_layout = QVBoxLayout(self)

        # ── 标签栏 ──
        from PySide6.QtWidgets import QTabWidget
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)

        # ── Tab 1: API 设置 ──
        self._build_api_tab()
        # ── Tab 2: WavEDA 路径 ──
        self._build_waveda_paths_tab()
        # ── Tab 3: 语言 ──
        self._build_language_tab()

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self._save_all_and_accept)
        buttons.rejected.connect(self.reject)
        main_layout.addWidget(buttons)

    # ─── API Tab ─────────────────────────────────
    def _build_api_tab(self) -> None:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(14)

        desc = QLabel(get_text("settings_api_desc"))
        desc.setStyleSheet(f"color:{COLORS['muted']};font-size:12px;")
        desc.setWordWrap(True)
        layout.addWidget(desc)

        form = QFormLayout()
        form.setSpacing(10)

        self.provider_combo = QComboBox()
        for name, _, _ in LLM_PROVIDERS:
            self.provider_combo.addItem(name)
        current_url = self.settings.llm_base_url.rstrip("/")
        current_idx = 0
        for i, (_, url, _) in enumerate(LLM_PROVIDERS):
            if url == current_url:
                current_idx = i
                break
        self.provider_combo.setCurrentIndex(current_idx)
        self.provider_combo.currentIndexChanged.connect(self._on_provider_changed)
        form.addRow(get_text("settings_api_provider") + ":", self.provider_combo)

        self.key_edit = QLineEdit(self.settings.llm_api_key)
        self.key_edit.setPlaceholderText("sk-...")
        self.key_edit.setEchoMode(QLineEdit.Password)
        form.addRow(get_text("settings_api_key") + ":", self.key_edit)

        self.api_info_label = QLabel()
        self.api_info_label.setStyleSheet(f"color:{COLORS['subtle']};font-size:11px;")
        self._on_provider_changed(current_idx)
        form.addRow(self.api_info_label)

        layout.addLayout(form)
        layout.addStretch()
        self.tabs.addTab(tab, get_text("settings_api_tab"))

    def _on_provider_changed(self, index: int) -> None:
        _, url, model = LLM_PROVIDERS[index]
        self.api_info_label.setText(f"URL: {url}   |   Model: {model}")

    # ─── WavEDA Paths Tab ─────────────────────────
    def _build_waveda_paths_tab(self) -> None:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(14)

        desc = QLabel(get_text("settings_waveda_paths_desc"))
        desc.setStyleSheet(f"color:{COLORS['muted']};font-size:12px;")
        desc.setWordWrap(True)
        layout.addWidget(desc)

        form = QFormLayout()
        form.setSpacing(10)

        self.waveda_root_edit = QLineEdit(self._display_path(self.settings.waveda_root))
        self.waveda_root_edit.setPlaceholderText(r"D:\Program Files\WavEDA")
        form.addRow(get_text("settings_waveda_root") + ":", self.waveda_root_edit)

        self.waveda_help_root_edit = QLineEdit(self._display_path(self.settings.waveda_help_root))
        self.waveda_help_root_edit.setPlaceholderText(r"D:\Program Files\WavEDA\documentation\helpHtml")
        form.addRow(get_text("settings_waveda_help_root") + ":", self.waveda_help_root_edit)

        self.waveda_example_root_edit = QLineEdit(self._display_path(self.settings.waveda_example_root))
        self.waveda_example_root_edit.setPlaceholderText(r"D:\Program Files\WavEDA\Example")
        form.addRow(get_text("settings_waveda_example_root") + ":", self.waveda_example_root_edit)

        hint = QLabel(get_text("settings_waveda_paths_hint"))
        hint.setStyleSheet(f"color:{COLORS['subtle']};font-size:11px;")
        hint.setWordWrap(True)
        form.addRow(hint)

        layout.addLayout(form)
        layout.addStretch()
        self.tabs.addTab(tab, get_text("settings_waveda_paths_tab"))

    def _display_path(self, path: Path | None) -> str:
        if path is None:
            return ""
        try:
            return str(path.relative_to(self.settings.project_root))
        except ValueError:
            return str(path)

    # ─── Language Tab ────────────────────────────
    def _build_language_tab(self) -> None:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(14)

        desc = QLabel(get_text("settings_lang_desc"))
        desc.setStyleSheet(f"color:{COLORS['muted']};font-size:12px;")
        desc.setWordWrap(True)
        layout.addWidget(desc)

        form = QFormLayout()
        form.setSpacing(10)

        self.lang_combo = QComboBox()
        self.lang_combo.addItem(get_text("settings_lang_zh"), "zh")
        self.lang_combo.addItem(get_text("settings_lang_en"), "en")
        current_lang = get_language()
        self.lang_combo.setCurrentIndex(0 if current_lang == "zh" else 1)
        form.addRow(get_text("settings_lang_label") + ":", self.lang_combo)

        layout.addLayout(form)
        layout.addStretch()
        self.tabs.addTab(tab, get_text("settings_lang_tab"))

    # ─── Save ────────────────────────────────────
    def _save_all_and_accept(self) -> None:
        # 保存 API
        _, url, model = LLM_PROVIDERS[self.provider_combo.currentIndex()]
        env_path = Path(__file__).resolve().parents[3] / "config" / ".env"
        lines: list[str] = []
        if env_path.exists():
            lines = env_path.read_text(encoding="utf-8").splitlines()
        new_lines: list[str] = []
        for line in lines:
            if not any(line.startswith(k + "=") for k in (
                "RAG_LLM_BASE_URL", "RAG_LLM_API_KEY", "RAG_LLM_MODEL",
                "WAVEDA_ROOT", "WAVEDA_HELP_ROOT", "WAVEDA_EXAMPLE_ROOT",
            )):
                new_lines.append(line)
        new_lines.append(f"RAG_LLM_BASE_URL={url}")
        new_lines.append(f"RAG_LLM_API_KEY={self.key_edit.text().strip()}")
        new_lines.append(f"RAG_LLM_MODEL={model}")

        waveda_root = self.waveda_root_edit.text().strip()
        waveda_help_root = self.waveda_help_root_edit.text().strip() or "wavEDA_docs/helpHtml/helpHtml"
        waveda_example_root = self.waveda_example_root_edit.text().strip()
        new_lines.append(f"WAVEDA_ROOT={waveda_root}")
        new_lines.append(f"WAVEDA_HELP_ROOT={waveda_help_root}")
        new_lines.append(f"WAVEDA_EXAMPLE_ROOT={waveda_example_root}")

        # 保存语言
        lang = self.lang_combo.currentData()
        lang_found = False
        for i, line in enumerate(new_lines):
            if line.startswith("RAG_LANGUAGE="):
                new_lines[i] = f"RAG_LANGUAGE={lang}"
                lang_found = True
                break
        if not lang_found:
            new_lines.append(f"RAG_LANGUAGE={lang}")

        env_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
        set_language(lang)
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
        self._source_snapshot: SourceSnapshot = {}
        self._watch_pending_snapshot: SourceSnapshot | None = None
        self._watch_rebuild_requested = False
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
        self._start_source_watcher()
        # 后台预编码所有图片，用户第一次问就不慢了
        self._preload_images()

    def _preload_images(self) -> None:
        """后台异步预编码所有图片到缓存，用户第一次提问时不再等待"""
        from functools import partial
        worker = Worker(partial(_preload_all_images, self._image_index))
        worker.signals.finished.connect(lambda: print("Image preload complete"))
        self._start_worker(worker)

    def _build_image_index(self) -> None:
        """Build image index with project assets first, then user WavEDA paths."""
        image_roots = [
            (self._project_root / "knowledge_base" / "assets" / "images", ""),
            (self._project_root / "assets" / "images", ""),
            (self._project_root / "wavEDA_docs" / "helpHtml" / "helpHtml", ""),
        ]
        if self.settings.waveda_help_root:
            image_roots.append((self.settings.waveda_help_root, ""))
        if self.settings.waveda_root:
            image_roots.append((self.settings.waveda_root / "Example", "Example"))
            image_roots.append((self.settings.waveda_root / "documentation" / "helpHtml", ""))
            image_roots.append((self.settings.waveda_root / "helpHtml", ""))
            image_roots.append((self.settings.waveda_root / "helpHtml" / "helpHtml", ""))
        if self.settings.waveda_example_root:
            image_roots.append((self.settings.waveda_example_root, "Example"))

        for root, key_prefix in image_roots:
            if root.exists():
                self._add_images_from_root(root, key_prefix=key_prefix)
        print(f"Image index: {len(set(self._image_index.values()))} files, {len(self._image_index)} keys loaded")

    def _add_images_from_root(self, root: Path, key_prefix: str = "") -> None:
        root = root.resolve()
        for image_path in root.rglob("*"):
            if not image_path.is_file() or image_path.suffix.lower() not in IMAGE_EXTENSIONS:
                continue
            abs_path = str(image_path).replace(os.sep, "/")
            rel_key = _normalize_image_key(image_path.relative_to(root).as_posix())
            name_key = image_path.name.lower()
            self._image_index.setdefault(rel_key, abs_path)
            if key_prefix:
                self._image_index.setdefault(_normalize_image_key(f"{key_prefix}/{rel_key}"), abs_path)
            self._image_index.setdefault(name_key, abs_path)

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
        subtitle = QLabel(get_text("app_subtitle"))
        subtitle.setObjectName("subtitle")
        titles.addWidget(subtitle)
        header.addLayout(titles)
        header.addStretch(1)
        badge = QLabel(get_text("badge_waveda_first"))
        badge.setObjectName("badge")
        header.addWidget(badge, alignment=Qt.AlignRight | Qt.AlignVCenter)
        return header

    def _left_panel(self) -> QFrame:
        panel = self._panel(270)
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        section = QLabel(get_text("sidebar_status"))
        section.setObjectName("section")
        layout.addWidget(section)

        self.status_card = MetricCard(get_text("card_knowledge_base"), get_text("status_loading_index"))
        self.chunk_card = MetricCard(get_text("card_chunks"), "-", COLORS["warning"])
        self.model_card = MetricCard(get_text("card_model"), self.settings.llm_model if self.settings.llm_api_key else get_text("model_local"))
        layout.addWidget(self.status_card)
        layout.addWidget(self.chunk_card)
        layout.addWidget(self.model_card)
        self.watch_card = MetricCard("监听", "启动中", COLORS["accent2"])
        layout.addWidget(self.watch_card)

        self.import_button = self._button("导入资料入库", primary=True)
        self.import_button.clicked.connect(self._import_document)
        layout.addWidget(self.import_button)

        self.reload_button = self._button(get_text("btn_reload_index"))
        self.reload_button.clicked.connect(self._load_pipeline_if_ready)
        layout.addWidget(self.reload_button)

        self.api_button = self._button(get_text("btn_api_settings"))
        self.api_button.clicked.connect(self._open_api_settings)
        layout.addWidget(self.api_button)

        self.fav_button = self._button(get_text("btn_favorites"))
        self.fav_button.clicked.connect(self._open_favorites)
        layout.addWidget(self.fav_button)

        prompt_label = QLabel(get_text("quick_questions_label"))
        prompt_label.setObjectName("section")
        layout.addSpacing(10)
        layout.addWidget(prompt_label)
        for key in ("quick_q1", "quick_q2", "quick_q3"):
            prompt = get_text(key)
            button = self._button(prompt)
            button.clicked.connect(lambda _checked=False, text=prompt: self._ask(text))
            layout.addWidget(button)

        note = QLabel(get_text("search_note"))
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
        section = QLabel(get_text("section_qa"))
        section.setObjectName("section")
        self.activity_label = QLabel(get_text("status_ready"))
        self.activity_label.setStyleSheet(f"color: {COLORS['accent']};")
        top.addWidget(section)
        top.addStretch(1)
        top.addWidget(self.activity_label)
        layout.addLayout(top)

        self.chat = QWebEngineView()
        self.chat.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        self.chat.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, False)

        # 自定义页面：拦截 console.log 消息
        wb_ref = self
        class _FavPage(QWebEnginePage):
            def javaScriptConsoleMessage(self2, level, msg, line, source):
                if msg == "RAGGG_FAV":
                    wb_ref._do_fav()
        self.chat.setPage(_FavPage(self.chat))

        # 读取实际的 chunk 数量和模型名
        chunks_path = self.settings.data_dir / "index" / "chunks.json"
        chunk_count_str = "-"
        if chunks_path.exists():
            try:
                import json
                data = json.loads(chunks_path.read_text(encoding="utf-8"))
                chunk_count_str = str(len(data))
            except Exception:
                pass
        model_name_str = self.settings.llm_model if self.settings.llm_api_key else get_text("model_local")
        self.chat.setHtml(self._welcome_html(chunk_count=chunk_count_str, model_name=model_name_str))
        self.chat.setMinimumHeight(300)
        layout.addWidget(self.chat, stretch=1)

        composer = QHBoxLayout()
        composer.setSpacing(10)
        self.question = QLineEdit()
        self.question.setPlaceholderText(get_text("placeholder_input"))
        self.question.returnPressed.connect(self._ask)
        self.ask_button = self._button(get_text("btn_ask"), primary=True)
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
        title = QLabel(get_text("section_sources"))
        title.setObjectName("section")
        subtitle = QLabel(get_text("sources_subtitle"))
        subtitle.setObjectName("muted")
        self._source_list_html = self._empty_sources_html()
        self.sources = QWebEngineView()
        self.sources.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        self.sources.page().urlChanged.connect(self._on_src_url)
        self.sources.setHtml(self._source_list_html)
        src_nav = QHBoxLayout()
        src_nav.setSpacing(6)
        back_btn = QPushButton(get_text("btn_back_to_sources"))
        back_btn.setCursor(Qt.PointingHandCursor)
        back_btn.clicked.connect(lambda: self.sources.setHtml(self._source_list_html))
        src_nav.addWidget(back_btn)
        src_nav.addStretch(1)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addLayout(src_nav)
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
            self.status_card.set_value(get_text("kb_not_built"), COLORS["danger"])
            self.chunk_card.set_value("-", COLORS["warning"])
            self.sources.setHtml(self._empty_sources_html(get_text("sources_not_built")))
            return
        self.pipeline = RAGPipeline(self.settings)
        self.status_card.set_value(get_text("kb_loaded"), COLORS["accent"])
        self.chunk_card.set_value(str(len(self.pipeline.store.chunks)), COLORS["warning"])
        model_name = self.settings.llm_model if self.settings.llm_api_key else get_text("model_local")
        model_color = COLORS["accent"] if self.settings.llm_api_key else COLORS["warning"]
        self.model_card.set_value(model_name, model_color)
        self.sources.setHtml(self._empty_sources_html())

    def _on_src_url(self, url: QUrl) -> None:
        """拦截 ragsrc:// 链接，在原位加载完整帮助页"""
        if url.scheme() == "ragsrc":
            html_rel = url.toString().replace("ragsrc://", "")
            html_path = self._project_root / "wavEDA_docs" / html_rel
            if html_path.exists():
                with open(html_path, "r", encoding="utf-8") as f:
                    html_content = f.read()
                # Fix image sources to absolute paths
                img_base = str(html_path.parent / "images").replace(os.sep, "/")
                css_base = str(self._project_root / "wavEDA_docs" / "helpHtml" / "helpHtml" / "css").replace(os.sep, "/")
                html_content = re.sub(r'src="\.?/?images/', f'src="file:///{img_base}/', html_content)
                html_content = re.sub(r'href="\.\./css/', f'href="file:///{css_base}/', html_content)
                self.sources.setHtml(html_content)

    def _on_console_msg(self, level, msg: str, line: int, source: str) -> None:
        if msg == "RAGGG_FAV":
            self._do_fav()
        elif msg.startswith("RAGGG_FAVDEL:"):
            # Not used here; favorites dialog uses Qt buttons now
            pass

    def _do_fav(self) -> None:
        q, a = self._last_qa
        if q and a:
            favs = self._load_favs()
            favs.append({"question": q, "answer": a, "time": __import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M")})
            with open(self._fav_file, "w", encoding="utf-8") as f:
                import json as _json; _json.dump(favs, f, ensure_ascii=False, indent=2)
            self.status_card.set_value(get_text("favorites_saved"), COLORS["accent"])

    def _load_favs(self) -> list:
        import json as _json
        if self._fav_file.exists():
            with open(self._fav_file, "r", encoding="utf-8") as f:
                return _json.load(f)
        return []


    def _open_favorites(self) -> None:
        favs = self._load_favs()
        if not favs:
            QMessageBox.information(self, get_text("favorites_title"), get_text("msg_favorites_empty"))
            return
        dialog = QDialog(self)
        dialog.setWindowTitle(get_text("favorites_title"))
        dialog.resize(750, 550)
        layout = QVBoxLayout(dialog)
        from PySide6.QtWidgets import QScrollArea
        scroll = QWidget()
        scroll_layout = QVBoxLayout(scroll)
        for i, f in enumerate(reversed(favs)):
            card = QFrame()
            card.setObjectName("metricCard")
            card_layout = QVBoxLayout(card)
            # Q&A 合并显示在一个文本框里，统一背景
            from PySide6.QtWidgets import QTextEdit
            qa_text = QTextEdit()
            qa_text.setReadOnly(True)
            html_body = (
                f"<p style='color:{COLORS['accent']};font-weight:700;margin:0;'>Q: {html.escape(f['question'])}</p>"
                f"<p style='color:{COLORS['subtle']};font-size:11px;margin:2px 0 6px 0;'>{f.get('time','')}</p>"
                f"<hr style='border-color:{COLORS['border']};margin:6px 0;'>"
                f"<p style='color:{COLORS['text']};line-height:1.55;margin:0;white-space:pre-wrap;'>{html.escape(f['answer'])}</p>"
            )
            qa_text.setHtml(html_body)
            qa_text.setMaximumHeight(250)
            qa_text.setStyleSheet(f"background:{COLORS['surface2']};border:0;")
            card_layout.addWidget(qa_text)
            del_btn = QPushButton(get_text("btn_delete"))
            del_btn.setStyleSheet(f"background:{COLORS['danger']};color:#fff;border:0;padding:2px 8px;font-size:11px;")
            real_idx = len(favs) - 1 - i
            del_btn.clicked.connect(lambda ch=False, idx=real_idx: self._do_fav_del(idx, dialog))
            card_layout.addWidget(del_btn)
            scroll_layout.addWidget(card)
        scroll.setMinimumSize(700, len(favs) * 180)
        scroll_layout.addStretch(1)
        area = QScrollArea()
        area.setWidgetResizable(True)
        area.setWidget(scroll)
        layout.addWidget(area, stretch=1)
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
        dialog = SettingsDialog(self.settings, self)
        if dialog.exec() == QDialog.Accepted:
            self.settings = load_settings()
            self._load_pipeline_if_ready()
            self._refresh_ui_language()
            QMessageBox.information(self, get_text("settings_title"), get_text("msg_api_saved"))

    def _refresh_ui_language(self) -> None:
        """刷新所有 UI 文本以反映当前语言设置"""
        lang = get_language()
        # 侧边栏按钮
        self.reload_button.setText(get_text("btn_reload_index"))
        self.api_button.setText(get_text("btn_api_settings"))
        self.fav_button.setText(get_text("btn_favorites"))

    def _import_document(self) -> None:
        if self.is_busy:
            return
        path, _ = QFileDialog.getOpenFileName(
            self,
            "选择要入库的资料",
            str(self._project_root),
            "Documents (*.md *.markdown *.html *.htm *.txt *.pdf *.docx)",
        )
        if not path:
            return

        self._set_busy(True, "正在导入资料并重建知识库")
        worker = Worker(lambda: self._import_and_rebuild(path))
        worker.signals.result.connect(self._on_import_done)
        worker.signals.error.connect(lambda message: self._show_error("导入失败", message))
        worker.signals.finished.connect(lambda: self._set_busy(False, "就绪"))
        self._start_worker(worker)

    def _import_and_rebuild(self, path: str) -> tuple[IngestReport, BuildReport]:
        ingest_report = ingest_document(self.settings, path)
        build_report = build_knowledge_base(self.settings)
        return ingest_report, build_report

    def _on_import_done(self, result: tuple[IngestReport, BuildReport]) -> None:
        ingest_report, build_report = result
        self.chunk_card.set_value(str(build_report.chunk_count), COLORS["warning"])
        self._load_pipeline_if_ready()
        self._sync_watch_snapshot()
        QMessageBox.information(
            self,
            "导入完成",
            f"已导入: {ingest_report.imported_path.name}\n知识块: {build_report.chunk_count}",
        )

    def _rebuild_async(self) -> None:
        if self.is_busy:
            return
        self._set_busy(True, get_text("status_building"))
        worker = Worker(lambda: build_knowledge_base(self.settings))
        worker.signals.result.connect(self._on_rebuild_done)
        worker.signals.error.connect(lambda message: self._show_error(get_text("error_rebuild_title"), message))
        worker.signals.finished.connect(lambda: self._set_busy(False, get_text("status_ready")))
        self._start_worker(worker)

    def _on_rebuild_done(self, report: BuildReport) -> None:
        self.chunk_card.set_value(str(report.chunk_count), COLORS["warning"])
        self._load_pipeline_if_ready()
        self._sync_watch_snapshot()

    def _start_source_watcher(self) -> None:
        self._sync_watch_snapshot()
        self._watch_timer = QTimer(self)
        self._watch_timer.setInterval(5000)
        self._watch_timer.timeout.connect(self._check_source_changes)
        self._watch_timer.start()

        self._watch_debounce_timer = QTimer(self)
        self._watch_debounce_timer.setSingleShot(True)
        self._watch_debounce_timer.setInterval(2000)
        self._watch_debounce_timer.timeout.connect(self._trigger_watch_rebuild)

    def _sync_watch_snapshot(self) -> None:
        self._source_snapshot = scan_source_tree(self.settings.obsidian_vault_root)
        self._watch_pending_snapshot = None
        self._watch_rebuild_requested = False
        if hasattr(self, "watch_card"):
            self.watch_card.set_value("监听中", COLORS["accent2"])

    def _check_source_changes(self) -> None:
        current = scan_source_tree(self.settings.obsidian_vault_root)
        if not snapshot_changed(self._source_snapshot, current):
            return
        self._watch_pending_snapshot = current
        self.watch_card.set_value("检测到变化", COLORS["warning"])
        if not self.is_busy:
            self.activity_label.setText("检测到知识库变化，等待文件稳定")
            self.activity_label.setStyleSheet(f"color: {COLORS['warning']};")
        self._watch_debounce_timer.start()

    def _trigger_watch_rebuild(self) -> None:
        if self._watch_pending_snapshot is None:
            return
        if self.is_busy:
            self._watch_rebuild_requested = True
            self.watch_card.set_value("等待空闲", COLORS["warning"])
            return

        snapshot_after_change = self._watch_pending_snapshot
        self._set_busy(True, "知识库变化，正在自动重建")
        self.watch_card.set_value("自动重建", COLORS["warning"])
        worker = Worker(lambda: build_knowledge_base(self.settings))
        worker.signals.result.connect(lambda report: self._on_watch_rebuild_done(report, snapshot_after_change))
        worker.signals.error.connect(lambda message: self._show_error("自动重建失败", message))
        worker.signals.finished.connect(lambda: self._set_busy(False, "就绪"))
        self._start_worker(worker)

    def _on_watch_rebuild_done(self, report: BuildReport, snapshot_after_change: SourceSnapshot) -> None:
        self.chunk_card.set_value(str(report.chunk_count), COLORS["warning"])
        self._load_pipeline_if_ready()
        self._source_snapshot = snapshot_after_change
        self._watch_pending_snapshot = None
        self._watch_rebuild_requested = False
        self.watch_card.set_value("监听中", COLORS["accent2"])

    def _ask(self, question: str | None = None) -> None:
        if self.is_busy:
            return
        text = (question or self.question.text()).strip()
        if not text:
            return
        if self.pipeline is None:
            QMessageBox.information(self, get_text("error_no_kb_title"), get_text("error_no_kb_msg"))
            return
        self.question.clear()
        self._append_user(text)
        self._set_busy(True, get_text("status_searching"))
        worker = Worker(lambda: AskResult(text, self.pipeline.ask(text)))
        worker.signals.result.connect(self._on_answer_done)
        worker.signals.error.connect(lambda message: self._append_assistant(get_text("msg_generation_failed") + message))
        worker.signals.finished.connect(lambda: self._set_busy(False, get_text("status_ready")))
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
        all_images = _extract_images_from_sources(result.answer.sources, self._image_index)
        if all_images:
            img_html = '<div style="margin:12px 0 8px 0;"><div style="color:' + COLORS["accent2"] + ';font-weight:700;margin-bottom:8px;">' + get_text("screenshot_label") + '</div>'
            for img_path, title in all_images[:6]:
                abs_path = img_path.replace(os.sep, "/")
                data_uri = _path_to_data_uri(abs_path)
                if not data_uri:
                    continue
                safe_title = html.escape(title)
                img_html += f'<p style="margin:6px 0;"><span style="color:{COLORS["muted"]};font-size:12px;">{safe_title}</span><br><img src="{data_uri}" style="max-width:100%;max-height:400px;border-radius:8px;border:1px solid {COLORS["border"]};margin-top:4px;"></p>'
            img_html += '</div>'
            self._append_html(web_wrapper(img_html))
        self._source_list_html = self._sources_html(result.answer.sources)
        self.sources.setHtml(self._source_list_html)

    def _set_busy(self, busy: bool, text: str) -> None:
        self.is_busy = busy
        self.activity_label.setText(text)
        self.activity_label.setStyleSheet(f"color: {COLORS['warning' if busy else 'accent']};")
        for button in (self.ask_button, self.reload_button, self.import_button):
            button.setDisabled(busy)
        if not busy and self._watch_rebuild_requested and self._watch_pending_snapshot is not None:
            self._watch_rebuild_requested = False
            QTimer.singleShot(0, self._trigger_watch_rebuild)

    def _append_user(self, question: str) -> None:
        self._last_qa = (question, "")  # 记住问题，等回答来了配对
        msg_html = web_wrapper(
            f"""<div style="margin:16px 0 8px 0;">
              <div style="color:{COLORS['accent']};font-weight:700;font-size:13px;">{get_text("you_label")}</div>
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
                <button onclick="var p=this.parentElement.nextElementSibling;var t=document.createElement('textarea');t.value=p.innerText;document.body.appendChild(t);t.select();document.execCommand('copy');document.body.removeChild(t);var s=this.innerHTML;this.innerHTML='{get_text("btn_copied")}';setTimeout(function(){{this.innerHTML=s;}}.bind(this),1000)"
                  style="background:{COLORS['surface3']};color:{COLORS['muted']};border:1px solid {COLORS['border']};border-radius:6px;padding:2px 10px;font-size:11px;cursor:pointer;"
                  onmouseover="this.style.color='{COLORS['accent']}'" onmouseout="this.style.color='{COLORS['muted']}'">{get_text("btn_copy")}</button>
                <button onclick="console.log('RAGGG_FAV');this.innerHTML='{get_text("btn_faved")}';this.style.color='{COLORS['accent']}';setTimeout(function(){{this.innerHTML='{get_text("btn_fav")}';this.style.color='{COLORS['muted']}'}}.bind(this),1500)"
                  style="background:{COLORS['surface3']};color:{COLORS['muted']};border:1px solid {COLORS['border']};border-radius:6px;padding:2px 10px;font-size:11px;cursor:pointer;"
                  onmouseover="this.style.color='{COLORS['accent']}'" onmouseout="this.style.color='{COLORS['muted']}'">{get_text("btn_fav")}</button>
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
            if chunk.source_type == "waveda_help":
                badge_label, badge_color = get_text("badge_waveda_help"), "#103430"
            elif chunk.source_type == "user_tutorial":
                badge_label, badge_color = get_text("badge_team_tutorial"), "#1f472b"
            else:
                badge_label, badge_color = get_text("badge_theory_notes"), "#1f2937"
            source_link = chunk.relative_path

            # Link to the original HTML help file (with images + CSS)
            if chunk.source_type in ("waveda_help", "user_tutorial") and chunk.relative_path:
                # Map extracted_pages/EM_Project/Boundary.md -> helpHtml/same_path.html
                html_rel = chunk.relative_path.replace("extracted_pages/", "helpHtml/")
                html_rel = re.sub(r"\.md$", ".html", html_rel)
                source_link = f"<a href='ragsrc://{html_rel}' style='color:{COLORS['accent2']};cursor:pointer;'>{html.escape(chunk.relative_path)}</a>"

            cards.append(
                f"""<div style="background:{COLORS['surface2']};border:1px solid {COLORS['border']};border-radius:8px;padding:10px 12px;margin-bottom:8px;">
                  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
                    <span style="font-weight:700;color:{COLORS['text']};">[{rank}] {html.escape(chunk.title)}</span>
                    <span style="background:{badge_color};color:{color};border-radius:8px;padding:2px 10px;font-size:11px;font-weight:600;">{badge_label}</span>
                  </div>
                  <div style="color:{COLORS['muted']};font-size:11px;margin-bottom:4px;">{source_link}</div>
                  <div style="color:{color};font-size:11px;">{get_text("match_score")} {score_pct:.1%}</div>
                </div>"""
            )
        return web_wrapper("\n".join(cards))

    def _welcome_html(self, chunk_count: str = "-", model_name: str = "DeepSeek") -> str:
        return web_wrapper(
            f"""<div style="text-align:center;padding:60px 20px;">
            <div style="font-size:22px;font-weight:700;color:{COLORS['accent']};margin-bottom:12px;">WavEDA Knowledge Workbench</div>
            <div style="color:{COLORS['muted']};margin-bottom:24px;">{get_text("startup_brand_subtitle")}</div>
            <div style="display:flex;justify-content:center;gap:12px;flex-wrap:wrap;">
              <div style="background:{COLORS['surface2']};border-radius:10px;padding:14px 18px;text-align:center;min-width:100px;">
                <div style="font-size:20px;font-weight:700;color:{COLORS['accent']};">{chunk_count}</div>
                <div style="color:{COLORS['muted']};font-size:12px;">{get_text("startup_chunks_label")}</div>
              </div>
              <div style="background:{COLORS['surface2']};border-radius:10px;padding:14px 18px;text-align:center;min-width:100px;">
                <div style="font-size:20px;font-weight:700;color:{COLORS['accent2']};">{get_text("badge_waveda_first")}</div>
                <div style="color:{COLORS['muted']};font-size:12px;">{get_text("startup_strategy_label")}</div>
              </div>
              <div style="background:{COLORS['surface2']};border-radius:10px;padding:14px 18px;text-align:center;min-width:100px;">
                <div style="font-size:20px;font-weight:700;color:{COLORS['warning']};">{model_name}</div>
                <div style="color:{COLORS['muted']};font-size:12px;">{get_text("startup_llm_label")}</div>
              </div>
            </div>
            <div style="margin-top:28px;color:{COLORS['subtle']};font-size:13px;">{get_text("startup_hint")}</div>
          </div>"""
        )

    def _empty_sources_html(self, message: str | None = None) -> str:
        if message is None:
            message = get_text("sources_empty")
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
