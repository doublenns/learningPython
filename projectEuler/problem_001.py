#!/usr/bin/env python3

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
multiples of 3 or 5 below 1000.
'''

# Solution simply brute force iterates thru every single int. If the iteration 
# is either a multiple of 3 of 5, it adds them to the running tally & prints 
# the sum when iteration is complete.

sum =0

for i in range(1000):
    if not (i % 3) or not (i % 5):
        sum += i

print('The sum of all multiple of 3 or 5 below 1000 is:', sum)
