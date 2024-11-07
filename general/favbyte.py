from pwn import *
flag = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

scrt = ord('c')
key = flag[0] ^ scrt

for i in flag:
    print(chr(i ^ key), end="")