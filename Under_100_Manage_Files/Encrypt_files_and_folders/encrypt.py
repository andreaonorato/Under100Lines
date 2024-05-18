import os
import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Load key from file or generate a new one if not exists
def load_or_generate_key():
    key_file = "key.key"
    if os.path.exists(key_file):
        with open(key_file, "rb") as f:
            key = f.read()
    else:
        key = generate_key()
        with open(key_file, "wb") as f:
            f.write(key)
    return key

# Encrypt a file
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as f:
        data = f.read()
    encrypted_data = fernet.encrypt(data)
    with open(file_path + ".encrypted", "wb") as f:
        f.write(encrypted_data)

# Decrypt a file
def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as f:
        data = f.read()
    decrypted_data = fernet.decrypt(data)
    with open(os.path.splitext(file_path)[0], "wb") as f:
        f.write(decrypted_data)

# Encrypt a folder
def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

# Decrypt a folder
def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(".encrypted"):
                decrypt_file(file_path, key)

# Select file or folder for encryption or decryption
def select_file_or_folder():
    selected_path = filedialog.askopenfilename(initialdir="/", title="Select file or folder")
    if selected_path:
        return selected_path
    else:
        return None

# Main function for encryption
def encrypt():
    key = load_or_generate_key()
    file_or_folder = select_file_or_folder()
    if file_or_folder:
        if os.path.isfile(file_or_folder):
            encrypt_file(file_or_folder, key)
        elif os.path.isdir(file_or_folder):
            encrypt_folder(file_or_folder, key)
        print("Encryption completed.")

# Main function for decryption
def decrypt():
    key = load_or_generate_key()
    file_or_folder = select_file_or_folder()
    if file_or_folder:
        if os.path.isfile(file_or_folder):
            decrypt_file(file_or_folder, key)
        elif os.path.isdir(file_or_folder):
            decrypt_folder(file_or_folder, key)
        print("Decryption completed.")

# Create tkinter GUI
root = tk.Tk()
root.title("File Encryption/Decryption")

# Create buttons for encryption and decryption
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack(pady=10)

# Run the GUI
root.mainloop()
