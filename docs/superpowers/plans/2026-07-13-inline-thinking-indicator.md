# Inline Thinking Indicator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the full-screen answer-generation overlay with a compact status indicator above the chat composer while preserving the startup overlay.

**Architecture:** Extend the existing loader with an explicit `overlay` or `inline` presentation variant. Keep `busyText` in `App` as the state source, pass it to `ChatPage`, and render the inline variant beside the composer instead of at the application root.

**Tech Stack:** React, TypeScript, Tailwind CSS, Vitest, Testing Library

## Global Constraints

- Startup loading remains a full-screen overlay.
- Answer progress never blocks the navigation, source panel, message history, or composer.
- No new runtime dependency is added.
- `data/conversations.json` remains untouched.

---

### Task 1: Add an inline loader presentation

**Files:**
- Modify: `frontend/src/components/ui/ai-loader.tsx`
- Test: `frontend/src/components/ui/ai-loader.test.tsx`

**Interfaces:**
- Consumes: `LoaderProps.size?: number`, `LoaderProps.text?: string`
- Produces: `LoaderProps.variant?: "overlay" | "inline"`, defaulting to `"overlay"`

- [ ] **Step 1: Write the failing test**

Add a test that renders `<Component variant="inline" text="正在生成" />`, expects `data-testid="ai-loader-inline"`, `role="status"`, and verifies its class does not contain `fixed` or `inset-0`.

- [ ] **Step 2: Run the focused test and verify RED**

Run `npm test -- --run src/components/ui/ai-loader.test.tsx`. Expected: TypeScript or assertion failure because `variant` and `ai-loader-inline` do not exist.

- [ ] **Step 3: Implement the minimal inline variant**

Add `variant` to `LoaderProps`. For `inline`, render a themed rounded status row with a compact animated orbit and the complete status text; add `role="status"` and `aria-live="polite"`. Keep the existing overlay branch unchanged for startup.

- [ ] **Step 4: Run the focused test and verify GREEN**

Run `npm test -- --run src/components/ui/ai-loader.test.tsx`. Expected: all loader tests pass.

### Task 2: Move answer progress into the chat composer

**Files:**
- Modify: `frontend/src/App.tsx`
- Modify: `frontend/src/features/chat/chat-page.tsx`
- Test: `frontend/src/App.test.tsx`

**Interfaces:**
- Consumes: `App.busyText: string`
- Produces: `ChatPageProps.busyText: string`; `busy` remains derived with `Boolean(busyText)` for the prompt stop control

- [ ] **Step 1: Write the failing application test**

During `answer_progress`, assert that `ai-loader-inline` is visible, `ai-loader-overlay` is absent, and the navigation button remains present. Keep the existing completion assertion that the loader disappears.

- [ ] **Step 2: Run the application test and verify RED**

Run `npm test -- --run src/App.test.tsx`. Expected: failure because answer progress still renders the overlay and no inline indicator exists.

- [ ] **Step 3: Implement the chat integration**

Pass `busyText={busyText}` to `ChatPage`. Add `busyText: string` to its props and render `<AiLoader variant="inline" size={48} text={props.busyText} />` above `PromptInput` when non-empty. Remove `{busyText && <AiLoader ... />}` from the root of `App`.

- [ ] **Step 4: Run focused and full verification**

Run `npm test -- --run src/App.test.tsx`, then `npm test -- --run`, `npm run typecheck`, and `npm run build`. Expected: 0 failures and successful production output.

- [ ] **Step 5: Verify the desktop interface and commit**

Launch an isolated desktop instance, confirm the main interface remains visible during generation, then commit source, tests, and generated `frontend/dist` assets with message `fix: embed thinking status in chat`.
