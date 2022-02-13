from itertools import permutations

string = "PleaseSubscribe!"

with open("list.txt","a+") as file:
    for i in range(10000):
        res = string+str(i)
        file.write(res + '\n')
