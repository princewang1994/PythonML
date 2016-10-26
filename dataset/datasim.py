# data generator
import numpy as np
import matplotlib.pyplot as plt


class DataSimulor:

	def __init__(self):
		pass
	'''
		draw a line
	'''
	@staticmethod
	def draw_line(f, xmin=0, xmax=10):
		x = np.linspace(xmin, xmax)
		y = f(x)
		plt.plot(x, y, 'r')

	'''
		generate function (use as testing data)
		example:
			get_data(lambda x: math.sin(x), xmin=0, xmax=6.28, space=0.01, lamda=0.1)
		xmin, xmax: low and high bound of data
		lamda: tremble factor
		space: space between 2 neighbor point

	'''
	@staticmethod
	def get_data(f, xmin=0, xmax=10, space=0.01, lamda=0.1):
		x = np.arange(xmin, xmax, space)
		y = f(x)
		factor = 2 * lamda * np.random.random(x.size) - lamda + 1
		return x, y*factor