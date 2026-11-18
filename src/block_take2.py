
from blocks import markdown_to_blocks, block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType
from htmlnode import ParentNode

def blockquote_to_string(block):
    lines = block.split("\n")
    stripped_list = []
    for line in lines:
        stripped = line.lstrip("> ")
        stripped_list.append(stripped)
    string = " ".join(stripped_list)
    return string

def unordered_list_to_nodes(block):
    lines = block.split("\n")
    stripped_list = []
    for line in lines:
        stripped = line.lstrip("- ")
        children = text_to_children(stripped)
        listnodes = ParentNode("li", children)
        stripped_list.append(listnodes)
    return stripped_list

def ordered_list_to_nodes(block):
    lines = block.split("\n")
    stripped_list = []
    for line in lines:
        split = line.split(". ", 1)
        children = text_to_children(split[1])
        listnodes = ParentNode("li", children)
        stripped_list.append(listnodes)
    return stripped_list

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    htmlnodes = [text_node_to_html_node(tn) for tn in text_nodes]
    return htmlnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        blocktype = block_to_block_type(block)
        if blocktype == BlockType.QUOTE:
            string = blockquote_to_string(block)
            htmlnodes = text_to_children(string)
            quote_node = ParentNode("blockquote", htmlnodes)
            children.append(quote_node)
        elif blocktype == BlockType.CODE:
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
        elif blocktype == BlockType.UNORDERED_LIST:
            listnodes = unordered_list_to_nodes(block)
            ul_node = ParentNode("ul", listnodes)
            children.append(ul_node)
        elif blocktype == BlockType.ORDERED_LIST:
            listnodes = ordered_list_to_nodes(block)
            ol_node = ParentNode("ol", listnodes)
            children.append(ol_node)
        else:
            string = blockquote_to_string(block)
            htmlnodes = text_to_children(string)
            paragraph_node = ParentNode("p", htmlnodes)
            children.append(paragraph_node)
    return ParentNode("div", children)
