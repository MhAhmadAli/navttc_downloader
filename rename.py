import os
import re
from urllib.parse import unquote

def rename_files():
    # Get the downloads directory path
    downloads_dir = 'downloads'
    
    # Ensure the directory exists
    if not os.path.exists(downloads_dir):
        print(f"Error: {downloads_dir} directory not found!")
        return
    
    # Get all files in the directory
    files = os.listdir(downloads_dir)
    
    # Counter for renamed files
    renamed_count = 0
    
    # Process each file
    for filename in files:
        # Skip if it's a directory
        if os.path.isdir(os.path.join(downloads_dir, filename)):
            continue
            
        # Decode URL-encoded characters
        new_filename = unquote(filename)
        
        # If the filename has changed, rename it
        if new_filename != filename:
            old_path = os.path.join(downloads_dir, filename)
            new_path = os.path.join(downloads_dir, new_filename)
            
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")
                renamed_count += 1
            except OSError as e:
                print(f"Error renaming {filename}: {str(e)}")
    
    print(f"\nRenaming complete! {renamed_count} files renamed.")

if __name__ == "__main__":
    rename_files()
