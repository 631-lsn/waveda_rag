from pathlib import Path
from tempfile import TemporaryDirectory
import json
import sys
import types
import unittest
from unittest.mock import Mock, patch
import zipfile

from raggg.config import Settings
from raggg.pipeline.builder import build_knowledge_base


def make_settings(root: Path) -> Settings:
    return Settings(
        project_root=root,
        waveda_root=None,
        waveda_help_root=root / "wavEDA_docs" / "helpHtml" / "helpHtml",
        waveda_example_root=None,
        obsidian_vault_root=root / "knowledge_base",
        data_dir=root / "data",
        embedding_model="local-hashed-vectors",
        llm_base_url="https://api.deepseek.com",
        llm_api_key="",
        llm_model="deepseek-chat",
    )


def write_docx(path: Path, *paragraphs: str) -> None:
    body = "\n".join(
        f"<w:p><w:r><w:t>{paragraph}</w:t></w:r></w:p>"
        for paragraph in paragraphs
    )
    document_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>{body}</w:body>
</w:document>
"""
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("word/document.xml", document_xml)


class BuilderDocumentTests(unittest.TestCase):
    def test_build_indexes_pdf_and_docx_files_in_knowledge_base(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            kb = root / "knowledge_base"
            kb.mkdir()
            write_docx(kb / "manual.docx", "DOCX paragraph")
            (kb / "paper.pdf").write_bytes(b"%PDF-test")
            fake_reader = Mock()
            fake_reader.pages = [Mock(extract_text=Mock(return_value="PDF paragraph"))]
            fake_pypdf = types.SimpleNamespace(PdfReader=Mock(return_value=fake_reader))

            with patch.dict(sys.modules, {"pypdf": fake_pypdf}):
                report = build_knowledge_base(make_settings(root))

            chunks = json.loads((root / "data" / "index" / "chunks.json").read_text(encoding="utf-8"))
            joined = "\n".join(chunk["content"] for chunk in chunks)
            self.assertEqual(report.obsidian_document_count, 2)
            self.assertIn("DOCX paragraph", joined)
            self.assertIn("PDF paragraph", joined)


if __name__ == "__main__":
    unittest.main()
