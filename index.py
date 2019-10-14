

from child1 import Child1
from child2 import Child2

class Index:
	print('index ')


#Child1()
# Child2()
# Child1()


x = lambda a : a + 10

print(x(5))


a  = [1,3,5,7,9,11,13]

result = filter(lambda x : x%2, a)
print(list(result))

dict = { };

dict[1] = 'raki'
dict[2] = 'bablu'


for key, item in dict.items():
	print item