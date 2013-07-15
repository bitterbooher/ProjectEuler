# 3.py

# Find the prime factors
# How to find prime factors?

#http://stackoverflow.com/questions/23287/prime-factors
#http://en.wikipedia.org/wiki/Quadratic_sieve
"""
It aims to set up a congruence of squares modulo
	which is what exactly
		which leads to the factorization of n

To factorize n		
it looks for a number such that
a**2 % n is a square
the project euler question asks for the largest prime factor of 600851475143
"""

def pfactors(n):
	factors = [] # a list of factors
	d = 2 #start with trying to divide by 2
	while n > 1:
		while n % d == 0: # means its a factor
			factors.append(d) # keep a list of the factors
			n /= d # n = n/d  # divide that part by the factor you found and keep going
		d = d + 1
	print factors
	
pfactors(600851475143)
		