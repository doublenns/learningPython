#!/usr/bin/env python3

# Adds asterisks as bullet points to the beginning of each line
# of text from the file specified.


'''
Todo:
    * Read text from file into variable -- sys.argv to specify file
    * Print the 1 line string that was read in
    * Split the lines by \n but store in single var
    * Print the new var -- should be a list
    * Iterate through the list and print the lines 'normally'
    * Iterate thru the list and join results back into single string
'''

import sys

file = sys.argv[1]

 with open
   text = f.read()

print("The following is how the file gets saved as a single string:")
print(test+'\n')


# Seperate lines and add stars
lines = text.split('\n')
print("The following is how the file gets saved as a bulleted list after splitting the string:")
print(lines+'\n')


print ("The following is how the file gets outputted w/ iteration:")
for i in range(len(lines)):     #loop thru al indexes in the "lines" list
    lines[i] = '* ' + lines[1]  # add star to each string in "lines" list
