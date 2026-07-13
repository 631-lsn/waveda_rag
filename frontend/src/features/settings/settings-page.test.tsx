import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";

import { SettingsPage } from "./settings-page";
import type { BootstrapPayload } from "@/lib/contracts";

const bootstrap = {
  locale: "en",
  theme: "dark",
  personality: "normal",
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
  chunkCount: 10,
  indexStatus: "ready",
  watcherStatus: "active",
  conversations: [],
  favorites: [],
} as BootstrapPayload;

describe("personality settings", () => {
  it("saves the selected assistant personality", async () => {
    const user = userEvent.setup();
    const onSave = vi.fn();
    render(
      <SettingsPage
        locale="en"
        theme="dark"
        bootstrap={bootstrap}
        onSave={onSave}
      />,
    );

    await user.click(screen.getByRole("button", { name: "Personality" }));
    await user.click(screen.getByRole("button", { name: /Cat/ }));
    await user.click(screen.getByRole("button", { name: "Save settings" }));

    expect(onSave).toHaveBeenCalledWith(expect.objectContaining({ personality: "cat" }));
  });
});
