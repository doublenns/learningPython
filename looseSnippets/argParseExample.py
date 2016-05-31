#!/usr/bin/env python3

'''
Example script on using the Argparse module
'''

import argparse


parser = argparse.ArgumentParser()

oses = ["Linux", "L",
    "Windows", "Win", "W",
    "Solaris", "SunOS", "S"]

parser.add_argument("-n", "--name",
    help = "Input a string for the script to use as name.")
parser.add_argument("-o", "--os", type = str.capitalize, choices=oses,
    help = "Give the script an OS.")
parser.add_argument("-p", "--port", type=int,
    help = "Input a number for the script to use as the port.")
parser.add_argument("-v", "--verbosity", action="store_true",
    help = "Turn script verbosity on")

args = parser.parse_args()

if args.verbosity:
    print("Verbosity has been turned ON")
    print("The arguments passed to this script are: ", end="")
print(args)
