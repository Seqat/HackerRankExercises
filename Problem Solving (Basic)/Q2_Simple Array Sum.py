
"""
HackerRank Problem Solving: Basic  Practice  (in Python3) 
Q2 : Simple Array Sum

Given an array of integers, find the sum of its elements.

Complete the simpleArraySum function in the editor below. 
It must return the sum of the array elements as an integer.

simpleArraySum has the following parameter(s):

ar: an array of integers


Sedat Ali ZEVİT
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()



