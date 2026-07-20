# Desktop Modularization, Citations, and Build Progress Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Split the desktop window into focused modules, add clickable numbered citations, and show staged knowledge-index progress while preserving current behavior.

**Architecture:** Pure rendering and image-index functions move into dedicated modules, while favorites, sessions, and reusable view construction move behind small mixins/components. `WorkbenchWindow` remains the coordinator for pipeline, workers, and cross-WebView events. Builder progress uses an optional typed callback so CLI and existing callers remain compatible.

**Tech Stack:** Python 3.11+, PySide6 Qt Widgets/WebEngine, `unittest`, NumPy, existing RAGGG pipeline and theme helpers.

## Global Constraints

- Keep the current retrieval order, index file formats, favorites JSON format, session storage format, and desktop theme.
- Keep compatibility imports for helpers currently imported from `raggg.desktop.main_window`.
- `src/raggg/desktop/main_window.py` must contain fewer than 800 physical lines.
- Do not modify or publish user-owned knowledge files.
- Do not batch-delete files or directories.
- Write a failing test and observe the expected failure before each production change.

---

### Task 1: Builder progress callback

**Files:**
- Modify: `src/raggg/pipeline/builder.py`
- Modify: `tests/test_builder_documents.py`

**Interfaces:**
- Produces: `BuildProgress(stage: str, message: str, current: int | None = None, total: int | None = None)`
- Produces: `build_knowledge_base(settings: Settings, on_progress: Callable[[BuildProgress], None] | None = None) -> BuildReport`

- [ ] **Step 1: Write the failing progress-order test**

Add a test that builds a one-document temporary knowledge base:

```python
def test_build_reports_ordered_progress_stages(self) -> None:
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        kb = root / "knowledge_base"
        kb.mkdir(parents=True)
        (kb / "one.md").write_text("# One\n\nPort setup", encoding="utf-8")
        events = []

        build_knowledge_base(make_settings(root), on_progress=events.append)

        self.assertEqual(
            [event.stage for event in events],
            ["scan", "chunk", "embed", "save", "complete"],
        )
        self.assertTrue(all(event.message for event in events))
```

- [ ] **Step 2: Run the focused test and confirm RED**

Run:

```powershell
$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest tests.test_builder_documents.BuilderDocumentTests.test_build_reports_ordered_progress_stages -v
```

Expected: `TypeError` because `build_knowledge_base()` does not accept `on_progress`.

- [ ] **Step 3: Add the typed progress contract and emissions**

Add:

```python
from typing import Callable

@dataclass(frozen=True)
class BuildProgress:
    stage: str
    message: str
    current: int | None = None
    total: int | None = None

ProgressCallback = Callable[[BuildProgress], None]

def _report_progress(
    callback: ProgressCallback | None,
    stage: str,
    message: str,
    current: int | None = None,
    total: int | None = None,
) -> None:
    if callback is not None:
        callback(BuildProgress(stage, message, current, total))
```

Change the builder signature and emit exactly once per stage:

```python
def build_knowledge_base(
    settings: Settings,
    on_progress: ProgressCallback | None = None,
) -> BuildReport:
    _report_progress(on_progress, "scan", "正在扫描知识文档")
    # load documents
    _report_progress(on_progress, "chunk", "正在复用或切分文档", 0, len(documents))
    # chunk loop
    _report_progress(on_progress, "embed", "正在生成向量", len(chunks), len(chunks))
    # vectors
    _report_progress(on_progress, "save", "正在写入索引")
    # save
    _report_progress(on_progress, "complete", "索引构建完成", len(documents), len(documents))
```

- [ ] **Step 4: Run builder tests and confirm GREEN**

Run:

```powershell
$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest tests.test_builder_documents -v
```

Expected: all builder tests pass.

- [ ] **Step 5: Commit**

```powershell
git add -- src/raggg/pipeline/builder.py tests/test_builder_documents.py
git commit -m "feat: report staged index build progress"
```

### Task 2: Rendering and image-index extraction

**Files:**
- Create: `src/raggg/desktop/rendering.py`
- Create: `src/raggg/desktop/image_index.py`
- Modify: `src/raggg/desktop/main_window.py`
- Create: `tests/test_desktop_rendering.py`
- Modify: `tests/test_desktop_layout.py`

