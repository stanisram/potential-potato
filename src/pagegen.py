import os
from utils import extract_title
from block_markdown import markdown_to_html_node # Adjust this import to wherever your markdown parsing logic lives

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # 1. Read the markdown file
    with open(from_path, "r") as f:
        markdown_content = f.read()

    # 2. Read the template file
    with open(template_path, "r") as f:
        template_content = f.read()

    # 3. Convert markdown to HTML string
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # 4. Extract the title
    title = extract_title(markdown_content)

    # 5. Replace placeholders
    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)

    # 6. Create directories if they don't exist
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    # 7. Write the full HTML to the destination file
    with open(dest_path, "w") as f:
        f.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """Recursively generate HTML pages from markdown files in content directory."""
    # List all entries in the content directory
    for entry in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, entry)
        
        if os.path.isfile(from_path):
            # If it's a file and ends with .md, generate the corresponding HTML
            if entry.endswith(".md"):
                # Replace .md with .html
                html_filename = entry.replace(".md", ".html")
                dest_path = os.path.join(dest_dir_path, html_filename)
                generate_page(from_path, template_path, dest_path)
        elif os.path.isdir(from_path):
            # If it's a directory, recurse into it
            dest_subdir = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(from_path, template_path, dest_subdir)