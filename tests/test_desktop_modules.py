from pathlib import Path
import unittest

from raggg.desktop.favorites import FavoritesMixin, favorite_matches, favorite_score
from raggg.desktop.sessions import SessionPanel
from raggg.desktop.views import WorkbenchViewsMixin
from raggg.desktop.main_window import (
    ImageIndex,
    markdown_to_html,
    render_inline_markdown,
    web_wrapper,
)


class DesktopModuleTests(unittest.TestCase):
    def test_main_window_stays_below_800_lines(self) -> None:
        path = Path("src/raggg/desktop/main_window.py")

        self.assertLess(len(path.read_text(encoding="utf-8").splitlines()), 800)

    def test_extracted_types_are_importable(self) -> None:
        self.assertTrue(FavoritesMixin)
        self.assertTrue(SessionPanel)
        self.assertTrue(WorkbenchViewsMixin)
        self.assertTrue(favorite_matches({"question": "port setup"}, "port"))
        self.assertGreater(
            favorite_score({"question": "port port"}, "port"),
            0,
        )
        self.assertTrue(ImageIndex)
        self.assertIn("<p", markdown_to_html("answer"))
        self.assertEqual(render_inline_markdown("plain"), "plain")
        self.assertIn("<html", web_wrapper("body"))


if __name__ == "__main__":
    unittest.main()
