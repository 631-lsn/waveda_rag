import { describe, expect, it } from "vitest";

import { PERSONALITY_OPTIONS, getWelcomeCopy } from "./personality";

describe("personality welcome copy", () => {
  it("provides distinct bilingual welcome copy for all six personalities", () => {
    expect(PERSONALITY_OPTIONS.map((item) => item.id)).toEqual([
      "normal",
      "mature",
      "sweet",
      "dog",
      "cat",
      "workhorse",
    ]);

    for (const option of PERSONALITY_OPTIONS) {
      const zh = getWelcomeCopy("zh", option.id);
      const en = getWelcomeCopy("en", option.id);
      expect(zh.title).toBeTruthy();
      expect(zh.intro).toBeTruthy();
      expect(zh.detail).toBeTruthy();
      expect(en.title).toBeTruthy();
      expect(en.intro).toBeTruthy();
      expect(en.detail).toBeTruthy();
    }

    expect(getWelcomeCopy("en", "cat").title).not.toBe(
      getWelcomeCopy("en", "normal").title,
    );
  });
});
