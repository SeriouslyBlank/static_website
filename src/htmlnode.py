
class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = {}
		if props != None:
			self.props[tag] = value
			self.props.update(props)
		else:
			self.props[tag] = value
		

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



