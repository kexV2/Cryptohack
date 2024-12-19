from Crypto.PublicKey import RSA

f = open('C:/Users/Dylan Keogh/Desktop/bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pem', 'r')
pubkey = RSA.import_key(f.read())  # This works for importing the public key

print(pubkey.n)
