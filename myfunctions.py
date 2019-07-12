from __future__ import division
from numpy import array, arange

def factorial(n):
	# dazhutou
	f = 1.0
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
	hhhhhhhhhhhhhhhhhhhh

def trapezoidal(a,b,N,f):
	h = (b - a)/N
	print "h=",h
	s = 0.5 * f(a) + 0.5 * f(b)
	for k in range(1,N):
		s += f(a + k * h)
		print s
	Int = h * s
	print Int
	return Int

	
