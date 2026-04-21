import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        """Should be equal: identical text and type, both URLs are None"""
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        """Should be equal: all three properties match exactly"""
        node = TextNode("Check this out", TextType.LINK, "https://boot.dev")
        node2 = TextNode("Check this out", TextType.LINK, "https://boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        """Should NOT be equal: text content is different"""
        node = TextNode("This is text", TextType.TEXT)
        node2 = TextNode("This is different text", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        """Should NOT be equal: text is same, but type is different"""
        node = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        """Should NOT be equal: one has a URL, the other is None"""
        node = TextNode("Link", TextType.LINK, "https://boot.dev")
        node2 = TextNode("Link", TextType.LINK)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()