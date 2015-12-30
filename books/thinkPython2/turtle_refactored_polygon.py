#!/usr/bin/env python3

import turtle
import sys


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)


try:
    length = int(sys.argv[1])
    n = int(sys.argv[2])
except Exception:
    print("You didn't enter all the required parameters to run the script")
    sys.exit()

bob = turtle.Turtle()
# Use of keyword arguments allow the input vars to be in an arbitrary order
polygon(bob, length=length, n=n)
turtle.mainloop()
