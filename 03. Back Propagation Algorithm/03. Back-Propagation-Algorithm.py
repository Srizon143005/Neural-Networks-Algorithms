"""
Code: Back Propagation Algorithm
Title: Main Algorithm
Author: Azmain Yakin Srizon
"""

# importing necessary libraries
import pandas
import random
import math

# reading training data
df = pandas.read_csv('Train-Data.csv')

# defining input, hidden and output lines
input_line = int(df.size/len(df))-1
output_line = len(list(df['class'][0]))-2
hidden_line = 5

# defining parameters
k1 = 0.5
k2 = 0.5
eta1 = 0.5
eta2 = 0.5

weight_ij = []
weight_jk = []

threshold_j = []
threshold_k = []

output_i = []
output_j = []
output_k = []

deltaw_ij = []
deltaw_jk = []
deltau_j = []
deltau_k = []

# initializing weights from input to hidden
for i in range(0,input_line):
    tmp = []
    for j in range(0, hidden_line):
        tmp.append(0.1*random.randint(1,10))
    weight_ij.append(tmp)

# initializing thresholds of hidden nodes
for j in range(0,hidden_line):
    threshold_j.append(0.1*random.randint(1,10))

# initializing weights from hidden to output
for j in range(0,hidden_line):
    tmp = []
    for k in range(0, output_line):
        tmp.append(0.1*random.randint(1,10))
    weight_jk.append(tmp)

# initializing thresholds of output nodes
for k in range(0,output_line):
    threshold_k.append(0.1*random.randint(1,10))


#   Training...
steps = 0
inputs = 0
error_handled = False # used for error handling

filename = 'Log-Training.log'
train_log = open(filename, 'w') # open train log

# writing in train log - the general logs
train_log.write('Number of Input Nodes: ' + str(input_line) + '\n')
train_log.write('Number of Hidden Nodes: ' + str(hidden_line) + '\n')
train_log.write('Number of Output Nodes: ' + str(output_line) + '\n')

train_log.write('Initial Weights: \n')
train_log.write('Weight from i to j: ' + str(weight_ij) + '\n')
train_log.write('Weight from j to k: ' + str(weight_jk) + '\n')

train_log.write('Initial Thresholds: \n')
train_log.write('Threshold of j layer: '+ str(threshold_j) + '\n')
train_log.write('Threshold of k layer: '+ str(threshold_k) + '\n')
train_log.write('\n\n')

