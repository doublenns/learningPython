#!/usr/bin/env python3

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
multiples of 3 or 5 below 1000.
'''

### Solution 1 ####
# Solution simply brute force iterates thru every single int. If the iteration 
# is either a multiple of 3 of 5, it adds them to the running tally & prints 
# the sum when iteration is complete.

valueSum = 0

for i in range(1000):
    # Determine if iteration is multiple of 3 or 5.
    if not (i % 3) or not (i % 5):
        valueSum += i

print('The sum of all multiple of 3 or 5 below 1000 is:', valueSum)


'''
Potential optimizations:
    * Already know the sum of all numbers below 10 is 23. Can use range(10, 1000)
        and start the sum at 23 instead of 0.
    * Iterate less. (990 / 3) = 330. (990 / 5) = 198. (330 + 198) = 528.
        Only iterating thru multiple of 3 and 5 could cut down iterations by almost
        half.
            ~ Would have to discard sums of items that multiple of both 3 and 5
    * Math based operation to add factors more efficiently.
'''


### Solution 2 ####
# Another shorter solution which iterates less and avoids using a
# for loop. 

# The values var stores the union of the two sets of 3 and 5 factors from 0-999.
# The result is stored as a list, which is then passed to the sum function, which
# adds all the items in the list together and returns the result.

values = set(range(3,1000,3)) | set(range(5,1000,5))
print('The sum of all multiple of 3 or 5 below 1000 is:', sum(values))
# Changed the sum variable in the 1st solution so wouldn't shadow the sum function.
