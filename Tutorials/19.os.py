'''
os module allows python to do tasks like:
create/delete folders and files,
rename file,
list files,
check file/folder existence,
read environment variables, etc.
'''

import os

# Get current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# List files and directories in the current directory
items = os.listdir(cwd)
print("Items in Directory:", items)

# Create a new directory
# new_dir = "test_dir"
# os.mkdir(new_dir)
# print(f"Directory '{new_dir}' created.")
# os.makedirs("A/B/C")
# print("Nested directories 'A/B/C' created.")

# os.rmdir("test_dir")   # only removes empty folder
# os.removedirs("A/B/C")
print("Directories removed.")

# Rename a file
# os.rename("old_name.txt", "new_name.txt")

# Check if a file or directory exists
# exists = os.path.exists("new_name.txt")   
# print("Does 'new_name.txt' exist?", exists)

# Get environment variables
# path_var = os.getenv("PATH")
# print("PATH Environment Variable:", path_var)

