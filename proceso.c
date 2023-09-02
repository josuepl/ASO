#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(){
 int pid;
 if((pid = fork())== 0){//HIJO
  printf("HIJO-> vPID:%d, PID:%d, PPID:%d\n",pid, getpid(), getppid());
  if((pid = fork())== 0){//NIETO
  printf("NIETO-> vPID:%d, PID:%d, PPID:%d\n",pid, getpid(), getppid());
 }
 else{//PADRE-HIJO
  sleep(1);
  printf("PADREH-> vPID:%d, PID:%d, PPID:%d\n",pid, getpid(), getppid());
  }
 }
 else{//PADRE
  sleep(1);
  printf("PADRE-> vPID:%d, PID:%d, PPID:%d\n",pid, getpid(), getppid());
  if((pid = fork())== 0){//HIJO
   printf("HIJO-> vPID:%d, PID:%d, PPID:%d\n",pid, getpid(), getppid());
  }
  else{//PADRE
   sleep(1);
   printf("PADRE-> vPID:%d, PID:%d, PPID:%d\n",pid, getpid(), getppid());
  }

 }
 
 return 0;
}