**Interfaces:**
- Produces: `markdown_to_html(text: str) -> str`
- Produces: `render_inline_markdown(text: str) -> str`
- Produces: `web_wrapper(body_html: str, extra_css: str = "") -> str`
- Produces: `render_citations(text: str) -> str`
- Produces: `ImageIndex(project_root: Path)` with `build()` and `extract_from_sources()`
- Keeps compatibility imports from `raggg.desktop.main_window`.

- [ ] **Step 1: Write failing citation and image-index import tests**

Create:

```python
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from raggg.desktop.image_index import ImageIndex
from raggg.desktop.rendering import markdown_to_html


class DesktopRenderingTests(unittest.TestCase):
    def test_adjacent_citations_render_as_clickable_superscripts(self) -> None:
        rendered = markdown_to_html("结论。[1][2]")
        self.assertIn("RAGGG_CITATION:1", rendered)
        self.assertIn("RAGGG_CITATION:2", rendered)
        self.assertEqual(rendered.count("<sup"), 2)

    def test_image_index_maps_relative_path_and_filename(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            image = root / "wavEDA_docs" / "helpHtml" / "helpHtml" / "guide" / "images" / "port.png"
            image.parent.mkdir(parents=True)
            image.write_bytes(b"png")
            index = ImageIndex(root)
            index.build()
            self.assertEqual(index.paths["guide/images/port.png"], str(image))
            self.assertEqual(index.paths["port.png"], str(image))
```

- [ ] **Step 2: Run the tests and confirm RED**

Run:

```powershell
$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest tests.test_desktop_rendering -v
```

Expected: import failures because both modules are absent.

- [ ] **Step 3: Move pure rendering and image code**

Move Markdown/LaTeX/WebView functions and constants into `rendering.py`. Add citation replacement after HTML escaping and before bold replacement:

```python
CITATION_RE = re.compile(r"(?<![\w/])\[(\d+)\]")

def render_citations(text: str) -> str:
    return CITATION_RE.sub(
        lambda match: (
            '<sup class="citation"><a href="#" '
            f'onclick="console.log(\'RAGGG_CITATION:{match.group(1)}\');return false;">'
            f'[{match.group(1)}]</a></sup>'
        ),
        text,
    )
```

Add citation CSS to `web_wrapper()`. Move image key normalization, directory scanning, source extraction, and data-URI access into `ImageIndex`. Import these names in `main_window.py` so existing callers remain valid:

```python
from raggg.desktop.image_index import ImageIndex
from raggg.desktop.rendering import (
    markdown_to_html,
    render_inline_markdown,
    web_wrapper,
)
```

Replace `_build_image_index()` and related methods with:

```python
self.image_index = ImageIndex(self._project_root)
self.image_index.build()
self._image_index = self.image_index.paths
```

- [ ] **Step 4: Run rendering and desktop tests and confirm GREEN**

Run:

```powershell
$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest tests.test_desktop_rendering tests.test_desktop_layout -v
```

Expected: all tests pass.

- [ ] **Step 5: Commit**

```powershell
git add -- src/raggg/desktop/rendering.py src/raggg/desktop/image_index.py src/raggg/desktop/main_window.py tests/test_desktop_rendering.py tests/test_desktop_layout.py
git commit -m "refactor: extract desktop rendering and image index"
```

### Task 3: Prompt citations and source-panel linking

**Files:**
- Modify: `src/raggg/generation/prompt_builder.py`
- Modify: `src/raggg/desktop/main_window.py`
- Create: `tests/test_prompt_builder_citations.py`
- Modify: `tests/test_desktop_layout.py`

**Interfaces:**
- Consumes: `markdown_to_html()` from Task 2.
- Produces: source cards with DOM IDs `source-1`, `source-2`, and so on.
- Produces: `WorkbenchWindow._focus_source(rank: int) -> None`.

- [ ] **Step 1: Write failing prompt and source-card tests**

Create:

```python
import unittest
from raggg.generation.prompt_builder import build_prompt


class PromptCitationTests(unittest.TestCase):
    def test_prompt_requires_sentence_end_citations(self) -> None:
        prompt = build_prompt("端口如何设置？", [])
        self.assertIn("[1][2]", prompt)
        self.assertIn("句末", prompt)
        self.assertIn("不得编造", prompt)
```

Extend desktop layout tests to assert `_sources_html()` contains `id="source-1"` and
that `_on_console_msg(..., "RAGGG_CITATION:1", ...)` invokes `_focus_source(1)`.

- [ ] **Step 2: Run the focused tests and confirm RED**

Run:

```powershell
$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest tests.test_prompt_builder_citations tests.test_desktop_layout -v
```

