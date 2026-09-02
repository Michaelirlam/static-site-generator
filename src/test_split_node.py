import unittest
from textnode import TextType, TextNode
from split_node import split_nodes_delimiter, split_nodes_image, split_nodes_link

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

class SplitImages(unittest.TestCase):
    def test_empty_string(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [])

    def test_non_text_type(self):
        node = TextNode("I am a **bold node**", TextType.BOLD)
        new_nodes = split_nodes_image([node])
        expected = [node]
        self.assertEqual(new_nodes, expected)

    def test_single_image_no_text_single_node(self):
        node = TextNode("![image](url)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("image", TextType.IMAGE, "url")
        ]
        self.assertEqual(new_nodes, expected)

    def test_single_image_leading_text_single_node(self):
        node = TextNode("This is an ![image](url)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "url")
        ]
        self.assertEqual(new_nodes, expected)

    def test_single_image_trailing_text_single_node(self):
        node = TextNode("![image](url) this is an image", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("image", TextType.IMAGE, "url"),
            TextNode(" this is an image", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_single_image_leading_and_trailing_text_single_node(self):
        node = TextNode("This is an ![image](url) with trailing text", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "url"),
            TextNode(" with trailing text", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_muliple_image_no_text_single_node(self):
        node = TextNode("![image1](url)![image2](url)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("image1", TextType.IMAGE, "url"),
            TextNode("image2", TextType.IMAGE, "url")
        ]
        self.assertEqual(new_nodes, expected)

    def test_muliple_image_text_inbetween_single_node(self):
        node = TextNode("![image1](url) inbetween ![image2](url)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("image1", TextType.IMAGE, "url"),
            TextNode(" inbetween ", TextType.TEXT),
            TextNode("image2", TextType.IMAGE, "url")
        ]
        self.assertEqual(new_nodes, expected)

    def test_multiple_nodes(self):
        node1 = TextNode("![image1](url) inbetween ![image2](url)", TextType.TEXT)
        node2 = TextNode("This is an ![image](url) with trailing text", TextType.TEXT)
        new_nodes = split_nodes_image([node1, node2])
        expected = [
            TextNode("image1", TextType.IMAGE, "url"),
            TextNode(" inbetween ", TextType.TEXT),
            TextNode("image2", TextType.IMAGE, "url"),
            TextNode("This is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "url"),
            TextNode(" with trailing text", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

class SplitLinks(unittest.TestCase):
    def test_empty_string(self):
            node = TextNode("", TextType.TEXT)
            new_nodes = split_nodes_link([node])
            self.assertEqual(new_nodes, [])
    
    def test_non_text_type(self):
        node = TextNode("I am a **bold node**", TextType.BOLD)
        new_nodes = split_nodes_link([node])
        expected = [node]
        self.assertEqual(new_nodes, expected)

    def test_single_link_no_text_single_node(self):
        node = TextNode("[alt_text](url)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("alt_text", TextType.LINK, "url")
        ]
        self.assertEqual(new_nodes, expected)

    def test_single_link_leading_text_single_node(self):
        node = TextNode("This is a link [alt_text](url)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is a link ", TextType.TEXT),
            TextNode("alt_text", TextType.LINK, "url")
        ]
        self.assertEqual(new_nodes, expected)

    def test_single_link_trailing_text_single_node(self):
        node = TextNode("[alt_text](url) this is a link", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("alt_text", TextType.LINK, "url"),
            TextNode(" this is a link", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_single_link_leading_and_trailing_text_single_node(self):
        node = TextNode("This is a link [alt_text](url) with trailing text", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is a link ", TextType.TEXT),
            TextNode("alt_text", TextType.LINK, "url"),
            TextNode(" with trailing text", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_muliple_link_no_text_single_node(self):
        node = TextNode("[alt_text1](url)[alt_text2](url)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("alt_text1", TextType.LINK, "url"),
            TextNode("alt_text2", TextType.LINK, "url")
        ]
        self.assertEqual(new_nodes, expected)

    def test_muliple_link_text_inbetween_single_node(self):
        node = TextNode("[alt_text1](url) inbetween [alt_text2](url)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("alt_text1", TextType.LINK, "url"),
            TextNode(" inbetween ", TextType.TEXT),
            TextNode("alt_text2", TextType.LINK, "url")
        ]
        self.assertEqual(new_nodes, expected)
#
    def test_multiple_nodes(self):
        node1 = TextNode("[alt_text1](url) inbetween [alt_text2](url)", TextType.TEXT)
        node2 = TextNode("This is an [alt_text](url) with trailing text", TextType.TEXT)
        new_nodes = split_nodes_link([node1, node2])
        expected = [
            TextNode("alt_text1", TextType.LINK, "url"),
            TextNode(" inbetween ", TextType.TEXT),
            TextNode("alt_text2", TextType.LINK, "url"),
            TextNode("This is an ", TextType.TEXT),
            TextNode("alt_text", TextType.LINK, "url"),
            TextNode(" with trailing text", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)