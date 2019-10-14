

class a :

	b = 5

	def __init__(self):
		self.b = 10

	def value(self):
		return self.b


class b(a):
	
	def value(self):
		return self.b+1

c = b()
print(c.value())