#!/usr/bin/env python

'''
    Example script to install packages using yum Python API, such as to
    fulfill the deps for a script.
'''

import yum

yb=yum.YumBase()
inst = yb.rpmdb.returnPackages()
installed = [x.name for x in inst]

# The list of packages below can be changed
packages = [
                "nc",
                "chrony",
                "sysstat"
]

for package in packages:
    if package in installed:
        print("{0} is already installed".format(package))
    else:
        kwarg = {'name':package}
        yb.install(**kwarg)
        yb.resolveDeps()
        yb.buildTransaction()
        print('Installing {0}'.format(package))

yb.processTransaction()
