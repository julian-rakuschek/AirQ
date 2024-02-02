import os
from pathlib import Path

def list_directory_hierarchy(root_path, output_file):
    with open(output_file, 'w') as file:
        for foldername, subfolders, filenames in os.walk(root_path):
            foldername = foldername.replace(root_path, '')  # Make paths relative to the root
            file.write(f"Folder: {foldername}\n")
            for subfolder in subfolders:
                file.write(f"  - Subfolder: {subfolder}\n")
            for filename in filenames:
                file.write(f"  - File: {filename}\n")

if __name__ == "__main__":
    root_path = str(Path(__file__).parents[0])
    output_file = "directory_hierarchy.txt"

    list_directory_hierarchy(root_path, output_file)
    print(f"Directory hierarchy saved to {output_file}")
