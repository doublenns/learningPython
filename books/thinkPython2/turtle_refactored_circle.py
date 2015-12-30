#!/usr/bin/env python3

import turtle
import sys
import math


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def circle(t, r):
    arc(t, r, 360)


bob = turtle.Turtle()
try:
    circle(bob, r=int(sys.argv[1]))
except Exception:
    print("You didn't enter all the required parameters to run the script")
    sys.exit()

turtle.mainloop()
