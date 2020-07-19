#!/usr/bin/env python3

'''
Simplified use case for dictionary comprehensions
'''

users = [
    (0, "Bob", "password"),
    (1, "Ralph", "hunter2"),
    (2, "Jose", "long4assword"),
    (4, "username", "1234"),
]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect")