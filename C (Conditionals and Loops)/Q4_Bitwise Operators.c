/*
HackerRank C (Conditionals and Loops) Practice   
Q4 : Bitwise Operator

Sedat Ali ZEVİT
*/


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
    //Initialize variables
    int i,j;
    int temp_and=0,temp_or=0,temp_xor=0;
    int max_and=temp_and, max_or=temp_or, max_xor=temp_xor;

    for(i=1;i<n;i++){
    
        for(j=i+1;j<=n;j++){
        
        //if a & b < k && a & b > max, max_and = a&b
        temp_and = i&j;
        if(temp_and<k && temp_and>max_and){
            max_and=temp_and;
        }

        //if a|b < k &&  a|b > max, set max_or = a|b        
        temp_or = i|j;        
        if(temp_or<k &&temp_or>max_or){
            max_or=temp_or;
        }        
        
        //if a^b < k &&  a^b > max, set max_xor = a^b
        temp_xor = i^j;        
        if(temp_xor<k &&temp_xor>max_xor){
            max_xor=temp_xor;
        }       
        //end of innerfor loop 
        }
    //end of outer for loop
    }
    printf("%d\n%d\n%d",max_and,max_or,max_xor);
}

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k); 
    return 0;
}

