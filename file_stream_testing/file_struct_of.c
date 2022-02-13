#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int main(){
    char * ptr = malloc(0x500);
    char * ptr2 = malloc(0x50);
    free(ptr);
    char * ptr3 = malloc(0x50);
    char * ptr4 = malloc(0x50);
    strcpy(ptr4,"AAAAAAAA");
}