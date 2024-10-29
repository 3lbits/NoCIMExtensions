import subprocess
import re
import os
import time

def run_bash_command(command, commandName):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{commandName} executed successfully.")
        print(result.stdout)
    else:
        print(f"{commandName} failed.")
        print(result.stderr)

def to_camel_case(snake_str: str):
    if not re.match(r'^[a-z]+(_[a-z]+)*$', snake_str):
        return print("Warning: Input string is not in snake_case format")

    components = snake_str.split('_')
    return ''.join(x.title() for x in components)

def remove_all_md_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Removed {file_path}")
                except Exception as e:
                    print(f"Failed to remove {file_path}: {e}")
    print("All .md files removed successfully.")

# def is_file_ready(file_path):
#     """Check if the file is ready by trying to open it."""
#     try:
#         with open(file_path, 'a'):
#             return True
#     except PermissionError:
#         return False

# def wait_until_file_is_ready(file_path, timeout=30):
#     """Wait until the file is ready or the timeout is reached."""
#     start_time = time.time()
#     while time.time() - start_time < timeout:
#         if is_file_ready(file_path):
#             return True
#         time.sleep(0.5)  # Wait for 0.5 seconds before retrying
#     return False

# # Replace grep command with Python logic
# def remove_files_matching_pattern(directory, pattern):
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.endswith(".md"):
#                 file_path = os.path.join(root, file)
#                 # Check if file is ready
#                 if wait_until_file_is_ready(file_path):
#                     with open(file_path, "r") as f:
#                         content = f.read()
#                         if re.search(pattern, content):
#                             print(f"Removing {file_path}")
#                             os.remove(file_path)
#                 else:
#                     print(f"File {file_path} was not ready within the timeout period.")
#     print("Removing files executed successfully.")

# # Pattern to match
# pattern = r"^# (Slot|Type): "
# # Run the function
# remove_files_matching_pattern("docs", pattern)