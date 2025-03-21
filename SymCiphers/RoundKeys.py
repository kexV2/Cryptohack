def roundkeys(matrix):
    # Converts 4x4 matrix into  16-byte array 
    return bytes([byte for row in matrix for byte in row])

def add_round_key(s, k):
    # XOR each byte with corresponding byte of the round key
    return [[s[i][j] ^ k[i][j] for j in range(4)] for i in range(4)]

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

# Perform AddRoundKey
result = add_round_key(state, round_key)

# Convert to bytes and print the flag
print(roundkeys(result))  
