import os

def kebab_to_snake(name):
    return name.replace('-', '_')

def rename_all(base_path):
    # Go bottom-up to rename files and folders safely
    for root, dirs, files in os.walk(base_path, topdown=False):
        # Rename files first
        for name in files:
            if '-' in name:
                old_path = os.path.join(root, name)
                new_name = kebab_to_snake(name)
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed file: {old_path} -> {new_path}")

        # Rename folders second
        for name in dirs:
            if '-' in name:
                old_path = os.path.join(root, name)
                new_name = kebab_to_snake(name)
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed folder: {old_path} -> {new_path}")

if __name__ == "__main__":
    base_folder = r"/d/developer/pylang/harry-playbook"
    rename_all(base_folder)
    print("✅ All kebab-case names changed to snake_case.")
