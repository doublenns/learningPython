#!/usr/bin/env python3

'''Example script on using Argparse module
'''

import argparse
import sys


def setup_args(argv=None):
    '''
    Function builds parsing object to pass to main function.

    Since option logic can get complex and even verbose, seperate it out into
    it's own separate function and then call it from the main funtion.
    '''

    oses = ["linux", "l",
        "windows", "win", "w",
        "solaris", "sunos", "s"]

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name",
        help = "Input a string for the script to use as name.")
    parser.add_argument("-o", "--os", type = str.lower, choices=oses,
        help = "Give the script an OS.")
    parser.add_argument("-p", "--port", type=int,
        help = "Input a number for the script to use as the port.")
    parser.add_argument("-v", "--verbosity", action="store_true",
        help = "Turn script verbosity on")
    return parser


def main(argv=None):
    '''
    The scripts main fucntion.

    Setting main to take in an optional "argv" argument allows calling the
    function from the interactive Python prompt.
    '''
    p = setup_args()
    args = p.parse_args()

    print(args)


if __name__ == "__main__":
    main()
