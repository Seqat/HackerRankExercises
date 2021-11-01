

"""
HackerRank Python Practice   
Q1 : List Comprehension

Sedat Ali ZEVİT
"""



if __name__ == '__main__':
    #Taking values
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

#Creating list with list comprehensions based on the requirements    
lst= [[i, j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n ]

#print list
print(lst)