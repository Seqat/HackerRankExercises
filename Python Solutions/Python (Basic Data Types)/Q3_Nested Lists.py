"""
HackerRank Python (Basic Data Types) Practice   
Q3 : Nested Lists

Sedat Ali ZEVİT
"""

if __name__ == '__main__':
    
    #Create an empty list
    lst=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        #append each values
        lst.append([name,score])
    

    #sort list based on grades, if grades are same sort in alphabetically order
    lst.sort(key = lambda x: (x[1],x[0]))
    

    #find the second highest score
    second_highest = sorted(set(j for i,j in lst))[1]
    

    #prints the second lowest graded students
    print("\n".join(sorted(i for i,j in lst if j==second_highest)))


