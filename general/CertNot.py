from Crypto.PublicKey import RSA

rf = open("C:/Users/Dylan Keogh/Desktop/2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der", "rb")
flag = RSA.importKey(rf.read())
print(flag.n)