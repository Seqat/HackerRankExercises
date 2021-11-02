/*
HackerRank C (Conditionals and Loops) Practice   
Q3 : Sum of Digits of a Five Digit Number

Sedat Ali ZEVİT
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void sum_of_digits(int n){
    
    int i;
    int temp,result=0;
    
    //Loops 5 times
    for(i=0;i<5;i++){

        //Taking the last digit
        temp=n%10;

        //adding each diğit 
        result+=temp;

        //Remove the last diğit
        n/=10;
        
    }
    //Print the result
    printf("%d",result);
}

//Main Code
int main() {
	
    int n;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    
    sum_of_digits(n);
    
    return 0;
}