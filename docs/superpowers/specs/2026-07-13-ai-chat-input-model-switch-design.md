# AI Chat Input and Model Switching Design

## Goal

Replace the existing chat composer with the supplied animated React prompt-input concept, reduced to the features required by the desktop RAG application, and make its model selector switch the Python backend's active LLM provider.

## Scope

The new prompt input keeps:

- compact-to-expanded spring animation;
- controlled text input and automatic height growth;
- Enter to send and Shift+Enter for a new line;
- model-provider selection;
- send and busy/stop states;
- light and dark theme compatibility;
- responsive behavior inside the existing chat workspace.

The new prompt input removes:

- microphone access and speech recognition;
- simulated voice input;
- effort/reasoning-strength selection;
- image selection, attachment thumbnails, gallery preview, and upload metadata;
- external model-logo URLs.

No image assets or Unsplash images are required.

## Existing Project Structure

The React application already supports TypeScript, Tailwind CSS 4, and a shadcn-compatible structure.

- shadcn configuration: `frontend/components.json`
- UI components: `frontend/src/components/ui`
- global styles: `frontend/src/index.css`
- utility alias: `@/lib/utils`
- UI alias: `@/components/ui`

Because the React application is rooted under `frontend`, `frontend/src/components/ui` is the effective `/components/ui` directory referenced by the component instructions. Creating a second repository-root `components/ui` directory would bypass the configured `@` alias and split the component library.

## Component Architecture

Create `frontend/src/components/ui/ai-chat-input.tsx` with a focused public API:

```ts
export interface ModelOption {
  id: string;
  label: string;
  model: string;
}

export interface PromptInputProps {
  value: string;
  onChange(value: string): void;
  onSubmit(): void;
  busy: boolean;
  onStop(): void;
  placeholder?: string;
  models: ModelOption[];
  selectedModelId: string;
  onModelChange(modelId: string): void;
  modelSwitching?: boolean;
  className?: string;
}
```

The component remains controlled by `App`, so changing pages, receiving bridge events, or completing a request cannot leave an isolated copy of the prompt text inside the component.

Internal subcomponents handle morphing labels and the provider menu. Icons come from `lucide-react`; no inline SVG icon components or external logo URLs are introduced.

`tw-animate-css` is added because the supplied transition classes use its animation utilities. Existing theme tokens are extended with valid shadcn semantic aliases. The malformed `var(----color-...)` declarations from the supplied snippet are not copied.

## Chat Integration

`frontend/src/features/chat/chat-page.tsx` replaces its current composer card with `PromptInput`.

- The existing `question`, `onQuestionChange`, `onAsk`, `busy`, and `onStop` flow remains authoritative.
- While an answer is running, the action button invokes `onStop`.
- Empty text cannot be submitted.
- The current provider and available providers are supplied from `App`.
- The existing document-import entry point remains elsewhere in the workbench; it is not represented as an image attachment button in the prompt input.

## Provider Catalog

The selector uses the original desktop application's provider presets rather than the fictional model names in the supplied demo:

| Provider | Base URL | Model |
| --- | --- | --- |
| DeepSeek | `https://api.deepseek.com` | `deepseek-chat` |
| Kimi (Moonshot) | `https://api.moonshot.cn/v1` | `moonshot-v1-8k` |
| 通义千问 | `https://dashscope.aliyuncs.com/compatible-mode/v1` | `qwen-plus` |
| 阿里云百炼 | `https://dashscope.aliyuncs.com/compatible-mode/v1` | `qwen-plus` |
| OpenAI | `https://api.openai.com/v1` | `gpt-4o-mini` |

The provider catalog is defined once in Python and used by both the retained legacy settings dialog and the web bridge. Bootstrap data exposes sanitized provider metadata to React; API keys are never included.

## Backend Switching Flow

Add a bridge operation conceptually equivalent to:

```ts
selectProvider(providerId: string): Promise<BootstrapPayload>
```

The flow is:

1. The user selects a provider from `PromptInput`.
2. React disables repeated selection and calls the desktop bridge.
3. Python validates the provider ID against the fixed catalog.
4. Python updates `RAG_LLM_PROVIDER`, `RAG_LLM_BASE_URL`, and `RAG_LLM_MODEL` in `config/.env`. The non-secret provider ID is required because the 通义千问 and 阿里云百炼 presets share the same URL and model.
5. Python preserves the current `RAG_LLM_API_KEY` exactly as stored.
6. The web bridge reloads runtime settings and rebuilds the RAG pipeline so the next question uses the selected provider.
7. The bridge returns a sanitized bootstrap payload, and React updates the selected provider and displayed model.

The selector changes the active provider immediately and persists the choice across restarts. It does not attempt to maintain a separate key per provider.

## Error Handling

- Unknown provider IDs are rejected without modifying `config/.env`.
- A failed settings write leaves the current runtime pipeline unchanged and returns an actionable error.
- While switching, the selector is disabled to prevent concurrent writes.
- If the retained API key is invalid for the new provider, the existing RAG fallback behavior remains active: local retrieval still answers, and the UI reports that the user should replace the API key in Settings.
- Model switching never exposes the stored API key to React, logs, tests, or error messages.

## Responsive and Accessibility Behavior

- The prompt input fills the available composer width, up to the existing chat content width rather than the demo's 480-pixel limit.
- Its provider menu opens above the composer so it remains visible near the bottom edge.
- At narrow widths, labels truncate before the send button is compressed.
- Buttons have localized accessible labels.
- Escape closes the provider menu; Enter sends; Shift+Enter inserts a line break.
- `prefers-reduced-motion` continues to use the global reduced-motion rule.

## Testing

Frontend component tests cover:

- compact input expansion;
- controlled text changes;
- Enter submission and Shift+Enter behavior;
- provider selection callback;
- busy state invoking stop instead of submit;
- absence of microphone, effort, and attachment controls.

Frontend integration tests verify that selecting a provider calls the bridge, refreshes the displayed model, and preserves the existing answer lifecycle.

Python tests cover:

- the exact provider catalog;
- sanitized bootstrap provider metadata;
- provider selection updating only Base URL and model;
- API-key preservation;
- invalid provider rejection without file changes;
- runtime pipeline refresh after a valid selection.

Final verification includes frontend tests, Python tests, TypeScript checking, Python compilation, and a production Vite build.

## Non-Goals

- multimodal/image questions;
- file upload through the prompt input;
- voice transcription;
- reasoning-effort controls;
- per-provider API-key storage;
- provider discovery from remote APIs;
- changing the existing RAG retrieval algorithm.
