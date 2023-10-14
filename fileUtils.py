import os
from shutil import move

# Python script to sort files in a directory by their extension
""" This Python script organizes files in a directory by sorting them into subdirectories 
    based on their file extensions. It identifies the file extension and moves the file 
    to the appropriate subdirectory. This can be useful for decluttering your downloads folder 
    or organizing files for a specific project
"""


def sort_files(directory_path):
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            file_extension = filename.split('.')[-1]
            destination_directory = os.path.join(directory_path, file_extension)
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            move(os.path.join(directory_path, filename), os.path.join(destination_directory, filename))


# Python script to remove empty folders in a directory
""" This Python script searches for and deletes empty folders within a specified directory. 
    It can help you maintain a clean and tidy folder structure, especially when dealing with 
    large sets of data
"""


def remove_empty_folders(directory_path):
    for root, dirs, _ in os.walk(directory_path, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)


# Python script to rename multiple files in a directory
""" This Python script allows you to rename multiple files in a directory simultaneously. 
    It takes the old name and the new name as inputs and replaces the old name with the new one 
    for all the files that match the specified criteria.
"""


def rename_files(directory_path, old_name, new_name):
    for filename in os.listdir(directory_path):
        if old_name in filename:
            new_filename = filename.replace(old_name, new_name)
            os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))
