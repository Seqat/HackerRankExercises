/*
HackerRank C (Introduction) Practice   
Q4 : Functions in C

Sedat Ali ZEVİT
*/

#include <stdio.h>

//define function prototype
int max_of_four(int,int,int,int);

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(int a,int b, int c, int d){
    
    int big1, big2;
    
    //Find bigger number of the first two 
    if (a<b){
        big1 =b;
    }
    else{
        big1=a;
    }
    
    //Find bigger number of the last two 
    if (c<d){
        big2 =d;
    }
    else{
        big2=c;
    }
    
    //Find the biggest number of the four and returns it 
    if (big2<big1){
        return big1;
    }
    else{
        return big2;
    }
    
}


int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

