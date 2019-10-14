import itertools


a_team = ['raki', 'mohi']
b_team = ['hari', 'gandhi']

anss = itertools.product(a_team, b_team);


for ans in anss:
	print(ans)
	print(type(ans))
	#if(ans[0] == 'raki' || ans[1] == 'raki'):
		#print("your team wins")
	#else:
		#print("you lose")
