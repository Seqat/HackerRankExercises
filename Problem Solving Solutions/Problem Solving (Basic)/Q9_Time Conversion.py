
"""
HackerRank Problem Solving: Basic  Practice  (in Python3) 
Q9 : Time Conversion

    Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.



Sedat Ali ZEVİT
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    #Splits string based on ":", and creates a list like ['Hour','Minute','Second(AM/PM)']
    x = s.split(":", 3)
    
    #Take the "AM/PM" part
    a=x[2]


    b=a[:2:]
    a=a[2::]

    #Revise the list like ['Hour','Minute','Second']
    x.remove(x[2])
    x.append(b)

    
    print(x)
    
    if(int(x[0])<=11 and int(x[0])>=1 and a=="PM"):
        x[0]=str(int(x[0])+12)
        return(":".join(x))        
    
    elif(int(x[0])==12 and a=="AM"):
        x[0]=str(int(x[0])-12) + "0"
        
        return(":".join(x))
    
    else:
        return(":".join(x))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    
    fptr.write(result + '\n')
    fptr.close()
