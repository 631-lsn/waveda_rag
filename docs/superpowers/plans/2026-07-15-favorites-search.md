# Favorites Search Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an instant search field to the favorites dialog that matches both saved questions and answers.

**Architecture:** Keep persistence and favorite ordering unchanged. Add a pure `favorite_matches()` helper for normalized substring matching, then let the existing PySide6 dialog toggle its already-created favorite cards as the search text changes.

**Tech Stack:** Python 3, PySide6, `unittest`

## Global Constraints

- Search both the `question` and `answer` fields.
- Match English text case-insensitively and Chinese text by substring containment.
- Update results immediately as the user types.
- Clearing the query restores every favorite in the existing newest-first order.
- Show “未找到相关收藏” when no card matches.
- Searching must not modify `data/favorites.json`.
- Preserve the existing view and delete behavior.
- Do not add a full-text index or change the persisted favorite schema.

---

### Task 1: Favorite text matching

**Files:**
- Modify: `src/raggg/desktop/main_window.py:80-100`
- Test: `tests/test_desktop_layout.py`

**Interfaces:**
- Consumes: a favorite mapping containing optional `question` and `answer` values, plus a string query.
- Produces: `favorite_matches(favorite: dict, query: str) -> bool`.

- [ ] **Step 1: Write the failing matching tests**

Add the helper import and this test method to `DesktopLayoutTests`:

```python
from raggg.desktop.main_window import AILoaderOverlay, WorkbenchWindow, favorite_matches

def test_favorite_search_matches_question_and_answer_case_insensitively(self) -> None:
    favorite = {
        "question": "How do I set a Wave Port?",
        "answer": "在边界设置中选择端口截面。",
    }

    self.assertTrue(favorite_matches(favorite, "wave port"))
    self.assertTrue(favorite_matches(favorite, "端口截面"))
    self.assertTrue(favorite_matches(favorite, ""))
    self.assertFalse(favorite_matches(favorite, "PML"))
```

- [ ] **Step 2: Run the focused test and verify RED**

Run:

```powershell
$env:PYTHONPATH = (Join-Path (Get-Location) "src")
& "D:\waveda_rag\.venv\Scripts\python.exe" -m unittest tests.test_desktop_layout.DesktopLayoutTests.test_favorite_search_matches_question_and_answer_case_insensitively -v
```

Expected: import failure because `favorite_matches` does not exist.

- [ ] **Step 3: Add the minimal matcher**

Add near the module-level regular expressions in `main_window.py`:

```python
def favorite_matches(favorite: dict, query: str) -> bool:
    normalized_query = query.strip().casefold()
    if not normalized_query:
        return True
    searchable_text = "\n".join(
        str(favorite.get(field, "")) for field in ("question", "answer")
    ).casefold()
    return normalized_query in searchable_text
```

- [ ] **Step 4: Run the focused test and verify GREEN**

Run the command from Step 2.

Expected: one test passes.

- [ ] **Step 5: Commit the matching behavior**

```powershell
git add -- src/raggg/desktop/main_window.py tests/test_desktop_layout.py
git commit -m "test: define favorites search matching"
```

### Task 2: Live filtering in the favorites dialog

**Files:**
- Modify: `src/raggg/desktop/main_window.py:1497-1544`
- Modify: `src/raggg/i18n.py:640-650`
- Test: `tests/test_desktop_layout.py`

**Interfaces:**
- Consumes: `favorite_matches(favorite: dict, query: str) -> bool` from Task 1 and localized strings from `get_text()`.
- Produces: a `QLineEdit` named `favoritesSearchInput`, favorite cards named `favoriteCard`, and a localized empty-result `QLabel` named `favoritesNoResults`.

- [ ] **Step 1: Write the failing dialog filtering test**

Add `QDialog`, `QFrame`, `QLabel`, and `QLineEdit` to the test imports, then add:

