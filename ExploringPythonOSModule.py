# 1. Exploring Python's OS Module
"""
Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

Task 1: Directory Inspector:

Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.

Code Example:
    import os

    def list_directory_contents(path):
        # List and print all files and subdirectories in the given path
Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. Handle exceptions for invalid paths or inaccessible directories.

"""

import os

def list_directory_contents(path, level = 0):
    try:
        indent = ' ' * (level * 2)
        with os.scandir(path) as files:
            files_list = list(files)
            files_list.sort(key=lambda f: f.name.lower())
            for file in files_list:
                print(f"{indent}- File: {file.name}")
        with os.scandir(path) as entries:
            entries_list = list(entries)
            entries_list.sort(key=lambda e: e.name.lower())
            for entry in entries_list:
                if entry.is_dir():
                    print(f"\n{indent}~ Sub-Directory: {entry.name} ~")
                    list_directory_contents(entry.path, level + 1)
            
    except FileNotFoundError:
        print(f"The directory {path} was not found.")
    except PermissionError:
        print(f"You don't have access to {path}.")
    except OSError as e:
        print(f"Error accessing {path}: {e}")

def directory_inspector():
    def menu():
        print("\n.~* Directory Inspector *~.")
        print("1. List Contents of Directory")
        print("2. Exit")
        user_input = input("Enter your choice: ")
        try:
            choice = int(user_input)
        except ValueError:
            print("\nThat is not a valid choice. Please enter the digit that corresponds with your selection.")
            menu()
        else:
            if choice == 1:
                path = input("\nEnter the path of the directory to list contents: ")
                print("* Directory Contents: *")
                list_directory_contents(path)
                menu()
            elif choice == 2:
                print("\nThank you for using Directory Inspector!")
            else:
                print("Invalid choice. Please try again.")
                menu()
    try:
        menu()
    finally:
        print("Exiting program...")

if __name__ == "__main__":
    directory_inspector()