# Manual Index Rebuild Button Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a visible manual “重建索引” action to the active data sidebar and connect it to the existing asynchronous rebuild pipeline.

**Architecture:** Extend `_sidebar_panel()` with one `rebuild_index_button`; reuse `_rebuild_async()`, `_on_rebuild_done()`, and `_set_busy()` instead of creating a second build path. Add only localized text and focused PySide6 regression coverage.

**Tech Stack:** Python 3, PySide6, `unittest`

## Global Constraints

- Place the button below the four status cards and above the existing settings/favorites actions.
- Run `build_knowledge_base(self.settings)` in the existing background worker.
- Disable asking, importing, and rebuilding while a build is active.
- Reload the pipeline, update chunk count, and sync the watcher after success.
- Reuse the existing rebuild error dialog.
- Do not change automatic watcher rebuilding, index format, or startup loading behavior.
- Support Chinese and English button labels.

---

### Task 1: Add the localized sidebar action

**Files:**
- Modify: `src/raggg/i18n.py:53-60`
- Modify: `src/raggg/desktop/main_window.py:1350-1375,1827-1835,2228-2234`
- Test: `tests/test_desktop_layout.py:30-70`

**Interfaces:**
- Consumes: existing `_rebuild_async()`, `_set_busy()`, and `get_text()`.
- Produces: `WorkbenchWindow.rebuild_index_button: QPushButton` connected to `_rebuild_async()`.

- [ ] **Step 1: Write the failing sidebar button test**

Add this test to `DesktopLayoutTests`:

```python
def test_sidebar_has_manual_rebuild_button_and_busy_state(self) -> None:
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        with patch.object(WorkbenchWindow, "_build_image_index"), \
             patch.object(WorkbenchWindow, "_preload_images"), \
             patch.object(WorkbenchWindow, "_load_pipeline_if_ready"), \
             patch.object(WorkbenchWindow, "_start_source_watcher"):
            window = WorkbenchWindow(make_settings(root))

        button = getattr(window, "rebuild_index_button", None)
        self.assertIsNotNone(button)
        self.assertEqual(button.text(), "重建索引")
        with patch.object(window, "_rebuild_async") as rebuild:
            button.click()
            rebuild.assert_called_once_with()

        window._set_busy(True, "正在重建知识库")
        self.assertTrue(button.isDisabled())
        window._set_busy(False, "就绪")
        self.assertFalse(button.isDisabled())
```

- [ ] **Step 2: Run the focused test and verify RED**

```powershell
$env:PYTHONPATH = (Join-Path (Get-Location) "src")
$env:QT_QPA_PLATFORM = "offscreen"
$env:QTWEBENGINE_DISABLE_SANDBOX = "1"
& "D:\waveda_rag\.venv\Scripts\python.exe" -m unittest tests.test_desktop_layout.DesktopLayoutTests.test_sidebar_has_manual_rebuild_button_and_busy_state -v
```

Expected: FAIL because `rebuild_index_button` does not exist.

- [ ] **Step 3: Add the localized label**

Add to `TEXTS` near the other button labels:

```python
"btn_rebuild_index": {
    "zh": "重建索引",
    "en": "Rebuild Index",
},
```

- [ ] **Step 4: Add and connect the active-sidebar button**

Immediately after `layout.addLayout(status_grid)` in `_sidebar_panel()` add:

```python
self.rebuild_index_button = self._button(get_text("btn_rebuild_index"), primary=True)
self.rebuild_index_button.clicked.connect(self._rebuild_async)
layout.addWidget(self.rebuild_index_button)
```

Do not add the button to the unused `_left_panel()`.

- [ ] **Step 5: Include the button in language refresh and busy-state disabling**

Extend `_refresh_ui_language()`:

```python
self.rebuild_index_button.setText(get_text("btn_rebuild_index"))
```

Extend `_set_busy()`:

```python
for button in (self.ask_button, self.import_button, self.rebuild_index_button):
    button.setDisabled(busy)
```

- [ ] **Step 6: Run the focused test and verify GREEN**

Run the command from Step 2.

Expected: one test passes.

- [ ] **Step 7: Commit the button integration**

```powershell
git add -- src/raggg/i18n.py src/raggg/desktop/main_window.py tests/test_desktop_layout.py
git commit -m "feat: add manual index rebuild button"
```

### Task 2: Regression verification

**Files:**
- Verify: `src/raggg/desktop/main_window.py`
- Verify: `src/raggg/i18n.py`
- Verify: `tests/test_desktop_layout.py`

**Interfaces:**
- Consumes: `rebuild_index_button` and the existing asynchronous rebuild callbacks from Task 1.
- Produces: verified UI behavior without a second indexing implementation.

- [ ] **Step 1: Run the desktop layout tests**

```powershell
& "D:\waveda_rag\.venv\Scripts\python.exe" -m unittest tests.test_desktop_layout -v
```

Expected: all desktop tests pass.

- [ ] **Step 2: Run the complete suite and static checks**

```powershell
& "D:\waveda_rag\.venv\Scripts\python.exe" -m unittest discover -s tests -v
& "D:\waveda_rag\.venv\Scripts\python.exe" -m compileall -q src tests
git diff --check
```

Expected: all tests pass with zero failures and errors; compileall and diff checks exit 0.
