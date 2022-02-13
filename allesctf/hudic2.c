#include <stdio.h>
#include <stdlib.h>
#include <string.h>




void echo(void)
{
  long in_FS_OFFSET;
  char local_118 [264];
  undefined8 local_10;
  
  local_10 = *(undefined8 *)(in_FS_OFFSET + 0x28);
  do {
    fgets(local_118,0x100,stdin);
    printf(local_118);
  } while( true );
}

int main(){
  echo();
  return 0;
}