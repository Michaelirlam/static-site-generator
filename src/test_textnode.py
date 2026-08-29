import unittest
from textnode import TextType, TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is a test node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_text_not_eq(self):
        node1 = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is also a test node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_text_type_not_eq(self):
        node1 = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is a test node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_url_is_none(self):
        node = TextNode("This is a test node", TextType.BOLD)
        self.assertIsNone(node.url)

    def test_url_is_not_none(self):
        node = TextNode("This is a test node", TextType.BOLD, "https://www.boot.dev")
        self.assertIsNotNone(node.url)

if __name__ == "__main__":
    unittest.main()