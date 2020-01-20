#include "caen1190.h"

int main(int argc,char *argv[]) {
	unsigned int ii,jj;
    unsigned int data[NCHANS][MAXHITSPERCHAN];
    unsigned int len[NCHANS];
    caen1190_init();
    caen1190_read((unsigned int*)data,len);
    for (ii=0; ii<NCHANS; ii++) {
        printf("MAIN: %d\n",len[ii]);
        for (jj=0; jj<len[ii]; jj++) {
            printf("MAIN: %d %d %u\n",ii,jj,data[ii][jj]);
        }
    }
    return(0);
}
