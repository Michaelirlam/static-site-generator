from textnode import TextNode, TextType

def main():
    text_node = TextNode("hello world", TextType.BOLD, "https://www.boot.dev")
    print(text_node)

main()