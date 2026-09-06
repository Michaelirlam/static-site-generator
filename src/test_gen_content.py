import unittest
from gen_content import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_h1_exists(self):
        markdown = "# Title\n\nThis is the body of the markdown"
        header = extract_title(markdown)
        self.assertEqual(
            header,
            "Title"
        )

    def test_no_h1_exists(self):
        markdown = "There is no h1 here!"
        self.assertRaisesRegex(Exception, "No h1 in this markdown", extract_title, markdown)