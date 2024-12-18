import base64
import json

#token
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiY3J5cHRve2p3dF9jb250ZW50c19jYW5fYmVfZWFzaWx5X3ZpZXdlZH0iLCJ1c2VyIjoiQ3J5cHRvIE1jSGFjayIsImV4cCI6MjAwNTAzMzQ5M30.shKSmZfgGVvd2OSB2CGezzJ3N6WAULo3w9zCl_T47KQ"

# the below statement will split the token into header, payload, and signature
header, payload, signature = token.split('.')

# Decode the payload
def decode_base64url(data):
    padding = '=' * (4 - len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)

# Extract and print payload
decoded_payload = json.loads(decode_base64url(payload))
flag = decoded_payload.get("flag")
print("Flag:", flag)
