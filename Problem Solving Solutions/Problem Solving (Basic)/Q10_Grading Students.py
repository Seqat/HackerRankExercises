
"""
HackerRank Problem Solving: Basic  Practice  (in Python3) 
Q10 : Grading Students

Sam is a professor at the university and likes to round each student's grade according to these rules:

Rule 1:
-> If the difference between the grade and the next multiple of 5 is less than 3, 
round grade up to the next multiple of 5.

Rule 2:
-> If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.



Sedat Ali ZEVİT
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    

    for i in range(len(grades)):

        #Check Rule 2. If grade is less than 38, do nothig
        if(grades[i]<38):
            continue
        
        else:
            #calculate upper grade
            upper_grade = 5* ((int(grades[i])//5)+1)

            #Check the Rule 1 , if it satisfies the condition, update the grade
            if(upper_grade-grades[i]<3):
                grades[i]=grades[i]+(upper_grade-grades[i])
    
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
