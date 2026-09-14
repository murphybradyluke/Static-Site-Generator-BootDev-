from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://boot.dev")
    node2 = HTMLNode("h1", "This is some anchor text", "children list", {"href": "https://www.google.com", "target": "_blank"})


    print(node)
    print(HTMLNode.props_to_html(node2))

main()
