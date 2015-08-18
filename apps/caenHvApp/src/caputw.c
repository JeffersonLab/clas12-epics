#include <stdio.h>
#include <unistd.h>

int main(int argc,char *argv[]){

unsigned long long t;
int chassi=atoi(argv[1]);
int slot=atoi(argv[2]);
int channel=atoi(argv[3]);
int command=atoi(argv[4]);
double value=atoi(argv[5]);

//double value=5.34;

unsigned long long value64;
value64 = (unsigned long long) ((double) value*100.);
printf("%lld\n", value64 );

printf("%ld %ld %ld\n",sizeof(long long), sizeof(long int), sizeof(long));

t= (chassi << 0) + (slot << 8)+(channel << 16) + (command << 24) +
   (value64 << 32);

char tmp[400];
sprintf(tmp, "caput B/HV/ALL_SET_VALUES %lld", t);

printf("%s\n", tmp);

system(tmp);


chassi= 0xff & t; t = t >> 8;
slot= 0xff & t; t = t >> 8;
channel= 0xff & t; t = t >> 8;
command= 0xff & t; t = t >> 8; 
value=(((double) t)/100.);

printf("%d %d %d %d %f\n",chassi, slot, channel, command, value);

//4000000000000000000
//printf("1\n");
return 1;

}
