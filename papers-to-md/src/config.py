from pathlib import Path

PAPERS_FOLDER = "Papers"
PAPERS_MD_FOLDER = "Papers md"
PDF_EXTENSION = ".pdf"
MARKDOWN_EXTENSION = ".md"


class Config:
    """Simple runtime config object used by the watcher.

    Resolves folders relative to the project root (two levels above this file).
    """

    def __init__(self, base: str | Path | None = None):
        if base:
            self.base = Path(base)
        else:
            # project root is three levels up from src/config.py (workspace root)
            self.base = Path(__file__).resolve().parents[2]

        self.source_folder = str(self.base / PAPERS_FOLDER)
        self.target_folder = str(self.base / PAPERS_MD_FOLDER)
        self.pdf_extension = PDF_EXTENSION
        self.md_extension = MARKDOWN_EXTENSION