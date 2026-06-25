from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "src" / "convert_pdf.py"
SPEC = importlib.util.spec_from_file_location("convert_pdf", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ConvertPdfTests(unittest.TestCase):
    def test_normalize_markdown(self) -> None:
        raw = "Title  \r\n\r\n\r\n\r\nBody\x00  \r\n"
        self.assertEqual(MODULE.normalize_markdown(raw), "Title\n\n\nBody\n")

    def test_validate_rejects_wrong_extension(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "sample.txt"
            path.write_bytes(b"%PDF-1.7")
            with self.assertRaisesRegex(ValueError, r"\.pdf extension"):
                MODULE.validate_input(path, 1)

    def test_validate_rejects_wrong_signature(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "sample.pdf"
            path.write_bytes(b"not a pdf")
            with self.assertRaisesRegex(ValueError, "valid PDF signature"):
                MODULE.validate_input(path, 1)

    def test_available_output_avoids_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "sample.md"
            path.write_text("existing", encoding="utf-8")
            self.assertEqual(
                MODULE.available_output(path, overwrite=False).name,
                "sample-converted.md",
            )


if __name__ == "__main__":
    unittest.main()
