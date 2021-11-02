/*
HackerRank C (Conditionals and Loops) Practice   
Q5 : Printing Pattern Using Loops

Sedat Ali ZEVİT
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n;
    scanf("%d", &n);
  	// Complete the code to print the pattern.
    
    //Each length of the numbers in cube ->  2*number - 1
    int len = n*2 - 1;
    
    for(int i=0;i<len;i++){
        for(int j=0;j<len;j++){
            
            // Minimum difference between vertical & horizontal sides
            int min = i < j ? i : j;
            
            // Minimum difference between vertical sides 
            min = min < len-i ? min : len-i-1;
            
            // Minimum difference between horizontal sides 
            min = min < len-j-1 ? min : len-j-1;
            
            printf("%d ", n-min);
        }
        printf("\n");
    }  
    
    return 0;
}