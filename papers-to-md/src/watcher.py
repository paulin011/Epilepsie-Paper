class FileWatcher:
    import os
    import time
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    from converter import PDFConverter
    from config import Config

    def __init__(self):
        self.config = Config()
        self.observer = Observer()
        self.converter = PDFConverter()

    def run(self):
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
        def __init__(self, converter, config):
            self.converter = converter
            self.config = config

        def on_created(self, event):
            if event.src_path.endswith('.pdf'):
                self.converter.convert(event.src_path)