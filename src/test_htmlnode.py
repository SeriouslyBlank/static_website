import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode




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


class TestParentNode(unittest.TestCase):
	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)

	def test_to_html_with_props(self):

		child = LeafNode("b", "Bold text")
		props = {"class": "highlight", "id": "main-text"}
		parent = ParentNode("p", [child], props)

		html_output = parent.to_html()

		expected_html = '<p class="highlight" id="main-text" ><b>Bold text</b></p>'
		self.assertEqual(html_output, expected_html)







if __name__ == "__main__":
    unittest.main()


