#!/usr/bin/env python3

# FizzBuzz!
# Prints the numbers from 1 to 10 with "fizz" for
# multiples of 3, and "buzz" for multiples of 5


def print_fizz_buzz(i, limit):

    if not (i % 3) and not (i % 5):
        print(i, "FizzBuzz")
    elif (i % 3) == 0:
        print(i, "Fizz")
    elif not (i % 5):
        print(i, "Buzz")
    else:
        print(i)
    if(i < limit):
        print_fizz_buzz(i + 1, limit)

print_fizz_buzz(1, 100)


# Python's max loop bound is about 1000 by default, otherwise
# overflows the stack and bails.
