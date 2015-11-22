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
    """This method should return the single value"""
    if not (number % 3) and not (number % 5):
        return("BOTH")
    elif (number % 3) == 0:
        return("THREE")
    elif not (number % 5):
        return("FIVE")
    else:
        return(number)


def getNumberRange(first, last):
    if (last < first):
        step = -1
    else:
        step = 1

    result = []
    for i in range(first, last+step, step):
        result.append(getNumber(i))
    return result


'''
Test Case:
    tests=[(0,"BOTH"),
    (1,1),
    (2,2),
    (3,"THREE"),
    (4,4),
    (5,"FIVE"),
    (10,"FIVE"),
    (15,"BOTH"),
    (18,"THREE"),
    (19,19),
    (30,"BOTH"),
    (150,"BOTH"),
    (-1,-1),
    (-3,"THREE"),
    (-15,"BOTH"),
    (-50,"FIVE"),
    ]

    for input, expected in tests:
        Test.assert_equals(getNumber(input), expected);

    # test_getNumberRange

    tests=[(1,15,[1,2,"THREE",4,"FIVE","THREE",7,8,"THREE","FIVE",11,"THREE",13,14,"BOTH"]),
        (1,-15,[1,"BOTH",-1,-2,"THREE",-4,"FIVE","THREE",-7,-8,"THREE","FIVE",-11,"THREE",-13,-14,"BOTH"]),
    ]

    for first, last, expected in tests:
        Test.assert_equals(getNumberRange(first, last), expected);
'''

# Note to self: Need to learn how to do TDD
