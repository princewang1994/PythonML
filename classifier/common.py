import numpy as np
import matplotlib.pyplot as plt
# data generator


class DataSimulor(object):

	def __init__(self):
		pass

	@staticmethod
	def draw_line(f, xmin=0, xmax=10):
		x = np.linspace(xmin, xmax)
		y = f(x)
		plt.plot(x, y, 'r')

	@staticmethod
	def get_data(f, xmin=0, xmax=10, space=0.01, lamda=0.1):
		x = np.arange(xmin, xmax, space)
		y = f(x)
		factor = 2 * lamda * np.random.random(x.size) - lamda + 1
		return x, y * factor


class Model:
	def __init__(self):
		pass


class Classifier:

	def __init__(self):
		pass

	def train(self, x, y):
		pass

	def classify(self, x, y):
		pass

	def precision(self):
		pass

	def error(self):
		pass
