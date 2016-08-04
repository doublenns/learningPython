#!/usr/bin/env python

import subprocess

def run_shell_cmd(cmd, *shell):
    # Might want to use a "try" or call.check in case Command fails
    if "shell" in shell:
        process = subprocess.Popen(cmd,
                stdout=subprocess.PIPE, shell=True)
    else:
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
