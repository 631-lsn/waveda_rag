# Citation Source Popup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make clicking an answer citation such as `[1]` open its original knowledge document in the existing 960×680 `SourceViewer` window.

**Architecture:** Keep the citation renderer and console-message mapping unchanged. Change only `WorkbenchViewsMixin._focus_source()` so its existing source-path lookup and HTML conversion feed a `SourceViewer` instead of the narrow sidebar WebView.

**Tech Stack:** Python 3, PySide6, Qt WebEngine, unittest/pytest.

## Global Constraints

- Resolve citations only through the current answer's `_source_paths` mapping.
- Reuse the existing `SourceViewer`; do not add another window type.
- Keep the main chat window and right sidebar state unchanged.
- Preserve the existing missing-source warning.

---

### Task 1: Open cited documents in `SourceViewer`

**Files:**
- Modify: `src/raggg/desktop/views.py:992-1032`
- Test: `tests/test_desktop_layout.py`

**Interfaces:**
- Consumes: `self._source_paths: dict[int, str]`, `SourceViewer(title: str, html_content: str, parent: QWidget)`
- Produces: `WorkbenchViewsMixin._focus_source(rank: int) -> None` that shows the matching source viewer.

- [ ] **Step 1: Replace the sidebar regression test with a failing popup test**

```python
def test_citation_focus_opens_corresponding_source_document(self) -> None:
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        source_path = root / "port.md"
        source_path.write_text(
            "# Port setup\n\nConfigure the port here.",
            encoding="utf-8",
        )
        with patch.object(WorkbenchWindow, "_build_image_index"), \
             patch.object(WorkbenchWindow, "_preload_images"), \
             patch.object(WorkbenchWindow, "_load_pipeline_if_ready"), \
             patch.object(WorkbenchWindow, "_start_source_watcher"):
            window = WorkbenchWindow(make_settings(root))

        window._source_paths[1] = str(source_path)
        self.assertTrue(window.sidebar_container.isHidden())
        with patch("raggg.desktop.views.SourceViewer") as viewer_type:
            window._focus_source(1)

        self.assertTrue(window.sidebar_container.isHidden())
        title, rendered_html, parent = viewer_type.call_args.args
        self.assertEqual(title, "port")
        self.assertIn("Configure the port here.", rendered_html)
        self.assertIs(parent, window)
        viewer_type.return_value.show.assert_called_once_with()
```

- [ ] **Step 2: Run the test and verify the current sidebar behavior fails**

Run:

```powershell
$env:PYTHONPATH='src'
$env:QT_QPA_PLATFORM='offscreen'
$env:QTWEBENGINE_DISABLE_SANDBOX='1'
& 'C:\Users\30748\anaconda3\python.exe' -m pytest tests/test_desktop_layout.py::DesktopLayoutTests::test_citation_focus_opens_corresponding_source_document -q
```

Expected: FAIL because `SourceViewer` is not constructed and the sidebar becomes visible.

- [ ] **Step 3: Change `_focus_source()` to show the existing viewer**

Keep the current rank lookup, missing-file warning, and source-to-HTML conversion. Replace the final sidebar rendering block with:

```python
viewer = SourceViewer(file_path.stem, html_content, self)
viewer.show()
```

- [ ] **Step 4: Run focused and full automated verification**

Run the focused command from Step 2 and expect `1 passed`.

Then run:

```powershell
$env:PYTHONPATH='src'
$env:QT_QPA_PLATFORM='offscreen'
$env:QTWEBENGINE_DISABLE_SANDBOX='1'
& 'C:\Users\30748\anaconda3\python.exe' -m pytest -q
```

Expected: all tests pass, with only the existing environment-dependent skips.

- [ ] **Step 5: Perform a real WebEngine click smoke test**

Render `Answer sentence.[1]` with `markdown_to_html()`, click
`.citation a` through `runJavaScript()`, and verify a visible
`SourceViewer` exists whose document contains `Configure the port here.`.

- [ ] **Step 6: Commit and push the PR branch**

```powershell
git add src/raggg/desktop/views.py tests/test_desktop_layout.py
git commit -m "fix(desktop): open citations in source viewer"
git push origin feat/desktop-citations-progress
```
