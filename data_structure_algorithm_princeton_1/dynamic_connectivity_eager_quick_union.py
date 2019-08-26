import numpy as np

class dynamic_connectivity():
	'''
	union and search of a pair elements
	0  1  2  3  4  5
	0  1  2  3  4  5
	1  1  4  2  4  5  union(0, 1), union(2, 4)
	1  1  5  2  5  5  union()
	'''

	def __init__(self, n):
		# fill the elemt list with indexes for easy interpertibility
		self.element_list = np.arange(0, n + 1)

	def root(self, node):
		while(node != self.element_list[node]):
					node_new = self.element_list[node]
					node = node_new
		return node

	def union(self, p, q):
		if(self.connection(p, q) is False):
			ip = self.root(p)
			iq = self.root(q)
			self.element_list[ip] = iq

	def connection(self, p, q):
		if(self.root(p) == self.root(q)):
			return True
		else:
			return False

if __name__ == '__main__':

	n = int(input())
	conn = dynamic_connectivity(10)
	print(conn.element_list)
	print(conn.connection(2, 9))
	conn.union(4, 3)
	print(conn.element_list)
	print(conn.connection(2, 9))
	conn.union(3, 8)
	conn.union(6, 5)
	print(conn.element_list)
	conn.union(9, 4)
	print(conn.element_list)
	conn.union(2, 1)
	conn.union(5, 0)	
	conn.union(7, 2)
	conn.union(6, 1)
	conn.union(7, 3)
	print(conn.element_list)



