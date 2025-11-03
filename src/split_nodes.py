from textnode import TextNode, TextType

from regx_func import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_node = []
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_node.append(node)
		else:
			if delimiter not in node.text:
				new_node.append(node)
			else:
				old_s = node.text.split(delimiter)
				new_node_l = [TextNode(old_s[0], TextType.TEXT),TextNode(old_s[1], text_type), TextNode(old_s[2], TextType.TEXT)]
				new_node.extend(new_node_l)
	return new_node


def split_nodes_image(old_nodes):
	new_node = []
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_node.append(node)
		else:
			original = node.text
			ex = extract_markdown_images(original)
			for alt,link in ex:
				before,after = original.split(f"![{alt}]({link})", 1)

				if before:
					new_node.append(TextNode(before, TextType.TEXT))

				new_node.append(TextNode(alt, TextType.IMAGE, link))

				original = after

			if original:
				new_node.append(TextNode(original, TextType.TEXT))

	return new_node


def split_nodes_link(old_nodes):
	new_node = []
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_node.append(node)
		else:
			original = node.text
			ex = extract_markdown_links(original)
			for alt,link in ex:
				before,after = original.split(f"[{alt}]({link})", 1)

				if before:
					new_node.append(TextNode(before, TextType.TEXT))

				new_node.append(TextNode(alt, TextType.LINK, link))

				original = after

			if original:
				new_node.append(TextNode(original, TextType.TEXT))


	return new_node


def text_to_textnodes(text):
	nodes = TextNode(text, TextType.TEXT)

	
	nodes = split_nodes_image([nodes])
	nodes = split_nodes_link(nodes)
	nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
	nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
	nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)


	return nodes
