my_dict = {}
my_list = []
for i in range(1,10):
	my_list.append([str(i)]*5)
	my_dict[str(i)] = my_list
	print i,my_dict[str(i)]
	#for j in range(1,1000):

	#wait = raw_input("Type any key : ")
#print my_list
#print my_dict