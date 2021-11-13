/*
HackerRank C (Introduction) Practice   
Q6 : Functions

Sedat Ali ZEVİT
*/

#include <iostream>
#include <cstdio>
using  std::printf , std::scanf;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(int a,int b,int c, int d){
    
    int max1,max2;

    max1 =a<b ? b:a;
    max2 =c<d ? d:c;

return max1<max2 ? max2 : max1;    
    
    
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}