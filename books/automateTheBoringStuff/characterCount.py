#!/usr/bin/python3

# Short program that counts the number of occurances of each letter in a string.

message = 'It was all a dream; I used to read Word Up! Magazine.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)

# Program loops over each char in message's string, counting how often each char
# appears. The setdefault() method call ensures that the key is in the count
# dictionary, w/ the default value of 0.
