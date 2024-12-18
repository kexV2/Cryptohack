import jwt

secretkey = "secret"

encoded = jwt.encode({'username': "admin", "admin": True}, secretkey, algorithm='HS256')
print(encoded)