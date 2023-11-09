import os

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
    root_path = "C:\\Users\\erank\\Documents\\TUG\\PRESENT\\AirQ_Seminarraum\\f08112023\\2023.uncrypt"  # Replace with the directory you want to analyze
    output_file = "directory_hierarchy.txt"

    list_directory_hierarchy(root_path, output_file)
    print(f"Directory hierarchy saved to {output_file}")
