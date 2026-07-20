from pathlib import Path
import unittest

from raggg.desktop.favorites import FavoritesMixin, favorite_matches, favorite_score
from raggg.desktop.sessions import SessionPanel
from raggg.desktop.views import WorkbenchViewsMixin


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


if __name__ == "__main__":
    unittest.main()
