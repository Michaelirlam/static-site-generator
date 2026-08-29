import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_is_empty(self):
        node = HTMLNode("p", "this is a test", None, None)
        self.assertEqual(node.props_to_html(), "")


    def test_props_to_html_is_not_none(self):
        node = HTMLNode("a", None, None, {"href": "https://www.boot.dev"})
        props_html = node.props_to_html()
        self.assertEqual(props_html, ' href="https://www.boot.dev"')

    def test_props_to_html_multiple(self):
        node = HTMLNode("a", None, None, {"href": "https://www.boot.dev", "target": "_blank"})
        props_html = node.props_to_html()
        self.assertEqual(props_html,' href="https://www.boot.dev" target="_blank"')

    def test_props_to_html_empty_dict(self):
        node = HTMLNode("p", "hello", None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("p", "hello", None, {"class": "text"})
        self.assertEqual(repr(node), "p, hello, None, {'class': 'text'}",)