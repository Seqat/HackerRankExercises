

"""
HackerRank Python (Basic Data Types) Practice   
Q2 : Find the Runner-Up Score! 

Sedat Ali ZEVİT
"""



if __name__ == '__main__':
    
    #Taking the inputs
    n = int(input())    
    
    arr = list(map(int, input().split()))
    
    #set() function removes repetitve values and sorts in ascending order
    arr=set(arr)    
    
    #remove max value to find runner-up score
    arr.remove(max(arr)) 
    

    #prints runner up score
    print(max(arr)) 