```python
def test_favorites_dialog_filters_question_and_answer_content(self) -> None:
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        root.joinpath("data").mkdir()
        root.joinpath("data", "favorites.json").write_text(
            json.dumps([
                {"question": "如何设置波端口？", "answer": "选择端口截面", "time": "2026-07-15 10:00"},
                {"question": "网格怎么划分？", "answer": "使用自适应网格", "time": "2026-07-15 11:00"},
            ], ensure_ascii=False),
            encoding="utf-8",
        )
        with patch.object(WorkbenchWindow, "_build_image_index"), \
             patch.object(WorkbenchWindow, "_preload_images"), \
             patch.object(WorkbenchWindow, "_load_pipeline_if_ready"), \
             patch.object(WorkbenchWindow, "_start_source_watcher"):
            window = WorkbenchWindow(make_settings(root))

        def inspect_dialog(dialog: QDialog) -> int:
            search_input = dialog.findChild(QLineEdit, "favoritesSearchInput")
            self.assertIsNotNone(search_input)
            search_input.setText("自适应网格")
            cards = dialog.findChildren(QFrame, "favoriteCard")
            self.assertEqual(sum(not card.isHidden() for card in cards), 1)
            self.assertTrue(dialog.findChild(QLabel, "favoritesNoResults").isHidden())
            search_input.setText("不存在的内容")
            self.assertTrue(all(card.isHidden() for card in cards))
            self.assertFalse(dialog.findChild(QLabel, "favoritesNoResults").isHidden())
            search_input.clear()
            self.assertTrue(all(not card.isHidden() for card in cards))
            return QDialog.Rejected

        with patch.object(QDialog, "exec", autospec=True, side_effect=inspect_dialog):
            window._open_favorites()
```

Also add `import json` at the top of the test module.

- [ ] **Step 2: Run the dialog test and verify RED**

Run:

```powershell
$env:PYTHONPATH = (Join-Path (Get-Location) "src")
& "D:\waveda_rag\.venv\Scripts\python.exe" -m unittest tests.test_desktop_layout.DesktopLayoutTests.test_favorites_dialog_filters_question_and_answer_content -v
```

Expected: failure because `favoritesSearchInput` is missing.

- [ ] **Step 3: Add localized UI copy**

Add to `TEXTS` in `i18n.py`:

```python
"favorites_search_placeholder": {
    "zh": "搜索问题和回答…",
    "en": "Search questions and answers…",
},
"favorites_no_results": {
    "zh": "未找到相关收藏",
    "en": "No matching favorites",
},
```

- [ ] **Step 4: Add the search field and live card visibility updates**

In `_open_favorites()`, insert a `QLineEdit` before the scroll area, name it `favoritesSearchInput`, and use the localized placeholder. Name each card `favoriteCard` and retain `(card, favorite)` pairs. Add a `QLabel` named `favoritesNoResults` after the cards and hide it initially. Connect `search_input.textChanged` to this function:

```python
def filter_cards(query: str) -> None:
    visible_count = 0
    for favorite_card, favorite in favorite_cards:
        matches = favorite_matches(favorite, query)
        favorite_card.setVisible(matches)
        visible_count += int(matches)
    no_results.setVisible(visible_count == 0)

search_input.textChanged.connect(filter_cards)
```

The existing card order, HTML rendering, delete-index calculation, and JSON writes remain unchanged.

- [ ] **Step 5: Run the focused desktop tests and verify GREEN**

Run:

```powershell
$env:PYTHONPATH = (Join-Path (Get-Location) "src")
& "D:\waveda_rag\.venv\Scripts\python.exe" -m unittest tests.test_desktop_layout -v
```

Expected: all desktop layout tests pass.

- [ ] **Step 6: Run the complete regression suite**

Run:

```powershell
$env:PYTHONPATH = (Join-Path (Get-Location) "src")
& "D:\waveda_rag\.venv\Scripts\python.exe" -m unittest discover -s tests -v
```

Expected: all existing and new tests pass with zero failures and zero errors.

- [ ] **Step 7: Commit the live search UI**

```powershell
git add -- src/raggg/desktop/main_window.py src/raggg/i18n.py tests/test_desktop_layout.py
git commit -m "feat: search saved questions and answers"
```
