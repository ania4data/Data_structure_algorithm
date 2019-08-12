import matplotlib.pyplot as plt
import numpy as np
import time

def fibonacci_naive(n):

	if(n <= 1):
		return n
	else:
		return fibonacci_naive(n-1) + fibonacci_naive(n-2)

def fibonacci_list(n):
	fib_list = [None] * (n+1)

	for i in range(n+1):
		if(i <= 1): 
			fib_list[i] = i
		else:
			fib_list[i] = fib_list[i-1] + fib_list[i-2]
	return fib_list[n]

if __name__ == '__main__':

	results_n = []
	times_n = []
	results_li = []
	times_li = []	
	print('add 0 <= n <= 30')
	n = int(input())
	if (n <= 1000  and n >= 0):
		i = 0
		while(i <= n):
			start_n = time.time()
			result_n = fibonacci_naive(i)
			end_n = time.time()
			times_n.append(end_n - start_n)
			results_n.append(result_n)

			start_li = time.time()
			result_li = fibonacci_list(i)
			end_li = time.time()
			times_li.append(end_li - start_li)
			results_li.append(result_li)			
			print(result_n, end_n - start_n, result_li, round(end_li - start_li, 4))
			i += 1
	else:
		print('try within the limit')

	plt.plot(np.arange(n+1), np.array(results_n))
	plt.plot(np.arange(n+1), np.array(results_li))
	plt.show()
	plt.plot(np.arange(n+1), np.array(times_n))
	plt.plot(np.arange(n+1), np.array(times_li))
	plt.show()