class Employee(object):
	emp_id = 0
	def __init__(self, name):
		self.name = name
		Employee.emp_id += 1
		self.id = Employee.emp_id

	def Colleague(self,name):
		self.colleague = name

	def DisplayEmployee(self):
		print self.name, self.id


john = Employee("John")
david = Employee("David")
basil = Employee("Basil")
john.Colleague("Basil")
john.DisplayEmployee()
david.DisplayEmployee()
basil.DisplayEmployee()

print "Total Employees : ", Employee.emp_id