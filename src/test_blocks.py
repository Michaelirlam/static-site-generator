import unittest
from blocks import markdown_to_blocks, block_to_block_type, BlockType

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

class TestBlockToBlockType(unittest.TestCase):
    def test_heading_one(self):
        block = "# I am a H1"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.HEADING
        )

    def test_heading_two(self):
        block = "## I am a H2"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.HEADING
        )

    def test_heading_three(self):
        block = "### I am a H3"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.HEADING
        )

    def test_heading_four(self):
        block = "#### I am a H4"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.HEADING
        )

    def test_heading_five(self):
        block = "##### I am a H5"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.HEADING
        )

    def test_heading_six(self):
        block = "###### I am a H6"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.HEADING
        )

    def test_heading_seven_is_not_heading(self):
        block = "####### I am not a heading"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )

    def test_hash_without_space_is_not_heading(self):
        block = "#This is not a heading"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )
    
    def test_is_code(self):
        block = "```This is code```"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.CODE
        )

    def test_is_not_code(self):
        block = "```This is not code"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )

    def test_quote(self):
        block = ">This is a quote"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE
        )

    def test_is_unordered_list(self):
        block = "- This is an unordered list"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.UNORDERED_LIST
        )

    def test_is_not_unordered_list(self):
        block = "-This is not an unordered list"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )

    def test_is_an_ordered_list(self):
        block = "1. This is not an ordered list"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST
        )

    def test_is_not_an_ordered_list(self):
        block = "1.This is not an ordered list"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )

    def test_two_digit_ordered_list(self):
        block = "10. This is an ordered list"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST
        )

    def test_paragraph(self):
        block = "This is a normal paragraph"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )

    def test_empty_block(self):
        block = ""
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )