"""
Code: Back Propagation Algorithm
Title: Train-Test Dataset Generator
Author: Azmain Yakin Srizon
"""

import pandas
import random

train_percentage = 0.2

filename = 'Train-Data.csv'
train_file = open(filename, 'w') # creating train csv

filename = 'Test-Data.csv'
test_file = open(filename, 'w') # creating test csv

df = pandas.read_csv('Final-Data.csv') # reading dataset
train_elements = int(train_percentage*len(df))
test_elements = len(df)-train_elements
train = []
test = []

# take random rows and enter in train set
tmp = train_elements
while(tmp!=0):
    a = random.randint(0,len(df)-1)
    if a not in train:
        train.append(a)
        tmp=tmp-1

# Take the remaining samples in test set
for i in range(0,len(df)):
    if i not in train:
        test.append(i)

# calculating features
a = df.size
b = len(df)
features = int(a/b)

# creatig column names
for i in range(0,features-1):
    train_file.write(str(i+1)+',')
train_file.write('class\n')

# creating rows one by one
for i in train:
    for j in range(0,features-1):
        train_file.write(str(df[str(j+1)][i]))
        train_file.write(',')
    train_file.write(str(df['class'][i]))
    train_file.write('\n')

train_file.close() # closing train file


# creating column names for test 
for i in range(0,features-1):
    test_file.write(str(i+1)+',')
test_file.write('class\n')

# creating rows one by one for test
for i in test:
    for j in range(0,features-1):
        test_file.write(str(df[str(j+1)][i]))
        test_file.write(',')
    test_file.write(str(df['class'][i]))
    test_file.write('\n')

test_file.close() # closing test file
