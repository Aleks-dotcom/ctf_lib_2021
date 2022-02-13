#include <stdio.h>
#include <stdlib.h>

int *arbitrary_pointer = NULL;

int main()
{
    int *our_pointer = NULL;

    int *a = malloc(8);

    free(a);
    
    a[0] = (unsigned long long) &arbitrary_pointer;

    malloc(8);
    our_pointer = malloc(8);
    return 0;
}



