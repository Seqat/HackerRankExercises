
/*
HackerRank C (Introduction) Practice   
Q2 : Playing with Characters

Sedat Ali ZEVİT
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    //Defining inputs
    char ch;
    char s[100];
    char newline[100];
    
    //Taking the characters in STDIN. Be careful about "\n" in each inputs!!
    scanf("%c\n",&ch);
    scanf("%[^\n]%*c", s);     
    scanf("%[^\n]%*c", newline);    
    
    //Prints the results
    printf("%c\n",ch);
    printf("%s\n",s);
    printf("%s\n",newline);
    
    return 0;
}