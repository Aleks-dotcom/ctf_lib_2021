from pwn import *


arr =[ 0x336c707b67616c66, 0x6e3172705f337361,0x5f687431775f6674,0x5f6e303174756163,0xa7d6c78336139]
flag  = ""
for elem in arr:
    while elem > 0:
        flag +=chr(elem & 0xff)
        elem = elem >>0x8

print(flag)
