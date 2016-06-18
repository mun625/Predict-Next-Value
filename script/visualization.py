import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def ListToGraph(intList):
	if type(intList) != list:
		raise ValueError("A sequence's type should be list")
	if not all(isinstance(n, int) or isinstance(n, long) for n in intList):
		raise ValueError("The element of sequence should be integer type")
	plt.plot(intList)
	plt.ylabel('value')
	plt.show()

train_data = pd.read_csv('./data/train.csv')

start_index = 0
last_index = 5

for index in range(start_index, last_index+1):
	my_list = train_data.iloc[index]['Sequence'].split(',')
	my_list = map(int,my_list)
	ListToGraph(my_list)