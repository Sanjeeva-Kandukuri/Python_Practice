# 5.1 Using os.path.join() for Cross-Platform Compatibility

import os
file_path = os.path.join("folder", "example.txt")
with open(file_path, "r") as file:
    print(file.read())


# 5.2 Getting File Information

import os 
file_path = "example.txt"
if os.path.exists(file_path):
    print("File Size:", os.path.getsize(file_path), "bytes")
    print("Absolute Path:", os.path.abspath(file_path))

else:
    print("File does not exist.")

