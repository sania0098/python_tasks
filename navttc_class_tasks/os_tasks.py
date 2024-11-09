# import os
#
#
# def find(path, dir_name):
#     for root, dirs, files in os.walk(path):
#
#         if dir_name in dirs:
#             abspath =os.path.join(root, dir_name)
#             print(abspath)
#
# find("./tree", "python")
###################################FIND NUMBER OF DIRECTORIES AND FILES
import os


def count_files_and_directories(path):
    num_files = 0
    num_dirs = 0

    # os.walk() generates the file names in a directory tree
    for root, dirs, files in os.walk(path):
        num_dirs += len(dirs)  # Count the number of directories
        num_files += len(files)  # Count the number of files

    return num_files, num_dirs


# Example usage
path = input("Enter the path: ")

if os.path.exists(path):
    files, dirs = count_files_and_directories(path)
    print(f"Number of files: {files}")
    print(f"Number of directories: {dirs}")
else:
    print("The provided path does not exist.")

##########################DELETE ALL EMPTY DIRECTORIES IN A GIVEN PATH













