with open("listofnums.txt","a+") as file:
	for num in range(10000):
		file.write(str(num)+'\n')

	
