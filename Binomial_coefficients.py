from myfunctions import *
from numpy import zeros

for n in range(1,11):
	pascal=zeros(n+1)
	for k in range(n+1):
		pascal[k] = binomial(n,k)
	print pascal

