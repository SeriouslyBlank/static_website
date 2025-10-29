import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node3 = TextNode("This is a text node", TextType.PLAIN, "https://www.boot.dev")
        node4 = TextNode("This is a text node", TextType.PLAIN, "https://www.boot.dev")
    
        self.assertEqual(node3, node4)

    def test_unequal_types(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.PLAIN)

        self.assertNotEqual(node, node2)

    def test_unequal_link(self):
        node2 = TextNode("This is a text node", TextType.PLAIN)
        node3 = TextNode("This is a text node", TextType.PLAIN, "https://www.boot.dev")

        self.assertNotEqual(node2, node3)

    def test_unequal_link_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.PLAIN, "https://www.boot.dev")

        self.assertNotEqual(node, node3)




if __name__ == "__main__":
    unittest.main()