import unittest

# Adjust these imports to your project
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter  # e.g., where you defined the function


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_single_code_span_split(self):
        old = [TextNode("This has `code` inside.", TextType.TEXT)]
        new = split_nodes_delimiter(old, "`", TextType.CODE)
        self.assertEqual(
            new,
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" inside.", TextType.TEXT),
            ],
        )


    def test_single_bold_split(self):
        old = [TextNode("This has **code** inside.", TextType.TEXT)]
        new = split_nodes_delimiter(old, "**", TextType.BOLD)
        self.assertEqual(
            new,
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("code", TextType.BOLD),
                TextNode(" inside.", TextType.TEXT),
            ],
        )

    """
    
    def test_old_multi(self):
        old = [TextNode("This has `code` inside.", TextType.TEXT),TextNode("This is **bold** text.", TextType.TEXT), TextNode("This has *italic* text.", TextType.TEXT)]
        first = split_nodes_delimiter(old, "`", TextType.CODE)
        second = split_nodes_delimiter(first, "**", TextType.BOLD)
        last = split_nodes_delimiter(second, "*", TextType.ITALIC)
        self.assertEqual(
            last,
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" inside.", TextType.TEXT),
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode("text.", TextType.TEXT),
                TextNode("This has ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode("text.", TextType.TEXT),
                
            ],
        )
    
    """

    

if __name__ == "__main__":
    unittest.main(verbosity=2)
