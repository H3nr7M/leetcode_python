import os
import random

def select_random_folder(current_path):
    # Get all folders in the directory
    folders = [f for f in os.listdir(current_path) if os.path.isdir(os.path.join(current_path, f))]
    # Choose a random folder
    random_folder = random.choice(folders)
    return random_folder

def select_random_file(folder_path):
    # Get all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    # Choose a random file
    random_file = random.choice(files)
    return random_file

if __name__ == "__main__":
    # folder_path = input("Enter the path of the folder: ")
    folder_path = os.path.join(os.getcwd(), select_random_folder(os.getcwd()))
    random_file = select_random_file(folder_path)
    print('\n')
    print("Selected random file:", random_file, "from folder:", os.path.basename(folder_path))
