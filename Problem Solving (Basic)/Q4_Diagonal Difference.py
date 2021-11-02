"""
HackerRank Problem Solving: Basic  Practice  (in Python3) 
Q4 : Diagonal Difference

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

Function description

Complete the diagonalDifference() function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers

--Return--

int: the absolute diagonal difference


Sedat Ali ZEVİT
"""




#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    j=-1
    
    left=0
    right =0 
    
    for i in range(n):
        left = left + arr[i][i]
        right= right + arr[i][j]
        j=j-1
    
    return abs(left-right)


#Main Code
#  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()