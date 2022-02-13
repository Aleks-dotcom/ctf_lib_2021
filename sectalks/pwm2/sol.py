from pwn import *
p = process('./many_passwords')
print p.recvuntil('Action: ')
p.sendline('0')
print p.recvuntil('Password 1: ')
p.sendline('AAAAAAAAAAA')
p.recvuntil('Password 2: ')
p.sendline('monkeymonkey1234')
p.recvuntil('Password 3:')
p.sendline('StrongPassword1!')
p.recvuntil('Password 4: ')



password = [0x58, 0x5f, 0x6f, 0x61, 0x69, 0x63, 0x43, 0x5f, 0x50, 0x35, 0x52, 0x59 ,0x6b, 0x5f ,0x69 ,0x3c]
num = 0
password2 = ''
while num < 16:
	password2 += chr(password[num] + num)
	num +=1 
print password2	
