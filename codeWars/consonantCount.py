#!/usr/bin/env python3

'''
Write a function that takes a string of English-language text and returns
the number of consonants in the string.
Consonants = all letters excluding the vowels a, e, i, o, u.
'''


# Solution 1
import string

def consonant_count(s):
    # Trims all whitespace from string
    s = s.translate(None, string.whitespace)

    num_vowels = 0
    num_nonAlpha = 0

    vowels_list = "aeiouAEIOU"
    for vowel in vowels_list:
        num_vowels += s.count(vowel)

    for char in s:
        if not char.isalpha():
            num_nonAlpha += 1

    return len(s) - num_vowels - num_nonAlpha


# Solution 2
def consonant_count(s):
    return sum(1 for char in s if char.isalpha() and char.lower() not in "aeiou")
