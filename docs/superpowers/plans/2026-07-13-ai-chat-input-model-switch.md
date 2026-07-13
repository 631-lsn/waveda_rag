# AI Chat Input and Model Switching Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the existing composer with an animated text-and-model prompt input whose provider selection immediately changes the Python RAG backend while preserving the single current API key.

**Architecture:** A canonical Python provider catalog supplies sanitized provider metadata to bootstrap data. `DesktopStore` persists provider changes, `DesktopBridge` reloads the runtime pipeline, and the typed React bridge updates `App` state. A controlled shadcn-style `PromptInput` owns only presentation state and delegates text, submission, stop, and provider changes upward.

**Tech Stack:** Python 3.14, PySide6/QWebChannel, React 19, TypeScript 5.8, Tailwind CSS 4, shadcn-compatible components, lucide-react, tw-animate-css, Vitest, Testing Library, unittest.

## Global Constraints

- Keep exactly one current API key; provider switching must not alter `RAG_LLM_API_KEY`.
- Persist `RAG_LLM_PROVIDER` because the `qwen` and `bailian` presets share the same Base URL and model.
- Remove voice input, effort selection, image attachments, and external logo assets.
- Use the provider presets from the original desktop GUI.
- Use `lucide-react` for component icons.
- Preserve `data/conversations.json`; never add it to a commit.
- Do not use recursive or batch deletion commands.

---

### Task 1: Canonical provider catalog and persistent provider selection

**Files:**
- Create: `src/raggg/desktop/providers.py`
- Modify: `src/raggg/desktop/main_window.py`
- Modify: `src/raggg/desktop/store.py`
- Test: `tests/test_desktop_store.py`

**Interfaces:**
- Produces: `LLMProvider`, `LLM_PROVIDERS`, `provider_payloads()`, and `get_provider(provider_id)`.
- Produces: `DesktopStore.select_provider(provider_id: str) -> dict[str, Any]`.
- Bootstrap adds `providers` and `providerId` without exposing API keys.

- [ ] **Step 1: Write failing provider-store tests**

Add tests asserting the five provider IDs and models, sanitized bootstrap metadata, preservation of `RAG_LLM_API_KEY`, persistence of provider ID/Base URL/model, and byte-for-byte unchanged `.env` content after an invalid ID.

```python
def test_select_provider_preserves_api_key_and_updates_model(self) -> None:
    self.env_path.write_text(
        "RAG_LLM_API_KEY=secret-value\nRAG_LLM_MODEL=deepseek-chat\n",
        encoding="utf-8",
    )
    payload = DesktopStore(self.settings).select_provider("openai")
    saved = self.env_path.read_text(encoding="utf-8")
    self.assertIn("RAG_LLM_API_KEY=secret-value", saved)
    self.assertIn("RAG_LLM_PROVIDER=openai", saved)
    self.assertIn("RAG_LLM_BASE_URL=https://api.openai.com/v1", saved)
    self.assertIn("RAG_LLM_MODEL=gpt-4o-mini", saved)
    self.assertEqual(payload["providerId"], "openai")

def test_invalid_provider_does_not_change_env(self) -> None:
    original = "RAG_LLM_API_KEY=secret-value\n"
    self.env_path.write_text(original, encoding="utf-8")
    with self.assertRaisesRegex(ValueError, "Unknown provider"):
        DesktopStore(self.settings).select_provider("missing")
    self.assertEqual(self.env_path.read_text(encoding="utf-8"), original)
```

- [ ] **Step 2: Run the focused tests and verify RED**

Run: `$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest tests.test_desktop_store -v`

Expected: failures because the provider catalog, bootstrap fields, and `select_provider` do not exist.

- [ ] **Step 3: Implement the provider catalog and store operation**

Define immutable records with IDs `deepseek`, `kimi`, `qwen`, `bailian`, and `openai`. `provider_payloads()` returns only `id`, `label`, `baseUrl`, and `model`. `select_provider` validates before reading/writing, then delegates to the existing settings writer with `providerId`, `baseUrl`, and `model`; it never supplies `apiKey`.

Update the legacy `SettingsDialog` to import the canonical catalog instead of maintaining its own tuple list.

- [ ] **Step 4: Run the focused tests and verify GREEN**

Run: `$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest tests.test_desktop_store -v`

Expected: all desktop-store tests pass.

- [ ] **Step 5: Commit Task 1**

```powershell
git add src/raggg/desktop/providers.py src/raggg/desktop/main_window.py src/raggg/desktop/store.py tests/test_desktop_store.py
git commit -m "feat: add persistent LLM provider selection"
```

---

### Task 2: Expose provider switching through the typed desktop bridge

