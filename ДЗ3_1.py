import os
import sys
import shutil

def copy_and_sort(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Walk through the source directory recursively
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Get the full path of the file
            source_file_path = os.path.join(root, file)
            # Get the extension of the file
            _, file_extension = os.path.splitext(file)
            # Define the destination subdirectory based on the file extension
            destination_subdir = os.path.join(destination_dir, file_extension[1:])
            # Create the subdirectory if it doesn't exist
            if not os.path.exists(destination_subdir):
                os.makedirs(destination_subdir)
            # Define the destination file path
            destination_file_path = os.path.join(destination_subdir, file)
            try:
                # Copy the file to the destination directory
                shutil.copy2(source_file_path, destination_file_path)
                print(f"Successfully copied '{source_file_path}' to '{destination_file_path}'")
            except Exception as e:
                print(f"Failed to copy '{source_file_path}' to '{destination_file_path}': {e}")

if __name__ == "__main__":
    # Check if both source directory and destination directory are provided as command line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    # If destination directory is not provided, use 'dist' as default
    if not destination_directory:
        destination_directory = 'dist'

    copy_and_sort(source_directory, destination_directory)