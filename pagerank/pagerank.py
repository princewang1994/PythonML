import numpy as np

def pagerank(a, b):
	for i in xrange(100):
		b = np.dot(a, b)
	return b

a = [[1.0/3, 1.0/3, 0.0, 1.0/3], [1.0/3, 0.0, 0.0, 1.0/2], [1.0/3, 1.0/2, 1.0, 0.0], [1.0/3, 0.0, 0.0, 0.0]]
b = [1.0/4, 1.0/4, 1.0/4, 1.0/4]
m = pagerank(np.array(a), np.array(b))
print m 
