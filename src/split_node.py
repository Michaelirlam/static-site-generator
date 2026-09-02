from textnode import TextNode, TextType
from matches import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes:list[TextNode], delimiter:str, text_type:TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            split_node = node.text.split(delimiter)
            if len(split_node) % 2 == 0:
                raise Exception("This is not valid Markdown syntax.")
            else:
                for i in range(len(split_node)):
                    if split_node[i] == "":
                        continue
                    if i % 2 == 0:
                        new_node = TextNode(split_node[i], TextType.TEXT)
                        new_nodes.append(new_node)
                    else:
                        new_node = TextNode(split_node[i], text_type)
                        new_nodes.append(new_node)
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text == "":
            continue
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        elif extract_markdown_images(node.text) == []:
            new_nodes.append(node)
        else:
            image_tuples = extract_markdown_images(node.text)
            remaining_text = node.text
            for image in image_tuples:
                alt_text, url = image[0], image[1]
                split = remaining_text.split(f"![{alt_text}]({url})", 1)
                if split[0] != "":
                    text_node = TextNode(split[0], TextType.TEXT)
                    new_nodes.append(text_node)
                image_node = TextNode(alt_text, TextType.IMAGE, url)
                new_nodes.append(image_node)
                remaining_text = split[1]
            if len(remaining_text) != 0:
                text_node = TextNode(remaining_text, TextType.TEXT)
                new_nodes.append(text_node)
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text == "":
            continue
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        elif extract_markdown_links(node.text) == []:
            new_nodes.append(node)
        else:
            link_tuples = extract_markdown_links(node.text)
            remaining_text = node.text
            for link in link_tuples:
                alt_text, url = link[0], link[1]
                split = remaining_text.split(f"[{alt_text}]({url})", 1)
                if split[0] != "":
                    text_node = TextNode(split[0], TextType.TEXT)
                    new_nodes.append(text_node)
                link_node = TextNode(alt_text, TextType.LINK, url)
                new_nodes.append(link_node)
                remaining_text = split[1]
            if len(remaining_text) != 0:
                text_node = TextNode(remaining_text, TextType.TEXT)
                new_nodes.append(text_node)
    return new_nodes