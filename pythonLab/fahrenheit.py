#!/usr/bin/env python3
#
'''
Simple program to convert a user-inputted temperature
from Celcius to Fahrenheit
'''

# Note: This makes the print fucntion work the same
# in both Python 2 and Python 3
from __future__ import print_function

# Put there to help convert to zero, but not implemented yet
import math

# Note: This makes the input fucntion work the same
# in both Python 2 and Python 3
try:
    input = raw_input
except NameError:
    pass

import datetime

temperature_ranges = {
    "January":    (-5, 5),
    "February":   (-5, 5),
    "March":      (-5, 5),
    "April":      (-5, 5),
    "May":        (-5, 5),
    "June":       (-5, 5),
    "July":       (-5, 5),
    "August":     (-5, 5),
    "September":  (-5, 5),
    "October":    (-5, 5),
    "November":   (-5, 15),
    "December":   (-5, 5)
}


# def round()

# User input wrapped in input validation
while True:
    input_temp = input("What is the temperature in Fahrenheit? ")
    if input_temp.isdecimal():
       break
    else:
        print("Please enter the temperature in numeric characters only.\n")

fahrenheit = int(input_temp)
celsius = ((fahrenheit - 32) / 1.8)
# Can also use .tcnow to give GMT time so consistenet across systems and
# not affected by daylight savings time
currentmonth = datetime.datetime.now().month
print(currentmonth)
now = datetime.datetime.now()
print('Python thinks the current month abbreviation is:', now.strftime("%b"))
print('Python thinks the current month name is:', now.strftime("%b"))


output_template =  "Celsius: {CL:.2f} * is equal to * Fahrenheit: {FH:.2f}"
output = output_template.format(FH=fahrenheit, CL=celsius)
# Can only put a placeholder inside of a string. Is a placeholder for a variable

print(output)

print("\nCelcius:", round(celsius, 2), "* is equal to *" , "Fahrenheit:", fahrenheit )



# Input is different in Python 2 and Python 3
    # In Python 2, accepts input as a program and tries to execute it
# Division is different in Python 2 and Python 3
    # In Python 2, division truncates by default (e.g. Int division)
