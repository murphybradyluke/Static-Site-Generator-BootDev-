from extract_links import extract_markdown_images, extract_markdown_links
from splitdelim import split_nodes_delimiter
from textnode import TextType, TextNode

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if not images:            # no images → keep the node as-is
            new_list.append(node)
            continue

        remaining = node.text
        for alt, url in images:
            before, remaining = remaining.split(f"![{alt}]({url})", 1)
            if before != "":
                new_list.append(TextNode(before, TextType.TEXT))
            new_list.append(TextNode(alt, TextType.IMAGE, url))

        # after the loop: whatever text is left over
        if remaining != "":
            new_list.append(TextNode(remaining, TextType.TEXT))
    return new_list

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_list = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if not links:            # no images → keep the node as-is
            new_list.append(node)
            continue

        remaining = node.text
        for alt, url in links:
            before, remaining = remaining.split(f"[{alt}]({url})", 1)
            if before != "":
                new_list.append(TextNode(before, TextType.TEXT))
            new_list.append(TextNode(alt, TextType.LINK, url))

        # after the loop: whatever text is left over
        if remaining != "":
            new_list.append(TextNode(remaining, TextType.TEXT))
    return new_list
