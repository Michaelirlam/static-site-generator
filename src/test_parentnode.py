import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tag(self):
        child_node = LeafNode("a", "child", {"href": "https://www.childprop.com"})
        parent_node = ParentNode(None, [child_node])
        self.assertRaisesRegex(ValueError, "No tag provided.", parent_node.to_html)

    def test_to_html_no_children_none(self):
        parent_node = ParentNode("p", None)
        self.assertRaisesRegex(ValueError, "No children provided.", parent_node.to_html)

    def test_to_html_no_children_empty_list(self):
        parent_node = ParentNode("p", [])
        self.assertRaisesRegex(ValueError, "No children provided.", parent_node.to_html)

    # Test for when I add props
    """
    def test_to_html_with_props(self):
        child_node = LeafNode("a", "child", {"href": "https://www.childprop.com"})
        parent_node = ParentNode("p", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<p><a href="https://www.childprop.com">child</a></p>'
        )
    """