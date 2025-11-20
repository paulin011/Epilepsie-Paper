import os
from watcher import FileWatcher
from config import Config


def main():
    # Use the runtime Config to determine folders
    cfg = Config()

    # Create output folder if it doesn't exist
    os.makedirs(cfg.target_folder, exist_ok=True)

    # Initialize the file watcher (it uses the Config internally)
    file_watcher = FileWatcher()

    # Start watching for new PDF files
    print(f"Watching for new PDF files in {cfg.source_folder}...")
    file_watcher.run()


if __name__ == "__main__":
    main()