"""
HackerRank Problem Solving: Basic  Practice  (in Python3) 
Q8 : Birthday Cake Candles

    You are in charge of the cake for a child's birthday. You have decided the cake 
will have one candle for each year of their total age. They will only be able to blow 
out the tallest of the candles. Count how many candles are tallest.



Sedat Ali ZEVİT
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    
    
    result=0
    #Find the maximum height of candle
    maxi = max(candles)
    
    for i in range(len(candles)):
        #If the candle height is same as maximum height candle,                # increment result
        
        if(candles[i]==maxi):
            result=result+1
    
    #retuns the result value
    return result
    


# Main Code
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()
