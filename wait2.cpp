#include <iostream>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

using namespace std;
int main(){
    pid_t pa, pb, pc;
    if((pa = fork()) == 0){//Hijo A
        cout<<"HIJOA ->"<<getpid()<<" - "<<getppid()<<endl;
    }
    else{//padre
        waitpid(pa, NULL, 0);
        if((pb = fork()) == 0){//Hijo B
            cout<<"HIJOB ->"<<getpid()<<" - "<<getppid()<<endl;
            if((pc = fork()) == 0){//Nieto C
                cout<<"NIETOC ->"<<getpid()<<" - "<<getppid()<<endl;
            }else{
                waitpid(pc,NULL,0);
                //cout<<"HIJOB ->"<<getpid()<<" - "<<getppid()<<endl;
            }
        }
        else{//padre
            waitpid(pb, NULL, 0);
            cout<<"PADRE ->"<<getpid()<<" - "<<getppid()<<endl;
        }
    }
    return 0;
} 
