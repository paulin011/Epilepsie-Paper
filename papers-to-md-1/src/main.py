import os
import time
from watcher import FileWatcher
from converter import PDFConverter
from config import INPUT_FOLDER, OUTPUT_FOLDER

def main():
    # Create output folder if it doesn't exist
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # Initialize the PDF converter
    pdf_converter = PDFConverter()

    # Initialize the file watcher
    file_watcher = FileWatcher(INPUT_FOLDER, pdf_converter)

    # Start watching for new PDF files
    print(f"Watching for new PDF files in {INPUT_FOLDER}...")
    file_watcher.start()

if __name__ == "__main__":
    main()