def gcd(a, b):
	'''
	greatest common divisor
	recursive approach, get a remainder until
	remainder divisable by both a and b
	a = a_prime + b*q
	if a and b divisble by z,
	a_prime has to be divisable by z

	for greedy solution have to loop through smaller number
	backward one by one try divide both a and b until finding
	common divisors
	'''
	while a % b != 0:
		remainder = a % b
		a = b
		b = remainder
		print('loop', a, b)
	return b


if __name__ == '__main__':
	x, y = tuple(map(int, input('input two numbers with space: ').split()))
	print(x,  y)
	if x >= y:
		print(gcd(x, y))
	else:
		print(gcd(y, x))