Expected: missing citation instruction, source ID, and focus method assertions fail.

- [ ] **Step 3: Add prompt rule and source focus behavior**

Append a language-neutral citation contract to the final prompt:

```python
CITATION_INSTRUCTION = (
    "引用规则：凡是由检索资料支持的事实，请在对应句末标注来源编号，如 [1]；"
    "多个来源连续写成 [1][2]。只能使用上方实际存在的编号，不得编造；"
    "没有资料支持的内容不要添加引用。"
)
```

Wrap every source card with `id="source-{rank}"`. Handle citation messages before
other console commands:

```python
if msg.startswith("RAGGG_CITATION:"):
    try:
        self._focus_source(int(msg.partition(":")[2]))
    except ValueError:
        return
```

Add:

```python
def _focus_source(self, rank: int) -> None:
    if rank not in self._source_paths:
        return
    source_id = json.dumps(f"source-{rank}")
    self.sources.page().runJavaScript(
        f"""const card=document.getElementById({source_id});
if(card){{card.scrollIntoView({{behavior:'smooth',block:'center'}});
card.classList.add('citation-target');
setTimeout(()=>card.classList.remove('citation-target'),1600);}}"""
    )
```

- [ ] **Step 4: Run prompt, rendering, and desktop tests and confirm GREEN**

Run:

```powershell
$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest tests.test_prompt_builder_citations tests.test_desktop_rendering tests.test_desktop_layout -v
```

Expected: all tests pass.

- [ ] **Step 5: Commit**

```powershell
git add -- src/raggg/generation/prompt_builder.py src/raggg/desktop/main_window.py tests/test_prompt_builder_citations.py tests/test_desktop_layout.py
git commit -m "feat: link answer citations to source cards"
```

### Task 4: Favorites, sessions, and views extraction

**Files:**
- Create: `src/raggg/desktop/favorites.py`
- Create: `src/raggg/desktop/sessions.py`
- Create: `src/raggg/desktop/views.py`
- Modify: `src/raggg/desktop/main_window.py`
- Modify: `tests/test_desktop_layout.py`
- Create: `tests/test_desktop_modules.py`

**Interfaces:**
- Produces: favorite helper functions and `FavoritesMixin`.
- Produces: `SessionPanel` with `new_requested`, `switch_requested`, `delete_requested`, and `toggle_requested` signals.
- Produces: `WorkbenchViewsMixin` for panel and reusable HTML view construction.
- Keeps compatibility imports for `favorite_matches` and `favorite_score`.

- [ ] **Step 1: Write failing module-boundary and line-count tests**

Create:

```python
from pathlib import Path
import unittest

from raggg.desktop.favorites import FavoritesMixin, favorite_matches, favorite_score
from raggg.desktop.sessions import SessionPanel
from raggg.desktop.views import WorkbenchViewsMixin


class DesktopModuleTests(unittest.TestCase):
    def test_main_window_stays_below_800_lines(self) -> None:
        path = Path("src/raggg/desktop/main_window.py")
        self.assertLess(len(path.read_text(encoding="utf-8").splitlines()), 800)

    def test_extracted_types_are_importable(self) -> None:
        self.assertTrue(FavoritesMixin)
        self.assertTrue(SessionPanel)
        self.assertTrue(WorkbenchViewsMixin)
        self.assertTrue(favorite_matches({"question": "port setup"}, "port"))
        self.assertGreater(favorite_score({"question": "port port"}, "port"), 0)
```

- [ ] **Step 2: Run the test and confirm RED**

Run:

```powershell
$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest tests.test_desktop_modules -v
```

Expected: imports fail because modules do not exist.

- [ ] **Step 3: Extract responsibilities and compose the window**

Move favorite persistence/search/dialog methods to `FavoritesMixin`; move panel controls
to `SessionPanel`; move panel construction and HTML view generation to
`WorkbenchViewsMixin`. Compose:

```python
class WorkbenchWindow(FavoritesMixin, WorkbenchViewsMixin, QMainWindow):
    ...
```

Connect the session component in `_build_ui()`:

```python
self.session_panel = SessionPanel(self._session_manager, self)
self.session_panel.new_requested.connect(self._new_session)
self.session_panel.switch_requested.connect(self._switch_session)
self.session_panel.delete_requested.connect(self._delete_session)
```

Keep the main window as the only owner of pipeline, worker, watcher, and cross-view
coordination. Remove moved implementations from `main_window.py` until the file is below
800 lines.

