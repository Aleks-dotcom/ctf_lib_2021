string = "w1{1wq80haib767"
final = [None] * 15

def re(string, final,stevec):
	if stevec == 15:
		with open('flags.txt', 'a') as file:
			file.write(''.join(final)+'\n')
	else:
		final[stevec] = chr(ord(string[stevec]) +2)
		re(string,final,stevec +1)
		final[stevec] = chr(ord(string[stevec]) -5)
		re(string,final,stevec +1)
re(string,final,0)