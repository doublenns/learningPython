#!/usr/bin/env python3

'''
List comprehensions are often described as being more "Pythonic" than
loops or map().
Main benefit of using a list comprehension in Python is that it's a single tool
that can use in many different situations. In addition to standard list creation,
list comprehensions can also be used for mapping and filtering; don't have to use
a different approach for each scenario.
'''


numbers = [1,2,3]

# For Loop
loop_doubled = []
for num in numbers:
    loop_doubled.append(num * 2)
print(f"For loop: {loop_doubled}")

# List comprehension that does the same thing
'''
Rather than creating an empty list and adding each element to the end,
simply define the list and it's contents at the same time using the formats:
`new_list = [expression for member in iterable (if conditional)]`
`new_list = [expression (if conditional) for member in iterable]`

"iterable" - a list, set, sequence, generator, or any other object that
returns its elements one at a time.

Because the "expressions" requirement is so flexible, a list comprehension
works well in many places where a map() might be used. Main distinction is
that the list comprehension returns a list, not a map object.
'''
lc_doubled = [num * 2 for num in numbers]
print(f"List comprehension: {lc_doubled}")



friends = ["Justin", "Chris", "Tim", "Tiffany", "Terrell", "Carl"]

# For Loop
loop_starts_with_t = []
for friend in friends:
    if friend.startswith("T"):
        loop_starts_with_t.append(friend)
print(f"For loop: {loop_starts_with_t}")

# List Comprehension
lc_starts_with_t = [friend for friend in friends if friend.startswith("T")]
print(f"List Comprehension: {loop_starts_with_t}")


# If need a more complex conditional filter, can move the conditional logic
# to a separate function - https://realpython.com/list-comprehension-python/
sentence = 'The rocket, who was named Ted, came back \
    from Mars because he missed his friends.'

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonants = [i for i in sentence if is_consonant(i)]


# If want to change a member value instead of filtering it out, useful to
# place the conditional near the beginning of the expression.
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(f"List comprehension with element modification: {prices}")

# Above is the same as below:
def get_price(price):
    return price if price > 0 else 0
prices = [get_price(i) for i in original_prices]
print(f"List comprehension with element modification: {prices}")