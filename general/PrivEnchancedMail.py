from Crypto.PublicKey import RSA

rf = open("C:/Users/Dylan Keogh/Desktop/privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem", "rb")

flag = RSA.importKey(rf.read())
print(flag.d)