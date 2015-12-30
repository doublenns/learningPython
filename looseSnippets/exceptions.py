#!/usr/bin/env python3

'''In except (catch-all) blocks, the raise statement can be used w/o arguments
to re-raise whatever exception occured.
Code within the finally statement runs no matter what error occurs -- after
execution of the code in the try, and possibly in the except blocks.'''


try:
    num = 5 / 0
except:
    print("Except statement: An error occurred")
    raise
finally:
    print("Finaly: This code will be ran regardless")

# The code after the error handling won't be ran because of the raise
# which causes the program to immediately stop, just as regular Exceptions do.
print("This is code outside of the exception handling")
