#!/usr/bin/env python3

# FizzBuzz!
# Prints the numbers from 1 to 10 with "fizz" for
# multiples of 3, and "buzz" for multiples of 5



def generate_fizz_buzz(limit):
    i = 0
    while i < limit:
        if not (i % 3) and not (i % 5):
            yield(i,"FizzBuzz")
        elif (i % 3) == 0:
            yield "Fizz"
        elif not (i % 5):
            yield  "Buzz"
        else:
            yield i

        i += 1

fizzbuzzer = generate_fizz_buzz(100)
for output in fizzbuzzer:
    print(output)

# Generators help avoid stack overflow by minimizing memory usage
# or to limit memory use in general, i.e. if have a 100 gb file that
# needs to be parsed on a server w/ 1 gb of RAM.
