import os

current_directory = os.getcwd()
print("Current Directory:", current_directory)

file_path = os.path.join(current_directory, "Example1.txt")
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        print("File Content:\n", file.read())

else:
    print("Current File does not exist")