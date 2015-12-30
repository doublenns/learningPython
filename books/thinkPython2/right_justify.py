#!/usr/bin/env python3

import sys


def right_justify(s):

    ''' Function that takesa string and prints the string w/ enough
    leading spaces so that the last letter of the string is in column
    70 of the display.
    '''

    length = len(s)
    whitespace_multiplier = 70 - length
    print(" " * whitespace_multiplier + s)


try:
    right_justify(sys.argv[1])
except Exception:
    print('You did not pass the script an argument.')
