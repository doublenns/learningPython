#!/usr/bin/env python3

import turtle
import sys
import math


def polyline(t, n, length, angle):
'''Draws n line segments w/ given length and
angle (in degrees) between them. t is a turtle'''
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


try:
    r = int(sys.argv[1])
    angle = int(sys.argv[2])
except Exception:
    print("You didn't enter all the required parameters to run the script")
    sys.exit()

bob = turtle.Turtle()
arc(bob, r, angle)
turtle.mainloop()
