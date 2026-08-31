from textnode import TextNode, TextType

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