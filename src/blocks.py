import re

from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

def markdown_to_blocks(markdown):
    blocks = re.split(r"\n\s*\n", markdown)
    new_blocks = []
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block != "":
            new_blocks.append(stripped_block)
    return new_blocks

def block_to_block_type(block):
    if block.startswith(("# ","## ","### ","#### ","##### ","###### ")):
        return BlockType.HEADING
    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    block_lines = block.split("\n")
    if all(line.startswith(">") for line in block_lines):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in block_lines):
        return BlockType.UNORDERED_LIST
    elif all(line.startswith(f"{i}. ") for i, line in enumerate(block_lines, 1)):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
