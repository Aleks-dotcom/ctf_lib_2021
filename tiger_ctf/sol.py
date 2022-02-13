from pwn import *

#ip = xDmems
#port = xDmemes 



with open('/usr/share/dict/american-english','r') as file:
	p= remote(ip,port)
	for line in file.readlines()
		p.sendlineafter("What's my word?\n",line)
		if "nay" in p.recvline():
			p.close()
			p.shutdown()
			continue
		print "flag found " + p.recv(1024)