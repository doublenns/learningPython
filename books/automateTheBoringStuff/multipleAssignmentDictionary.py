#!/usr/bin/python3

'''
This is an example of using multiple assignment in a for loop
to assign a key and value to separate variables
'''

# Creating spam, which is a dictionary
spam = {'color': 'red', 'age': 26, 'name': 'DoubleNNs'}

# Using multiple assignment for the k and v variables and printing them
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))
