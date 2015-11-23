#!/usr/bin/env python3

'''
Create a function named divisors that takes an integer and returns
an array with all of the integer's divisors(except for 1 and the
number itself).
If the number is prime return the string: '(integer) is prime'
'''


# Solution 1
def divisors(i):
    from math import ceil
    arr = []

    for num in range(2, int(ceil(i / 2)) + 1):
        if not i % num:
            arr.append(num)

    return arr if arr else str(i) + ' is prime'


# Solution 2
def divisors(num):
    l = [a for a in range(2, num) if num % a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l
