"""
Title: Nearest Neighbour Algorithm
Author: Azmain Yakin Srizon
"""
"""
Class 1: y=x*2
Class 2: y=x*5
"""

import math

# Declaring train data
train_data = [[1,2,1],[2,4,1],
              [3,6,1],[4,8,1],
              [5,10,1],[1,5,2],
              [2,10,2],[3,15,2],
              [4,20,2],[5,25,2]]

# Declaring test data
test_data = [[6,12],[7,35],
             [8,40],[9,18]]

# Calculating Euclidean distance
print('Euclidean Distance:')
for i in test_data:
    minimum_distance = 99999999999999
    selected_node = 0
    for j in train_data:
        distance = math.sqrt((j[0]-i[0])*(j[0]-i[0])+(j[1]-i[1])*(j[1]-i[1]))
        if distance < minimum_distance:
            minimum_distance = distance
            selected_node = j[2]
    print('Input: ' + str(i) + ', Predicted class: ' + str(selected_node))

# Calculating Mahattan Distance
print('\nManhattan Distance:')
for i in test_data:
    minimum_distance = 99999999999999
    selected_node = 0
    for j in train_data:
        distance = abs(j[0]-i[0])+abs(j[1]-i[1])
        if distance < minimum_distance:
            minimum_distance = distance
            selected_node = j[2]
    print('Input: ' + str(i) + ', Predicted class: ' + str(selected_node))
    
# Calculating Square Distance
print('\nSquare Distance:')
for i in test_data:
    minimum_distance = 99999999999999
    selected_node = 0
    for j in train_data:
        distance = max(abs(j[0]-i[0]),abs(j[1]-i[1]))
        if distance < minimum_distance:
            minimum_distance = distance
            selected_node = j[2]
    print('Input: ' + str(i) + ', Predicted class: ' + str(selected_node))