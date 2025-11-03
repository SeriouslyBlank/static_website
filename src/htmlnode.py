
from textnode import TextNode,TextType

from split_nodes import markdown_to_blocks, text_to_textnodes
from blocktype import BlockType, block_to_block_type


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
		return LeafNode("img","", {"src": TextNode.url, "alt": TextNode.text})
	else:
		raise Exception("Not valid text type -> text, bold, italic, code, link, image")


def txt_to_children(text):
	nodes = text_to_textnodes(text)
	html_nodes = []
	for node in nodes:
		html_nodes.append(text_node_to_html_node(node))
	return html_nodes

def list_items(block):
	block_lines = block.split("\n")
	result = []
	for i in range(len(block_lines)):
		if f"{i+1}. " in block_lines[i]:
			result.append(block_lines[i].replace(f"{i+1}. ", ""))
		else:
			result.append(block_lines[i].replace("- ", ""))



	return result






def markdown_to_html_node(markdown):
	blocks = markdown_to_blocks(markdown)
	children_nodes = []
	for block in blocks:
		type_block = block_to_block_type(block)
		if type_block == BlockType.PARAGRAPH:
			normalized = " ".join(block.splitlines())
			children_nodes.append(ParentNode('p', txt_to_children(normalized)))
		elif type_block == BlockType.HEADING:
			heading = block.count("#")
			children_nodes.append(ParentNode(f'h{heading}', txt_to_children(block)))
		elif type_block == BlockType.QUOTE:
			children_nodes.append(ParentNode("blockquote", txt_to_children(block)))
		elif type_block == BlockType.ORDERED_LIST:
			list_nodes = []
			li = list_items(block)

			for item in li:
				list_nodes.append(ParentNode("li", txt_to_children(item)))
			children_nodes.append(ParentNode("ol", list_nodes))
		elif type_block == BlockType.UNORDERED_LIST:
			list_nodes = []
			li = list_items(block)
			for item in li:
				list_nodes.append(ParentNode("li", txt_to_children(item)))
			children_nodes.append(ParentNode("ul", list_nodes))
		elif type_block == BlockType.CODE:
			lines = block.split("\n")
			if len(lines)>1 and lines[0].startswith("```") and lines[-1].endswith("```"):
				inner = "\n".join(lines[1:-1]) + "\n"
			else:
				inner = block if block.endswith("\n") else block + "\n"

			node = TextNode(inner, TextType.CODE)

			node = text_node_to_html_node(node)
			children_nodes.append(ParentNode("pre", [node]))

	return ParentNode("div", children_nodes)









