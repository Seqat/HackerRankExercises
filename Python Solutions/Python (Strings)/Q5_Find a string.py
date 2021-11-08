

"""
HackerRank Python Practice   
Q5 : Find a String

Sedat Ali ZEVİT
"""

import  re

def count_substring(string, sub_string):
    
    #create a regular expression rule with sub string
    p = re.compile('(?=({}))'.format(sub_string))
    
    #apply the rule & find patterns
    matches = re.finditer(p, string)
    

    #give the results
    return len([(i.group(1), i.start()) for i in matches]) 
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
