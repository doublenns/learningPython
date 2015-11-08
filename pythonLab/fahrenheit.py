#!/usr/bin/env python3

'''
Simple program to convert a user-inputted temperature
from Fahrenheit to Celsius
'''


# Note: This makes the print function work the same
# in both Python 2 and Python 3
from __future__ import print_function

# Note: This makes the input fucntion work the same
# in both Python 2 and Python 3
try:
    input = raw_input
except NameError:
    pass


import datetime, calendar
# math imported here to help round decimals, but not implemented yet
import math


# Ranges taken from online graph included on:
# currentresults.com/Weather/US/washington-dc-temperatures-by-month-average.php
temperature_ranges = {
    "January":    (-2, 6),
    "February":   (-1, 8),
    "March":      (3, 13),
    "April":      (8, 9),
    "May":        (14, 24),
    "June":       (19, 29),
    "July":       (22, 31),
    "August":     (21, 30),
    "September":  (17, 26),
    "October":    (10, 20),
    "November":   (5, 14),
    "December":   (0, 8)
}


# Function that rounds only to most significant digit. Wasn't useful in this program.
def round_to_1(x):
    return round(x, -int(math.floor(math.log10(abs(x)))))


# Input validation to ensure user uses only number chars:
while True:
    input_temp = input("What is the temperature in Fahrenheit? ")
    try:
       val = float(input_temp)
       print(); break
    except ValueError:
       print("*Please enter the temperature in numeric characters only.\n")

# Old Method: doesn't work on negatives or decimals since '-' and '.' aren't digits
# Note: could also use 'isdigits' instead of 'isdecimal' (I believe)
#while True:
#    input_temp = input("What is the temperature in Fahrenheit? ")
#    if input_temp.isdecimal():
#        print(); break # Print an empty line and then break out of loop
#    else:
#        print("Please enter the temperature in numeric characters only.\n")





fahrenheit = input_temp
celsius = ((float(fahrenheit) - 32) / 1.8)

# Use format to round Celsius to 2 decimal places and print the degree sign.
output_template =  "Fahrenheit: {FH}{DS} * is equal to * Celsius: {CL:.2f}{DS}"
output = output_template.format(FH=fahrenheit, CL=celsius, DS=u'\N{DEGREE SIGN}')
# Can only put a placeholder inside of a string; is a placeholder for a variable
print(output,'\n')

# Using round function to round Celsius to 2 deciml places
# print("\nCelcius:", round(celsius, 2), "* is equal to *" , "Fahrenheit:", fahrenheit )


# A way of parsing the numeric month from datetime.now, which could be useful
# when not dsplaying the result to the user.
# currentmonth = datetime.datetime.now().month
# Can also use .tcnow to give GMT time so consistenet across systems and
# not affected by daylight savings time

now = datetime.datetime.now()
# Below are 3 different ways of returning the Month Name from datetime output
month_name = calendar.month_name[now.month]
# print('The abbreviation of the current month is:', now.strftime("%b"))
# print('The current month name is:', now.strftime("%B"))
print('The current month is:', month_name)

month_temp_range = temperature_ranges[month_name]
low, high = month_temp_range


if low <= celsius <= high:
    print("This is a normal temp for this time of year")
elif celsius < low:
    print("It is unseasonably cold!")
elif celsius > high:
    print("It is rather warm!")
else:
    print("I'm mathematically impossible!")


print('The avg temperature range for this month in Washington, DC is:')
print('\t', 'Low:', str(low) + 'C','\t', 'High:', str(high) + 'C')


# Input is different in Python 2 and Python 3
    # In Python 2, accepts input as a program and tries to execute it
# Division is different in Python 2 and Python 3
    # In Python 2, division truncates by default (e.g. Int division)
