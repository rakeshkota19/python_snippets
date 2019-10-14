
class a:
	b = 10
	site = "base"

	def __init__(self):
		print("inside a constructur")

	def get_value(self):
		print(self.site) 

class b(a):
	c = 20
	site = "olx"

	def __init__(self):
		print("inside b constructur")

class c(a,b):
	pass
	#def __init__(self):
		#print("inside c constructur")




d = b()
d.get_value()

if(0.1 + 0.2 == 0.3):
	print('true')
else:
	print('false')




