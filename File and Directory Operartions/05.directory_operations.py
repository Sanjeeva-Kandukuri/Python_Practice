# 6.1 Creating a Directory

import os
os.mkdir("new_folder")


# Creating Nested Directories

os.makedirs("parent_folder/child_folder")


# 6.2 Checking if a Directory Exists

import os
if not os.path.exists("new_folder"):
    os.mkdir("new_folder")
    print("Folder Created!.")
else:
    print("Folder already exists.")


# 6.3 Removing a Directory

import os
os.rmdir("new_folder")   # Removes an empty directory

# Removing a Non-Empty Directory

import shutil
shutil.rmtree("parent_folder") # Deletes folder and all its contents


# Best Practice

# Before deleting a folder, check whether it exists:

import os
import shutil

folder = "parent-folder"

if os.path.exists(folder):
    shutil.rmtree(folder)
    print("Folder deleted!.")
else:
    print("Folder does not exist.")


# 6.4 Listing Files in a Directory

import os
files = os.listdir(".")
for file in files:
    print(files)


# 6.5 Changing the Current Working Directory

import os

os.chdir("path/to/directory")
print("Currrent Directory:", os.getcwd())


# 7. Real-World Example: Logging System

def log_activity(activity):
    with open("log.txt", "a") as log_file:
        log_file.write(activity + "\n")

        print(activity)

log_activity("User logged in.")
log_activity("User uploaded a file.")



# 8. Real-World Example: Organizing Files by Type
import os
import shutil

def organize_files(folder):
    if not os.path.exists(os.path.join(folder, "Images")):
        os.mkdir(os.path.join(folder, "images"))
    if not os.path.exists(os.path.join(folder, "Documents")):
        os.mkdir(os.path.join(folder, "Documents"))


    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            if file.endswith(".jpg"):
                shutil.move(file_path, os.path.join(folder, "Images", file))

            elif file.endswith(".pdf"):
                shutil.move(file_path, os.path.join(folder, "Documents", file))

organize_files("C:/Users/ksanj/Downloads")
