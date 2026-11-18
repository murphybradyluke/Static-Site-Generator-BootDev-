import unittest
from generate import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        proper = extract_title("# hello")
        self.assertEqual(proper, "hello")

    def test_extract_title_no_header(self):
        with self.assertRaises(Exception):
            extract_title("hello")
