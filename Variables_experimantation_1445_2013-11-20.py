import os
global_var = {}
def fileread(num_str):
	global global_var
	num = ''
	dict_index = 0
	for i in range(len(num_str)):
		if num_str[i] == '\n':
			global_var[str(dict_index)] = int(num)
			dict_index += 1
			num = ''
		else:
			num += num_str[i]
	return


os.chdir("/Users/ranjani")
f = open("test.txt", "r")
num_str = f.read()
fileread(num_str)
f.close()

read_status = {}
for i in global_var.keys():
	read_status[str(global_var[i])] = 0
print global_var
print read_status