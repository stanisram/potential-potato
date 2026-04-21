import sys
from textnode import TextNode, TextType
from copystatic import copy_files_recursive
from utils import extract_title
from pagegen import generate_pages_recursive


def main():
    # Get basepath from CLI argument, default to "/"
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    print(f"Building site with basepath: {basepath}")
    print("Copying static files...")
    copy_files_recursive("static", "docs")
    
    print("Generating content...")
    generate_pages_recursive(
        "content",
        "template.html",
        "docs",
        basepath
    )

if __name__ == "__main__":
    main()