import unittest

from htmlnode import HTMLNode, LeafNode




class TestHTMLNode(unittest.TestCase):
	def test_nothing_eq(self):
		node1 = HTMLNode()
		node2 = HTMLNode()

		self.assertEqual(node1, node2) 

	def test_tag_eq(self):

		node1 = HTMLNode("a", "https://www.google.com")
		node2 = HTMLNode("a", "https://www.google.com")

		self.assertEqual(node1, node2) 

	def test_tag_neq(self):
		node1 = HTMLNode("a", "https://www.google.com")
		node2 = HTMLNode("b", "https://www.google.com")

		self.assertNotEqual(node1, node2) 
	
	def test_tag_eq(self):
		node1 = HTMLNode("a", "https://www.google.com",None, {"target": "_blank"})
		node2 = HTMLNode("a", "https://www.google.com",None, {"target": "_blank"})

		r_1 = node1.props_to_html()
		r_2 = node2.props_to_html()

		self.assertEqual(r_1, r_2) 




class TestLeafNode(unittest.TestCase):
	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_leaf_props_eq(self):
		node1 = LeafNode("a", "Google link", {"href": "https://www.google.com", "target": "_blank"})

		self.assertEqual(node1.to_html(), "<a href=\"https://www.google.com\" target=\"_blank\" >Google link</a>") 







if __name__ == "__main__":
    unittest.main()


