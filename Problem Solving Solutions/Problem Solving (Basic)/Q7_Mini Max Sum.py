"""
HackerRank Problem Solving: Basic  Practice  (in Python3) 
Q7 : Mini Max Sum

    Given five positive integers, find the minimum and maximum values that can be calculated by 
summing exactly four of the five integers. Then print the respective minimum and maximum 
values as a single line of two space-separated long integers.



Sedat Ali ZEVİT
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    
    #minimum sum = sum of all elements - maximum element
    minimum = sum(arr)- max(arr)

    #maximum sum = sum of all elements - minimum element
    maximum = sum(arr)- min(arr)
    
    #prints the results
    print(minimum, maximum)
    

#Main Code
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
