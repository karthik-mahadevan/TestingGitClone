import os

try:
	os.chdir("/Users/ranjani")
	f = open("test.txt","w")
	for i in range(2,100,4):
		f.write(str(i) + "\n")
	f.close()
except:
	print "Write Exception !!"

try:
	f = open("/Users/ranjani/test.txt","r")
	number = f.read()
	print number
	f.close()
except:
	print "Read Exception !!"