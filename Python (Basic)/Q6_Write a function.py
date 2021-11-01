

"""
HackerRank Python Practice   
Q5 : Write a Function

Sedat Ali ZEVİT
"""

# Function decleration
def is_leap(year):

    leap = False    # Assume the input is not leap year
    
    if(year%400 ==0 ): # if the year is divisible by 400 , it's leap year
        leap=True
    
    elif(year%100 ==0 ): # if the year is divisible by 100 , it's not leap year
        leap=False   
        
    elif(year%4 ==0 ): # if the year is divisible by 4 , it's leap year
        leap=True    
        
        
    return leap # return the result
#End of function

# Main Code

year = int(input())
print(is_leap(year)) # Function calls & print the result