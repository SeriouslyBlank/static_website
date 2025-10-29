
from textnode import TextNode,TextType

class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props
		

	def to_html(self):
		raise NotImplementedError("method not done")

	def props_to_html(self):
		result = " "
		for key,value in self.props.items():
			result += key +"=\"" + value +"\"" + " "
		return result

	def __repr__(self):
		return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

	def __eq__(self, other):
		if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
			return True
		return False



class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag=tag, value=value, children=None, props=props)

	def to_html(self):
		if self.value == None:
			raise ValueError("No value passed for the tag")
		if self.tag == None:
			return self.value
		else:
			if self.props == None:
				return f"<{self.tag}>{self.value}</{self.tag}>"

			else:
				result = self.props_to_html()
				return f"<{self.tag}{result}>{self.value}</{self.tag}>"



class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag=tag, value =None, children=children, props=props)

	def to_html(self):
		if self.tag == None:
			raise ValueError("No tag passed")
		if self.children == None:
			raise ValueError("children is missing a value")

		result_c = ""

		for child in self.children:
			result_c += child.to_html()

		result_p = ""

		if self.props != None:
			result_p = self.props_to_html()


		return f"<{self.tag}{result_p}>{result_c}</{self.tag}>"




def text_node_to_html_node(TextNode):
	if TextNode.text_type == TextType.TEXT:
		return LeafNode(None, TextNode.text)
	elif TextNode.text_type == TextType.BOLD:
		return LeafNode("b", TextNode.text)
	elif TextNode.text_type == TextType.ITALIC:
		return LeafNode("i", TextNode.text)
	elif TextNode.text_type == TextType.CODE:
		return LeafNode("code", TextNode.text)
	elif TextNode.text_type == TextType.LINK:
		return LeafNode("a", TextNode.text, {"href": TextNode.url})
	elif TextNode.text_type == TextType.IMAGE:
		return LeafNode("img","", {"src": TextType.url, "alt": TextType.text})
	else:
		raise Exception("Not valid text type -> text, bold, italic, code, link, image")

