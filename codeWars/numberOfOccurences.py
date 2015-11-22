#!/usr/bin/env python3

'''
The numberOfOccurrences function must return the number of occurrences of an 
element (s)  in an array (xs).
'''


def number_of_occurrences_solution1(s, xs):
    count=0
    for i in xs:
        if i == s:
            count += 1
    return count


def number_of_occurrences_solution2(s, xs):
    return xs.count(sO
