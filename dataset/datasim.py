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
	def draw_line(f, xmin=0, xmax=10, style='r'):
		x = np.linspace(xmin, xmax)
		y = f(x)
		plt.plot(x, y, style)

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
		factor = np.random.normal(0, 10 * lamda, x.size)
		return x, y + factor

	'''
		data: numpy array stand for data matrix without label

		label: one-dimension integer array, each number stands for a class

		f1, f2: index of feature to plot

		choose: the label you choose to plot it's binary diagram

		example:
			data = [[1, 3, 4],
					[2, 3, 5],
					[2, 3, 1]]
		label: [0, 0, 1]
	'''
	@staticmethod
	def plot_binary(data, f1, f2, label, choose):
		d0 = data[label == choose]
		d1 = data[label != choose]
		plt.plot(d0[:, f1], d0[:, f2], '.r')
		plt.plot(d1[:, f1], d1[:, f2], 'b.')