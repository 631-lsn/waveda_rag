from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from raggg.loaders.markdown_loader import load_markdown_document


class MarkdownLoaderTests(unittest.TestCase):
    def test_frontmatter_priority_overrides_folder_default(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "05_reference" / "imported.md"
            path.parent.mkdir()
            path.write_text(
                "---\ncontent_kind: imported\npriority: 5\n---\n\n# Imported\n\nText",
                encoding="utf-8",
            )

            document = load_markdown_document(path, root)

            self.assertEqual(document.metadata["priority"], 5)
            self.assertEqual(document.metadata["content_type"], "imported")

    def test_invalid_priority_uses_folder_default(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "01_team_tutorials" / "guide.md"
            path.parent.mkdir()
            path.write_text("---\npriority: 99\n---\n\n# Guide\n\nText", encoding="utf-8")

            document = load_markdown_document(path, root)

            self.assertEqual(document.metadata["priority"], 5)


if __name__ == "__main__":
    unittest.main()
