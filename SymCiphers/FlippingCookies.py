import requests

# Function to get the initial cookie
def get_cookie():
    url = 'https://aes.cryptohack.org/flipping_cookie/get_cookie/'
    return requests.get(url).json()

# Function to check for the flag using the modified IV and cookie
def get_flag(cookie, iv):
    url = f'https://aes.cryptohack.org/flipping_cookie/check_admin/{cookie}/{iv}'
    return requests.get(url).json()

# XOR operation for two byte strings
def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

# Main logic
data = get_cookie()['cookie']
iv = bytes.fromhex(data[:32])  # Extract the IV
cookie = data[32:]  # Extract the actual cookie

# Original and target texts
original_text = b'admin=False;expi'
target_text = b'admin=True;expir'

# Create the forged IV
xor_result = xor_bytes(iv, original_text)
forged_iv = xor_bytes(xor_result, target_text).hex()

# Get the flag
response = get_flag(cookie, forged_iv)
print(response["flag"])
