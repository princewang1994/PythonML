import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


'''
	data generator
'''
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
		factor = np.random.normal(0, lamda, x.size)
		return x, y + factor

import pandas as pd



class Classifier:

	def __init__(self):
		pass

	def train(self, x, y):
		pass

	def classify(self, x, y):
		pass

	def predict(self, x, y):
		pass

	def precision(self):
		pass

	def error(self):
		pass
