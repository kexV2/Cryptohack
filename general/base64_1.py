import base64

String = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

data = bytes.fromhex(String)
base64_encoded = base64.b64encode(data)
print(base64_encoded.decode())