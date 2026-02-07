# Write a program to print the contents of a directory using the os module. Search online for the function which does that. 
import os

# Specify the directory you want to list
# Use '.' for current directory
directory = "."

try:
    # os.listdir() returns a list of entries in the directory
    files = os.listdir(directory)

    print(f"Contents of directory '{directory}':")
    for file in files:
        print(file)

except FileNotFoundError:
    print(f"The directory {directory} does not exist.")
except PermissionError:
    print(f"Permission denied to access {directory}.")
