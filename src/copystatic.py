import os
import shutil

def copy_files_recursive(source_dir, dest_dir):
    # 1. Clean the destination if it exists
    if os.path.exists(dest_dir):
        print(f"Cleaning destination directory: {dest_dir}")
        shutil.rmtree(dest_dir)
    
    # 2. Create the destination directory fresh
    os.mkdir(dest_dir)

    # 3. List everything in the source
    if not os.path.exists(source_dir):
        raise Exception(f"Source directory {source_dir} does not exist!")

    nodes = os.listdir(source_dir)

    for node in nodes:
        source_path = os.path.join(source_dir, node)
        dest_path = os.path.join(dest_dir, node)
        
        print(f" * {source_path} -> {dest_path}")

        if os.path.isfile(source_path):
            # Base Case: It's a file, just copy it
            shutil.copy(source_path, dest_path)
        else:
            # Recursive Step: It's a directory, create it and call self
            # We don't rmtree here because we want to preserve the tree we're building
            os.mkdir(dest_path)
            copy_internal(source_path, dest_path)

def copy_internal(source, dest):
    """Helper to handle recursion without re-deleting the root 'public' folder"""
    for node in os.listdir(source):
        s_path = os.path.join(source, node)
        d_path = os.path.join(dest, node)
        print(f" * {s_path} -> {d_path}")
        
        if os.path.isfile(s_path):
            shutil.copy(s_path, d_path)
        else:
            os.mkdir(d_path)
            copy_internal(s_path, d_path)