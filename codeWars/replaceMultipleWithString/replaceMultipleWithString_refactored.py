#!/usr/bin/env python3

'''
write two methods.

Method 1

The first method takes in a valid int (positive or negative)
and returns the following:

for any multiple of 3 the string "THREE",
for any multiple of 5 the string "FIVE",
for any multiple of both the string "BOTH",
for all other numbers the original int.
Method 2

The second method takes valid ints (positive or negative) and returns
a list of the values that follow the above rules.

The first value may be greater than or less than the second and the
list should increment/decrement appropriately

For example an input of 10,13 should generate a response of
['FIVE', 11, 'THREE', 13].
'''


def getNumber(number):
    return "BOTH" if number % 15 == 0 else "FIVE" if number % 5 == 0 \
        else "THREE" if number % 3 == 0 else number


def getNumberRange(first, last):
    step = 1 if first < last else -1
    return [getNumber(n) for n in range(first, last+step, step)]
