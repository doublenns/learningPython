#!/usr/bin/env python3

import turtle
import sys
import math


def usage():
    print("Please pass a radius as an int to the script.")
    sys.exit()


def polygon(t, length, n):
    for i in range(n):
        angle = 360 / n
        t.fd(length)
        t.lt(angle)


def center_circle(t, r):
    t.pu()
    t.rt(90)
    t.fd(r)
    t.lt(90)
    t.pd()


def circle(t, r):
    center_circle(t, r)

    circumference = 2 * math.pi * r
    n = 100
    length = circumference / n
    polygon(t, length, n)


try:
    radius = int(sys.argv[1])
except Exception:
    usage()

bob = turtle.Turtle()
circle(bob, radius)
turtle.mainloop()
