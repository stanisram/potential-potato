import unittest
from block_markdown import (
    markdown_to_blocks, 
    block_to_block_type, 
    BlockType, 
    markdown_to_html_node  # <-- Add this!
)

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        """Test that excessive newlines are handled correctly"""
        md = """
This is a paragraph


This is another paragraph
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a paragraph",
                "This is another paragraph",
            ],
        )

if __name__ == "__main__":
    unittest.main()

from block_markdown import block_to_block_type, BlockType

class TestBlockType(unittest.TestCase):
    def test_block_to_block_types(self):
        self.assertEqual(block_to_block_type("# heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("```\ncode\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> quote\n> more quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- item 1\n- item 2"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. first\n2. second"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("this is just a paragraph"), BlockType.PARAGRAPH)

    def test_ordered_list_fail(self):
        """Should be a paragraph if numbers don't start at 1 or increment correctly"""
        self.assertEqual(block_to_block_type("2. wrong start"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("1. first\n3. skipped"), BlockType.PARAGRAPH)

    def test_quote_fail(self):
        """Should be a paragraph if one line is missing the > symbol"""
        self.assertEqual(block_to_block_type("> quote\nmissing"), BlockType.PARAGRAPH)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_node(self):
        md = """
# Heading

This is a paragraph with **bold** text.

* Item 1
* Item 2
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertIn("<h1>Heading</h1>", html)
        self.assertIn("<p>This is a paragraph with <b>bold</b> text.</p>", html)
        self.assertIn("<ul><li>Item 1</li><li>Item 2</li></ul>", html)

    def test_complex_nesting(self):
        md = "> This is a quote\n> with **bold** inside"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><blockquote>This is a quote with <b>bold</b> inside</blockquote></div>")