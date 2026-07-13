# WavEDA React GUI Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the complete PySide6 widget GUI with a responsive React, TypeScript, Tailwind, and shadcn-compatible desktop interface while preserving the Python RAG backend and `start.bat` launch flow.

**Architecture:** Build a Vite React SPA into `frontend/dist` and load it in a new PySide6 `QWebEngineView` window. A JSON-based, typed `QWebChannel` bridge exposes bootstrap, question answering, history, favorites, settings, document ingestion, and index operations while Python remains the persistence and backend authority.

**Tech Stack:** Python 3, PySide6/QWebEngine/QWebChannel, React, TypeScript, Vite, Tailwind CSS, shadcn-compatible primitives, lucide-react, styled-jsx, Vitest, React Testing Library.

## Global Constraints

- Do not batch-delete files or directories and do not use `del /s`, `rd /s`, `rmdir /s`, `Remove-Item -Recurse`, or `rm -rf`.
- Keep `src/raggg/desktop/main_window.py` as a non-default legacy fallback; do not delete it.
- Keep the existing Python RAG, ingestion, source watching, knowledge-base content, and `start.bat` production entry flow.
- Use `frontend/src/components/ui` as the shadcn component path and `frontend/src/index.css` as the global style path.
- Copy the supplied AI loader API and animation into `frontend/src/components/ui/ai-loader.tsx`.
- Dark mode is the default; light mode must be complete.
- Production must not require a frontend development server or globally installed Node.js.
- API keys must never be returned to React as plaintext.
- No batch-delete UI is permitted.

---

### Task 1: Frontend Toolchain and Loader Contract

**Files:**
- Create: `frontend/package.json`
- Create: `frontend/tsconfig.json`
- Create: `frontend/tsconfig.app.json`
- Create: `frontend/tsconfig.node.json`
- Create: `frontend/vite.config.ts`
- Create: `frontend/components.json`
- Create: `frontend/index.html`
- Create: `frontend/src/main.tsx`
- Create: `frontend/src/index.css`
- Create: `frontend/src/components/ui/ai-loader.tsx`
- Create: `frontend/src/components/ui/ai-loader.test.tsx`
- Modify: `.gitignore`

**Interfaces:**
- Produces: `Component({ size?: number, text?: string })` from `@/components/ui/ai-loader`.
- Produces: `npm run typecheck`, `npm test -- --run`, and `npm run build` scripts.
- Produces: relative-path Vite output in `frontend/dist` for `file://` loading.

- [ ] **Step 1: Create the package and TypeScript configuration**

Use React, React DOM, lucide-react, styled-jsx, class-variance-authority, clsx, tailwind-merge, Vite, TypeScript, Tailwind, Vitest, jsdom, and Testing Library. Configure `@/*` to resolve to `src/*`, set Vite `base: "./"`, use the React Babel plugin `styled-jsx/babel`, and configure Vitest with `jsdom`.

- [ ] **Step 2: Write the failing loader test**

```tsx
import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { Component } from "./ai-loader";

describe("AI loader", () => {
  it("renders custom text one letter at a time in a sized overlay", () => {
    const { container } = render(<Component size={144} text="正在检索" />);
    expect(screen.getByText("正")).toBeInTheDocument();
    expect(screen.getByText("索")).toBeInTheDocument();
    expect(container.querySelector('[data-testid="ai-loader-orbit"]')).toHaveStyle({
      width: "144px",
      height: "144px",
    });
  });
});
```

- [ ] **Step 3: Run the focused test and verify RED**

Run: `npm test -- --run src/components/ui/ai-loader.test.tsx`

Expected: FAIL because `ai-loader.tsx` does not exist.

- [ ] **Step 4: Add the supplied loader**

Copy the user-supplied implementation into `frontend/src/components/ui/ai-loader.tsx`, retain the `Component` export and `LoaderProps`, and add only `data-testid="ai-loader-orbit"` to the sized inner wrapper for behavioral testing. Preserve the `<style jsx>` keyframes.

- [ ] **Step 5: Verify GREEN and build**

Run: `npm test -- --run src/components/ui/ai-loader.test.tsx`

Expected: one passing test.

Run: `npm run typecheck && npm run build`

Expected: exit code 0 and `frontend/dist/index.html` exists.

### Task 2: Typed Frontend Bridge Adapter

