"""
HackerRank Python (Basic Data Types) Practice   
Q4 : Lists

Sedat Ali ZEVİT
"""


if __name__ == '__main__':
    
    N = int(input())
    
    #create variables
    lst=[]

    command=[]

    for x in range(N):
        #taking commands and splits based on whitespaces " "
        command  =  str(input()).split()
        
        #Check which operation is requested, and executed
        if command[0]=="append":
            lst.append(int(command[1]))
        
        elif command[0] == "remove":
            lst.remove(int(command[1]))
        
        elif command[0] == "print":
            print(lst)
        
        elif command[0] == "insert":
            lst.insert(int(command[1]),int(command[2]))
        
        elif command[0] == "sort":
            lst.sort()
        
        elif command[0] == "pop":
            lst.pop()
        
        elif command[0] == "reverse":
            lst.reverse()
        
        else:
            continue   
        
