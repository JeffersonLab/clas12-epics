#include <stdio.h>
#include <unistd.h>


int main(){

unsigned long long t;
int chassi=255;
int slot=255;
int channel=255;
int command=255;
double value=9998888.34;

unsigned long long value64;
value64 = (unsigned long long) ((double) value*100.);
printf("%lld\n", value64 );

printf("%ld %ld %ld\n",sizeof(long long), sizeof(long int), sizeof(long));

t= (chassi << 0) + (slot << 8)+(channel << 16) + (command << 24) +
   (value64 << 32);
 
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
