#!/usr/bin/python3

from elftools.elf.elffile import ELFFile
from struct import pack

with open('anti', 'rb+') as f:
    elffile = ELFFile(f)
    e_shnum = len(elffile.get_section(28).data().decode('ascii').split('\x00')) + 1 
    f.seek(48)
    f.write(pack('h', e_shnum))
