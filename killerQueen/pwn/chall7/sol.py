from pwn import *

p = process('./fufu')
pid = gdb.attach(p, gdbscript="""
        b * display
        
        
        
        """)

def create(index,size,content):
    global p
    p.sendlineafter(b'do?\n',b'1')
    p.sendlineafter(b'on?\n',str(index))
    p.sendlineafter(b'want?\n',str(size))
    p.sendlineafter(b'content.\n',str(content))


def display(index):
    global p
    p.sendlineafter(b'do?\n',b'2')
    p.sendlineafter(b'display?\n',str(index))


def reset(index):
    global p
    p.sendlineafter(b'do?\n',b'3')
    p.sendlineafter(b'reset?\n',str(index))



create(0,0x20,0x20*'A')
create(0,0x50,0x3a*'B')
display(0)



