# WavEDA React GUI Redesign Design

## Goal

Replace the entire existing PySide6 widget interface with a polished React desktop interface while preserving the current Python RAG engine, document ingestion, index watching, history, favorites, settings, sources, localization, and `start.bat` launch experience.

The new interface uses a professional research-workbench visual language: dark navy is the default theme, cyan-blue accents are restrained, information hierarchy is clear, and a complete light theme remains available.

## Scope

The redesign covers the full desktop application rather than only the chat screen:

- Main navigation and application shell.
- Conversation welcome state, message stream, composer, and generation controls.
- Source list and source detail view.
- Conversation history and favorites.
- Knowledge-base status and document ingestion.
- Model and API settings.
- Theme, language, data, and index settings.
- Loading, empty, success, warning, and error states.
- Chinese and English UI text.

The existing Python RAG implementation and knowledge-base content remain the source of truth. This project does not replace retrieval, generation, ingestion, persistence, or source-watching algorithms unless a small adapter is required to expose them to React.

## Chosen Architecture

Create a Vite React single-page application under `frontend/` and load its production build inside the existing PySide6 `QWebEngineView`. A typed `QWebChannel` bridge connects React to the current Python services.

This approach preserves the desktop window, Python runtime, `start.bat`, and existing backend behavior. It avoids the local-port lifecycle and cross-origin complexity of a FastAPI frontend server and avoids the packaging rewrite required by Electron or Tauri.

The frontend state layer uses focused React contexts and hooks. Redux is not required. Python remains responsible for persistent state; React owns only current presentation and interaction state.

## Frontend Stack and Structure

The frontend uses:

- React with TypeScript.
- Vite for development and production builds.
- Tailwind CSS for layout and design tokens.
- shadcn-compatible component structure and primitives.
- `lucide-react` for interface icons.
- Vitest and React Testing Library for frontend tests.
- `styled-jsx` build support so the supplied loader component can retain its `<style jsx>` structure.

The default frontend structure is:

```text
frontend/
├─ src/
│  ├─ components/
│  │  └─ ui/
│  │     └─ ai-loader.tsx
│  ├─ features/
│  ├─ lib/
│  ├─ App.tsx
│  └─ index.css
├─ components.json
├─ package.json
├─ tailwind.config.ts
└─ tsconfig.json
```

Within the frontend source root, `/components/ui` resolves to `frontend/src/components/ui` through the `@/components/ui` alias. This convention is mandatory because shadcn component generation, imports, and future upgrades rely on a predictable shared UI directory. Global Tailwind styles and theme tokens live in `frontend/src/index.css`.

No stock photography is needed for this application. The interface is product UI rather than a marketing page. All SVG-style interface symbols use `lucide-react`; no hand-authored SVG logos are introduced.

## Supplied AI Loader

Copy the supplied loader into `frontend/src/components/ui/ai-loader.tsx` with its public API intact:

```ts
interface LoaderProps {
  size?: number;
  text?: string;
}
```

The exported component remains named `Component`, with default `size = 180` and `text = "Generating"`. The build supports its `<style jsx>` block so the circular glow and per-letter animation are preserved.

Use the loader for blocking operations only:

- Application initialization: `正在载入` / `Loading`.
- Retrieval: `正在检索` / `Retrieving`.
- Answer generation: `正在生成` / `Generating`.
- Document ingestion and index rebuild: state-specific localized text.

The default diameter is 180 pixels and becomes 144 pixels at the narrow desktop breakpoint. Routine navigation does not show the full-screen loader. Every success and failure path must clear the loader.

## Application Shell and Navigation

The wide-screen application uses three regions:

1. A left navigation rail for product identity, new conversation, history, favorites, knowledge base, document ingestion, and settings. Its footer shows index state, current model, theme, and language controls.
2. A central work area containing the conversation header, welcome or message state, and a fixed composer.
3. A right source panel containing citations for the current answer, match metadata, summaries, and source detail navigation.

History and favorites open as full central-work-area pages rather than being compressed into the navigation rail. The knowledge-base page shows document count, chunk count, watcher status, index status, and recent imports. Settings use four sections: model and API, interface, language, and data and index.

The composer supports multiline input, document import, send, and stop-generation actions. The current Python backend may not support true model cancellation; if cancellation cannot interrupt the provider request safely, the stop action must end frontend waiting and ignore a late response without corrupting conversation state.

## Responsive Behavior

The default desktop window is approximately 1280 by 820 pixels and the supported minimum is 960 by 640 pixels.

- Wide layout: left navigation, central work area, and right source panel are visible.
- Medium layout: the source panel becomes a right-side drawer.
- Narrow supported layout: both side regions become drawers while chat and composer remain usable.

Visual verification covers 1280 by 820, 1024 by 720, and 960 by 640. Long answers, formulas, Chinese text, English text, and error messages must not obscure the composer or essential actions.

## Themes and Localization

Dark mode is the default. It uses navy-black surfaces, cyan-blue interactive accents, high-contrast text, and limited glow effects. Light mode provides equivalent hierarchy and contrast without reusing the existing pink-to-blue glass gradient.

