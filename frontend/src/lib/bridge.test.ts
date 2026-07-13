import { describe, expect, it, vi } from "vitest";

import { DesktopBridgeClient, type QtBackend } from "./bridge";
import type { BridgeEvent } from "./contracts";

class FakeSignal {
  private listeners: Array<(payload: string) => void> = [];

  connect(listener: (payload: string) => void) {
    this.listeners.push(listener);
  }

  emit(payload: unknown) {
    const encoded = typeof payload === "string" ? payload : JSON.stringify(payload);
    this.listeners.forEach((listener) => listener(encoded));
  }
}

function makeBackend() {
  const event_json = new FakeSignal();
  const selectProvider = vi.fn((_payload: string, done: (result: string) => void) =>
    done(
      JSON.stringify({
        locale: "zh",
        theme: "dark",
        apiConfigured: true,
        providerId: "openai",
        providers: [],
        model: "gpt-4o-mini",
        baseUrl: "https://api.openai.com/v1",
        chunkCount: 4974,
        indexStatus: "ready",
        watcherStatus: "active",
        conversations: [],
        favorites: [],
      }),
    ),
  );
  const backend: QtBackend = {
    event_json,
    select_provider: selectProvider,
    bootstrap: (_payload, done) =>
      done(
        JSON.stringify({
          locale: "zh",
          theme: "dark",
          apiConfigured: true,
          providerId: "deepseek",
          providers: [
            {
              id: "deepseek",
              label: "DeepSeek",
              baseUrl: "https://api.deepseek.com",
              model: "deepseek-chat",
            },
          ],
          model: "deepseek-chat",
          baseUrl: "https://api.deepseek.com",
          chunkCount: 4974,
          indexStatus: "ready",
          watcherStatus: "active",
          conversations: [],
          favorites: [],
        }),
      ),
  };
  return { backend, event_json, selectProvider };
}

describe("DesktopBridgeClient", () => {
  it("parses sanitized bootstrap data", async () => {
    const { backend } = makeBackend();
    const client = new DesktopBridgeClient(backend);

    const result = await client.bootstrap();

    expect(result.theme).toBe("dark");
    expect(result.chunkCount).toBe(4974);
    expect(JSON.stringify(result)).not.toContain("apiKey");
  });

  it("forwards typed backend events", () => {
    const { backend, event_json } = makeBackend();
    const client = new DesktopBridgeClient(backend);
    const seen: BridgeEvent[] = [];
    client.subscribe((event) => seen.push(event));

    event_json.emit({
      type: "answer_progress",
      requestId: "request-1",
      phase: "retrieving",
    });

    expect(seen[0]).toEqual({
      type: "answer_progress",
      requestId: "request-1",
      phase: "retrieving",
    });
  });

  it("turns malformed backend events into a safe bridge error", () => {
    const { backend, event_json } = makeBackend();
    const client = new DesktopBridgeClient(backend);
    const seen: BridgeEvent[] = [];
    client.subscribe((event) => seen.push(event));

    event_json.emit("not-json");

    expect(seen).toEqual([
      {
        type: "bridge_error",
        message: "Received an invalid desktop event.",
      },
    ]);
  });

  it("forwards provider selection and returns refreshed bootstrap data", async () => {
    const { backend, selectProvider } = makeBackend();
    const client = new DesktopBridgeClient(backend);

    const result = await client.selectProvider("openai");

    expect(selectProvider).toHaveBeenCalledWith(
      JSON.stringify({ providerId: "openai" }),
      expect.any(Function),
    );
    expect(result.providerId).toBe("openai");
    expect(result.model).toBe("gpt-4o-mini");
  });
});
