from pwn import *




p = remote('localhost',8080)

p.send(p32(0))


