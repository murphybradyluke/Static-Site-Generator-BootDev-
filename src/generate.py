from block_take2 import markdown_to_html_node
import os
from pathlib import Path


def extract_title(markdown: str):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line.split("# ", 1)
            return title[1]
    raise Exception("No header in provided file")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r', encoding='utf-8') as f:
        from_path_content = f.read()
    with open(template_path, 'r', encoding='utf-8') as f:
        template_path_content = f.read()
    html_string = markdown_to_html_node(from_path_content).to_html()
    title = extract_title(from_path_content)
    new_title = template_path_content.replace("{{ Title }}", title)
    new_content = new_title.replace("{{ Content }}", html_string)

    dirname = os.path.dirname(dest_path)
    os.makedirs(dirname, exist_ok=True)
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    src = os.listdir(dir_path_content)
    for item in src:
        joined_src = os.path.join(dir_path_content, item)
        if os.path.isfile(joined_src):
            print(f"Generating page from {joined_src} to {dest_dir_path} using {template_path}")
            with open(joined_src, 'r', encoding='utf-8') as f:
                from_path_content = f.read()
            with open(template_path, 'r', encoding='utf-8') as f:
                template_path_content = f.read()
            html_string = markdown_to_html_node(from_path_content).to_html()
            title = extract_title(from_path_content)
            new_title = template_path_content.replace("{{ Title }}", title)
            new_content = new_title.replace("{{ Content }}", html_string)
            new_content.replace('href="/', f'href="{basepath}')
            new_content.replace('src="/', f'src="{basepath}')
            dirname = os.path.dirname(dest_dir_path)
            os.makedirs(dirname, exist_ok=True)
            to_rename = os.path.join(dest_dir_path, item)
            renamed = Path(to_rename).with_suffix(".html")
            with open(renamed, 'w', encoding='utf-8') as f:
                f.write(new_content)
        else:
            new_dst = os.path.join(dest_dir_path, item)
            if not os.path.exists(new_dst):
                os.mkdir(new_dst)
            generate_pages_recursive(joined_src, template_path, new_dst, basepath)
