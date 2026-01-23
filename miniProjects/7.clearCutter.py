'''
Write a program to clear the clutter inside a folder on your computer.
You should use os module to rename all the png images frin 1.png all the way
till n.png where n is the number of png files in that folder.
Do the same for other file formats like .jpg, .pdf, .txt etc.
'''

import os

def clear_clutter(folder_path):

    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return
    
    files = os.listdir(folder_path)

    counts = {}

    for file in files:
        full_path = os.path.join(folder_path, file)

        if os.path.isdir(full_path):
            continue

        name, ext = os.path.splitext(file)

        if ext == "":
            continue

        ext

        if ext not in counts:
            counts[ext] = 1

        new_name = f"{counts[ext]}{ext}"
        new_path = os.path.join(folder_path, new_name)

        while os.path.exists(new_path):
            counts[ext] += 1
            new_name = f"{counts[ext]}{ext}"
            new_path = os.path.join(folder_path, new_name)

        os.rename(full_path, new_path)
        print(f"Renamed: {file} -> {new_name}")
        counts[ext] += 1

# Example usage:
folder = input("Enter the folder path to clear clutter: ")
clear_clutter(folder)