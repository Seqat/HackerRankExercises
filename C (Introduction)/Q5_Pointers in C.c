
/*
HackerRank C (Introduction) Practice   
Q5 : Pointers in C

Sedat Ali ZEVİT
*/

#include <stdio.h>

//Include this library for using abs()(absolute value) function
#include<stdlib.h>

//Function declaration
void update(int *a,int *b) {
    // Complete this function 
    
    int c,d;
    
    //Storing the values temporarly
    c=*a;
    d=*b;
    
    //Changing the pointers' value depends on the requirements 
    (*a)=c+d;
    (*b)= abs(c-d);
    
}

//Main Code

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}

