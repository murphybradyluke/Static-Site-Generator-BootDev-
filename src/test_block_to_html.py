import unittest

from src.block_take2 import markdown_to_html_node

class TestBlockToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_unordered_list(self):
        md = """
- Item one
- Item two
- Item three
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item one</li><li>Item two</li><li>Item three</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. Item one
2. Item two
3. Item three
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Item one</li><li>Item two</li><li>Item three</li></ol></div>",
        )
