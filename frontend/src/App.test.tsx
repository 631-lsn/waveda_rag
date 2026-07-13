import { act, render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";

import App from "./App";
import type { DesktopBridgeClient } from "@/lib/bridge";
import type { BootstrapPayload, BridgeEvent } from "@/lib/contracts";

const bootstrap: BootstrapPayload = {
  locale: "zh",
  theme: "dark",
  personality: "cat",
  apiConfigured: true,
  providerId: "deepseek",
  providers: [
    {
      id: "deepseek",
      label: "DeepSeek",
      baseUrl: "https://api.deepseek.com",
      model: "deepseek-chat",
    },
    {
      id: "openai",
      label: "OpenAI",
      baseUrl: "https://api.openai.com/v1",
      model: "gpt-4o-mini",
    },
  ],
  model: "deepseek-chat",
  baseUrl: "https://api.deepseek.com",
  chunkCount: 4974,
  indexStatus: "ready",
  watcherStatus: "active",
  conversations: [],
  favorites: [],
};

function makeBridge() {
  let listener: ((event: BridgeEvent) => void) | undefined;
  const bootstrapMock = vi.fn<() => Promise<BootstrapPayload>>().mockResolvedValue(bootstrap);
  const askMock = vi.fn<
    (requestId: string, question: string, conversationId?: string) => Promise<{ accepted: boolean }>
  >().mockResolvedValue({ accepted: true });
  const selectProviderMock = vi.fn<(providerId: string) => Promise<BootstrapPayload>>()
    .mockImplementation(async (providerId) => ({
      ...bootstrap,
      providerId,
      model: providerId === "openai" ? "gpt-4o-mini" : "deepseek-chat",
      baseUrl: providerId === "openai" ? "https://api.openai.com/v1" : "https://api.deepseek.com",
    }));
  const bridge = {
    bootstrap: bootstrapMock,
    subscribe: vi.fn((next: (event: BridgeEvent) => void) => {
      listener = next;
      return () => undefined;
    }),
    ask: askMock,
    stopAnswer: vi.fn().mockResolvedValue({ stopped: true }),
    selectAndImportDocument: vi.fn().mockResolvedValue({ accepted: true }),
    getConversation: vi.fn(),
    renameHistory: vi.fn(),
    deleteHistory: vi.fn(),
    saveFavorite: vi.fn(),
    deleteFavorite: vi.fn(),
    saveSettings: vi.fn().mockResolvedValue(bootstrap),
    selectProvider: selectProviderMock,
    rebuildIndex: vi.fn().mockResolvedValue({ accepted: true }),
  };
  return {
    bridge: bridge as unknown as DesktopBridgeClient,
    bootstrapMock,
    askMock,
    selectProviderMock,
    emit(event: BridgeEvent) {
      act(() => listener?.(event));
    },
  };
}

describe("WavEDA React workbench", () => {
  it("shows the startup loader and then the complete navigation", async () => {
    let resolveBootstrap: (value: BootstrapPayload) => void = () => undefined;
    const setup = makeBridge();
    setup.bootstrapMock.mockImplementation(
      () => new Promise<BootstrapPayload>((resolve) => (resolveBootstrap = resolve)),
    );

    render(<App bridge={setup.bridge} />);
    expect(screen.getByTestId("ai-loader-orbit")).toBeInTheDocument();

    resolveBootstrap(bootstrap);
    expect(await screen.findByText("喵。本喵是 WavEDA 助手")).toBeInTheDocument();

    expect(await screen.findByRole("button", { name: "新建会话" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "历史记录" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "收藏" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "知识库" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "设置" })).toBeInTheDocument();
  });

  it("moves through answer phases and clears the loader on completion", async () => {
    const setup = makeBridge();
    const user = userEvent.setup();
    render(<App bridge={setup.bridge} />);
    await screen.findByRole("textbox", { name: "提问输入框" }, { timeout: 3000 });

    await user.type(screen.getByRole("textbox", { name: "提问输入框" }), "波端口怎么设置？");
    await user.click(screen.getByRole("button", { name: "发送" }));

    const requestId = setup.askMock.mock.calls[0][0];
    setup.emit({ type: "answer_progress", requestId, phase: "retrieving" });
    expect(screen.getByTestId("ai-loader-inline")).toBeInTheDocument();
    expect(screen.queryByTestId("ai-loader-overlay")).not.toBeInTheDocument();
    expect(screen.getByRole("main")).toBeInTheDocument();
    setup.emit({ type: "answer_progress", requestId, phase: "generating" });
    setup.emit({
      type: "answer_completed",
      requestId,
      answer: "请先选择 Domain 上的非金属面。",
      sources: [],
      warning: null,
      conversation: {
        id: "conversation-1",
        title: "波端口怎么设置？",
        createdAt: "2026-07-13T00:00:00Z",
        updatedAt: "2026-07-13T00:00:00Z",
        messages: [
          {
            id: "m1",
            role: "user",
            content: "波端口怎么设置？",
            createdAt: "2026-07-13T00:00:00Z",
          },
          {
            id: "m2",
            role: "assistant",
            content: "请先选择 Domain 上的非金属面。",
            createdAt: "2026-07-13T00:00:00Z",
          },
        ],
      },
    });

    await waitFor(() => expect(screen.queryByTestId("ai-loader-inline")).not.toBeInTheDocument());
    expect(screen.getByText("请先选择 Domain 上的非金属面。")).toBeInTheDocument();
  });

  it("renders a reconnect state instead of a blank page", async () => {
    const setup = makeBridge();
    setup.bootstrapMock.mockRejectedValue(new Error("bridge offline"));

    render(<App bridge={setup.bridge} />);

    expect(await screen.findByText("无法连接桌面服务")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "重新连接" })).toBeInTheDocument();
  });

  it("switches the active backend provider from the prompt input", async () => {
    const setup = makeBridge();
    const user = userEvent.setup();
    render(<App bridge={setup.bridge} />);

    await user.click(await screen.findByRole("button", { name: "询问 WavEDA 操作、仿真设置或错误排查…" }));
    await user.click(screen.getByRole("button", { name: "选择模型. 当前: DeepSeek" }));
    await user.click(screen.getByRole("button", { name: "OpenAI · gpt-4o-mini" }));

    await waitFor(() => expect(setup.selectProviderMock).toHaveBeenCalledWith("openai"));
    expect(await screen.findByRole("button", { name: "选择模型. 当前: OpenAI" })).toBeInTheDocument();
    expect(screen.getAllByText("gpt-4o-mini").length).toBeGreaterThan(0);
    expect(document.body.textContent).not.toContain("secret-value");
  });
});
