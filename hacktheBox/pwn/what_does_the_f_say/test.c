#include <stdio.h>
#include <stdlib.h>

int main(){
    puts("hello world");
    int * a = (int *)malloc(sizeof(int));
    *a = 10;
    printf("this is a: %d",*a);
    return 0;
}