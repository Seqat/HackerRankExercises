"""
HackerRank Problem Solving: Basic  Practice  (in Python3) 
Q5 : Plus Minus

Given an array of integers, calculate the ratios of its elements that are positive, 
negative, and zero. Print the decimal value of each fraction on a new line with 
places after the decimal.


Sedat Ali ZEVİT
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here

    # Define the variables
    positive=0
    negative=0
    zeros=0

    #Loops in length of the arr
    for i in range(len(arr)):
        #if the value is positive, increment it
        if(arr[i]>0):
            positive = positive + 1
        #if the value is negative, increment it
        elif(arr[i]<0):
            negative = negative +1
        #if the value is zero, increment it
        else:
            zeros = zeros +1
    
    #Print the ratios
    print(positive/len(arr))
    
    print(negative/len(arr))
    
    print(zeros/len(arr))

#Main Code

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

