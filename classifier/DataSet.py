import pandas as pd

class DataSet:

	def __init__(self, dataFrame, class_col='class'):
		self.dataFrame = pd.DataFrame(dataFrame)
		self.labels = dataFrame[class_col]
		feats = dataFrame.columns
		self.features = feats[feats != class_col]
		self.names = dataFrame.index

	def info(self):
		print 'labels:', self.labels.unique()
		print 'features', self.features.values
		print 'names', self.names.values
		print 'data', self.dataFrame.info()


class RawData(DataSet):

	def __init__(self, dataFrame, class_col='class'):
		super(dataFrame, class_col)

	def __split__(self, ):
		pass

	def __sample__(self):
		pass


class TrainingData(DataSet):
	def __init__(self, dataFrame, class_col='class'):
		super(dataFrame, class_col)


class ValidateData(DataSet):
	def __init__(self, dataFrame, class_col='class'):
		super(dataFrame, class_col)


class TstData(DataSet):
	def __init__(self, dataFrame, class_col='class'):
		super(dataFrame, class_col)

if __name__ == '__main__':

	f = open('test.txt', 'r')
	d = DataSet(pd.read_table(f), class_col='sex')
	d.info()