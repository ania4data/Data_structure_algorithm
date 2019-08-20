# Uses python3
def calc_fib(n):
	fib_list = [None] * (n+1)

	for i in range(n+1):
		if(i <= 1): 
			fib_list[i] = i
		else:
			fib_list[i] = fib_list[i-1] + fib_list[i-2]
	return fib_list[n]

n = int(input())
print(calc_fib(n))