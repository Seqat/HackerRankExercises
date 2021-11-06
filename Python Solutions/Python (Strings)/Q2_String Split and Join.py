
"""
HackerRank Python Practice   
Q2 : String Split (.split()) and Join(.join())

Sedat Ali ZEVİT
"""

def split_and_join(line):
    # write your code here

    #   First, split string each " ", then join each element 
    # with "-", then return the result
    
    return "-".join(line.split())
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)