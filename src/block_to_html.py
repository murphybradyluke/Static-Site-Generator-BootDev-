from src.blocks import markdown_to_blocks, BlockType, block_to_block_type
from src.textnode import TextNode, TextType, text_node_to_html_node
from src.text_to_textnodes import text_to_textnodes
from src.htmlnode import ParentNode
from src.splitnodes import split_nodes_delimiter


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        blocktype = block_to_block_type(block)
        text_nodes = text_to_textnodes(block)
        if blocktype == BlockType.CODE:
            inner_text = block[4:-4]
            code_text_node = TextNode(inner_text, TextType.CODE)
            code_html_node = [text_node_to_html_node(code_text_node)]
            code_node = ParentNode("code", code_html_node)
            code_pre_node = ParentNode("pre", [code_node])
            children.append(code_pre_node)
        elif blocktype == BlockType.HEADING:
            parts = block.split(" ", 1)
            level = len(parts[0])
            heading_text_node = text_to_textnodes(parts[1])
            heading_html_node = [text_node_to_html_node(tn) for tn in heading_text_node]
            heading_node = ParentNode(f"h{level}", heading_html_node)
            children.append(heading_node)
        else:
            block_node = text_to_children(text_nodes, blocktype)
            children.append(block_node)
    return ParentNode("div", children)

def text_to_children(text_nodes, blocktype):
    htmlnodes = [text_node_to_html_node(tn) for tn in text_nodes]
    if blocktype == BlockType.PARAGRAPH:
        paragraph_node = ParentNode("p", htmlnodes)
        return paragraph_node
    if blocktype == BlockType.QUOTE:
        split_nodes = split_nodes_delimiter(htmlnodes, ">", TextType.TEXT)
        quote_node = ParentNode("blockquote", split_nodes)
        return quote_node
