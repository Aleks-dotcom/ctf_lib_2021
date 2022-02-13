#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

signed long RANCTX = 0xf1ea5eed;
signed long RANCTX_8 = time(NULL);
signed long RANCTX_16 = RANCTX_8;
signed long RANCTX_24 = RANCTX_8;

long ranval()
{
  long *plVar1;
  long lVar2;
  
  plVar1 = (long *)((long)RANCTX - ((ulong)RANCTX_8 >> 5 | RANCTX_8 << 0x1b));
  RANCTX = (long *)(RANCTX_8 ^ ((ulong)RANCTX_16 >> 0xf | RANCTX_16 << 0x11));
  lVar2 = (long)RANCTX + (long)plVar1;
  RANCTX_8 = RANCTX_16 + RANCTX_24;
  RANCTX_16 = RANCTX_24 + (long)plVar1;
  RANCTX_24 = lVar2;
  return lVar2;
}

int main(){
	ranval();
	printf("%ld",time(NULL));
	printf("%ld,%ld,%ld,%ld",RANCTX,RANCTX_24,RANCTX_16,RANCTX_8);
	return 0;
}

