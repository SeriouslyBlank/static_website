from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_node = []
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_node.extend(node)
		else:
			if delimiter not in node.text:
				raise Exception("delimiter not found in text, invalid markdown syntax")
			old_s = node.text.split(delimiter)
			new_node_l = [TextNode(old_s[0], TextType.TEXT),TextNode(old_s[1], text_type), TextNode(old_s[2], TextType.TEXT)]
			new_node.extend(new_node_l)
	return new_node