while inputs<len(df): # for each input
    steps = steps + 1 # calculating the steps
    
    # taking present input
    input_i = []
    for i in range(0,input_line):
        input_i.append(df[str(i+1)][inputs])
    
    # taking present output
    output_i = []
    for i in input_i:
        output_i.append(i)
    
    # calculating net_j
    net_j = []
    for j in range(0,hidden_line):
        tmp = 0.0
        for i in range(0,input_line):
            tmp = tmp + weight_ij[i][j]*output_i[i]
        net_j.append(tmp)
    
    # calculating activ_j
    activ_j = []
    for j in range(0,hidden_line):
        activ_j.append(net_j[j]+threshold_j[j])
        
    # calculating output_j
    output_j = []
    for j in range(0,hidden_line):
        output_j.append(1.0/(1.0+math.exp(-k1*activ_j[j])))
    
    # calculating net_k
    net_k = []
    for k in range(0, output_line):
        tmp = 0.0
        for j in range(0, hidden_line):
            tmp = tmp + weight_jk[j][k]*output_j[j]
        net_k.append(tmp)
    
    # calculating activ_k
    activ_k = []
    for k in range(0,output_line):
        activ_k.append(net_k[k]+threshold_k[k])
    
    # calculating output_k
    output_k = []
    for k in range(0,output_line):
        output_k.append(1.0/(1.0+math.exp(-k2*activ_k[k])))
    
    # reading targets
    target = []
    a = df['class'][inputs]
    a = list(a)
    for i in a:
        if i!="'":
            target.append(int(i))
    
    # calculating errors
    error = 0.0
    for k in range(0,output_line):
        error = error + 0.5*(target[k]-output_k[k])*(target[k]-output_k[k])
    
    # calculating one by one error
    delta_k = []
    for k in range(0,output_line):
        delta_k.append(target[k]-output_k[k])
    
    # if error happens
    if error>0.2:
        # update weight among hidden and output
        deltaw_jk = []
        for j in range(0,hidden_line):
            tmp = []
            for k in range(0,output_line):
                tmp.append(0.0)
            deltaw_jk.append(tmp)
        
        for j in range(0,hidden_line):
            for k in range(0,output_line):
                deltaw_jk[j][k] = eta2*k2*delta_k[k]*output_j[j]*output_k[k]*(1-output_k[k])
        
        for j in range(0,hidden_line):
            for k in range(0,output_line):
                weight_jk[j][k] = weight_jk[j][k] + deltaw_jk[j][k]
        
        # update thresholds of output nodes
        deltau_k = []
        for k in range(0,output_line):
            deltau_k.append(eta2*k2*delta_k[k]*output_k[k]*(1-output_k[k]))
        
        for k in range(0,output_line):
            threshold_k[k] = threshold_k[k] + deltau_k[k]
        
        # update weights among input and hidden
        deltaw_ij = []
        for i in range(0,input_line):
            tmp = []
            for j in range(0,hidden_line):
                tmp.append(0.0)
            deltaw_ij.append(tmp)
        
        for i in range(0,input_line):
            for j in range(0,hidden_line):
                tmp = 0.0
                for k in range(0,output_line):
                    tmp = tmp + delta_k[k]*weight_jk[j][k]
                deltaw_ij[i][j] = eta1*k1*output_i[i]*output_j[j]*(1-output_j[j])*tmp
        
        for i in range(0,input_line):
            for j in range(0,hidden_line):
                weight_ij[i][j] = weight_ij[i][j] + deltaw_ij[i][j]
                
        # update thresholds of hidden nodes
        deltau_j = []
        for j in range(0,hidden_line):
            tmp = 0.0
            for k in range(0,output_line):
                tmp = tmp + delta_k[k]*weight_jk[j][k]
            deltau_j.append(eta1*k1*output_j[j]*(1-output_j[j])*tmp)
        
        for j in range(0,hidden_line):
            threshold_j[j] = threshold_j[j] + deltau_j[j]
        
        error_handled = True # error handling
        
    else:
        if error_handled == True:
            error_handled = False
            if inputs!=0:
                inputs = 0 # go to first step
            else:
                inputs = inputs + 1 # go to next sample
        else:
            inputs = inputs + 1 # go to next sample

    # write down every parameters
    train_log.write('Step No: ' + str(steps) + '\n')
    train_log.write('Current Input: ' + str(input_i) + '\n')
    train_log.write('Net of j layer: ' + str(net_j) + '\n')
    train_log.write('Activ of j layer: ' + str(activ_j) + '\n')
    train_log.write('Output of j layer: ' + str(output_j) + '\n')
    train_log.write('Net of k layer: ' + str(net_k) + '\n')
    train_log.write('Activ of k layer: ' + str(activ_k) + '\n')
    train_log.write('Output of k layer: ' + str(output_k) + '\n')
    train_log.write('Delta_W from j to k layer: ' + str(deltaw_jk) + '\n')
    train_log.write('Updated Weight from j to k layer: ' + str(weight_jk) + '\n')
    train_log.write('Delta_U of k layer: ' + str(deltau_k) + '\n')
    train_log.write('Updated Threshold of k layer: ' + str(threshold_k) + '\n')
    train_log.write('Delta_W from i to j layer: ' + str(deltaw_ij) + '\n')
    train_log.write('Updated Weight from i to j layer: ' + str(weight_ij) + '\n')
    train_log.write('Delta_U of j layer: ' + str(deltau_j) + '\n')
    train_log.write('Updated Threshold of j layer: ' + str(threshold_j) + '\n')
    train_log.write('Target Output: ' + str(target) + '\n')
    train_log.write('Delta of k layer: ' + str(delta_k) + '\n')
    train_log.write('Current Error: ' + str(error) + '\n\n\n')
    
