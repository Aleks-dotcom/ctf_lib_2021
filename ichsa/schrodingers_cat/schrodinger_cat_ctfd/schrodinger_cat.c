#include <sys/ptrace.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <sys/user.h>   
#include <sys/reg.h> 
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <signal.h>
#include <semaphore.h>
#include <x86intrin.h>
#include <stdlib.h>
#include <stdint.h>
#include <pthread.h>
/*-------------Error Codes----------------*/
#define OK  (0)
#define NOFLAG (1)
#define NOFLAGADDRESS (2)
#define NOSYSCALL (3)
#define NOGENERALERROR (4)
#define NOUSERBUFFADDRESS (5)
#define NOERROR (6)
#define NOMEM (7)
#define NOFILEPATH (8)
#define NORAND ((uint32_t)-1)
/*-----------------------------------------*/
#define FLAG_ADDRESS ((void*)0x2444000ull)
#define FLAG_RANGE (0xD000ull)
#define USER_DATA_ADDRESS ((void*)FLAG_ADDRESS + (0x1000000000ull))
#define USER_DATA_SIZE (0x40*PAGE_SIZE)
#define USER_CODE_ADDRESS ((void*)((uint64_t)FLAG_ADDRESS - USER_DATA_SIZE))
#define INIT_SYSCALL_NUM (33)
#define MAX_NUMBER_DIGITS (7)

#define MUTEX "/mutex_lock"
#define OKTOWRITE "/condwrite"

pthread_mutexattr_t mutex_attr;
pthread_condattr_t cond_attr;


int read_flag(){
    int fd = open("flag.txt", O_RDONLY);
    if(fd < 0){
        printf("meow?");
        return -NOFLAG;
    }
    
    struct stat statbuf;
    int err = fstat(fd, &statbuf);
    if(err < 0){
        printf("meow??");
        return -NOFLAG;
    }
    

    int fd2 = open("/dev/urandom", O_RDONLY);
    if (fd2 < 0){
        printf("meow??");
        return -NOFLAG;
    }

    volatile uint32_t rand;
    ssize_t res = read(fd2, &rand, sizeof(rand));
    close(fd2);
    if (res < 0)
    {
      printf("meow??");
      return -NOFLAG;
    }


    volatile uint32_t page_number = rand % FLAG_RANGE;
    volatile void* hint_flag_address = FLAG_ADDRESS + (((uint64_t)page_number) << 12);
    volatile void* flag_address = mmap(hint_flag_address, statbuf.st_size, PROT_READ, MAP_PRIVATE | MAP_POPULATE , fd, 0);
    
    if(flag_address != hint_flag_address){
        printf("meow???");
        return -NOFLAGADDRESS;
    }
    close(fd);

    mprotect(flag_address, statbuf.st_size, PROT_WRITE);

    hint_flag_address = NULL;
    flag_address = NULL;
    page_number = 0;
    rand = 0;

	  return OK;
}

