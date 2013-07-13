#2.py

#iterative solution
#4 000 000

# Number -> Number
# Produce the fibsum of fibonnaci sequence whose individual values do not exceed 4 million
# and find the fibsum of even valued.

#recevenfib(34) # 2 + 8 + 34 = 44
"""
def iterativeevenfib(natural):
	fibsum = 0
	pt = 1 # pt is previous term
	ct = 2 # ct is currentterm
	
	while ct < natural:
		if (ct % 2) == 0:
			fibsum += ct
		buffer = ct
		ct += pt
		pt = buffer
	print fibsum


iterativeevenfib(4000000)
"""


def recursiveevenfib(rct, rpt, natural, rfibsum):
	if (rct >= natural):
		print rfibsum
	if (rct < natural):
		if (rct % 2 ) == 0:
			rfibsum += rct
			recursiveevenfib(rct + rpt, rct, natural, rfibsum + rct)
		recursiveevenfib(rct + rpt, rct, natural, rfibsum)

recursiveevenfib(2, 1, 4000000, 0)
