#!/usr/bin/env python3

# Adds asterisks as bullet points to the beginning of each line
# of text from the file specified.

# Use sample.txt from same folder to run script

'''
Todo:
    * Print usage if no file specified
    * Iterate through the list and print the lines w/ bulletpoints
    * Iterate thru the list and join results back into single string
'''

import sys

# Defined a function to read file instead of keeping inside script body, moreso for practice
def readFile(x):
    with open(x, "r") as f:
        t = f.read()
    return t


file = sys.argv[1]
text = readFile(file)

print("\nThe following is how the file gets saved as a single string (raw output):")
print(repr(text) + '\n')    # repr here used to attempt to print the raw string, preserving newline chars


# Seperate lines based on newline char
lines = text.split('\n')
print("The following is how the file gets saved as a list after splitting the string (note empty element at end):")
print(lines,'\n')     # repr() here isn't neccessary


print("The following is how the file gets outputted w/ iteration and bulletpoints:")
for i in range(len(lines)):     #loop thru al indexes in the "lines" list
    lines[i] = '* ' + lines[1]  # add star to each string in "lines" list



print("The following is how the file gets outputted when iterated thru then joined back into a single string")
