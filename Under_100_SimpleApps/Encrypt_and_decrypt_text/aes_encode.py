from Crypto.Cipher import AES
from Crypto import Random
from binascii import b2a_hex
import sys

def encrypt_and_decrypt(plain_text):
    # The key length must be 16 (AES-128), 24 (AES-192), or 32 (AES-256) Bytes.
    key = b'this is a 16 key'

    # Generate a non-repeatable key vector with a length
    # equal to the size of the AES block
    iv = Random.new().read(AES.block_size)

    # Use key and iv to initialize AES object, use MODE_CFB mode
    mycipher = AES.new(key, AES.MODE_CFB, iv)

    # Encrypt the plaintext
    ciphertext = iv + mycipher.encrypt(plain_text.encode())

    # To decrypt, use key and iv to generate a new AES object
    mydecrypt = AES.new(key, AES.MODE_CFB, ciphertext[:16])

    # Decrypt the encrypted ciphertext
    decrypttext = mydecrypt.decrypt(ciphertext[16:])

    # Save the encrypted data to a file
    with open("encrypted.bin", "wb") as file_out:
        file_out.write(ciphertext[16:])

    # Print the key, iv, encrypted data, and decrypted data
    print("The key k is:", key)
    print("IV is:", b2a_hex(ciphertext)[:16])
    print("The encrypted data is:", b2a_hex(ciphertext)[16:])
    print("The decrypted data is:", decrypttext.decode())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        plain_text = input("Enter the plaintext: ")
    else:
        plain_text = sys.argv[1]
    encrypt_and_decrypt(plain_text)
