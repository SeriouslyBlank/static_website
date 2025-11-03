from enum import Enum

class BlockType(Enum):
	PARAGRAPH = "paragraph"
	HEADING = "heading"
	CODE = "code"
	QUOTE = "quote"
	UNORDERED_LIST = "ul"
	ORDERED_LIST = "ol"



def block_to_block_type(block):
	lines = block.split("\n")
	if len(lines)>1 and lines[0].startswith("```") and lines[-1].endswith("```"):
		return BlockType.CODE
	if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
		return BlockType.HEADING

	ul = True
	ol = True
	quo = True
	for i in range(len(lines)):
		if not lines[i].startswith("- "):
			ul = False
		if not lines[i].startswith(f"{i+1}. "):
			ol = False
		if not lines[i].startswith("> "):
			quo = False

	if ul == True:
		return BlockType.UNORDERED_LIST
	elif ol == True:
		return BlockType.ORDERED_LIST
	elif quo == True:
		return BlockType.QUOTE
	else:
		return BlockType.PARAGRAPH		


