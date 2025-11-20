import os
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from config import Config
from converter import PDFConverter


class FileWatcher:
    def __init__(self, config: Config | None = None):
        # Use provided config or create one
        self.config = config or Config()
        # Ensure source/target folders exist (create target if missing)
        os.makedirs(self.config.source_folder, exist_ok=True)
        os.makedirs(self.config.target_folder, exist_ok=True)

        # PDFConverter expects input and output folders
        self.converter = PDFConverter(self.config.source_folder, self.config.target_folder)
        self.observer = Observer()

    def scan_and_convert_existing(self) -> None:
        """Scan the source folder for PDFs and convert those that don't yet have a .md in the target folder."""
        src_path = Path(self.config.source_folder)
        if not src_path.exists():
            print(f"Source folder does not exist: {src_path}")
            return

        for pdf in src_path.glob("*.pdf"):
            try:
                out = self.converter.get_output_file_name(pdf)
                if not out.exists():
                    print(f"Converting missing: {pdf.name} -> {out.name}")
                    try:
                        self.converter.process_pdf(pdf)
                    except Exception as e:
                        print(f"Failed to convert {pdf}: {e}")
                else:
                    # existing markdown found; skip
                    # If you want to re-generate on newer PDF mtime, expand logic here
                    continue
            except Exception as exc:
                print(f"Error while checking {pdf}: {exc}")

    def run(self):
        # Run initial scan to catch already-present PDFs without MD
        try:
            self.scan_and_convert_existing()
        except Exception as e:
            print(f"Initial scan failed: {e}")

        event_handler = self.FileEventHandler(self.converter, self.config)
        self.observer.schedule(event_handler, self.config.source_folder, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

    class FileEventHandler(FileSystemEventHandler):
        def __init__(self, converter: PDFConverter, config: Config):
            self.converter = converter
            self.config = config

        def on_created(self, event):
            # Ignore directory events
            if event.is_directory:
                return
            src = Path(event.src_path)
            if src.suffix.lower() == self.config.pdf_extension:
                try:
                    self.converter.process_pdf(src)
                except Exception as exc:
                    print(f"Error processing {src}: {exc}")

        # Also handle moved files (e.g., atomic saves)
        def on_moved(self, event):
            if event.is_directory:
                return
            src = Path(event.dest_path)
            if src.suffix.lower() == self.config.pdf_extension:
                try:
                    self.converter.process_pdf(src)
                except Exception as exc:
                    print(f"Error processing moved file {src}: {exc}")