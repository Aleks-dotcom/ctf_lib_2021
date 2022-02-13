from pwn import * 
p = process("./chal")
data = open("image.png", "r").read()

p.sendlineafter("\n\n",str(len(data)))

p.sendlineafter("\n\n",data)

p.interactive()
