
/*
HackerRank C (Introduction) Practice   
Q1 : "Hello, World!" in C

Sedat Ali ZEVİT
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
	//Taking  the input string
    char s[100];
    scanf("%[^\n]%*c", &s);

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    
    //Prints the result
    printf("Hello, World!\n");
    printf("%s",s);
    
    return 0;
}