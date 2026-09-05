from blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from matches import extract_markdown_unordered_list, extract_markdown_ordered_list
from split_node import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        html_node = block_type_to_html_node(block)
        html_nodes.append(html_node)
    div_node = ParentNode(tag="div", children=html_nodes)
    return div_node

def block_type_to_html_node(block:str) -> HTMLNode:
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        block = block.split("\n")
        block = " ".join(block)
        children = text_to_children(block)
        return ParentNode(tag="p", children=children)
    elif block_type == BlockType.HEADING:
        tag, value = heading_type(block)
        children = text_to_children(value)
        return ParentNode(tag=tag, children=children)
    elif block_type == BlockType.QUOTE:
        lines = block.split("\n")
        block = []
        for line in lines:
            line = line[1:].strip()
            block.append(line)
        block = " ".join(block)
        children = text_to_children(block)
        return ParentNode(tag="blockquote", children=children)
    elif block_type == BlockType.CODE:
        lines = block.split("\n")
        lines = lines[1:-1]
        code = "\n".join(lines)
        code = code + "\n"
        code_node = LeafNode(tag="code", value=code)
        parent_node = ParentNode(tag="pre", children=[code_node])
        return parent_node        
    elif block_type == BlockType.UNORDERED_LIST:
        return split_unordered_list(block)
    elif block_type == BlockType.ORDERED_LIST:
        return split_ordered_list(block)

def text_to_children(block: str) -> list[LeafNode]:
    text_nodes = text_to_textnodes(block)
    return [text_node_to_html_node(text_node) for text_node in text_nodes]

def heading_type(block: str) -> tuple[str, str]:
    if block.startswith("# "):
        return ["h1", block[2:]]
    elif block.startswith("## "):
        return ["h2", block[3:]]
    elif block.startswith("### "):
        return ["h3", block[4:]]
    elif block.startswith("#### "):
        return ["h4", block[5:]]
    elif block.startswith("##### "):
        return ["h5", block[6:]]
    elif block.startswith("###### "):
        return ["h6", block[7:]]

def split_unordered_list(block: str) -> ParentNode:
    list_elements = extract_markdown_unordered_list(block)
    unordered_children = []
    for i in list_elements:
        children = text_to_children(i)
        parent = ParentNode(tag="li", children=children)
        unordered_children.append(parent)
    unordered_parent = ParentNode(tag="ul", children=unordered_children)
    return unordered_parent

def split_ordered_list(block: str) -> ParentNode:
    list_elements = extract_markdown_ordered_list(block)
    ordered_children = []
    for i in list_elements:
        children = text_to_children(i)
        parent = ParentNode(tag="li", children=children)
        ordered_children.append(parent)
    ordered_parent = ParentNode(tag="ol", children=ordered_children)
    return ordered_parent