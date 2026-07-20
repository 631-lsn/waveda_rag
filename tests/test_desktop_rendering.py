from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from raggg.desktop.image_index import ImageIndex
from raggg.desktop.rendering import markdown_to_html


class DesktopRenderingTests(unittest.TestCase):
    def test_adjacent_citations_render_as_clickable_superscripts(self) -> None:
        rendered = markdown_to_html("结论。[1][2]")

        self.assertIn("RAGGG_CITATION:1", rendered)
        self.assertIn("RAGGG_CITATION:2", rendered)
        self.assertEqual(rendered.count("<sup"), 2)

    def test_image_index_maps_relative_path_and_filename(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            image = (
                root
                / "wavEDA_docs"
                / "helpHtml"
                / "helpHtml"
                / "guide"
                / "images"
                / "port.png"
            )
            image.parent.mkdir(parents=True)
            image.write_bytes(b"png")

            index = ImageIndex(root)
            index.build()

            self.assertEqual(index.paths["guide/images/port.png"], str(image))
            self.assertEqual(index.paths["port.png"], str(image))


if __name__ == "__main__":
    unittest.main()
