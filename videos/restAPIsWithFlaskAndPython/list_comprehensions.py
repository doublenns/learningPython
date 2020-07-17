#!/usr/bin/env python3

numbers = [1,2,3]

# For Loop
loop_doubled = []
for num in numbers:
    loop_doubled.append(num * 2)
print(f"For loop: {loop_doubled}")

# List comprehension that does the same thing
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