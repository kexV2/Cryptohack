def bytes2matrix(text):
    """ Converts 16-byte array into  4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    # Converts 4x4 matrix to 16-byte array. 
    return bytes([byte for row in matrix for byte in row])

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))  
