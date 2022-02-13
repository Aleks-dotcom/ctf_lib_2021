from pwn import *
context.clear(
    arch="amd64",
    terminal=['tmux','splitw'],
    log_level="debug"
)

frame = SigreturnFrame()
frame.rax = 0x3b
frame.rdi = 0xdeadbeef
frame.rsi = 0x6
frame.rdx = 0x5
frame.rip = 0xffffffff
print(bytes(frame)[1:172])
