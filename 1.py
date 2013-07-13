
def multiple3and5(natural):
	sum = 0
	x = 0
	while x < natural: 
		if (x % 3) == 0 or (x % 5) == 0:
			sum += x
		x += 1
		#print sum
	print sum
multiple3and5(1000)

