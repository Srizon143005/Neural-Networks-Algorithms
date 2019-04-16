"""
Code: Hopfield Network Algorithm
Title: Train-Test Dataset Generater
Author: Azmain Yakin Srizon
"""

# importing necessary libraries
import pandas as pd
import numpy as np

df = pd.read_csv('Final-Data.csv') # reading in dataframe
msk = np.random.rand(len(df)) < 0.49 # 50-50 in train test
train = df[msk] # define train
test = df[~msk] # define test

train.to_csv('Train-Data.csv', index = None, header=True) # write train
test.to_csv('Test-Data.csv', index = None, header=True) # write test