# Example script: batch_rename_configs.py
import os

# Get directory and prefix from user
target_dir = input("Enter the directory containing files to rename: ").strip()
prefix = input("Enter the prefix to add to each file: ").strip()

if not os.path.isdir(target_dir):
    print(f"Directory not found: {target_dir}")
else:
    for filename in os.listdir(target_dir):
        old_path = os.path.join(target_dir, filename)
        if os.path.isfile(old_path):
            # Construct new name with prefix
            new_filename = prefix + filename
            new_path = os.path.join(target_dir, new_filename)
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")
            except Exception as e:
                print(f"Failed to rename {filename}: {e}")
