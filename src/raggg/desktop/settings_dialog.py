"""设置对话框 — API / 路径 / 个性化 / 知识库管理"""
from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from raggg.config import Settings
from raggg.i18n import get_text, get_language, set_language
from raggg.theme import get_theme, set_theme, get_colors

COLORS = get_colors()

LLM_PROVIDERS = [
    ("DeepSeek",      "https://api.deepseek.com",                       "deepseek-chat"),
    ("Kimi (Moonshot)", "https://api.moonshot.cn/v1",                    "moonshot-v1-8k"),
    ("千问 (通义)",     "https://dashscope.aliyuncs.com/compatible-mode/v1", "qwen-plus"),
    ("百炼 (阿里云)",   "https://dashscope.aliyuncs.com/compatible-mode/v1", "qwen-plus"),
    ("OpenAI",        "https://api.openai.com/v1",                      "gpt-4o-mini"),
]

# 支持图片的多模态模型列表（后续出了新的加一行即可）
VISION_MODELS = {
    "gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "gpt-4-vision-preview",
    "claude-3-opus", "claude-3-sonnet", "claude-3-haiku",
    "claude-3.5-sonnet", "claude-opus-4", "claude-sonnet-5",
    "qwen-vl-plus", "qwen-vl-max", "qwen2.5-vl-7b", "qwen2.5-vl-72b",
    "gemini-2.0-flash", "gemini-1.5-flash", "gemini-1.5-pro",
}


class SettingsDialog(QDialog):
    """统一设置窗口，使用标签页组织：个性化 + API + 路径 + 知识库"""
    knowledge_changed = Signal()

    def __init__(self, settings: Settings, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.settings = settings
        self.setWindowTitle(get_text("settings_title"))
        self.setMinimumWidth(480)
        self.setMinimumHeight(360)

        main_layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)

        # ── Tab 1: 个性化（主题+人格+语言） ──
        self._build_personalization_tab()
        # ── Tab 2: API 设置 ──
        self._build_api_tab()
        # ── Tab 3: WavEDA 路径 ──
        self._build_waveda_paths_tab()
        # ── Tab 4: 知识库管理 ──
        self._build_knowledge_base_tab()

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self._save_all_and_accept)
        buttons.rejected.connect(self.reject)
        main_layout.addWidget(buttons)

    # ─── 个性化（主题 + 人格 + 语言合并） ──────────
    def _build_personalization_tab(self) -> None:
        from raggg.generation.personality import get_personality
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(18)

        # ── 主题 ──
        theme_label = QLabel(get_text("settings_theme_label"))
        theme_label.setStyleSheet(f"color:{COLORS['text']};font-weight:700;font-size:13px;")
        layout.addWidget(theme_label)

        self.theme_combo = QComboBox()
        self.theme_combo.addItem(get_text("settings_theme_light"), "light")
        self.theme_combo.addItem(get_text("settings_theme_dark"), "dark")
        self.theme_combo.setCurrentIndex(0 if get_theme() == "light" else 1)
        layout.addWidget(self.theme_combo)

        sep1 = QLabel("")
        sep1.setStyleSheet(f"border-top:1px solid {COLORS['border']};margin:4px 0;")
        layout.addWidget(sep1)

        # ── 人格 ──
        pers_label = QLabel(get_text("settings_personality_label"))
        pers_label.setStyleSheet(f"color:{COLORS['text']};font-weight:700;font-size:13px;")
        layout.addWidget(pers_label)

        self.personality_combo = QComboBox()
        personality_labels = {
            "normal": get_text("personality_normal"),
            "mature": get_text("personality_mature"),
            "sweet": get_text("personality_sweet"),
            "dog": get_text("personality_dog"),
            "cat": get_text("personality_cat"),
            "workhorse": get_text("personality_workhorse"),
        }
        for key, label in personality_labels.items():
            self.personality_combo.addItem(label, key)
        current = get_personality()
        for i, (key, _) in enumerate(personality_labels.items()):
            if key == current:
                self.personality_combo.setCurrentIndex(i)
                break
        layout.addWidget(self.personality_combo)

        sep2 = QLabel("")
        sep2.setStyleSheet(f"border-top:1px solid {COLORS['border']};margin:4px 0;")
        layout.addWidget(sep2)

        # ── 语言 ──
        lang_label = QLabel(get_text("settings_lang_label"))
        lang_label.setStyleSheet(f"color:{COLORS['text']};font-weight:700;font-size:13px;")
        layout.addWidget(lang_label)

        self.lang_combo = QComboBox()
        self.lang_combo.addItem(get_text("settings_lang_zh"), "zh")
        self.lang_combo.addItem(get_text("settings_lang_en"), "en")
        self.lang_combo.setCurrentIndex(0 if get_language() == "zh" else 1)
        layout.addWidget(self.lang_combo)

        desc = QLabel(get_text("settings_lang_desc"))
        desc.setStyleSheet(f"color:{COLORS['muted']};font-size:11px;")
        desc.setWordWrap(True)
        layout.addWidget(desc)

        layout.addStretch()
        self.tabs.addTab(tab, get_text("settings_personalization_tab"))

    # ─── API Tab ──────────────────────────────────
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

    # ─── Knowledge Base Manager Tab ───────────────
    def _build_knowledge_base_tab(self) -> None:
        from raggg.desktop.knowledge_manager import KnowledgeManager
        tab = KnowledgeManager(self.settings)
        tab.knowledge_changed.connect(self.knowledge_changed.emit)
        self.tabs.addTab(tab, get_text("kbm_tab"))

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

        # 保存主题
        theme = self.theme_combo.currentData()
        theme_found = False
        for i, line in enumerate(new_lines):
            if line.startswith("RAG_THEME="):
                new_lines[i] = f"RAG_THEME={theme}"
                theme_found = True
                break
        if not theme_found:
            new_lines.append(f"RAG_THEME={theme}")

        # 保存人格
        personality = self.personality_combo.currentData()
        pers_found = False
        for i, line in enumerate(new_lines):
            if line.startswith("RAG_PERSONALITY="):
                new_lines[i] = f"RAG_PERSONALITY={personality}"
                pers_found = True
                break
        if not pers_found:
            new_lines.append(f"RAG_PERSONALITY={personality}")

        env_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
        set_language(lang)
        set_theme(theme)
        from raggg.generation.personality import set_personality
        set_personality(personality)
        self.accept()
