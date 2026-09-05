import re

def extract_markdown_images(text):
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_unordered_list(text):
    matches = re.findall(r"^-\s+(.*)$", text, re.MULTILINE)
    return matches

def extract_markdown_ordered_list(text):
    matches = re.findall(r"^\d+\.\s+(.*)$", text, re.MULTILINE)
    return matches