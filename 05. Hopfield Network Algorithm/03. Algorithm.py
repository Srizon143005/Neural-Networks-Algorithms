"""
Code: Hopfield Network Algorithm
Title: Algorithm Implementation
Author: Azmain Yakin Srizon
"""

# adding necessary libraries
import pandas

df = pandas.read_csv('Train-Data.csv') # reading the training csv

filename = 'Log-Training.log' 
log = open(filename, 'w') #creating training log file

input_nodes = int(df.size/len(df)) # calculating number of inputs
f_h = 0.5 # threshold

weights = [] # initializing weights by 0
for i in range(input_nodes):
    tmp = []
    for j in range(input_nodes):
        tmp.append(0.0)
    weights.append(tmp)

inputs = [] # reading inputs
for j in range(0, len(df)):
    tmp=[]
    for i in range(0,input_nodes):
        tmp.append(df[str(i+1)][j])
    inputs.append(tmp)
    
for i in range(0,input_nodes): # calculating weights, training phase
    for j in range(0,input_nodes):
        for k in inputs:
            weights[i][j]=weights[i][j]+k[i]*k[j]

log.write(str(weights)) # printing weights in training log
log.close() # closing train log

df = pandas.read_csv('Test-Data.csv') # reading test csv

filename = 'Log-Testing.log'
log = open(filename, 'w') # creating test log

inputs = [] # reading inputs
for j in range(0, len(df)):
    tmp=[]
    for i in range(0,input_nodes):
        tmp.append(df[str(i+1)][j])
    inputs.append(tmp)

for k in inputs: # for each input
    main = k
    log.write('Given Input: ' + str(main) + '\n')
    while(1):
        prev = k
        for i in range(0,len(k)):
            tmp = 0
            for j in range(0,input_nodes): 
                tmp = tmp + weights[i][j]*k[j] # calculate summation
            if tmp<f_h: # hard thresholding - no
                k[i]=-1
            else: # hard thresholding - yes
                k[i]=1
        if prev == k: # matches? then break
            log.write('Best Match: ' + str(prev) + '\n\n') # writing in test log
            break

log.close() # closing test log