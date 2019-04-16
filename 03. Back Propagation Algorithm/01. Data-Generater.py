"""
Code: Back Propagation Algorithm
Title: Dataset Generater
Author: Azmain Yakin Srizon
"""

from numpy import binary_repr

filename = 'Final-Data.csv'
log = open(filename, 'w')

data = []

# defining input and output nodes
input_line = 10
output_line = 2

# calculating all possible inputs
for i in range (0,int(pow(2,input_line))):
    tmp = list(binary_repr(i,input_line))
    data.append(tmp)

# creating column names
for i in range(0,input_line):
    log.write(str(i+1)+',')
log.write('class\n')

# creating dataset
for i in data:
    for j in i:
        log.write('' + str(j) + ',')
    log.write("'")
    for j in range(0,output_line):
        if int(i[j])!=0:
            log.write('1') # class A
        else:
            log.write(str(i[j])) # class B
    log.write("'" + '\n')

log.close() # closing csv