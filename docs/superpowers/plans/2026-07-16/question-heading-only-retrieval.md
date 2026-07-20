# Question Heading-Only Retrieval Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Restrict retrieval matching to each chunk's question heading (`section`, the text after `Q:`), while still passing the matched chunk body to answer generation.

**Architecture:** `Retriever.search` will build both vector and lexical representations from `chunk.section` only. The returned `SearchResult` remains unchanged, so downstream prompt construction continues to use the full matched chunk. Existing query-order-independent lexical matching remains active.

**Tech Stack:** Python, NumPy, unittest, existing hashed embedding model.

## Global Constraints

- Do not change chunk storage or rebuild the index format.
- Do not use chunk body text for retrieval scoring.
- Keep matched chunk content available for answer generation.

---

### Task 1: Add heading-only retrieval regression tests

**Files:**
- Modify: `tests/test_retriever_quality.py`

- [ ] Add a test with two chunks whose headings differ, while only the body of the distractor contains the query words; assert the distractor is not selected for that query.
- [ ] Add a test asserting the FAQ question heading `S 参数怎么导出？` matches both `S参数如何导出` and `如何导出S参数`.
- [ ] Run `PYTHONPATH=src .venv/Scripts/python.exe -m unittest tests.test_retriever_quality -v` and confirm the new tests fail before implementation.

### Task 2: Restrict Retriever scoring inputs to question headings

**Files:**
- Modify: `src/raggg/retrieval/retriever.py`

- [ ] Set the query embedding comparison to `embed_text(chunk.section)` rather than the prebuilt body embedding.
- [ ] Use `chunk.section` for lexical and heading overlap calculations.
- [ ] Remove body-based special-term and formula boosts from retrieval scoring; preserve the returned `SearchResult.chunk` unchanged for downstream answer context.
- [ ] Run the focused retriever tests and confirm they pass.

### Task 3: Run full verification and commit

**Files:**
- No additional files.

- [ ] Run all tests with the offscreen Qt environment, compileall, and `git diff --check`.
- [ ] Commit with `feat: retrieve by question headings only`.
- [ ] Push `main` after verification.
