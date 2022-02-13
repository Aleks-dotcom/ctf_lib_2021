string = "aQLpavpKQcCVpfcg"
solution = ""


for elem in string:
	st = ord(str(elem))
	start = st - 65
	stevec = 0
	while ((8 * stevec + 19 ) % 61 )!= start:
		stevec +=1
	solution += chr(stevec)
print solution