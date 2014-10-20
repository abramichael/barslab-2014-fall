def inc(x):
	return x+1

def fact(n):
	if isinstance(n,int):
		if n>=0:
			if n == 0:
				return 1
			else:
				return n*fact(n-1)
		else:
			raise ValueError
	else:
		raise TypeError