import os
import zipfile

def zip_files_in_folder(folder_path):
    zip_path = folder_path + ".zip"
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, os.path.dirname(folder_path))
                zipf.write(file_path, arcname)

folder_to_zip = input("Enter the folder path containing files to zip: ")

zip_files_in_folder(folder_to_zip)

print(f"Files inside {folder_to_zip} have been zipped to {folder_to_zip}.zip")
