#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct node_s {
	uint64_t addr;
	int * conns;
	size_t nc;
	int visited;
} node_t;

node_t *nodes = 0;
size_t numnodes = 0;


int isjump(uint64_t a, uint64_t b){
	char * ap = (char*)(&a);
	char * bp = (char*)(&b);
	int numdiffs = 0;
	if(ap[0] != bp[0]) numdiffs++;
	if(ap[1] != bp[1]) numdiffs++;
	if(ap[2] != bp[2]) numdiffs++;
	if(ap[3] != bp[3]) numdiffs++;
	if(ap[4] != bp[4]) numdiffs++;
	if(ap[5] != bp[5]) numdiffs++;
	if(ap[6] != bp[6]) numdiffs++;
	if(ap[7] != bp[7]) numdiffs++;
	if(numdiffs <= 1) return 1;
	return 0;
}

int addedge(node_t *n, int b){
	n->nc++;
	n->conns = realloc(n->conns, n->nc*sizeof(int));
	n->conns[n->nc-1] = b;
}


int genedges(void){
	int x, y;
	for(x = 0; x < numnodes; x++){
	for(y = 0; y < numnodes; y++){
		if(x == y) continue;
		if(isjump(nodes[x].addr, nodes[y].addr)) addedge(&nodes[x],y);
	}
	}
}

int innodes(uint64_t a){
	size_t i;
	for(i = 0; i < numnodes; i++){
		if(nodes[i].addr == a) return i;
	}
	return -1;
}
void clearvisited(void){
	size_t i;
	for(i = 0; i < numnodes; i++){
		nodes[i].visited = 0;
	}
}
int addnode(uint64_t addr){
	int idx = innodes(addr);
	if(idx >=0) return idx;
	numnodes++;
	nodes = realloc(nodes, numnodes*sizeof(node_t));
	nodes[numnodes-1].addr = addr;
	nodes[numnodes-1].conns = 0;
	nodes[numnodes-1].nc = 0;
	nodes[numnodes-1].visited = 0;
	return numnodes-1;
}

int loadplaces(char * filenm, uint64_t bp){
	FILE *f = fopen(filenm, "r");
	if(!f) return -1;
	unsigned int ptr;
	int i = 0;
	while( fscanf(f, "%x", &ptr) == 1){
		i++;
//		printf("%p\n", ptr);
		uint64_t np = bp + (uint64_t)ptr;
		addnode(np);
		ptr = 0;
	}
	fclose(f);
	printf("loaded %i from file\n", i);
}

//goal is index
int dfs(node_t *current, int goal, int dtg){
	if(dtg<=0) return 0;
	if(current->visited) return 0;
	current->visited = 1;

	printf("%p\n", current->addr);
	size_t i;
	for(i = 0; i < current->nc; i++){
		int tidx = current->conns[i];
		if(tidx == goal){
			printf("GOOOOAL\n");
			printf("%p\n", nodes[goal].addr);
			printf("%p\n", current->addr);
			return 1;
		}
		node_t *t = &nodes[tidx];
		if(!t->visited && dfs(t, goal, dtg-1)){
			printf("%p\n", current->addr);
			return 1;
		}
	}
	return 0;
}

void printnodes(){
	int i;
	for(i = 0; i < numnodes; i++){
		node_t j = nodes[i];
		printf("%p %i\n", j.addr, j.nc);
	}

}

int dodfs(int start, int end, int md){
	int i;
	for(i = 1; i < md; i++){
		clearvisited();
//		printf("\n");
		if(dfs(&nodes[start], end,i)) break;
	}
}


int main(int argc, char ** argv){

	if(argc<5){
		printf("Usage: %s possibles bp start end\n", argv[0]);
		return -1;
	}
	uint64_t bp = strtoll(argv[2], 0, 16);
	uint64_t sp = strtoll(argv[3], 0, 16);
	uint64_t ep  = strtoll(argv[4], 0, 16);
	loadplaces(argv[1], bp);
	int start = addnode(sp+bp);
	int end = addnode(ep+bp);
	printf("start addr %p\n", nodes[start].addr);
	printf("end addr %p\n", nodes[end].addr);
	genedges();
	printf("edges genned\n");
//	printnodes();
	dodfs(start, end, 1000);
//	dodefs(start,end, 20);
//	dodefs(end,start, 5);
	return 0;
}
