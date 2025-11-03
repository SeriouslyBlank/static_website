import re


def extract_markdown_images(text):
	img_text = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
	return img_text


def extract_markdown_links(text):
	link_text = re.findall(r"\[(.*?)\]\((.*?)\)", text)

	return link_text

