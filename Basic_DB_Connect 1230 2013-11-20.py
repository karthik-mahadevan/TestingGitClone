import MySQLdb

try:
	db = MySQLdb.connect("ec2-107-20-214-225.compute-1.amazonaws.com", "eojtvdwdfdqgfn", "ijhG_SysuOKRUq884UK2flX8FV", "d94qqvnjkmq7sn")
except:
	print "Exception"



db.close()