train_log.close() # closing train log


#   Testing...
df = pandas.read_csv('Test-Data.csv') # reading test data

filename = 'Log-Testing.log'
test_log = open(filename, 'w') # creating testing log

# write initial parameters valiue in test log
test_log.write('Adjusted Weight from i to j layer: ' + str(weight_ij) + '\n')
test_log.write('Adjusted Threshold of j layer: ' + str(threshold_j) + '\n')
test_log.write('Adjusted Weight from j to k layer: ' + str(weight_jk) + '\n')
test_log.write('Adjusted Threshold of k layer: ' + str(threshold_k) + '\n\n')

errors = []
right = 0
wrong = 0
inputs = 0

# apply the same algorithm again without error handling
while inputs<len(df):
    steps = steps + 1
    
    input_i = []
    for i in range(0,input_line):
        input_i.append(df[str(i+1)][inputs])
    
    output_i = []
    for i in input_i:
        output_i.append(i)
    
    net_j = []
    for j in range(0,hidden_line):
        tmp = 0.0
        for i in range(0,input_line):
            tmp = tmp + weight_ij[i][j]*output_i[i]
        net_j.append(tmp)
    
    activ_j = []
    for j in range(0,hidden_line):
        activ_j.append(net_j[j]+threshold_j[j])
        
    output_j = []
    for j in range(0,hidden_line):
        output_j.append(1.0/(1.0+math.exp(-k1*activ_j[j])))
    
    net_k = []
    for k in range(0, output_line):
        tmp = 0.0
        for j in range(0, hidden_line):
            tmp = tmp + weight_jk[j][k]*output_j[j]
        net_k.append(tmp)
    
    activ_k = []
    for k in range(0,output_line):
        activ_k.append(net_k[k]+threshold_k[k])
    
    output_k = []
    for k in range(0,output_line):
        output_k.append(1.0/(1.0+math.exp(-k2*activ_k[k])))
    
    target = []
    a = df['class'][inputs]
    a = list(a)
    for i in a:
        if i!="'":
            target.append(int(i))
    
    error = 0.0
    for k in range(0,output_line):
        error = error + 0.5*(target[k]-output_k[k])*(target[k]-output_k[k])
    errors.append(error)
    
    flag = True
    for k in range(0,output_line):
        if int(target[k])!=int(round(output_k[k])): # rounding the output and matching
            flag = False
            break
    
    if flag == True:
        right = right + 1 # calculating correct predictions
    else:
        wrong = wrong + 1 # calculating wrong predictions
    
    inputs = inputs + 1
    
    # writing all parameters values
    test_log.write('Current Input: ' + str(input_i) + '\n')
    test_log.write('Target Output: ' + str(target) + '\n')
    test_log.write('Calculated Output: ' + str(output_k) + '\n')
    test_log.write('Error: ' + str(error) + '\n')
    if flag == True:
        test_log.write('Correctness: ' + 'Correct' + '\n')
    else:
        test_log.write('Correctness: ' + 'Not Correct' + '\n')
    test_log.write('\n')

test_log.write('\n\n')
test_log.write('Number of Right Prediction: ' + str(right) + '\n')
test_log.write('Number of Wrong Prediction: ' + str(wrong) + '\n')
test_log.write('Accuracy: ' + str(float(right/(right+wrong)*100.0)) + '\n')

avg = 0.0
for i in errors:
    avg = avg + i
avg = avg/(right+wrong) # calculating average error

test_log.write('Average Error: ' + str(avg) + '\n') # writing average error
test_log.close() # closing test log
print('Right: ' + str(right)) # printing number of rights
print('Wrong: ' + str(wrong)) # printing number of wrongs