- [ ] **Step 4: Run module and desktop tests and confirm GREEN**

Run:

```powershell
$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest tests.test_desktop_modules tests.test_desktop_layout -v
```

Expected: all tests pass and line-count assertion passes.

- [ ] **Step 5: Commit**

```powershell
git add -- src/raggg/desktop/favorites.py src/raggg/desktop/sessions.py src/raggg/desktop/views.py src/raggg/desktop/main_window.py tests/test_desktop_modules.py tests/test_desktop_layout.py
git commit -m "refactor: split desktop favorites sessions and views"
```

### Task 5: Loader progress integration and final verification

**Files:**
- Modify: `src/raggg/desktop/main_window.py`
- Modify: `src/raggg/desktop/widgets.py`
- Modify: `tests/test_desktop_layout.py`

**Interfaces:**
- Consumes: `BuildProgress` and `build_knowledge_base(..., on_progress=...)` from Task 1.
- Produces: `AILoaderOverlay.set_progress_text(text: str) -> None`.

- [ ] **Step 1: Write failing loader-progress tests**

Add:

```python
def test_loader_progress_text_updates_during_rebuild(self) -> None:
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        with patch.object(WorkbenchWindow, "_build_image_index"), \
             patch.object(WorkbenchWindow, "_preload_images"), \
             patch.object(WorkbenchWindow, "_load_pipeline_if_ready"), \
             patch.object(WorkbenchWindow, "_start_source_watcher"):
            window = WorkbenchWindow(make_settings(root))
        window._on_build_progress(BuildProgress("embed", "正在生成向量", 3, 10))
        self.assertIn("正在生成向量", window.loader_overlay.progress_label.text())
        self.assertIn("3/10", window.loader_overlay.progress_label.text())
```

Also patch `build_knowledge_base` in `_rebuild_async()` and assert the worker-supplied callback
is callable and emits a `BuildProgress`.

- [ ] **Step 2: Run the focused test and confirm RED**

Run:

```powershell
$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest tests.test_desktop_layout.DesktopLayoutTests.test_loader_progress_text_updates_during_rebuild -v
```

Expected: missing `progress_label` or `_on_build_progress`.

- [ ] **Step 3: Connect builder callbacks to the UI thread**

Add a progress label below the animation and:

```python
def set_progress_text(self, text: str) -> None:
    self.progress_label.setText(text)
    self.progress_label.setVisible(bool(text))

def _on_build_progress(self, progress: BuildProgress) -> None:
    suffix = ""
    if progress.current is not None and progress.total:
        suffix = f" ({progress.current}/{progress.total})"
    self.loader_overlay.set_progress_text(progress.message + suffix)
```

Create workers with a closure so `Worker.signals.progress` carries builder events:

```python
worker: Worker

def rebuild() -> BuildReport:
    return build_knowledge_base(
        self.settings,
        on_progress=worker.signals.progress.emit,
    )

worker = Worker(rebuild)
worker.signals.progress.connect(self._on_build_progress)
```

Use the same helper for watcher rebuilds and clear progress text when the loader hides.

- [ ] **Step 4: Run complete automated verification**

Run:

```powershell
$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest discover -s tests -v
$lineCount=(Get-Content 'src\raggg\desktop\main_window.py').Count; if ($lineCount -ge 800) { throw "main_window.py has $lineCount lines" }
```

Expected: all tests pass and no line-count exception.

- [ ] **Step 5: Run desktop offscreen smoke test**

Run:

```powershell
$env:PYTHONPATH='src'
$env:QT_QPA_PLATFORM='offscreen'
$env:QTWEBENGINE_DISABLE_SANDBOX='1'
@'
from unittest.mock import patch
from raggg.config import load_settings
from raggg.desktop.main_window import WorkbenchWindow
from PySide6.QtWidgets import QApplication

app = QApplication.instance() or QApplication([])
with patch.object(WorkbenchWindow, "_load_pipeline_if_ready"), patch.object(WorkbenchWindow, "_start_source_watcher"):
    window = WorkbenchWindow(load_settings())
    window.show()
    app.processEvents()
    print("desktop-smoke-ok", window.isVisible())
    window.close()
'@ | .\.venv\Scripts\python.exe -
```

Expected: `desktop-smoke-ok True`.

- [ ] **Step 6: Commit**

```powershell
git add -- src/raggg/desktop tests
git commit -m "feat: show live index build progress"
```