**Files:**
- Modify: `src/raggg/desktop/web_bridge.py`
- Modify: `frontend/src/lib/contracts.ts`
- Modify: `frontend/src/lib/bridge.ts`
- Modify: `frontend/src/lib/bridge.test.ts`
- Test: `tests/test_web_bridge.py`

**Interfaces:**
- Python slot: `DesktopBridge.select_provider(payload: str) -> str` accepting `{ "providerId": string }`.
- TypeScript type: `ModelProvider` with `id`, `label`, `baseUrl`, and `model`.
- Client method: `selectProvider(providerId: string): Promise<BootstrapPayload>`.

- [ ] **Step 1: Write failing Python bridge tests**

Test that a valid provider calls the store, refreshes runtime settings and pipeline, returns the new sanitized bootstrap payload, and that an invalid provider returns `{error}` without replacing the current pipeline.

```python
payload = json.loads(bridge.select_provider('{"providerId":"openai"}'))
self.assertEqual(payload["providerId"], "openai")
self.assertEqual(payload["model"], "gpt-4o-mini")
self.assertNotIn("apiKey", payload)
```

- [ ] **Step 2: Run the Python bridge test and verify RED**

Run: `$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest tests.test_web_bridge -v`

Expected: failure because `select_provider` is not exposed.

- [ ] **Step 3: Implement the Python bridge slot**

Decode and validate `providerId`, call `store.select_provider`, refresh settings from the returned `baseUrl` and `model`, replace the pipeline only after the settings operation succeeds, and encode errors using the bridge's existing error contract.

- [ ] **Step 4: Write failing TypeScript bridge tests**

Add a QWebChannel method mock and assert:

```ts
await client.selectProvider("openai");
expect(selectProviderMethod).toHaveBeenCalledWith(
  JSON.stringify({ providerId: "openai" }),
  expect.any(Function),
);
```

Extend `BootstrapPayload` with `providers: ModelProvider[]` and `providerId: string`.

- [ ] **Step 5: Run the frontend bridge test and verify RED**

Run: `npm test -- --run src/lib/bridge.test.ts`

Expected: TypeScript/test failure because `selectProvider` is missing.

- [ ] **Step 6: Implement the typed client method and verify both suites GREEN**

Run:

```powershell
$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest tests.test_web_bridge -v
Set-Location frontend
npm test -- --run src/lib/bridge.test.ts
```

Expected: both focused suites pass.

- [ ] **Step 7: Commit Task 2**

```powershell
git add src/raggg/desktop/web_bridge.py tests/test_web_bridge.py frontend/src/lib/contracts.ts frontend/src/lib/bridge.ts frontend/src/lib/bridge.test.ts
git commit -m "feat: expose LLM provider switching to React"
```

---

### Task 3: Build the reduced animated PromptInput component

**Files:**
- Create: `frontend/src/components/ui/ai-chat-input.tsx`
- Create: `frontend/src/components/ui/ai-chat-input.test.tsx`
- Modify: `frontend/package.json`
- Modify: `frontend/package-lock.json`
- Modify: `frontend/src/index.css`

**Interfaces:**
- Consumes: controlled prompt value, `ModelOption[]` (`id`, `label`, `model`), selected provider ID, submit/stop/model-change callbacks.
- Produces: `PromptInput`, `PromptInputProps`, and `ModelOption` exactly as defined in the approved design.

- [ ] **Step 1: Install the required animation dependency**

Run: `npm install tw-animate-css`

Expected: `package.json` and lockfile include `tw-animate-css`.

- [ ] **Step 2: Write failing component behavior tests**

Cover expansion, controlled text change, Enter submit, Shift+Enter no submit, provider selection, busy stop behavior, and absence of attachment/voice/effort controls.

```tsx
render(<PromptInput {...baseProps} />);
await user.click(screen.getByRole("button", { name: /open prompt input/i }));
await user.type(screen.getByRole("textbox", { name: /prompt/i }), "PML error{Enter}");
expect(baseProps.onSubmit).toHaveBeenCalledOnce();
expect(screen.queryByRole("button", { name: /voice|attachment|effort/i })).not.toBeInTheDocument();
```

- [ ] **Step 3: Run the component test and verify RED**

Run: `npm test -- --run src/components/ui/ai-chat-input.test.tsx`

Expected: failure because the component module does not exist.

- [ ] **Step 4: Implement the minimal component**

Adapt the supplied spring-resize and morphing-label behavior. Use `Bot`, `ChevronUp`, `Send`, `Square`, and `X` from `lucide-react`. Keep the provider menu above the composer, disable switching during `modelSwitching`, and use the existing `cn` helper.

