import matplotlib.pyplot as plt
import numpy as np
import time

def fibonacci_naive(n):

	if(n <= 1):
		return n
	else:
		return fibonacci_naive(n-1) + fibonacci_naive(n-2)

if __name__ == '__main__':

	results = []
	times = []
	print('add 0 <= n <= 30')
	n = int(input())
	if (n <= 30  and n >= 0):
		i = 0
		while(i <= n):
			start = time.time()
			result = fibonacci_naive(i)
			print(result, time.time() - start)
			i += 1
			times.append(time.time() - start)
			results.append(result)
	else:
		print('try within the limit')

	plt.plot(np.arange(n+1), np.array(results))
	plt.show()
	plt.plot(np.arange(n+1), np.array(times))
	plt.show()