#!/usr/bin/python3

# Short program that counts the number of occurances of each letter in a string.

import pprint

message = 'It was all a dream; I used to read Word Up! Magazine.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

# pprint() "pretty prints" a dictionary's value
pprint.pprint(count)

# If want to obtain the prettified text as string value instead of displaying it
# the screen, call pprint.pformat() instead.

# The following 2 lines are equivalent to each other:
# pprint.pprint(someDictionaryValue)
# print(pprint.pformat(someDictionaryValue)


'''
Program loops over each char in message's string, counting how often each char
appears. The setdefault() method call ensures that the key is in the count
dictionary, w/ the default value of 0.
Done so that the program doesn't throw a KeyError error when
count[character] += 1 is executed.
'''
