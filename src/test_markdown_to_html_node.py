import unittest
from markdown_to_html_node import *

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        node = markdown_to_html_node("# Heading 1\n\n### Heading 3")
        self.assertEqual(
            node.to_html(),
            "<div><h1>Heading 1</h1><h3>Heading 3</h3></div>",
        )

    def test_unordered_list(self):
        node = markdown_to_html_node("- One\n- Two\n- Three")
        self.assertEqual(
            node.to_html(),
            "<div><ul><li>One</li><li>Two</li><li>Three</li></ul></div>",
        )

    def test_ordered_list(self):
        node = markdown_to_html_node("1. First\n2. Second")
        self.assertEqual(
            node.to_html(),
            "<div><ol><li>First</li><li>Second</li></ol></div>",
        )

    def test_blockquote(self):
        node = markdown_to_html_node("> This is a quote")
        self.assertEqual(
            node.to_html(),
            "<div><blockquote>This is a quote</blockquote></div>",
        )

    def test_links_and_images(self):
        node = markdown_to_html_node(
            "[Boot.dev](https://www.boot.dev)\n\n![Logo](logo.png)"
        )
        self.assertEqual(
            node.to_html(),
            '<div><p><a href="https://www.boot.dev">Boot.dev</a></p>'
            '<p><img src="logo.png" alt="Logo"></p></div>',
        )
    
    def test_multiline_quote(self):
        node = markdown_to_html_node(
            "> First line\n> Second line with **bold** text"
        )
        html = node.to_html()
        self.assertIn("<blockquote>", html)
        self.assertIn("First line Second line with <b>bold</b> text", html)
        self.assertIn("</blockquote>", html)