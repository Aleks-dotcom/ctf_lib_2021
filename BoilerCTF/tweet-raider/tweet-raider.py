from pwn import *

p = process('./tweet-raider')

string = "spacerocketelectricfastdankdope420litcybertruckcybertrucktestlaboringtunnelflamethrowermeme"
p.recvuntil("Tweet: ")
