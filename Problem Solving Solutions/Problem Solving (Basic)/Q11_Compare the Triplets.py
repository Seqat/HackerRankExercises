"""
HackerRank Problem Solving: Basic  Practice  (in Python3) 
Q11 : Compare the Triplets

    Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, 
awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and 
difficulty.

The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's 
challenge is the triplet b = (b[0], b[1], b[2]).

The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] 
with b[2].

Rules:
-> If a[i] > b[i], then Alice is awarded 1 point.

-> If a[i] < b[i], then Bob is awarded 1 point.

-> If a[i] = b[i], then neither person receives a point.


Comparison points is the total points a person earned.

Given a and b, determine their respective comparison points.

Sedat Ali ZEVİT
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    
    score_a=0
    score_b=0
    
    for i in range(len(a)):
        
        #If Alice's number is bigger, give 1 point at Alice's score
        if(a[i]>b[i]):
            score_a += 1
        
        #If Bob's number is bigger, give 1 point at Bob's score        
        elif (a[i]<b[i]):
            score_b += 1
        
        #If it's equal, no points 
        else:
            continue
    
    #returns the result in list form
    return [score_a,score_b];
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