**Files:**
- Create: `frontend/src/lib/contracts.ts`
- Create: `frontend/src/lib/bridge.ts`
- Create: `frontend/src/lib/bridge.test.ts`
- Create: `frontend/src/vite-env.d.ts`

**Interfaces:**
- Produces: `DesktopBridgeClient` with `bootstrap`, `ask`, `stopAnswer`, `selectAndImportDocument`, `listHistory`, `renameHistory`, `deleteHistory`, `listFavorites`, `saveFavorite`, `deleteFavorite`, `saveSettings`, and `rebuildIndex`.
- Produces: `BridgeEvent` discriminated union using `requestId` for asynchronous operations.
- Consumes: a QWebChannel object exposing methods that accept JSON strings and return JSON strings through callbacks.

- [ ] **Step 1: Write failing adapter tests**

Test that bootstrap JSON is parsed, events are decoded, malformed payloads become a safe `bridge_error`, and API-key plaintext is not part of `BootstrapPayload`.

```ts
it("parses bootstrap and forwards typed events", async () => {
  const fake = makeFakeBackend({ locale: "zh", theme: "dark", apiConfigured: true });
  const client = new DesktopBridgeClient(fake);
  expect((await client.bootstrap()).theme).toBe("dark");
  const seen: BridgeEvent[] = [];
  client.subscribe((event) => seen.push(event));
  fake.emit({ type: "answer_progress", requestId: "r1", phase: "retrieving" });
  expect(seen[0]).toMatchObject({ type: "answer_progress", phase: "retrieving" });
});
```

- [ ] **Step 2: Run the adapter test and verify RED**

Run: `npm test -- --run src/lib/bridge.test.ts`

Expected: FAIL because the client is missing.

- [ ] **Step 3: Implement contracts and adapter**

Use a single `invoke(method, payload)` callback wrapper, lazy-load `qrc:///qtwebchannel/qwebchannel.js` only when `window.qt.webChannelTransport` exists, and provide a development fallback that reports bridge unavailability instead of rendering a blank page.

- [ ] **Step 4: Verify GREEN**

Run: `npm test -- --run src/lib/bridge.test.ts`

Expected: all bridge adapter tests pass.

### Task 3: Python Persistence and Sanitized Settings Services

**Files:**
- Create: `src/raggg/desktop/store.py`
- Create: `tests/test_desktop_store.py`

**Interfaces:**
- Produces: `DesktopStore(settings: Settings)`.
- Produces: `bootstrap_payload() -> dict`, `list_conversations() -> list[dict]`, `save_turn(conversation_id, question, answer, sources) -> dict`, `rename_conversation(id, title) -> dict`, `delete_conversation(id) -> bool`.
- Produces: `list_favorites()`, `save_favorite(payload)`, and `delete_favorite(id)` with migration support for current `data/favorites.json` records.
- Produces: `save_settings(payload) -> dict` while omitting API-key plaintext from every response.

- [ ] **Step 1: Write failing persistence tests**

Cover sanitized bootstrap, conversation creation and rename, single-record deletion, favorite migration, and preserving the existing API key when the frontend submits no replacement.

```python
def test_bootstrap_never_returns_api_key(self):
    store = DesktopStore(make_settings(self.root, api_key="secret-value"))
    payload = store.bootstrap_payload()
    self.assertTrue(payload["apiConfigured"])
    self.assertNotIn("apiKey", payload)
    self.assertNotIn("secret-value", json.dumps(payload))
```

- [ ] **Step 2: Run and verify RED**

Run: `$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest tests.test_desktop_store -v`

Expected: FAIL because `DesktopStore` is missing.

- [ ] **Step 3: Implement the JSON stores**

Write `data/conversations.json` and the existing `data/favorites.json` as UTF-8 JSON. Use UUID identifiers, ISO timestamps, deterministic titles from the first question, and a write-to-single-temp-file then replace operation. Never enumerate files for deletion; delete only the selected in-memory record and rewrite its one store file.

- [ ] **Step 4: Verify GREEN**

Run: `$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest tests.test_desktop_store -v`

Expected: all store tests pass.

### Task 4: RAG Progress Hook and QWebChannel Backend

**Files:**
- Modify: `src/raggg/pipeline/rag_pipeline.py`
- Create: `src/raggg/desktop/web_bridge.py`
- Create: `tests/test_web_bridge.py`
- Modify: `tests/test_desktop_layout.py`

