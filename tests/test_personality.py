from __future__ import annotations

import unittest

from raggg.generation.personality import (
    PERSONALITIES,
    get_personality,
    get_personality_prompt,
    set_personality,
)
from raggg.generation.prompt_builder import build_prompt
from raggg.i18n import set_language


class PersonalityTests(unittest.TestCase):
    def tearDown(self) -> None:
        set_personality("normal", persist=False)
        set_language("zh")

    def test_all_six_personalities_have_bilingual_prompts(self) -> None:
        self.assertEqual(
            set(PERSONALITIES),
            {"normal", "mature", "sweet", "dog", "cat", "workhorse"},
        )
        for name in PERSONALITIES:
            set_personality(name, persist=False)
            self.assertTrue(get_personality_prompt("zh"))
            self.assertTrue(get_personality_prompt("en"))
            self.assertEqual(get_personality(), name)

    def test_selected_personality_is_injected_into_generated_prompt(self) -> None:
        set_personality("cat", persist=False)

        prompt = build_prompt("How do I configure a port?", [])

        self.assertIn("布偶猫助手", prompt)

    def test_generated_prompt_uses_current_interface_language(self) -> None:
        set_personality("cat", persist=False)
        set_language("en")

        prompt = build_prompt("How do I configure a port?", [])

        self.assertIn("Ragdoll cat assistant", prompt)


if __name__ == "__main__":
    unittest.main()
