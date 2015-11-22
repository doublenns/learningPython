#!/usr/bin/env python3

# Return the number (count) of vowels in the given string.
# Consider a, e, i, o, and u as vowels


# Solution 1
# Forgot to test for uppercase Vowels
# Could have made list of vowels a string instead of tuple
def getCount(s):
    num_vowels = 0
    vowels_list = ("a", "e", "i", "o", "u")
    for vowel in vowels_list:
        num_vowels += s.count(vowel)
    return num_vowels


# Solution 2
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")
