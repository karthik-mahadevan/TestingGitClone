def getfirst(list):
	if len(list) > 0:
		print list[0]
		getfirst(list[1::])
	else:
		return

list1 = []
print list1
for i in range(100):
	list1.append(i ** 2)

getfirst(list1)
