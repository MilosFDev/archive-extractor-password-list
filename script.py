import os
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import py7zr
import rarfile

def extract_7z_archive(archive_path, password):
    try:
        with py7zr.SevenZipFile(archive_path, mode='r', password=password) as szf:
            szf.extractall()
        return True
    except py7zr.Bad7zFile:
        return False

def extract_rar_archive(archive_path, password):
    try:
        with rarfile.RarFile(archive_path) as rf:
            rf.setpassword(password)
            rf.extractall()
        return True
    except rarfile.BadRarFile:
        return False

def extract_button_click():
    archive_path = filedialog.askopenfilename(filetypes=[("Archive Files", "*.7z;*.rar")])
    password_file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    # Read password list from the file
    with open(password_file_path, 'r') as file:
        password_list = [line.strip() for line in file.readlines()]

    archive_extension = os.path.splitext(archive_path)[1].lower()

    if archive_extension == '.7z':
        for password in password_list:
            if extract_7z_archive(archive_path, password):
                messagebox.showinfo("Extraction Successful", f"Extraction successful with password: {password}")
                return
    elif archive_extension == '.rar':
        for password in password_list:
            if extract_rar_archive(archive_path, password):
                messagebox.showinfo("Extraction Successful", f"Extraction successful with password: {password}")
                return

    messagebox.showerror("Extraction Unsuccessful", "Extraction unsuccessful. Password not found.")

# Create the GUI
window = tk.Tk()
window.title("Archive Extractor")
window.geometry("800x600")

# Create a Frame for the content
content_frame = tk.Frame(window)
content_frame.pack(pady=20)

# Archive Label
archive_label = tk.Label(content_frame, text="Select Archive:")
archive_label.pack()

# Archive Path Entry
archive_path_entry = tk.Entry(content_frame, width=40)
archive_path_entry.pack()

# Browse Archive Button
def browse_archive():
    archive_path = filedialog.askopenfilename(filetypes=[("Archive Files", "*.7z;*.rar")])
    archive_path_entry.delete(0, tk.END)
    archive_path_entry.insert(tk.END, archive_path)

browse_button = tk.Button(content_frame, text="Browse", command=browse_archive)
browse_button.pack(pady=5)

# Password Label
password_label = tk.Label(content_frame, text="Select Password File:")
password_label.pack()

# Password Path Entry
password_path_entry = tk.Entry(content_frame, width=40)
password_path_entry.pack()

# Browse Password Button
def browse_password():
    password_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    password_path_entry.delete(0, tk.END)
    password_path_entry.insert(tk.END, password_path)

browse_button = tk.Button(content_frame, text="Browse", command=browse_password)
browse_button.pack(pady=5)
copyright_label = tk.Label(window, text="Created by MilosFDev")
copyright_label.pack()

# Extract Button
extract_button = tk.Button(window, text="Extract Archive", command=extract_button_click)
extract_button.pack(pady=10)

window.mainloop()
