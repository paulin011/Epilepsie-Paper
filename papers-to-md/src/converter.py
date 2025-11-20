from pathlib import Path
from typing import Union

# ensure name exists for static analysis
extract_text = None
try:
    from pdfminer.high_level import extract_text as _pdfminer_extract_text  # type: ignore
    extract_text = _pdfminer_extract_text
    _HAS_PDFMINER = True
except Exception:
    _HAS_PDFMINER = False
    try:
        from PyPDF2 import PdfReader  # type: ignore
    except Exception:
        PdfReader = None  # type: ignore


class PDFConverter:
    def __init__(self, input_folder: Union[str, Path], output_folder: Union[str, Path]):
        self.input_folder = Path(input_folder)
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)

    def _extract_text_with_pypdf2(self, path: Path) -> str:
        """Extract text using PyPDF2 as a fallback."""
        if PdfReader is None:
            raise RuntimeError("Neither pdfminer.six nor PyPDF2 is installed; cannot extract PDF text.")
        reader = PdfReader(str(path))
        texts = []
        for page in getattr(reader, "pages", []):
            try:
                page_text = page.extract_text()
            except Exception:
                page_text = None
            if page_text:
                texts.append(page_text)
        return "\n".join(texts)

    def convert_pdf_to_markdown(self, pdf_file: Union[str, Path]) -> str:
        """Extract text from a PDF and return a simple Markdown string.

        Uses pdfminer.six if available, otherwise falls back to PyPDF2.
        """
        path = Path(pdf_file)
        if _HAS_PDFMINER and extract_text is not None:
            try:
                text = extract_text(str(path)) or ""
            except Exception:
                # fallback to PyPDF2 if pdfminer fails at runtime
                text = self._extract_text_with_pypdf2(path)
        else:
            text = self._extract_text_with_pypdf2(path)

        # Basic markdown: title from filename + body text
        md = f"# {path.stem}\n\n" + text.strip() + "\n"
        return md

    def save_markdown(self, markdown_content: str, output_file: Union[str, Path]) -> None:
        outp = Path(output_file)
        outp.parent.mkdir(parents=True, exist_ok=True)
        outp.write_text(markdown_content, encoding="utf-8")

    def get_output_file_name(self, pdf_file: Union[str, Path]) -> Path:
        p = Path(pdf_file)
        return self.output_folder / (p.stem + ".md")

    def process_pdf(self, pdf_file: Union[str, Path]) -> Path:
        """Convert given PDF file and write markdown to the output folder. Returns output path."""
        p = Path(pdf_file)
        if not p.exists():
            raise FileNotFoundError(f"PDF not found: {p}")
        markdown = self.convert_pdf_to_markdown(p)
        out_file = self.get_output_file_name(p)
        self.save_markdown(markdown, out_file)
        return out_file