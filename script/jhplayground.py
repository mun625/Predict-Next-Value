import pandas as pd
import numpy as np
import jhmodel


train_data = pd.read_csv('./data/train.csv')
test_data = pd.read_csv('./data/test.csv')

model = jhmodel.Model()
#mo.set([3,2,1,0])
#mo.Checker([9,6,3,0])

model.set(test_data.iloc[0]['Sequence'].split(','))
count = 0
for row in test_data.iterrows():
	model.Checker(row[1]['Sequence'].split(','))
	count += 1
	print count