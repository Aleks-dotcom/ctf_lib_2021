from pwn import *

p = process('./a.out')
payload = p64(0x787c0563565b5846)
payload += p64(0x25d334c608030ac)

#raw_input('test')
print('testtest')
print(p.recvuntil(': '))
p.sendline('aaa')
p.interactive()
