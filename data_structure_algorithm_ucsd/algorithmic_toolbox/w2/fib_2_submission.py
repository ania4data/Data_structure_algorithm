# Uses python3
def calc_fib(n):
	'''
	last digit of fib number,
	onl
	'''
	fib_list_last = [None] * (n+1)

	for i in range(n+1):
		if(i <= 1): 
			fib_list_last[i] = i
		else:
			fib_list_last[i] = (fib_list_last[i-1] + fib_list_last[i-2]) % 10
	return fib_list_last[n]
# 0 1 2 3 4 5 6 7 8 9 10 11 12
# 0 1 1 2 3 5 8 13 21 34 55 -> if only add left digit, next fib number has correct last number
n = int(input())
print(calc_fib(n))