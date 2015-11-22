#!/usr/bin/env python3

# Function to round (up or down) an input (can be int or float)
# to the nearest 5.
# Base can be changed to round it to another number instead of 5

def myround(x, base=5):
    return int(base * round(float(x)/base))
