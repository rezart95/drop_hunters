import os

def generate_tree(startpath, show_files=True, exclude_dirs=None, exclude_files=None):
    if exclude_dirs is None:
        exclude_dirs = []
    if exclude_files is None:
        exclude_files = []

    for root, dirs, files in os.walk(startpath):
        # Exclude specified directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}|-- {os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        
        if show_files:
            # Exclude specified files
            for f in files:
                if f not in exclude_files:
                    print(f"{subindent}|-- {f}")

if __name__ == "__main__":
    # Replace '.' with the path of your app if this script is not in the root of your app
    generate_tree(
        '.', 
        show_files=True,
        exclude_dirs=['venv', '.vscode', 'temp', 'temp_images', '__pycache__', '.git', 'downloaded_images'],  # Exclude these directories
        exclude_files=['.dockerignore', '.env', '.gitignore', 'commands.txt']  # Exclude these files
    )