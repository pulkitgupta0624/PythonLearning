'''
Shutil : shell utilities
It is used for high level file and folder operations like:
- copy files
- move files
- delete folders
- archive (zip)
- disk usage
'''

import shutil

# copy a file
# shutil.copy('source.txt', 'destination.txt')  # copies source.txt to destination.txt

# copy with metadata
# shutil.copy2('source.txt', 'destination_with_metadata.txt')   

# move a file
# shutil.move('file_to_move.txt', 'new_location/file_to_move.txt')

# delete a folder
# shutil.rmtree('folder_to_delete')

# create a zip archive
# shutil.make_archive('archive_name', 'zip', 'folder_to_archive')

# extract a zip archive
# shutil.unpack_archive('archive_name.zip', 'extracted_folder')

# get disk usage statistics
total, used, free = shutil.disk_usage("/")
print(f"Total: {total // (2**30)} GiB")
print(f"Used: {used // (2**30)} GiB")
print(f"Free: {free // (2**30)} GiB")

# which command exists on system
path = shutil.which("python")
print(f"Python executable is located at: {path}")