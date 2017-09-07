
from numpy import array, arange

def factorial(n):
	f=1.0
	if n == 0:
		f = 1
	else:
		for k in arange(1, n+1):
			f *= k
	return f

def binomial(n,k):
	bi = factorial(n) / ( factorial(k) * factorial(n-k) )
	bi = int(bi)
	return bi
