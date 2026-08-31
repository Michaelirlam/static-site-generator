import unittest
from textnode import TextType, TextNode
from split_node import split_nodes_delimiter

class TestSplitNode(unittest.TestCase):
    def test_not_text_node(self):
        node = TextNode("This is a code node", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], None, None)
        expected = [TextNode("This is a code node", TextType.CODE)]
        self.assertEqual(new_nodes, expected)

    def test_no_delimiter(self):
        node = TextNode("This node has no delimiter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This node has no delimiter", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_single_delimiter(self):
        node = TextNode("This node contains **bold text** for this test", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This node contains ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" for this test", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_multiple_delimiters(self):
        node = TextNode("This node contains `this code`, but also `this code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This node contains ", TextType.TEXT),
            TextNode("this code", TextType.CODE),
            TextNode(", but also ", TextType.TEXT),
            TextNode("this code", TextType.CODE)
        ]
        self.assertEqual(new_nodes, expected)

    def test_mulitple_nodes(self):
        node1 = TextNode("This has a `code` word", TextType.TEXT)
        node2 = TextNode("This has no delimiter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        expected = [
            TextNode("This has a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("This has no delimiter", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_multiple_text_types(self):
        node1 = TextNode("This has `code` in it", TextType.TEXT)
        node2 = TextNode("already bold", TextType.BOLD)
        node3 = TextNode("already italic", TextType.ITALIC)
        new_nodes = split_nodes_delimiter([node1, node2, node3], "`", TextType.CODE)
        expected = [
            TextNode("This has ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" in it", TextType.TEXT),
            TextNode("already bold", TextType.BOLD),
            TextNode("already italic", TextType.ITALIC)
        ]
        self.assertEqual(new_nodes, expected)

    def test_starts_with_delimiter(self):
        node = TextNode("`This node` starts with code", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This node", TextType.CODE),
            TextNode(" starts with code", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_ends_with_delimiter(self):
        node = TextNode("This node ends with `code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This node ends with ", TextType.TEXT),
            TextNode("code", TextType.CODE)
        ]
        self.assertEqual(new_nodes, expected)

    def test_unclosed_delimiter(self):
        node = TextNode("This node's `delimiter doesnt close", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], "`", TextType.CODE)

    def test_empty_string(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [])