#!/usr/bin/env python3

# FizzBuzz!
# Prints the numbers from 1 to 10 with "fizz" for
# multiples of 3, and "buzz" for multiples of 5


for i in range(1, 101):
    if not (i % 3) and not (i % 5):
        print(i, "FizzBuzz")
    elif (i % 3) == 0:
        print(i, "Fizz")
    elif not (i % 5):
        print(i, "Buzz")
    else:
        print(i)


#values = set(range(3,101,3)) | set(range(5,101,5))
#print(values)
