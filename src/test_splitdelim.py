import unittest


from splitdelim import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitDelim(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_bold_node_split(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ])

    def test_italic_node_split(self):
        node = TextNode("This is text with a _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ])

    def test_leading_delimiter(self):
        node = TextNode("**This** text leads with a bold delimiter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This", TextType.BOLD),
            TextNode(" text leads with a bold delimiter", TextType.TEXT),
        ])

    def test_trailing_delimiter(self):
        node = TextNode("This text ends with a bold **delimiter**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This text ends with a bold ", TextType.TEXT),
            TextNode("delimiter", TextType.BOLD),
        ])

    def test_unmatched_delimiter(self):
        node = TextNode("This text has an unmatched **delimiter", TextType.TEXT)
        with self.assertRaisesRegex(Exception, "Missing delimiter"):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_unmatched_delimiter_three(self):
        node = TextNode("This **test** has an **unmatched delimiter", TextType.TEXT)
        with self.assertRaisesRegex(Exception, "Missing delimiter"):
            split_nodes_delimiter([node], "**", TextType.BOLD)
