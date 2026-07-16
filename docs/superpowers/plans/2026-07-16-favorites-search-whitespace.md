# Favorites Search Whitespace Tolerance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make favorites search insensitive to missing, repeated, and Unicode whitespace while restoring the existing dialog verification contract.

**Architecture:** Preserve the current multi-keyword matching behavior, but use one pure normalization helper for the compact substring path and compact relevance score. Restore the two Qt object names removed by the later dialog redesign so the existing end-to-end dialog test can verify the actual controls again.

**Tech Stack:** Python 3, PySide6, `unittest`

## Global Constraints

- Ignore ordinary spaces, repeated spaces, tabs, newlines, non-breaking spaces, and full-width spaces during compact matching.
- Preserve case-insensitive matching and unordered multi-keyword matching.
- A query containing only whitespace must show all favorites.
- Apply identical whitespace normalization to question and answer content.
- Keep favorite persistence, ordering, deletion, rendering, and highlighting behavior unchanged.
- Restore `favoritesSearchInput` and `favoritesNoResults` object names without visual changes.

---

### Task 1: Restore the favorites dialog verification contract

**Files:**
- Modify: `src/raggg/desktop/main_window.py:1575-1583,1680-1688`
- Test: `tests/test_desktop_layout.py:211-244`

**Interfaces:**
- Consumes: the existing `QLineEdit` search control and `QLabel` no-results control.
- Produces: Qt objects discoverable as `favoritesSearchInput` and `favoritesNoResults`.

- [ ] **Step 1: Re-run the existing failing dialog test**

```powershell
$env:PYTHONPATH = (Join-Path (Get-Location) "src")
$env:QT_QPA_PLATFORM = "offscreen"
$env:QTWEBENGINE_DISABLE_SANDBOX = "1"
& "D:\waveda_rag\.venv\Scripts\python.exe" -m unittest tests.test_desktop_layout.DesktopLayoutTests.test_favorites_dialog_filters_question_and_answer_content -v
```

Expected: FAIL because `dialog.findChild(QLineEdit, "favoritesSearchInput")` returns `None`.

- [ ] **Step 2: Restore the two stable object names**

Add these calls immediately after each widget is created:

```python
search_input = QLineEdit()
search_input.setObjectName("favoritesSearchInput")

no_results = QLabel(get_text("favorites_no_results"))
no_results.setObjectName("favoritesNoResults")
```

- [ ] **Step 3: Re-run the focused dialog test**

Run the command from Step 1.

Expected: one test passes.

- [ ] **Step 4: Commit the baseline repair**

```powershell
git add -- src/raggg/desktop/main_window.py
git commit -m "fix: restore favorites dialog test identifiers"
```

### Task 2: Normalize all whitespace in favorites matching

**Files:**
- Modify: `src/raggg/desktop/main_window.py:90-125`
- Test: `tests/test_desktop_layout.py:201-210`

**Interfaces:**
- Consumes: arbitrary search text plus favorite `question` and `answer` values.
- Produces: `normalize_favorite_search_text(text: object) -> str`; updated `favorite_matches(favorite: dict, query: str) -> bool`; consistent compact scoring from `favorite_score(favorite: dict, query: str) -> int`.

- [ ] **Step 1: Write the failing whitespace-tolerance test**

Add `favorite_score` to the import and add this test:

```python
def test_favorite_search_ignores_all_whitespace_variants(self) -> None:
    favorite = {
        "question": "How do I set a Wave Port?",
        "answer": "选择\u00a0端口\t截面。",
    }

    for query in (
        "waveport",
        "wave   port",
        "wave\tport",
        "wave\u3000port",
        "选择端口截面",
        "选择\n端口\u00a0截面",
    ):
        with self.subTest(query=query):
            self.assertTrue(favorite_matches(favorite, query))
            self.assertGreater(favorite_score(favorite, query), 0)

    self.assertTrue(favorite_matches(favorite, " \t\u00a0\n"))
```

- [ ] **Step 2: Run the whitespace test and verify RED**

```powershell
$env:PYTHONPATH = (Join-Path (Get-Location) "src")
$env:QT_QPA_PLATFORM = "offscreen"
$env:QTWEBENGINE_DISABLE_SANDBOX = "1"
& "D:\waveda_rag\.venv\Scripts\python.exe" -m unittest tests.test_desktop_layout.DesktopLayoutTests.test_favorite_search_ignores_all_whitespace_variants -v
```

Expected: FAIL for the compact Chinese query because the favorite answer contains non-breaking and tab whitespace that `.replace(" ", "")` does not remove.

- [ ] **Step 3: Add the shared normalization helper**

Add before `favorite_matches()`:

```python
def normalize_favorite_search_text(text: object) -> str:
    return "".join(str(text).casefold().split())
```

- [ ] **Step 4: Use shared normalization in matching and scoring**

Keep the current keyword path and replace the ASCII-space-only compact values with:

```python
query_compact = normalize_favorite_search_text(query)
searchable_compact = normalize_favorite_search_text(searchable_text)
```

In `favorite_matches()`, keep:

```python
return (
    all(kw in searchable_text for kw in keywords)
    or query_compact in searchable_compact
)
```

In `favorite_score()`, keep the existing keyword score and add the compact count only when `query_compact` is non-empty:

```python
if query_compact:
    score += searchable_compact.count(query_compact) * 2
return score
```

- [ ] **Step 5: Run focused search tests**

```powershell
& "D:\waveda_rag\.venv\Scripts\python.exe" -m unittest tests.test_desktop_layout.DesktopLayoutTests.test_favorite_search_matches_question_and_answer_case_insensitively tests.test_desktop_layout.DesktopLayoutTests.test_favorite_search_ignores_all_whitespace_variants tests.test_desktop_layout.DesktopLayoutTests.test_favorites_dialog_filters_question_and_answer_content -v
```

Expected: all three tests pass.

- [ ] **Step 6: Run the complete regression suite and static verification**

```powershell
& "D:\waveda_rag\.venv\Scripts\python.exe" -m unittest discover -s tests -v
& "D:\waveda_rag\.venv\Scripts\python.exe" -m compileall -q src tests
git diff --check
```

Expected: the complete suite passes with zero failures and errors; `compileall` and `git diff --check` exit with code 0.

- [ ] **Step 7: Commit the whitespace fix**

```powershell
git add -- src/raggg/desktop/main_window.py tests/test_desktop_layout.py
git commit -m "fix: normalize whitespace in favorites search"
```
