import unittest
from src.converter import PDFConverter

class TestPDFConverter(unittest.TestCase):

    def setUp(self):
        self.converter = PDFConverter()

    def test_convert_pdf_to_markdown(self):
        pdf_file = 'path/to/sample.pdf'  # Replace with a sample PDF file path
        expected_markdown_file = 'path/to/expected_output.md'  # Replace with expected output path
        
        # Assuming the converter has a method to convert and return the output path
        output_path = self.converter.convert(pdf_file)
        
        with open(expected_markdown_file, 'r') as f:
            expected_content = f.read()
        
        with open(output_path, 'r') as f:
            output_content = f.read()
        
        self.assertEqual(expected_content, output_content)

    def test_invalid_pdf(self):
        invalid_pdf_file = 'path/to/invalid.pdf'  # Replace with an invalid PDF file path
        
        with self.assertRaises(ValueError):
            self.converter.convert(invalid_pdf_file)

if __name__ == '__main__':
    unittest.main()