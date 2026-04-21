import unittest
from utils import extract_title # Adjust import based on your filename

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_basic(self):
        markdown = "# Hello World\n\nSome content."
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_extract_title_with_spaces(self):
        markdown = "#   Lots of spaces   "
        self.assertEqual(extract_title(markdown), "Lots of spaces")

    def test_extract_title_no_h1(self):
        markdown = "## Hello World\n\nNo h1 here."
        with self.assertRaises(Exception):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()