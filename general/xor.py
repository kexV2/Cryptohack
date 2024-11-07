from pwn import *
flag = "label"
integer = 13
print(xor(flag, integer))