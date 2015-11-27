#!/usr/bin/env python3

'''
Create a function that checks if a number is odd.

Expect negative and decimal numbers too. For negative numbers, return true if
its absolute value is odd. For decimal numbers, return true only if the number
is equal to its integer part and the integer part is odd.

Examples:
is_odd(5)--> true
is_odd(4)--> false
is_odd(-17)--> true
is_odd(-7.0)--> true
is_odd(4.23)--> false
'''

# Original Solution
def is_odd(n):
    whole = float(n).is_integer()
    odd = n % 2
    return False if not odd or not whole else True


# Simplest, shortest solution
def is_odd(n):
    return n % 2 == 1


# Can return boolean by passing expression that evaluates to a boolean
def is_odd(n):
    return n == int(n) and n % 2


# Another way to write "if.. else expression"
def is_odd(n):
   return [False,True][n % 2 == 1]
