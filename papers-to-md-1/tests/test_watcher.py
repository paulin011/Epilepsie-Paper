import os
import time
import unittest
from unittest.mock import patch, MagicMock
from src.watcher import FileWatcher

class TestFileWatcher(unittest.TestCase):
    def setUp(self):
        self.test_directory = 'Papers'
        self.file_watcher = FileWatcher(self.test_directory)

    @patch('os.listdir')
    def test_detect_new_file(self, mock_listdir):
        # Simulate the initial state with no files
        mock_listdir.return_value = []
        self.file_watcher.start_watching()
        
        # Simulate adding a new PDF file
        mock_listdir.return_value = ['new_file.pdf']
        new_files = self.file_watcher.check_for_new_files()
        
        self.assertIn('new_file.pdf', new_files)

    @patch('os.listdir')
    def test_no_new_files(self, mock_listdir):
        # Simulate the initial state with one file
        mock_listdir.return_value = ['existing_file.pdf']
        self.file_watcher.start_watching()
        
        # Simulate no new files being added
        new_files = self.file_watcher.check_for_new_files()
        
        self.assertEqual(new_files, [])

    @patch('time.sleep', return_value=None)  # Mock sleep to speed up tests
    def test_watching_loop(self, mock_sleep):
        with patch('os.listdir') as mock_listdir:
            mock_listdir.side_effect = [['file1.pdf'], ['file1.pdf', 'file2.pdf']]
            self.file_watcher.start_watching()
            new_files = self.file_watcher.check_for_new_files()
            self.assertIn('file2.pdf', new_files)

if __name__ == '__main__':
    unittest.main()