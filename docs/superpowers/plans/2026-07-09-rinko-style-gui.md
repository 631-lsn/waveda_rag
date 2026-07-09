# RINKO Style GUI Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the crowded three-column desktop UI with a reference-image-inspired minimal gradient chat interface.

**Architecture:** Keep the existing `RAGPipeline`, file ingestion, auto-watch, source rendering, settings, and favorites logic. Change only the PySide6 widget composition and styling in `src/raggg/desktop/main_window.py`, with a focused GUI structure test in `tests/test_desktop_layout.py`.

**Tech Stack:** Python 3, PySide6 Qt Widgets, QWebEngineView, unittest.

## Global Constraints

- Do not delete files or directories in batches.
- The main screen must not show "我在听，RINKO" or "我在听，WavEDA".
- The default screen should visually match the provided minimal gradient reference.
- Sources and status must be reachable through a show/hide sidebar button.
- Existing ask, import, settings, favorites, source, and auto-watch behavior must remain available.

---

### Task 1: GUI Contract Test

**Files:**
- Create: `tests/test_desktop_layout.py`

**Interfaces:**
- Consumes: `WorkbenchWindow(settings: Settings)`.
- Produces: tests asserting `sidebar_container`, `sidebar_toggle_button`, `question`, `ask_button`, and `import_button`.

- [ ] **Step 1: Write the failing test**

```python
def test_minimal_gui_starts_with_hidden_sidebar(self):
    window = WorkbenchWindow(make_settings(root))
    self.assertFalse(window.sidebar_container.isVisible())
    self.assertEqual(window.sidebar_toggle_button.text(), "☰")
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `$env:PYTHONPATH='src'; $env:QT_QPA_PLATFORM='offscreen'; .\.venv\Scripts\python.exe -m unittest tests.test_desktop_layout -v`

Expected: FAIL because the old UI has no `sidebar_container`.

### Task 2: Minimal Gradient Shell

**Files:**
- Modify: `src/raggg/desktop/main_window.py`

**Interfaces:**
- Consumes: existing `_chat_panel`, `_source_panel`, `_left_panel`, `_button`, `_ask`, `_import_document`.
- Produces: `_build_ui()` with a full-window gradient shell, bottom composer, top-right sidebar toggle, and hidden sidebar container.

- [ ] **Step 1: Replace the grid layout**

Create a main vertical overlay-like layout with a transparent chat area, a bottom glass input bar, and a right dock container hidden by default.

- [ ] **Step 2: Preserve behavior**

Connect `+` to `_import_document`, the arrow button to `_ask`, and the top-right toggle button to `_toggle_sidebar`.

- [ ] **Step 3: Run the GUI contract test**

Run: `$env:PYTHONPATH='src'; $env:QT_QPA_PLATFORM='offscreen'; .\.venv\Scripts\python.exe -m unittest tests.test_desktop_layout -v`

Expected: PASS.

### Task 3: Verification

**Files:**
- Verify: `src/raggg/desktop/main_window.py`
- Verify: `tests/test_desktop_layout.py`

**Interfaces:**
- Consumes: all modified files.
- Produces: clean test and compile evidence.

- [ ] **Step 1: Compile desktop files**

Run: `.\.venv\Scripts\python.exe -m py_compile app\desktop_app.py src\raggg\desktop\main_window.py src\raggg\i18n.py`

Expected: exit code 0.

- [ ] **Step 2: Run all tests**

Run: `$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest discover -s tests -v`

Expected: all tests pass.

- [ ] **Step 3: Smoke launch**

Run: `cmd /c start.bat`, confirm the GUI process starts, then close only the explicit test-launched process if needed.

Expected: `pythonw.exe` command line includes `D:\waveda_rag\app\desktop_app.py`.
