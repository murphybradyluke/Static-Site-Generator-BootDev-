import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "This is some anchor text", "children list: []", {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("h1", "This is some anchor text", "children list: []", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_header_not_eq(self):
        node = HTMLNode("h1", "This is some anchor text", "children list: []", {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("h2", "This is some anchor text", "children list: []", {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_value_not_eq(self):
        node = HTMLNode("h1", "This is some anchor text", "children list: []", {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("h1", "This is some other text", "children list: []", {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_children_not_eq(self):
        node = HTMLNode("h1", "This is some anchor text", "children list: []", {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("h1", "This is some anchor text", "children list: [HTMLNode2]", {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_leaf_to_html_ahref(self):
        node = LeafNode("a", "Hello, world!", {"href" : "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')

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

if __name__ == "__main__":
    unittest.main()
