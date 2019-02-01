from functools import reduce
def sum(a,b):
	total=reduce(lambda x,y: x+y,range(a+1,b,2))
	print(total)
sum(100,500)

