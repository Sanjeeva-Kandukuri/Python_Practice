import os
print("Current Directory:", os.getcwd())
if not os.path.exists("example_folder"):
    os.mkdir("example_folder")