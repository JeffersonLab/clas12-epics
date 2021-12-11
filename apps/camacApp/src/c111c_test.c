
/* c111c_test.c */

#include <stdio.h>
#include <stdlib.h> 
#include <unistd.h> 
#include <fcntl.h> 
#include <string.h> 
#include <pthread.h>

#include "c111cLib.h"

//#define DEBUG

int ll = 0;
void profile();
int r1 = 0;

short datain, dataout;
int  Q;
int numc = 0;

int
main(int argc, char *argv[])
{
  pthread_t thread1;
  int i, j, crate_id;
  int resp, items_per_row, total_items;
  char blk_ascii_buf[2048];
  unsigned int blk_transf_buf[300];
  short N, A, F;

  int sock;
  
  printf("Starting profiling thread ...\n");
  pthread_create(&thread1, NULL, (void *)profile, &r1);
  
  printf("Connecting...\n");
  
  /* Open connection with a Camac controller*/
  sock = ccconnect("129.57.160.156",2000);
  printf("%d\n",sock);
  if(sock==0)
  {
    printf("Connection failed \n");
    exit(0);
  }
  
  /*Read the data*/
  
  printf("Read data from slot7 \n");
  
  /* GANELEC CFDs FCC8

    F16A0 - write threshold to channel 0: 0<=data<=255, threshold is data/3.8mV ?
    F16A1 -                    channel 1
    F16A2 -                    channel 2
    F16A3 -                    channel 3
    F16A4 -                    channel 4
    F16A5 -                    channel 5
    F16A6 -                    channel 6
    F16A7 -                    channel 7

    F0A0 - read threshold from channel 0
    F0A1 -                     channel 1
    F0A2 -                     channel 2
    F0A3 -                     channel 3
    F0A4 -                     channel 4
    F0A5 -                     channel 5
    F0A6 -                     channel 6
    F0A7 -                     channel 7

    F16A8 - write output width A: 0<=data<=255
    F16A9 -                    B

    F0A8 - read output width A
    F0A9 -                   B

    F16A10/F0A10 - decision threshold for internal multiplicity: 0<=data<=255, data = 36.5*(M-1) where 1<=M<=8
    F16A11/F0A11 - decision threshold for total multiplicity: 0<=data<=255, data = 5.12*(M-1) where 1<=M<=50

 */




  N = 7;
  A = 0;

  /*
  F = 16;
  datain = 85;
  resp = CNAF16(sock, N, A, F, &Q, &datain);
  printf(" [%d] ======> resp=%d, Q=%d, N=%d, A=%d, F=%d, datain=%d\n",ll,resp,N,A,F,Q,datain);
  if (resp != 0)
  {
    printf("ERROR: Negative response from socket server\n");
    exit(0);
  }
  
  */
  while(1)
  {
    ll++;
    numc++;

    F = 0;
    resp = CNAF16(sock, N, A, F, &Q, &dataout);
#ifdef DEBUG
    printf(" [%d] ======> resp=%d, Q=%d, N=%d, A=%d, F=%d, dataout=%d\n",ll,resp,N,A,F,Q,dataout);
#endif
    if (resp != 0)
    {
      printf("ERROR: Negative response from socket server\n");
      exit(0);
    }

#ifdef DEBUG
    sleep(1);    
#endif
  }
}

void
profile()
{
  int sl = 1;
  while(1)
  {
    sleep(sl);
    printf("commands %6d, Q = %1d, dataout = %3d, rate = %d Hz\n",numc,Q,dataout,ll/sl);
    ll=0;
  }
}
