#include <stdio.h>

int main(){
	int a = 0;
	int b = 0;
	while(b < 141){
		a = a + (66 | 207) + ((66 & 207) - b);
		b++;
	}
	printf("%d",a);
	return 0;
}
	