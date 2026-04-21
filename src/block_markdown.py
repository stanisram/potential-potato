from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node


def markdown_to_blocks(markdown):
    # Split by double newlines to find potential blocks
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        # Strip whitespace from the edges
        block = block.strip()
        # Only add to our list if the block isn't just an empty string
        if block != "":
            filtered_blocks.append(block)
    return filtered_blocks

from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")

    # Heading check
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    # Code block check
    if len(lines) > 1 and block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Quote block check
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

# Unordered list check
    if block.startswith("- ") or block.startswith("* "):
        for line in lines:
            if not (line.startswith("- ") or line.startswith("* ")):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST

    # Ordered list check
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.QUOTE:
        return create_quote_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return create_ulist_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return create_olist_node(block)
    if block_type == BlockType.CODE:
        return create_code_node(block)
    if block_type == BlockType.HEADING:
        return create_heading_node(block)
    return create_paragraph_node(block)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

# --- Specific Block Creators ---

def create_paragraph_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def create_heading_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    content = block[level + 1 :]
    children = text_to_children(content)
    return ParentNode(f"h{level}", children)

def create_quote_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def create_code_node(block):
    # Remove the backticks (first and last lines)
    text = block.strip("```").strip("\n")
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def create_ulist_node(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        content = line[2:] # This correctly skips "- " or "* "
        children = text_to_children(content)
        items.append(ParentNode("li", children))
    return ParentNode("ul", items)

def create_olist_node(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        # Strip the "1. " or "2. " prefix
        content = line[line.find(". ") + 2:]
        children = text_to_children(content)
        items.append(ParentNode("li", children))
    return ParentNode("ol", items)