Theme tokens are defined in CSS variables and consumed through Tailwind classes. Components do not hard-code independent color systems. The existing Python preference remains persistent and is synchronized with React through the bridge.

All user-facing text is available in Chinese and English. React owns frontend translation keys, while Python-originated status and error codes are translated by the frontend whenever practical. Raw provider error details may be logged locally but are not shown directly when they contain sensitive data.

## Bridge API and State Boundary

React calls a typed frontend adapter rather than using raw `QWebChannel` objects inside components. The adapter exposes the following conceptual operations:

- `bootstrap()` returns sanitized settings, index status, model status, history summaries, current theme, and current locale.
- `ask(question, conversationId)` starts an asynchronous answer request.
- `stopAnswer(requestId)` cancels or detaches the current frontend request safely.
- `selectAndImportDocument()` lets Python open the native file picker and starts ingestion.
- History operations load, rename, and delete one explicitly selected conversation.
- Favorite operations list, create, open, and delete one explicitly selected favorite.
- Settings operations load sanitized values and save explicit updates.
- Index operations expose status and allow an explicit rebuild.

The bridge emits typed events for request progress, answer completion, answer failure, ingestion progress, ingestion completion, index changes, and source-watcher changes.

API keys never return from `bootstrap()` as plaintext. The frontend receives only configured or unconfigured state and may submit a replacement value. Persistent writes stay in Python so a frontend refresh cannot lose history, favorites, or configuration.

## Question and Answer Flow

1. React calls `bootstrap()` and shows the startup loader.
2. The user submits a non-empty question.
3. React adds the user message and invokes `ask` with a request identifier.
4. Python emits `retrieving`; React shows the retrieval loader text.
5. Python emits `generating`; React changes the loader text without replacing the request.
6. Python returns the answer and sources; React adds the assistant message and populates the source panel.
7. React clears the loader and restores composer controls.
8. On failure, React preserves the user question, renders a retry action, and clears the loader.

Only one blocking request is active for a conversation at a time. Late events for a detached or superseded request are ignored using the request identifier.

## Document Ingestion Flow

1. React requests document selection.
2. Python opens the native single-file picker.
3. Existing validation and collision-safe ingestion logic accepts the supported document formats.
4. Python emits ingestion and rebuild progress events.
5. The current usable index remains available until a replacement index is built successfully.
6. React refreshes knowledge-base statistics and recent imports after success.
7. A failure leaves the current index loaded and provides a readable error plus a local-log entry point.

The application does not add a batch-delete control. Deletion is limited to one explicit history record, favorite, or user-selected file at a time and requires confirmation when it affects persisted data.

## Error Handling

- Initialization failure renders a full error state with a reconnect action rather than a blank page.
- Answer failure preserves the question and offers retry.
- Missing API configuration links directly to model and API settings.
- Unsupported or missing import files produce readable validation errors and never overwrite an existing file.
- Index rebuild failure retains the current usable index and reports the failed stage.
- React runtime failures are caught by an error boundary.
- Bridge completion, cancellation, and failure paths all clear blocking UI state.
- Sensitive API values and provider payloads are excluded from user-facing errors and frontend logs.

## Testing and Verification

Frontend unit tests cover:

- Loader default and custom properties, localized text, and letter rendering.
- Navigation and responsive panel behavior.
- Dark and light theme switching.
- Question submission, progress phases, completion, failure, and retry.
- Source list and detail navigation.
- History, favorites, knowledge-base status, settings, and import states.
- Error boundary and bridge-unavailable states.

Bridge contract tests use a fake channel to verify request shapes and event handling without invoking the real RAG model. Python tests verify that the bridge adapter calls the existing backend services and emits sanitized, typed results.

Release verification includes:

- TypeScript type checking.
- Frontend unit tests.
- Frontend production build.
- Python compilation checks.
- The complete existing Python test suite.
- A PySide6 integration smoke test that loads the real frontend build.
- A real `start.bat` launch without a separate frontend development server.
- Visual checks at all three supported window sizes in dark and light themes, with Chinese and English content.

## Success Criteria

- The full desktop GUI uses React, TypeScript, Tailwind CSS, and a shadcn-compatible structure.
- `frontend/src/components/ui/ai-loader.tsx` implements the supplied loader API and animation.
- All existing core application capabilities remain reachable and functional.
- `start.bat` remains the normal production entry point.
- The application never leaves a blank page or permanent blocking loader after a handled failure.
- Dark and light themes are complete and visually consistent.
- The supported window sizes contain no overlapping or inaccessible essential controls.
- Frontend tests, production build, Python tests, and desktop smoke verification pass before completion is claimed.

## Explicit Non-Goals

- Replacing the Python RAG engine.
- Running a permanent local HTTP frontend server in production.
- Migrating to Electron or Tauri.
- Adding marketing imagery or Unsplash assets that do not serve the desktop workflow.
- Adding batch deletion.
- Redesigning or repopulating the WavEDA knowledge base itself.
