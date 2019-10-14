class Vehicle:
	total = 0

	def prin(self):
		print self.total

	def set(self, value):
		self.total = value

class Bike(Vehicle):
	pass

class Car(Vehicle,Bike):
    pass

Car().set(5)    

t = Car()
t.prin()