**Interfaces:**
- Extends: `RAGPipeline.ask(..., progress: Callable[[str], None] | None = None) -> RAGAnswer`.
- Produces: `DesktopBridge(QObject)` with `event_json = Signal(str)` and JSON-returning Qt slots matching the frontend adapter.
- Consumes: `DesktopStore`, `RAGPipeline`, `ingest_document`, `build_knowledge_base`, and the existing source watcher.

- [ ] **Step 1: Write failing progress and bridge tests**

Verify that `RAGPipeline.ask` reports `retrieving` before search and `generating` after retrieval. Verify bootstrap sanitization, asynchronous answer events, import success/failure, one-record history/favorite deletion, and that every error emits a terminal event.

- [ ] **Step 2: Run and verify RED**

Run: `$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest tests.test_web_bridge -v`

Expected: FAIL because `DesktopBridge` and the progress hook are missing.

- [ ] **Step 3: Add the progress hook**

Call `progress("retrieving")` immediately before retrieval and `progress("generating")` immediately after sources are available. Keep the default `None` so all existing callers remain compatible.

- [ ] **Step 4: Implement the bridge**

Validate every JSON payload, generate request IDs in React, use `QThreadPool` for blocking work, emit progress and terminal JSON events through Qt signals, ignore late detached answer results, and refresh pipeline/store state after successful settings or index changes.

- [ ] **Step 5: Verify GREEN and regression tests**

Run: `$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest tests.test_web_bridge tests.test_desktop_layout -v`

Expected: all focused Python tests pass.

### Task 5: Complete React Application Shell and Feature Pages

**Files:**
- Create: `frontend/src/App.tsx`
- Create: `frontend/src/App.test.tsx`
- Create: `frontend/src/lib/i18n.ts`
- Create: `frontend/src/components/ui/button.tsx`
- Create: `frontend/src/components/ui/dialog.tsx`
- Create: `frontend/src/components/ui/input.tsx`
- Create: `frontend/src/components/ui/scroll-area.tsx`
- Create: `frontend/src/features/layout/app-shell.tsx`
- Create: `frontend/src/features/chat/chat-page.tsx`
- Create: `frontend/src/features/sources/source-panel.tsx`
- Create: `frontend/src/features/history/history-page.tsx`
- Create: `frontend/src/features/favorites/favorites-page.tsx`
- Create: `frontend/src/features/knowledge/knowledge-page.tsx`
- Create: `frontend/src/features/settings/settings-page.tsx`

**Interfaces:**
- Consumes: `DesktopBridgeClient` and the contracts from Task 2.
- Produces: wide three-region layout, medium source drawer, narrow navigation and source drawers.
- Produces: dark-default and complete light themes, Chinese and English labels, and blocking loader phase mapping.

- [ ] **Step 1: Write failing application tests**

Cover initial loader, bootstrap success/failure, navigation, question progress and completion, retry, source detail, history rename/delete confirmation, favorites, import/rebuild, settings sanitization, theme, language, and drawer breakpoints.

```tsx
it("moves from retrieval to generation and clears the loader on completion", async () => {
  const bridge = makeBridge();
  render(<App bridge={bridge} />);
  await userEvent.type(screen.getByRole("textbox"), "波端口怎么设置？");
  await userEvent.click(screen.getByRole("button", { name: "发送" }));
  bridge.emit({ type: "answer_progress", requestId: bridge.lastRequestId, phase: "retrieving" });
  expect(screen.getByText("正")).toBeInTheDocument();
  bridge.emit({ type: "answer_progress", requestId: bridge.lastRequestId, phase: "generating" });
  bridge.emit({ type: "answer_completed", requestId: bridge.lastRequestId, answer: sampleAnswer });
  expect(screen.queryByTestId("ai-loader-orbit")).not.toBeInTheDocument();
});
```

- [ ] **Step 2: Run and verify RED**

Run: `npm test -- --run src/App.test.tsx`

Expected: FAIL because the app shell and pages are missing.

- [ ] **Step 3: Implement design tokens and reusable primitives**

Define CSS variables for dark and light themes in `index.css`; implement accessible focus states, reduced-motion handling, scrollbar styling, responsive drawers, cards, buttons, inputs, dialogs, badges, and skeleton states. Use lucide-react icons only.

- [ ] **Step 4: Implement the application shell and pages**

Keep feature files focused. The app shell owns navigation and responsive panels; the chat page owns conversations and composer; source, history, favorites, knowledge, and settings pages own their respective typed bridge calls. Render Markdown and formulas safely without `dangerouslySetInnerHTML` for untrusted raw input.

