import unittest
from blocks import markdown_to_blocks

class TestMarkDownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )

    def test_empty_string(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_strips_leading_and_trailing_whitespace(self):
        md = "  \n  First paragraph  \n\n  Second paragraph  \n"
        self.assertEqual(
            markdown_to_blocks(md),
            ["First paragraph", "Second paragraph"],
        )

    def test_whitespace_only_string(self):
        self.assertEqual(markdown_to_blocks("   \n\n  "), [])

    def test_single_block(self):
        self.assertEqual(
            markdown_to_blocks("A single paragraph"),
            ["A single paragraph"],
        )

    def test_preserves_newlines_inside_block(self):
        md = "First line\nSecond line\nThird line"
        self.assertEqual(
            markdown_to_blocks(md),
            ["First line\nSecond line\nThird line"],
        )

    def test_multiple_blank_lines(self):
        md = "First block\n\n\nSecond block"
        self.assertEqual(
            markdown_to_blocks(md),
            ["First block", "Second block"],
        )