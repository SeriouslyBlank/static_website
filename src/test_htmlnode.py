import unittest

from htmlnode import HTMLNode




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



if __name__ == "__main__":
    unittest.main()


