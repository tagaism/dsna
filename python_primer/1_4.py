def sum_of_sq(n):
	"""
	Takes a positive integer n and
	returns the sum of the squares of all
	the positive integers smaller than n
	"""
	summ = 0
	while n > 0:
		summ += n**2
		n -= 1
	return summ