from pathlib import Path
from typing import Union
from pdfminer.high_level import extract_text


class PDFConverter:
    def __init__(self, input_folder: Union[str, Path], output_folder: Union[str, Path]):
        self.input_folder = Path(input_folder)
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)

    def convert_pdf_to_markdown(self, pdf_file: Union[str, Path]) -> str:
        """Extract text from a PDF and return a simple Markdown string."""
        path = Path(pdf_file)
        text = extract_text(str(path)) or ""
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