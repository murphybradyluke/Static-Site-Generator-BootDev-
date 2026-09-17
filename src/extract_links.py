import re

def extract_markdown_images(text: str):
    matches = re.findall(r"!\[([^\]]*)\]\(([^\)]*)\)", text)
    return matches

def extract_markdown_links(text: str):
    matches = re.findall(r"(?<!!)\[([^\]]*)\]\(([^\)]*)\)", text)
    return matches

print (extract_markdown_images("This is text with a link [to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)"))
