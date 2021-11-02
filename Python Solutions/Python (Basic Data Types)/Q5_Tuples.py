"""
HackerRank Python (Basic Data Types) Practice   
Q4 : Tuples

Sedat Ali ZEVİT


!!! WARNING: This solution is tested by Pypy3 in HackerRank. I didn't check it's working with any Python version. !!!

"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    #creating the tuple
    t = tuple(integer_list)
    
    #hashing the tuple
    print(hash(t));