def factorial(i):
	
	fact = 1
	if(i == 1):
		return 1
	else:
		return i * factorial(i-1)

if __name__ == '__main__':

	n = int(input())
	print(factorial(n))