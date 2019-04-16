"""
Code: Hopfield Network Algorithm
Title: Dataset Generater
Author: Azmain Yakin Srizon
"""

from numpy import binary_repr # Adding binary conversion library
import random

filename = 'Final-Data.csv'
log = open(filename, 'w')  # creating csv file

data = []

input_line = 60 # define input lines

# creating dataset
numbers = []
for i in range(0,52,int(60/18)):
    numbers.append(int(pow(2,i))+random.randint( int(pow(2,i-1)),int(pow(2,i))))
    

for i in numbers: # generating data as binary form
    tmp = list(binary_repr(i,input_line))
    data.append(tmp) # adding to data

for i in range(0,input_line-1): # generating column names of csv file
    log.write(str(i+1)+',')
log.write(str(i+2)+'\n')
    
c = 0
for i in data: # adding data to csv file
    for j in i:
        c = c+1
        if int(j)==0:
            j=-1
        log.write(str(j)) # adding value in each column for a row
        if c!=input_line:
            log.write(',')
        else:
            c=0
    log.write('\n') # go to next row

log.close() # closing the csv file