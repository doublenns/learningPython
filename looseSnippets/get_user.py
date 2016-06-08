#!/usr/bin/env python3

'''
Multiple ways to get the present user of script
'''

import errno
import getpass
import os


try:
    print("User logged into the controlling terminal: [{}]".format(os.getlogin()) )
except OSError as exc:
    if exc.errno == errno.ENOENT:
        print("There is no controlling/login terminal.")
    else:
        raise
print("Effective user is: [{}]".format(getpass.getuser()) )
print("Env thinks the loginname is: [{}]".format(os.getenv('LOGNAME')) )
if os.getenv('USERNAME') is None:
    print("There is no $USERNAME var set in the env.")
else:
    print("Env thinks the username is: [{}]".format(os.getenv('USERNAME')) )
