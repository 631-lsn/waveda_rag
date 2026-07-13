# React Personality Welcome Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add six persistent assistant personalities to the React desktop GUI so the welcome copy and generated answers use the same selected style.

**Architecture:** A Python personality module owns valid identifiers and Prompt text. `DesktopStore` persists the selected identifier, the bridge refreshes runtime personality, and React receives it through bootstrap to drive both the settings selector and typed welcome-copy lookup.

**Tech Stack:** Python 3.14, PySide6 WebChannel, React, TypeScript, Tailwind CSS, unittest, Vitest, Testing Library

## Global Constraints

- Valid values are exactly `normal`, `mature`, `sweet`, `dog`, `cat`, and `workhorse`.
- Saving a personality takes effect without restarting the application.
- Welcome copy supports Chinese and English.
- No new dependency is added.
- API credentials and conversation records are not modified by tests.

---

### Task 1: Persist personality and inject it into prompts

**Files:**
- Create: `src/raggg/generation/personality.py`
- Modify: `src/raggg/desktop/store.py`
- Modify: `src/raggg/desktop/web_bridge.py`
- Modify: `src/raggg/generation/prompt_builder.py`
- Modify: `tests/test_desktop_store.py`
- Modify: `tests/test_web_bridge.py`
- Create: `tests/test_personality.py`

**Interfaces:**
- Produces: `PERSONALITIES`, `get_personality()`, `set_personality(name, persist=True)`, `get_personality_prompt(lang)`
- Produces: bootstrap field `personality: str` and settings field `personality`

- [ ] Write failing tests proving default personality is `normal`, saving `cat` survives reload, invalid values raise `ValueError`, bridge refreshes the runtime value, and `build_prompt()` contains the selected personality instruction.
- [ ] Run `python -m unittest tests.test_personality tests.test_desktop_store tests.test_web_bridge -v`; expect failures for missing personality APIs and payload fields.
- [ ] Backport the six definitions from `main`, validate settings against `PERSONALITIES`, persist `RAG_PERSONALITY`, refresh runtime state after save, and prepend the selected prompt fragment.
- [ ] Re-run the focused Python tests; expect all selected modules to pass.

### Task 2: Add typed personality settings to React

**Files:**
- Modify: `frontend/src/lib/contracts.ts`
- Modify: `frontend/src/lib/i18n.ts`
- Create: `frontend/src/lib/personality.ts`
- Modify: `frontend/src/features/settings/settings-page.tsx`
- Create: `frontend/src/features/settings/settings-page.test.tsx`

**Interfaces:**
- Produces: `Personality` union type and `PERSONALITY_OPTIONS`
- Produces: `getWelcomeCopy(locale, personality)` returning `{ title, intro, detail }`
- Consumes/produces: `SettingsUpdate.personality` and `BootstrapPayload.personality`

- [ ] Write failing tests that iterate all six values through `getWelcomeCopy`, then select `cat` in `SettingsPage` and expect `onSave` to receive `{ personality: "cat" }`.
- [ ] Run the two focused Vitest files; expect failures because the personality module and selector do not exist.
- [ ] Add typed bilingual labels, descriptions, welcome copy, a personality settings tab, six option cards, and save the selected value with the existing settings payload.
- [ ] Re-run focused tests; expect all personality/settings assertions to pass.

### Task 3: Render current personality on the welcome page

**Files:**
- Modify: `frontend/src/App.tsx`
- Modify: `frontend/src/App.test.tsx`
- Modify: `frontend/src/features/chat/chat-page.tsx`

**Interfaces:**
- Consumes: `bootstrap.personality`
- Produces: `ChatPageProps.personality: Personality`

- [ ] Extend the test bootstrap with `personality: "cat"` and assert the cat-specific welcome title is visible after bootstrap.
- [ ] Run `npm test -- --run src/App.test.tsx`; expect failure while `ChatPage` still uses generic `t("welcome")` copy.
- [ ] Pass personality into `ChatPage`, call `getWelcomeCopy`, and render title, intro, and detail in the empty-conversation welcome card.
- [ ] Run all Python tests, all frontend tests, `npm run typecheck`, and `npm run build`; expect zero failures.
- [ ] Launch an isolated desktop instance, visually inspect the personality selector and welcome page, then commit code, tests, and generated `frontend/dist` assets.
