#!/usr/bin/env python3

import turtle
import sys


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


bob = turtle.Turtle()
try:
    square(bob, int(sys.argv[1]))
except Exception:
    print("You didn't enter a correct argument to create the square.")
    sys.exit()

turtle.mainloop()
