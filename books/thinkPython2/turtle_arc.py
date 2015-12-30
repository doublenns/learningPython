#!/usr/bin/env python3

import turtle
import sys
import math


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


bob = turtle.Turtle()
try:
    arc(bob, r=int(sys.argv[1]), angle=int(sys.argv[2]))
except Exception:
    print("You didn't enter all the required parameters to run the script")
    sys.exit()

turtle.mainloop()
