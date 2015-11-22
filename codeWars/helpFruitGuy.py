#!/usr/bin/env python3

'''
Fruit guy has a bag_of_fruits of fruits (array of strings) where some fruits are rotten.
He wants to replace all the rotten fruits with good ones.
For example, given the array ["apple","rottenBanana","apple"] the replaced
array should be ["apple","banana","apple"].
Implement method that will take as an argument an array of strings containing
fruits & return array of strings with only good fruit.
'''

'''
Note: If the array is null or empty you should return empty array ([]).
The returned array should be in LOWER case.
'''

bag = []
bag2 = ["rottenApple", "rottenBanana", "Catelope", "rottenPineapple", "Kiwi"]


def remove_rotten(bag_of_fruits):
    # Checks to see if input is empty. If it is, returns empty list
    if not bag_of_fruits:
        return []

    for i in range(len(bag_of_fruits)):
        if "rotten" in bag_of_fruits[i]:
            bag_of_fruits[i] = bag_of_fruits[i][6:]
        bag_of_fruits[i] = bag_of_fruits[i].lower()

    return(bag_of_fruits)


print(remove_rotten(bag))
