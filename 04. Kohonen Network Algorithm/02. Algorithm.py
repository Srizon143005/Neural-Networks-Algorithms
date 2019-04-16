"""
Code: Kohonen Network Algorithm
Title: Algorithm Implementation
Author: Azmain Yakin Srizon
"""

# adding necessary libraries
import pandas
import random

df = pandas.read_csv('Final-Data.csv') # reading csv file

input_nodes = int(df.size/len(df)) # calculating number of input nodes
output_nodes = 20 # calculating numbe rof output nodes
eta = 0.9 #define eta

# initializing weights
weights = []
for i in range(0,input_nodes):
    tmp = []
    for j in range(0,output_nodes):
        tmp.append(0.1*random.randint(1,10))
    weights.append(tmp)

# initializing neighbors
neighbor = []
for i in range(0, output_nodes):
    neighbor.append(10)

# reading the inputs
inputs = []
for j in range(0, len(df)):
    tmp=[]
    for i in range(0,input_nodes):
        tmp.append(df[str(i+1)][j])
    inputs.append(tmp)

filename = 'Log-Training.log'
log = open(filename, 'w') # creating log file
winner_nodes = [] # set of winner nodes

for k in inputs: # for each input
    minimum_distance = 999999999999999999999999
    winning_node = 0
    for j in range(0,output_nodes): # selection of output node
        distance = 0
        for i in range(0,input_nodes): # selection of input node
            distance = distance + (k[i]-weights[i][j])*(k[i]-weights[i][j]) # calculating distance
        if distance < minimum_distance: # find out minimum distance node
            minimum_distance = distance
            winning_node = j # winner node
            winner_nodes.append(winning_node)
    log.write('Input: ' + str(k) + ', Winner node: ' + str(winning_node) + '\n') # writing the result
    
    # updating weights for winner node
    for i in range(0,input_nodes):
        weights[i][winning_node] = weights[i][winning_node] + eta*(k[i]-weights[i][winning_node])
    
    # updating weights for neighbors in left of winner nodes
    for j in range(1, neighbor[winning_node]+1):
        for i in range(0,input_nodes):
            if winning_node-j>=0:
                weights[i][winning_node-j] = weights[i][winning_node-j] + eta*(k[i]-weights[i][winning_node-j])
    
    # updating weights for neighbors in right of winner nodes
    for j in range(1, neighbor[winning_node]+1):
        for i in range(0,input_nodes):
            if winning_node+j<output_nodes:
                weights[i][winning_node+j] = weights[i][winning_node+j] + eta*(k[i]-weights[i][winning_node+j])
    
    # decreasing value of neighbour and eta
    if neighbor[winning_node]>1:
        neighbor[winning_node] = neighbor[winning_node]-1
    eta = eta-0.02
    
log.close() # closing log file