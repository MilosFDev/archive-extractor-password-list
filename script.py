import os
import py7zr

def extract_7z_archive(archive_path, password):
    try:
        with py7zr.SevenZipFile(archive_path, mode='r', password=password) as szf:
            szf.extractall()
        return True
    except py7zr.Bad7zFile:
        return False

def automate_extraction(archive_path, password_list):
    for password in password_list:
        if extract_7z_archive(archive_path, password):
            print(f"Extraction successful with password: {password}")
            return
        else:
            print(f"Extraction failed with password: {password}")

    print("Extraction unsuccessful. Password not found.")

# Example usage
archive_path = "C:/Users/milos/Downloads/Chessable Tame the Sicilian - The Alapin Variation.7z.001"
password_file_path = "C:/Users/milos/Downloads/password.txt"

# Read password list from the file
with open(password_file_path, 'r') as file:
    password_list = [line.strip() for line in file.readlines()]

automate_extraction(archive_path, password_list)
