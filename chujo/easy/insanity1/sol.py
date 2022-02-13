from pwn import  *

res = b'Invalid'
count = 0
while 'Invalid' in res.decode('utf-8').replace('\n',''):
	print('Trying num: ',count) 
	p = remote('insanity1.chujowyc.tf', 4004)
	p.recvline()
	p.sendlineafter('What is 2+2: ','4')
	p.sendlineafter('What number between 0 and 100 am I thinking about right now?\n','81')
	p.sendlineafter('What is 2+2: ',str(count))
	res = p.recvline()
	print(res)
	count +=1
	p.close()
	p.shutdown()
print('FOUND THE RIGHT ANSWER ',res)