import unittest


from blocktype import BlockType, block_to_block_type
from split_nodes import markdown_to_blocks

markdown = """
This is **bolded** paragraph    

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
- item last

1. ordered list
2. item 2
3. item 3

> quote check
> check
> check

```
code
more code
last code
```

# headinggggggggg
## headingggg
### heading
#### heading

lel another para or is it?
"""

result = markdown_to_blocks(markdown)

class TestBlocktoblockjtype(unittest.TestCase):
	def test_block_to_type(self):
		para = block_to_block_type(result[0])
		para_2 = block_to_block_type(result[1])
		para_3 = block_to_block_type(result[7])

		ul = block_to_block_type(result[2])

		ol = block_to_block_type(result[3])

		quo = block_to_block_type(result[4])

		code = block_to_block_type(result[5])

		head = block_to_block_type(result[6])




		self.assertEqual(
			para,
			BlockType.PARAGRAPH,
		)

		self.assertEqual(
			para_2,
			BlockType.PARAGRAPH,
		)
		self.assertEqual(
			para_3,
			BlockType.PARAGRAPH,
		)

		self.assertEqual(
			ul,
			BlockType.UNORDERED_LIST,
		)

		self.assertEqual(
			ol,
			BlockType.ORDERED_LIST,
		)

		self.assertEqual(
			quo,
			BlockType.QUOTE,
		)
		self.assertEqual(
			head,
			BlockType.HEADING,
		)
		self.assertEqual(
			code,
			BlockType.CODE,
		)


		



if __name__ == "__main__":
    unittest.main(verbosity=2)
