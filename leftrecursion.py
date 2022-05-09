def left_recursion(grammer):
	flag = 0
	pos = 0
	for key in grammer.copy(): 
		item = grammer[key]
		for prod in item:
			if key == prod[0:1]:
				print("left recursion found")
				flag = 1
				pos = pos +1
				subfix = prod[1:len(prod)]
		if flag == 1:
			grammer[key] = item[pos:len(item)][0]+key+"'"
			grammer.update({key+"'":["",subfix+key+"'"]})
			flag=pos=0
	return grammer


grammer = {"S":["abAB","abc","abcdA"]}
#grammer = {"A":["ABD","Aa","a"],"B":["Bc","b"]}
#grammer = {"S":["SOS1S","01"]}

print(grammer)
print(left_recursion(grammer))