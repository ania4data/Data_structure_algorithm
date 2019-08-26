import numpy as np

class dynamic_connectivity():
	'''
	union and search of a pair elements
	0  1  2  3  4  5
	0  1  2  3  4  5
	1  1  4  2  4  5  union(0, 1), union(2, 4)
	1  1  5  2  5  5  union(4, 5)
	'''

	def __init__(self, n):
		# fill the elemt list with indexes for easy interpertibility
		self.element_list = np.arange(0, n + 1)
	def union(self, p, q):
		if(self.connection(p, q) != True):
			ip = self.element_list[p]
			iq = self.element_list[q]
			for i, element in enumerate(self.element_list):
				if(element == ip):
					self.element_list[i] = iq


	def connection(self, p, q):
		if(self.element_list[p] == self.element_list[q]):
			return True
		else:
			return False

if __name__ == '__main__':

	n = int(input())
	conn = dynamic_connectivity(10)
	print(conn.element_list)
	print(conn.connection(0, 1))
	conn.union(0, 1)
	print(conn.element_list)
	print(conn.connection(0, 1))
	conn.union(3, 4)
	conn.union(5, 6)
	print(conn.element_list)
	conn.union(4, 6)
	print(conn.element_list)



