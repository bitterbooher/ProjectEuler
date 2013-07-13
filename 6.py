# difference between sum of squares and square of sum

def sumofsquares(max):
	x = 1
	sum1 = 0
	while x <= max:
		sum1 += x**2
		if x == max:
			print sum1
		x += 1
		

def squareofsums(max):
	y = 1
	sum2 = 0
	while y <= max:
		sum2 += y
		if y == max:
			print sum2**2
		y += 1
			
print squareofsums(100)
print sumofsquares(100)
#print squareofsums(100) - sumofsquares(100)

print 25502500-338350