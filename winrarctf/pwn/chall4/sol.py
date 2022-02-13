#!/usr/bin/python

from pwn import *
from time import sleep
p = process("./boring-flag-checker")

# sleep(100)

def get_base_address(proc):

    return int(open("/proc/{}/maps".format(proc.pid), 'rb').readlines()[0].split('-')[0], 16)

def debug(breakpoints):
    script = "handle SIGALRM ignore\n"
    PIE = get_base_address(p)
    script += "set $_base = 0x{:x}\n".format(PIE)
    for bp in breakpoints:
        script += "b *0x%x\n"%(PIE+bp)
    gdb.attach(p,gdbscript=script)


def leak():
    f = open('prog.bin','a+')
    f.write('\x00' * 8)
    f.write('\x01\x00')
    f.close()
    pass


def exploit():
    leak()
    breakpoints = [0x149d]
    debug(breakpoints)

if __name__ == '__main__':
    exploit()
    p.interactive()

