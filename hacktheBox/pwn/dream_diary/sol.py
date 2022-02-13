from pwn import *

p = process('./diary3')
pid = gdb.attach(p, gdbscript="""""")
p.sendlineafter('> ','2')
p.interactive()
