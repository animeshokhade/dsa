# question --> https://www.hackerrank.com/challenges/capitalize/copy-from/252815860
# default
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

    # my_code
    for i in range(len(s)):
        if (i != 0):
            if s[i].islower() == True:
                if s[i - 1] == ' ':
                    s = s[:i] + s[i].upper() + s[i + 1:]
        else:
            s = s[0].upper() + s[1:]
    return s

# default
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# end