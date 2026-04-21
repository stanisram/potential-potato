from textnode import TextNode, TextType
from copystatic import copy_files_recursive
from utils import extract_title
from pagegen import generate_pages_recursive


def main():
    print("Copying static files...")
    copy_files_recursive("static", "public")
    
    print("Generating content...")
    generate_pages_recursive(
        "content",
        "template.html",
        "public"
    )

if __name__ == "__main__":
    main()