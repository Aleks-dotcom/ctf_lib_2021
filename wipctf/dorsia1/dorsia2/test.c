#include "stdio.h"
#include "stdlib.h"

void main(){
    int i;
    for(;;){
        puts("hello world");
        scanf("%d",&i);
        if(i > 5) break; puts("delam po break");
    }
}