#include <stdio.h>

int main(){
    int A = 61657405;
    int B = 0;
    int C = 0;
    int program[16] = {2,4,1,2,7,5,4,3,0,3,1,7,5,5,3,0};
    while(A){
        B = A%8
        B = B^2
        C = A/(1<<B)
        B = B^C
        A = A/(8)
        B = B^7
        printf("%d\n",B%8)
        }
    return 0;
}