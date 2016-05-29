#!/usr/bin/env python3

'''
Fibonacci Numbers under 35

To-do:
* Allow for user to input Fibonacci numbers upper limit
* Print differently? CSV?
'''

# Uses multiple assignment
a, b = 0, 1
while b < 35:
	print(b)
	a, b = b, a + b