int run_user_payload(pthread_mutex_t* mutex, pthread_cond_t* cond, char* file_path){
    
    char* user_data = (char*)mmap(USER_DATA_ADDRESS, USER_DATA_SIZE, PROT_READ | PROT_WRITE, MAP_POPULATE | MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if(user_data != USER_DATA_ADDRESS){ 
      printf("meow?????");
      return -NOUSERBUFFADDRESS;
    }


    char* user_buf = (char*)mmap(USER_CODE_ADDRESS, 2*PAGE_SIZE, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_POPULATE | MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if(user_buf != USER_CODE_ADDRESS){ 
      printf("meow?????");
      return -NOUSERBUFFADDRESS;
    }
    

    printf("Read payload from %s\n", file_path);
    FILE* fptr = fopen(file_path, "rb");
    if(fptr == NULL){
      printf("meow????????");
      return -NOERROR;
    }

    size_t ret = fread(USER_CODE_ADDRESS, sizeof(char), 2*PAGE_SIZE, fptr);

    printf("payload size: %d\n", ret);
    fclose(fptr);

    mprotect(user_buf, 2*PAGE_SIZE, PROT_READ | PROT_EXEC);

    pthread_mutex_lock(mutex);
    pthread_cond_signal(cond);
    pthread_cond_wait(cond, mutex);
    pthread_mutex_unlock(mutex);
    
    /*clean*/
    shm_unlink(OKTOWRITE);
    shm_unlink(MUTEX);
    pthread_cond_destroy(cond);
    pthread_condattr_destroy(&cond_attr); 
    pthread_mutex_destroy(mutex);
    pthread_mutexattr_destroy(&mutex_attr);
    
    /*run payload*/  
    void(*user_func)() = (void(*)())user_buf;
    user_func();
}

int allow_syscall(long long orig_rax)
{
  switch(orig_rax){
    case 1:   //sys_write
    case 87:  //sys_unlink
    case 202: //sys_futex
    case 231: //sys_exit
      return 1;
    default:
      return 0;
  }
}

pthread_mutex_t* init_mutex(){
    pthread_mutex_t* mutex;
    int mutex_fd;
    int mode = S_IRWXU | S_IRWXG;

    mutex_fd = shm_open(MUTEX, O_CREAT | O_RDWR | O_TRUNC, mode);
    
    if (mutex_fd < 0) {
      exit(-NOERROR);
    }

    if (ftruncate(mutex_fd, sizeof(pthread_mutex_t)) == -1) {
      exit(-NOERROR);
    }
    
    mutex = (pthread_mutex_t*)mmap(NULL, sizeof(pthread_mutex_t), PROT_READ | PROT_WRITE, MAP_SHARED, mutex_fd, 0);
    
    if (mutex == MAP_FAILED ) {
      exit(-NOERROR);
    }
    
    pthread_mutexattr_setpshared(&mutex_attr, PTHREAD_PROCESS_SHARED);
    pthread_mutex_init(mutex, &mutex_attr);
    
    return mutex;
}


pthread_cond_t* init_cond(){
    pthread_cond_t* condition;
    int cond_fd;
    int mode = S_IRWXU | S_IRWXG;

    cond_fd = shm_open(OKTOWRITE, O_CREAT | O_RDWR | O_TRUNC, mode);
    
    if (cond_fd < 0) {
      exit(-NOERROR);
    }

    if (ftruncate(cond_fd, sizeof(pthread_cond_t)) == -1) {
      exit(-NOERROR);
    }
    
    condition = (pthread_cond_t*)mmap(NULL, sizeof(pthread_cond_t), PROT_READ | PROT_WRITE, MAP_SHARED, cond_fd, 0);
    
    if (condition == MAP_FAILED ) {
      exit(-NOERROR);
    }
    
    pthread_condattr_setpshared(&cond_attr, PTHREAD_PROCESS_SHARED);
    pthread_cond_init(condition, &cond_attr);
    
    return condition;
}

int main(int argc, char** argv)
{  
    pid_t child;
    long long orig_rax;
    pthread_mutex_t* mutex;
    pthread_cond_t* cond;
    
    if(argc != 2)
    {
      printf("meow?????????");
      exit(-NOFILEPATH);
    }


    mutex = init_mutex();
    cond = init_cond();
    
    child = fork();
    if(child == 0) {
        //drop_priv();
        int res = read_flag();
		    if(res != OK)
		    {
          printf("meow??????????");
			    exit(res);
		    }
        run_user_payload(mutex, cond, argv[1]);
    } else {
      int status;
      pthread_mutex_lock(mutex);
      pthread_cond_wait(cond, mutex);
      pthread_mutex_unlock(mutex);
      
      ptrace(PTRACE_ATTACH, child, 0, 0);
      
      pthread_mutex_lock(mutex);
      pthread_cond_signal(cond);
      pthread_mutex_unlock(mutex);
      
      /**/ 
      while(waitpid(child, &status, 0) && !WIFEXITED(status)) {
        
        orig_rax = ptrace(PTRACE_PEEKUSER,child,8*ORIG_RAX,NULL);
        
        if(orig_rax == -1)
        {
          fprintf(stderr, "Something went wrong... try again\n");
          exit(-NOGENERALERROR);
        }
        
        if(!allow_syscall(orig_rax)){
          fprintf(stderr, "syscalls can kill cats - %d\n", orig_rax);
          kill(child, SIGKILL);
          exit(-NOSYSCALL);
        }else{
          ptrace(PTRACE_SYSCALL,child,0,0);
        }
            
      }
    }
    return 0;
}
