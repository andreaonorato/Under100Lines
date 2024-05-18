import os
import tkinter as tk
from tkinter import filedialog, messagebox

def find_string_in_files(folder_path, search_string):
    found_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if search_string in content:
                        found_files.append(file_path)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
    return found_files

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def search_files():
    folder_path = folder_entry.get()
    search_string = string_entry.get()
    if not folder_path or not search_string:
        messagebox.showwarning("Warning", "Please provide folder path and search string.")
        return

    found_files = find_string_in_files(folder_path, search_string)
    if found_files:
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        for file in found_files:
            result_text.insert(tk.END, file + '\n')
        result_text.config(state=tk.DISABLED)
    else:
        messagebox.showinfo("Info", "No files found containing the search string.")

# Create Tkinter window
root = tk.Tk()
root.title("File Search")

# Folder path entry
folder_label = tk.Label(root, text="Folder Path:")
folder_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=0, column=1, padx=5, pady=5)

browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.grid(row=0, column=2, padx=5, pady=5)

# Search string entry
string_label = tk.Label(root, text="Search String:")
string_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

string_entry = tk.Entry(root, width=50)
string_entry.grid(row=1, column=1, padx=5, pady=5)

# Search button
search_button = tk.Button(root, text="Search", command=search_files)
search_button.grid(row=1, column=2, padx=5, pady=5)

# Result text
result_text = tk.Text(root, height=15, width=70)
result_text.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
result_text.config(state=tk.DISABLED)

root.mainloop()
