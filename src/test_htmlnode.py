import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        """Test a single property"""
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple(self):
        """Test multiple properties for correct spacing"""
        node = HTMLNode(
            props={
                "href": "https://www.google.com", 
                "target": "_blank",
            }
        )
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_values(self):
        """Test that constructor values are assigned correctly"""
        node = HTMLNode(
            "p",
            "This is a paragraph",
            None,
            {"class": "primary"}
        )
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"class": "primary"})

    def test_repr(self):
        """Test that the repr prints what we expect"""
        node = HTMLNode("h1", "Hello World")
        self.assertEqual(repr(node), "HTMLNode(h1, Hello World, children: None, None)")

if __name__ == "__main__":
    unittest.main()