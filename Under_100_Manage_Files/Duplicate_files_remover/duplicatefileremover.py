import hashlib
import os

# Function to calculate the hash of a file
def hash_file(filename):
    BLOCKSIZE = 65536  # Define block size to read from file
    hasher = hashlib.md5()  # Initialize MD5 hasher
    with open(filename, 'rb') as file:
        # Read file in blocks and update hasher
        buf = file.read(BLOCKSIZE)
        while(len(buf) > 0):
            hasher.update(buf)
            buf = file.read(BLOCKSIZE)
    return hasher.hexdigest()  # Return hexadecimal digest of the hash


if __name__ == "__main__":
    # Dictionary to store hash and corresponding file name
    hash_map = {}

    # List to store deleted files
    deleted_files = []

    # Get list of files in current directory
    file_list = [f for f in os.listdir() if os.path.isfile(f)]

    # Iterate through each file
    for f in file_list:
        key = hash_file(f)  # Get hash of the file
        # If hash already exists in the hash map, delete the file
        if key in hash_map.keys():
            deleted_files.append(f)
            os.remove(f)
        else:
            hash_map[key] = f  # Store hash and file name in the hash map

    # Print deleted files if any, otherwise print no duplicates found
    if len(deleted_files) != 0:
        print('Deleted Files:')
        for deleted_file in deleted_files:
            print(deleted_file)
    else:
        print('No duplicate files found')
