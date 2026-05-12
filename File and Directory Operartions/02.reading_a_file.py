# 2. Reading a File

file = open("example.txt")
content = file.resd()
lines = file.readlines()
line = file.readline()
print(content)
file.close()

# This is the best and safest way to handle files in Python. 🎉

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
