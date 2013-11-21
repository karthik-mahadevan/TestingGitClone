class Automobile(object):
	def __init__(self, maker, reg_no, colour):
		self.maker = maker
		self.reg_no = reg_no
		self.colour = colour

class Car(Automobile):
	def Initialise(self):
		self.wheels = 4
		self.passengers = 5
		self.cargo = 20

	def Display(self):
		print self.maker, self.reg_no, self.colour, self.wheels, self.passengers, self.cargo


class Truck(Automobile):
	def Initialise(self):
		self.wheels = 5
		self.passengers = 2
		self.cargo = 200

	def Display(self):
		print self.maker, self.reg_no, self.colour, self.wheels, self.passengers, self.cargo


class Aircraft(Automobile):
	def Initialise(self):
		self.wheels = 8
		self.passengers = 300
		self.cargo = 200000
		self.wings = 4

	def Display(self):
		print self.maker, self.reg_no, self.colour, self.wheels, self.passengers, self.cargo, self.wings


Getz = Car("Hyundai", "KA 2897", "Black")
Corrolla = Car("Toyota", "KA 3921", "Red")
Trucker = Truck("TATA", "RJ 6291", "Brown")
JumboJet = Aircraft("Airbus", "US 2904", "Silver")

Getz.Initialise()
Corrolla.Initialise()
Trucker.Initialise()
JumboJet.Initialise()

Getz.Display()
Corrolla.Display()
Trucker.Display()
JumboJet.Display()




