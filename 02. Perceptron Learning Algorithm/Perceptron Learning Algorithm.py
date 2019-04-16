"""
Algorithm Title: The Perceptron Learning Algorithm
Author: Azmain Yakin Srizon
"""


# importing necessary libraries
from numpy import binary_repr # for converting into binary
import random # for generating random numbers


# Specifications
input_line = 7 # defining number of input lines
print('Input Lines: ' + str(input_line)) # printing number of inputs
number_of_elements = pow(2,input_line) # calculating maximum number of inputs


# Making inputs
inputs = []
classes = []

i = 0
for i in range(0,number_of_elements):
    tmp = list(binary_repr(i,input_line)) # convert each number to binary list
    if tmp[0]=='0':
        classes.append('0') # defining class A
    else:
        classes.append('1') # defining class B
    inputs.append(tmp) # adding class
    i = i+1



# Making Train & Test Sets
train = []
train_class = []
test = []
test_class = []

train_percentage = 0.6 # set the train percentage
test_percentage = 1-train_percentage # calculating test percentage

tmp = int(train_percentage*(number_of_elements)) # calculating how many in train
print('In Train: ' + str(tmp)) # print number of train elements
print('In Test: ' + str(number_of_elements-tmp)) # print number of test elements
i = tmp
while i!=0:
    a = random.randint(0,tmp) # generating random numbers
    if inputs[a] not in train:
        train.append(inputs[a]) # adding to train data
        train_class.append(classes[a]) # adding class to train class
        i = i-1

train.sort() # sorting train data
train_class.sort() # sorting train class

c=0
for i in inputs:
    if i not in train: # checking who is not in train
        test.append(i) # adding data to test data
        test_class.append(classes[c]) # adding class to test class
    c=c+1



# Applying the algorithm to train
weights = []
for i in range(0,input_line):
    a = random.randint(1,10) # taking random value between 1 to 10
    weights.append(float(a)/10.0) # initializing weights
print('Initial Weights: ' + str(weights))

i = 0
f_h = 0.5 # initializing threshold
count = 0
flag = 0
eeta = 0.2 # initializing multiplicative factor
while i<tmp:
    count = count + 1
    y_t = 0.0
    c = 0
    for j in train[i]:
        y_t = y_t + float(j)*weights[c] # claculating summation
        c = c+1
    if y_t < f_h: # checking with threshold
        tmp_class = 0 # assigning temporary class A
    else:
        tmp_class = 1 # assigning temporary class B
        
    if int(train_class[i])!=int(tmp_class): # error caused
        flag = 1
        if tmp_class == 0: # should be 1
            cc = 0
            for j in train[i]:
                if int(j)==1:
                    weights[cc]=weights[cc]+eeta*1.0 # update the weigths
                cc = cc+1
        else: # should be 0
            cc = 0
            for j in train[i]:
                if int(j)==1:
                    weights[cc]=weights[cc]-eeta*1.0 # update the weights
                cc = cc+1
        continue
    else:
        if flag==1: # checking if need to start from the beginning again or not
            i=0
            flag=0
            continue
        i = i+1
    
print('Weights after adjustment: ') # printing the adjusted weights
s = ''
for i in weights:
    s = s + str("{0:.1f}".format(i)) + ' '
print(s)
print('Steps required: ' + str(count)) # printing the number of steps required



# It's time to test
i = 0
f_h = 0.5 # same threshold
wrong = 0 # variable to calculate number of wrongs
while i<number_of_elements-tmp:
    y_t = 0.0
    c = 0
    for j in test[i]:
        y_t = y_t + float(j)*weights[c] # calculating summations
        c = c+1
    if y_t < f_h:
        tmp_class = 0 # predicting class A
    else:
        tmp_class = 1 # predicting class B
    
    if int(test_class[i])!=int(tmp_class):
        wrong = wrong + 1
    i = i+1

accuracy = (1.0-float(wrong)/float(number_of_elements-tmp))*100.0 # calculating accuracy
print('Prediction Accuracy: ' + str("{0:.2f}".format(accuracy)) + '%') #printing accuracy
