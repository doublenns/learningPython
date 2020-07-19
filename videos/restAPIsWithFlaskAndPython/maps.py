#!/usr/bin/env python3

'''
Example taken from Real Python
https://realpython.com/list-comprehension-python/
'''

transactions = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08

def get_price_with_tax(txn):
    price_with_tax = txn * (1 + TAX_RATE)
    return round(price_with_tax, 2)


# For loop
loop_final_prices = []
for transaction in transactions:
    loop_final_prices.append(get_price_with_tax(transaction))
print(loop_final_prices)


# Map
'''
Pass in a function and an iterable. 'map()' will then create an object.
This object contains the output you would get from running each iterable
element through the supplied function. Can easily convert the map object
into a list using 'list()'.
'''
map_final_prices = map(get_price_with_tax, transactions)
print(list(map_final_prices))


def doubled(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubled = map(doubled, sequence)
print(sequence)
print(list(doubled))