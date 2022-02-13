#include <stdio.h>

int main(){
    int a = 0;
    int i; 
    while(i < 10){
        a = i++;
        printf("to je a: %d\n",a);
        printf("to je i: %d\n",i);
    }
    return 0;
}