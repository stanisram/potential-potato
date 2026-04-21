import os
from block_markdown import markdown_to_html_node # Assumes your parser location

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read files
    with open(from_path, "r") as f:
        markdown_content = f.read()
    with open(template_path, "r") as f:
        template = f.read()

    # Convert Markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # Get Title
    title = extract_title(markdown_content)

    # Replace placeholders
    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    # Ensure destination directory exists
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    # Write to file
    with open(dest_path, "w") as f:
        f.write(full_html)



def extract_title(markdown):
    """
    Finds the first H1 header in a markdown string.
    Example: "# My Title" -> "My Title"
    """
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No h1 header found in markdown")

