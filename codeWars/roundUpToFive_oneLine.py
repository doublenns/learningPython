#!/usr/bin/env python3

# Given an integer as input, round it to the next 5

'''
Examples:
input:    output:
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30

Input may be any positive or negative integer (including 0).
'''


def round_to_next5(n):
    return n + (5 - n) % 5

print(round_to_next5(-7))
