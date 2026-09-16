
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
        else:
            text = node.text
            split_text = text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise Exception("Missing delimiter")
            for index, value in enumerate(split_text):
                if value == "":
                    continue
                if index % 2 == 0:
                    new_list.append(TextNode(value, TextType.TEXT))
                if index % 2 != 0:
                    new_list.append(TextNode(value, text_type))
    return new_list

print (split_nodes_delimiter([TextNode("This is text with a `code block` word", TextType.TEXT)], "`", TextType.CODE))
