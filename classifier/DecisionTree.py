import numpy as np
import pandas as pd
from common import Classifier

class DecisionTree(Classifier):

	def __init__(self):
		pass

	def HA(self, D, A):
		n = D.shape[0]
		values = D[A].unique()
		DI = np.array([self.split(D, A, value).shape[0] for value in values])
		P = DI / float(n)
		return -np.sum(P * np.log(P))

	def entropy(self, D):
		return self.HA(D, 'class')

	def H(self, D, a):
		ent = [self.entropy(self.split(D, a, value)) for value in D[a].unique()]
		size = [self.split(D, a, value).shape[0] for value in D[a].unique()]
		return (np.array(ent) * np.array(size) / D.shape[0]).sum()

	def g(self, D, a):
		return self.entropy(D) - self.H(D, a)

	def delta_ent_rate(self, D, a):
		return self.g(D, a) / self.HA(D, a)

	def split(self, data, A, value):
		return data[data[A] == value]

	def maxCntFeat(self, D):
		label = D['class'].unique()
		mLableIndex = np.argmax([D[D['class'] == lbl].shape[0] for lbl in label])
		return label[mLableIndex]

	def createTree(self, data, features):
		n = data.shape[0]
		cls = data['class']
		if cls[cls == cls.iloc[0]].size == n:
			return self.maxCntFeat(data), n
		if features.size == 0:
			return self.maxCntFeat(data), n

		bestFeat = pd.Series({f: self.delta_ent_rate(data, f) for f in features}).argmax()
		tree = {bestFeat: {}}
		restFeat = np.delete(features, np.where(features == bestFeat)[0][0])
		# print restFeat

		for value in car[bestFeat].unique():
			Dv = self.split(data, bestFeat, value)
			if Dv.shape[0] == 0:
				tree[bestFeat][value] = self.maxCntFeat(data), 0
			else:
				tree[bestFeat][value] = self.createTree(self.split(data, bestFeat, value), restFeat)

		return tree


	def train(self, x, y):
		pass

	def predict(self, x, y):
		pass