Do not include `MediaStream`, `AudioContext`, speech recognition, `File`, object URLs, attachment state, effort state, inline SVG icons, or external image URLs.

- [ ] **Step 5: Add valid Tailwind/shadcn theme aliases**

Import `tw-animate-css` after Tailwind and map `background`, `foreground`, `card`, `muted`, `accent`, `border`, `input`, `ring`, `primary`, and matching foreground colors to the existing application variables. Do not add any `var(----...)` declarations.

- [ ] **Step 6: Run component tests and typecheck GREEN**

Run:

```powershell
npm test -- --run src/components/ui/ai-chat-input.test.tsx
npm run typecheck
```

Expected: component suite and TypeScript check pass.

- [ ] **Step 7: Commit Task 3**

```powershell
git add frontend/package.json frontend/package-lock.json frontend/src/index.css frontend/src/components/ui/ai-chat-input.tsx frontend/src/components/ui/ai-chat-input.test.tsx
git commit -m "feat: add animated model-aware prompt input"
```

---

### Task 4: Integrate provider switching into the chat workbench

**Files:**
- Modify: `frontend/src/features/chat/chat-page.tsx`
- Modify: `frontend/src/App.tsx`
- Modify: `frontend/src/App.test.tsx`
- Modify: `frontend/src/lib/i18n.ts`

**Interfaces:**
- `ChatPage` receives `providers`, `providerId`, `modelSwitching`, and `onModelChange`.
- `App.changeProvider(providerId)` calls `bridge.selectProvider`, updates bootstrap state, and reports errors through the existing notice toast.

- [ ] **Step 1: Write failing application integration tests**

Extend the bridge fixture with `selectProvider`. Add bootstrap provider metadata. Select OpenAI from the composer and assert the bridge receives `openai`, the displayed model becomes `gpt-4o-mini`, and the API key never appears in rendered output.

Also retain the existing answer lifecycle test to prove send/stop behavior remains connected.

- [ ] **Step 2: Run the App test and verify RED**

Run: `npm test -- --run src/App.test.tsx`

Expected: failure because the chat page still renders the old composer and `App` has no provider-switch handler.

- [ ] **Step 3: Integrate PromptInput and model switching**

Replace `.composer-card` with `PromptInput`, pass localized labels, keep the controlled `question` state, and retain the existing `ask` and `stop` functions. Track `modelSwitching` in `App`; on success replace bootstrap with the returned payload, and on failure restore the previous selection and show the existing notice toast.

Remove now-unused `Paperclip`, `Send`, `Square`, keyboard-handler, and composer imports. Keep document import available on the Knowledge page.

- [ ] **Step 4: Run frontend tests and verify GREEN**

Run: `npm test -- --run`

Expected: all frontend tests pass.

- [ ] **Step 5: Commit Task 4**

```powershell
git add frontend/src/features/chat/chat-page.tsx frontend/src/App.tsx frontend/src/App.test.tsx frontend/src/lib/i18n.ts
git commit -m "feat: connect prompt model selector to desktop backend"
```

---

### Task 5: Full regression and production verification

**Files:**
- Modify: `README.md`
- Regenerate: `frontend/dist/**`

**Interfaces:**
- Produces a committed desktop-loadable production bundle.

- [ ] **Step 1: Run all automated verification**

Run:

```powershell
$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m unittest discover -s tests -v
$env:PYTHONPATH='src'; .\.venv\Scripts\python.exe -m compileall -q app src scripts
Set-Location frontend
npm test -- --run
npm run typecheck
npm run build
```

Expected: all commands exit zero with no failed tests.

- [ ] **Step 2: Verify forbidden and removed features are absent**

Run:

```powershell
rg -n "MediaStream|AudioContext|SpeechRecognition|webkitSpeechRecognition|type=\"file\"|Max Effort|cloudinary|<svg" frontend/src/components/ui/ai-chat-input.tsx
rg -n "var\(----" frontend/src/index.css
```

Expected: both searches return no matches.

- [ ] **Step 3: Perform desktop smoke verification**

Launch through `start.bat`, verify the new composer expands, text sends, the five original providers appear, selecting a provider updates the displayed model, and switching preserves the current Key indicator without exposing the key.

- [ ] **Step 4: Document the model selector and commit the generated bundle**

Add a README note listing the five provider presets and explaining that the prompt selector changes Base URL/model immediately while retaining the single current API key, which may need replacement in Settings after switching providers.

```powershell
git add frontend/dist README.md
git commit -m "build: ship model-aware chat input"
```

- [ ] **Step 5: Confirm clean scoped status**

Run: `git status --short --branch`

Expected: branch changes are committed; `data/conversations.json` may remain untracked and must not be added.
