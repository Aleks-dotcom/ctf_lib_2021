from itertools import permutations

names = ['Luka','Jure','Sandi']
combination = [0,0,0]

def req(n,combinations,i):
	if i == 3:
		with open('list.txt','a') as file:
			file.write(''.join(combinations)+"\n")
	else:
		for num in range(len(n)):
			combinations[i]=n[num]
			req(n,combinations,i+1)

req(names,combination,0)