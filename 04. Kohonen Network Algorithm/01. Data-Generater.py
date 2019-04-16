"""
Code: Kohonen Network Algorithm
Title: Dataset Generater
Author: Azmain Yakin Srizon
"""

from numpy import binary_repr # Adding binary conversion library

filename = 'Final-Data.csv'
log = open(filename, 'w')  # creating csv file

data = []

input_line = 5 # define input lines

for i in range (0,int(pow(2,input_line))): # generating data as binary form
    tmp = list(binary_repr(i,input_line))
    data.append(tmp) # adding to data

for i in range(0,input_line-1): # generating column names of csv file
    log.write(str(i+1)+',')
log.write(str(i+2)+'\n')
    
c = 0
for i in data: # adding data to csv file
    for j in i:
        c = c+1
        log.write(str(j)) # adding value in each column for a row
        if c!=input_line:
            log.write(',')
        else:
            c=0
    log.write('\n') # go to next row

log.close() # closing the csv file