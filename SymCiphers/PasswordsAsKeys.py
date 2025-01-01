from Crypto.Cipher import AES
import hashlib
import random

# Function to decrypt the ciphertext using a hashed password
def decrypt(ciphertext, key):
    try:
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted = cipher.decrypt(bytes.fromhex(ciphertext))
        return decrypted
    except ValueError as e:
        return None

# Read the list of words from "words.txt"
with open("words.txt", "r") as file:
    words = [word.strip() for word in file]

# Encrypted message
ciphertext = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"

# Loop through words, hash each word, and try decrypting
for word in words:
    key = hashlib.md5(word.encode()).digest()
    decrypted = decrypt(ciphertext, key)
    if decrypted and b'crypto' in decrypted:
        print(f"Found: {decrypted.decode('utf-8')}")
        break
