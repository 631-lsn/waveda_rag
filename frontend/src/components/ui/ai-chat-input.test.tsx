import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { useState } from "react";
import { describe, expect, it, vi } from "vitest";

import { PromptInput, type PromptInputProps } from "./ai-chat-input";

const models = [
  { id: "deepseek", label: "DeepSeek", model: "deepseek-chat" },
  { id: "openai", label: "OpenAI", model: "gpt-4o-mini" },
];

function Harness(props: Partial<PromptInputProps> = {}) {
  const [value, setValue] = useState(props.value ?? "");
  return (
    <PromptInput
      value={value}
      onChange={setValue}
      onSubmit={props.onSubmit ?? vi.fn()}
      busy={props.busy ?? false}
      onStop={props.onStop ?? vi.fn()}
      models={models}
      selectedModelId="deepseek"
      onModelChange={props.onModelChange ?? vi.fn()}
      {...props}
    />
  );
}

describe("PromptInput", () => {
  it("expands, accepts controlled text, and submits with Enter", async () => {
    const user = userEvent.setup();
    const onSubmit = vi.fn();
    render(<Harness onSubmit={onSubmit} />);

    await user.click(screen.getByRole("button", { name: "Open prompt input" }));
    const input = screen.getByRole("textbox", { name: "Prompt" });
    await user.type(input, "PML error{Enter}");

    expect(input).toHaveValue("PML error");
    expect(onSubmit).toHaveBeenCalledOnce();
  });

  it("uses Shift+Enter for a new line without submitting", async () => {
    const user = userEvent.setup();
    const onSubmit = vi.fn();
    render(<Harness onSubmit={onSubmit} />);

    await user.click(screen.getByRole("button", { name: "Open prompt input" }));
    const input = screen.getByRole("textbox", { name: "Prompt" });
    await user.type(input, "line one{Shift>}{Enter}{/Shift}line two");

    expect(input).toHaveValue("line one\nline two");
    expect(onSubmit).not.toHaveBeenCalled();
  });

  it("reports a selected backend provider", async () => {
    const user = userEvent.setup();
    const onModelChange = vi.fn();
    render(<Harness onModelChange={onModelChange} />);

    await user.click(screen.getByRole("button", { name: "Open prompt input" }));
    await user.click(screen.getByRole("button", { name: "Select model. Current: DeepSeek" }));
    await user.click(screen.getByRole("button", { name: "OpenAI · gpt-4o-mini" }));

    expect(onModelChange).toHaveBeenCalledWith("openai");
  });

  it("shows stop while busy and omits removed controls", async () => {
    const user = userEvent.setup();
    const onStop = vi.fn();
    render(<Harness value="running" busy onStop={onStop} />);

    await user.click(screen.getByRole("button", { name: "Stop generation" }));

    expect(onStop).toHaveBeenCalledOnce();
    expect(screen.queryByRole("button", { name: /voice/i })).not.toBeInTheDocument();
    expect(screen.queryByRole("button", { name: /attachment/i })).not.toBeInTheDocument();
    expect(screen.queryByRole("button", { name: /effort/i })).not.toBeInTheDocument();
  });
});
