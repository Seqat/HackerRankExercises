"""
HackerRank Problem Solving: Basic  Practice  (in Python3) 
Q6 : Staircase

Its base and height are both equal to integer N . 
It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size N .

Example:

When N = 4:

OUTPUT (Hymens are showing for whitespaces):

---#
--##
-###
####


Sedat Ali ZEVİT
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(n):
        for j in range(n):
            
            if i+j+2 > n:
                print("#",end="")
                
            else:
                print(" ",end="")
                
        print("")        

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