- [ ] **Step 5: Verify GREEN and the full frontend suite**

Run: `npm test -- --run`

Expected: all frontend tests pass.

Run: `npm run typecheck && npm run build`

Expected: exit code 0 and production assets in `frontend/dist`.

### Task 6: PySide6 Web Window and Production Startup

**Files:**
- Create: `src/raggg/desktop/web_window.py`
- Create: `tests/test_web_window.py`
- Modify: `app/desktop_app.py`
- Modify: `setup_env.bat`
- Create: `scripts/build_frontend.ps1`
- Modify: `README.md`

**Interfaces:**
- Produces: `WebWorkbenchWindow(settings: Settings)` and `run_desktop_app() -> int`.
- Loads: `frontend/dist/index.html` through `QUrl.fromLocalFile`.
- Registers: bridge object name `backend` on a `QWebChannel` attached to the page.
- Preserves: `start.bat` as the user-facing launcher.

- [ ] **Step 1: Write failing window tests**

Verify 1280 by 820 default size, 960 by 640 minimum size, local frontend URL, registered bridge, application icon, and a readable missing-build fallback page.

- [ ] **Step 2: Run and verify RED**

Run: `$env:PYTHONPATH='src'; $env:QT_QPA_PLATFORM='offscreen'; .\.venv\Scripts\python.exe -m unittest tests.test_web_window -v`

Expected: FAIL because `WebWorkbenchWindow` is missing.

- [ ] **Step 3: Implement the web window and switch the app entry**

Configure local file access, disable remote content access in the QWebEngine page, register `DesktopBridge` as `backend`, load the production HTML, and keep the legacy Qt window import available only as a documented fallback.

- [ ] **Step 4: Add the local frontend build helper**

`scripts/build_frontend.ps1` must prefer existing Node/npm, otherwise download the current Windows x64 LTS ZIP from the official Node.js distribution metadata into `.tmp`, expand it into a versioned `.tmp` directory, run `npm install`, tests, typecheck, and build. It must not remove existing directories recursively. `setup_env.bat` calls this helper before building the knowledge index.

- [ ] **Step 5: Verify GREEN and startup wiring**

Run: `$env:PYTHONPATH='src'; $env:QT_QPA_PLATFORM='offscreen'; .\.venv\Scripts\python.exe -m unittest tests.test_web_window -v`

Expected: all window tests pass.

Run: `.\.venv\Scripts\python.exe -m py_compile app\desktop_app.py src\raggg\desktop\web_window.py src\raggg\desktop\web_bridge.py`

Expected: exit code 0.

### Task 7: Full Verification and Visual QA

**Files:**
- Verify: all files above.
- Modify if required by evidence: focused files only.

**Interfaces:**
- Consumes: completed React build and Python desktop integration.
- Produces: fresh evidence for tests, build, startup, and the three responsive sizes.

- [ ] **Step 1: Run all frontend checks**

Run from `frontend`: `npm test -- --run && npm run typecheck && npm run build`

Expected: zero test failures, type errors, or build errors.

- [ ] **Step 2: Run all Python checks**

Run: `$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest discover -s tests -v`

Expected: all Python tests pass.

Run: `.\.venv\Scripts\python.exe -m compileall -q app src scripts`

Expected: exit code 0.

- [ ] **Step 3: Run the desktop integration smoke test**

Launch `app\desktop_app.py` with the project virtual environment, confirm the process loads `frontend/dist/index.html`, wait for bootstrap completion, and close only the explicitly launched test process if required.

- [ ] **Step 4: Perform visual QA**

Inspect dark and light themes at 1280 by 820, 1024 by 720, and 960 by 640. Verify Chinese and English, empty state, long answer, formula, source drawer, settings, import loader, and error state. Record and fix any overlap, clipping, low contrast, or inaccessible action.

- [ ] **Step 5: Review the requirement checklist and working tree**

Confirm every success criterion in `docs/superpowers/specs/2026-07-13-react-gui-redesign-design.md`, run `git diff --check`, inspect `git status --short`, and ensure no secrets, generated Node runtime, `.tmp` content, or `node_modules` are staged.

- [ ] **Step 6: Commit the implementation**

Stage only the intended source, tests, documentation, lockfile, and production frontend assets. Commit with `feat: replace desktop GUI with React workbench` after all fresh verification commands pass.
