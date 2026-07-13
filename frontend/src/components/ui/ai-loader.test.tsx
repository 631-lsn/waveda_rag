import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { Component } from "./ai-loader";

describe("AI loader", () => {
  it("uses the application theme instead of an inverted hard-coded gradient", () => {
    render(<Component />);

    const overlay = screen.getByTestId("ai-loader-overlay");
    expect(overlay).toHaveClass("bg-[var(--bg)]", "text-[var(--text)]");
    expect(overlay.className).not.toContain("from-[#1a3379]");
    expect(overlay.className).not.toContain("dark:from-gray-100");
  });

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
