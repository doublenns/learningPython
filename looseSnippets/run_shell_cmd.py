#!/usr/bin/env python

import subprocess

def run_shell_cmd(cmd, *shell):
    process = subprocess.Popen(cmd.split(),
            stdout=subprocess.PIPE)
    output = process.communicate()[0]
    rc = process.returncode
    return output, rc

# Output will include the newline in it
output = (run_shell_cmd("echo hello")[0])
returncode = (run_shell_cmd("echo hello")[1])

print "The output of the shell command is:", output
print "The return code of the shell command is:", returncode
