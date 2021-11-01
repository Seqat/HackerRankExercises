

"""
HackerRank Python Practice   
Q2 : Find the Runner-Up Score! 

Sedat Ali ZEVİT
"""



if __name__ == '__main__':
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    arr=set(arr)
    
    arr.remove(max(arr))
    
    print(max(arr))

