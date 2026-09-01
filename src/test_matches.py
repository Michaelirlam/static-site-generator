import unittest
from matches import extract_markdown_images, extract_markdown_links

class TestMatches(unittest.TestCase):
    def test_extract_markdown_images_match_single(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_match_multiple(self):
        matches = extract_markdown_images(
            "This is text with an ![image1](https://i.imgur.com/zjjcJKZ.png) and ![image2](https:i.imgur/abcdeFGH.png)"
        )
        self.assertListEqual([("image1", "https://i.imgur.com/zjjcJKZ.png"), ("image2", "https:i.imgur/abcdeFGH.png")], matches)

    def test_extract_markdown_images_no_match(self):
        matches = extract_markdown_images(
            "This is text with no match"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_links_match_single(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_markdown_links_match_multiple(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
    
    def test_extract_markdown_links_no_match(self):
        matches = extract_markdown_links(
            "This is text with no match"
        )
        self.assertListEqual([], matches)
    

    