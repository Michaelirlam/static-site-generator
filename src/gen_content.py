from blocks import markdown_to_blocks
from markdown_to_html_node import heading_type, markdown_to_html_node
import os
from pathlib import Path

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    header = [block for block in blocks if block.startswith("# ")]
    if header == []:
        raise Exception("No h1 in this markdown.")
    return heading_type(header[0])[1]

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dir_path_content = Path(dir_path_content)
    dest_dir_path = Path(dest_dir_path)

    for item in dir_path_content.iterdir():
        if item.is_file():
            dest_dir_path.mkdir(parents=True, exist_ok=True)
            new_item = item.with_suffix(".html")
            dest = dest_dir_path / new_item.name
            generate_page(item, template_path, dest, basepath)
        else:
            dest = dest_dir_path / item.name
            dest.mkdir(parents=True, exist_ok=True)
            generate_pages_recursive(item, template_path, dest, basepath)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} {template_path}!")
    with open(from_path) as markdown:
        content = markdown.read()
    with open(template_path) as boiler_plate:
        template = boiler_plate.read()
    html_nodes = markdown_to_html_node(content)
    content_html = html_nodes.to_html()
    title = extract_title(content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content_html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    destination = os.path.dirname(dest_path)
    os.makedirs(destination, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template)