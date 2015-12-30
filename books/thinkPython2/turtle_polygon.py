#!/usr/bin/env python3

import turtle
import sys


def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


bob = turtle.Turtle()
try:
    polygon(bob, length=int(sys.argv[1]), n=int(sys.argv[2]))
except Exception:
    print("You didn't enter all the required parameters to run the script")
    sys.exit()

turtle.mainloop()
