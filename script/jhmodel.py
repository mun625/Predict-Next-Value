import numpy as np
from sklearn import linear_model

class Model:
	def __init__(self):
		self.next_value = 0
		self.main_sequence = []

	def set(self, seq):
		self.main_sequence = seq

	def Checker(self, comp_seq):
		print self.LinearChecker(comp_seq)
		self.PolynomialChecker(comp_seq)

	# Check if there is a linear relation between sequences.
	def LinearChecker(self, comp_seq):
		regr = linear_model.LinearRegression()
		X = np.array(comp_seq, dtype = 'float_').reshape(-1, 1)
		Y = np.array(self.main_sequence, dtype = 'float_').reshape(-1, 1)

		if len(X) < len(Y):
			return 0
		else:
			X = X[0:len(Y)]

		regr.fit(X,Y)
		#coefficients = [regr.coef_, regr.intercept_]
		return regr.score(X,Y)

	def PolynomialChecker(self, comp_seq):
		pass