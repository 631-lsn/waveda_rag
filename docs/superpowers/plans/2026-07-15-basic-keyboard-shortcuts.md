# Basic Keyboard Shortcuts Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add `Ctrl+L`, `Ctrl+N`, and `Ctrl+B` window-level shortcuts to the PySide6 workbench with safe busy-state behavior and discoverable tooltips.

**Architecture:** `WorkbenchWindow` owns three `QShortcut` instances created after the UI widgets exist. Small semantic handler methods isolate focus and busy-state rules, while existing `_new_session()` and `_toggle_sidebar()` methods remain the source of truth.

**Tech Stack:** Python 3, PySide6 (`QShortcut`, `QKeySequence`), unittest

## Global Constraints

- Use `Qt.WindowShortcut`; do not register system-global hotkeys.
- Add only `Ctrl+L`, `Ctrl+N`, and `Ctrl+B`; do not add `Esc`.
- Preserve the input field's existing `Enter`-to-send behavior.
- `Ctrl+N` must not change sessions while `is_busy` is true.
- `Ctrl+B` controls only `sidebar_container`, not the history panel.

---

### Task 1: Add and verify the three workbench shortcuts

**Files:**
- Modify: `tests/test_desktop_layout.py`
- Modify: `src/raggg/desktop/main_window.py`

**Interfaces:**
- Consumes: `_new_session() -> None`, `_toggle_sidebar() -> None`, `is_busy: bool`, and `question: QLineEdit`.
- Produces: `_setup_shortcuts() -> None`, `_focus_question_input() -> None`, `_new_session_from_shortcut() -> None`, plus three window-owned `QShortcut` attributes.

- [ ] **Step 1: Write failing shortcut tests**

Import `QKeySequence` and `QShortcut`. Add tests using the existing patched `WorkbenchWindow` construction pattern:

```python
def test_basic_shortcuts_are_window_scoped(self) -> None:
    expected = {
        "focusQuestionShortcut": "Ctrl+L",
        "newSessionShortcut": "Ctrl+N",
        "toggleSidebarShortcut": "Ctrl+B",
    }
    shortcuts = {item.objectName(): item for item in window.findChildren(QShortcut)}
    self.assertEqual(set(shortcuts), set(expected))
    for name, sequence in expected.items():
        self.assertEqual(shortcuts[name].key(), QKeySequence(sequence))
        self.assertEqual(shortcuts[name].context(), Qt.WindowShortcut)

def test_ctrl_l_focuses_and_selects_question_text(self) -> None:
    window.question.setText("replace me")
    window.focus_question_shortcut.activated.emit()
    self.assertTrue(window.question.hasFocus())
    self.assertEqual(window.question.selectedText(), "replace me")

def test_ctrl_n_creates_session_only_while_idle(self) -> None:
    original_id = window._session_manager.current_id
    window.new_session_shortcut.activated.emit()
    idle_id = window._session_manager.current_id
    self.assertNotEqual(idle_id, original_id)
    self.assertTrue(window.question.hasFocus())
    window.is_busy = True
    window.new_session_shortcut.activated.emit()
    self.assertEqual(window._session_manager.current_id, idle_id)

def test_ctrl_b_toggles_only_data_sidebar(self) -> None:
    session_was_visible = window.session_panel.isVisible()
    self.assertTrue(window.sidebar_container.isHidden())
    window.toggle_sidebar_shortcut.activated.emit()
    self.assertFalse(window.sidebar_container.isHidden())
    self.assertEqual(window.session_panel.isVisible(), session_was_visible)
```

- [ ] **Step 2: Run the new tests and verify RED**

Run:

```powershell
$env:PYTHONPATH='src'; runtime\python\python.exe -m unittest tests.test_desktop_layout.DesktopLayoutTests.test_basic_shortcuts_are_window_scoped tests.test_desktop_layout.DesktopLayoutTests.test_ctrl_l_focuses_and_selects_question_text tests.test_desktop_layout.DesktopLayoutTests.test_ctrl_n_creates_session_only_while_idle tests.test_desktop_layout.DesktopLayoutTests.test_ctrl_b_toggles_only_data_sidebar -v
```

Expected: FAIL because shortcut attributes and bindings do not exist.

- [ ] **Step 3: Implement the minimal bindings**

Import `QKeySequence` and `QShortcut`, call `self._setup_shortcuts()` after `self._build_ui()`, and add:

```python
def _setup_shortcuts(self) -> None:
    self.focus_question_shortcut = QShortcut(QKeySequence("Ctrl+L"), self)
    self.focus_question_shortcut.setObjectName("focusQuestionShortcut")
    self.focus_question_shortcut.setContext(Qt.WindowShortcut)
    self.focus_question_shortcut.activated.connect(self._focus_question_input)

    self.new_session_shortcut = QShortcut(QKeySequence("Ctrl+N"), self)
    self.new_session_shortcut.setObjectName("newSessionShortcut")
    self.new_session_shortcut.setContext(Qt.WindowShortcut)
    self.new_session_shortcut.activated.connect(self._new_session_from_shortcut)

    self.toggle_sidebar_shortcut = QShortcut(QKeySequence("Ctrl+B"), self)
    self.toggle_sidebar_shortcut.setObjectName("toggleSidebarShortcut")
    self.toggle_sidebar_shortcut.setContext(Qt.WindowShortcut)
    self.toggle_sidebar_shortcut.activated.connect(self._toggle_sidebar)

def _focus_question_input(self) -> None:
    self.question.setFocus(Qt.ShortcutFocusReason)
    self.question.selectAll()

def _new_session_from_shortcut(self) -> None:
    if self.is_busy:
        return
    self._new_session()
    self._focus_question_input()
```

Append `(Ctrl+B)` and `(Ctrl+N)` to the existing side-panel and new-session button tooltips, and set the input tooltip to `Ctrl+L`.

- [ ] **Step 4: Run the targeted tests and verify GREEN**

Repeat Step 2. Expected: all four tests PASS.

- [ ] **Step 5: Run regression tests**

```powershell
$env:PYTHONPATH='src'; runtime\python\python.exe -m unittest tests.test_desktop_layout -v
```

Expected: every desktop layout test PASS.

- [ ] **Step 6: Check scope and commit**

```powershell
git diff --check
git diff -- src/raggg/desktop/main_window.py tests/test_desktop_layout.py
git add -- src/raggg/desktop/main_window.py tests/test_desktop_layout.py docs/superpowers/plans/2026-07-15-basic-keyboard-shortcuts.md
git commit -m "feat: add basic workbench shortcuts"
```
