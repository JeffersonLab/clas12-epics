#include <stdio.h>
#include <stdlib.h> 
#include <fcntl.h> 
#include <string.h> 
#include <pthread.h>

#include "c111cLib.h"

int main(int argc, char *argv[])
{
  int Q, i, resp, sock;
  short N, A, F, datain, dataout, thresholds[20][8];

  short tSet=-1,slot=-1,chan=-1;

  const char* usage="cnd-cfd-thresh [-w(rite) #] [-s(lot) #(1-20)] [-c(han) #(1-8)]\n";
  if (argc>1) {
      if (argc%2 != 1) {
          printf("Invalid arguments.  Usage:\n");
          printf(usage);
          exit(1);
      }
      for (i=1; i<argc; i+=2) {
          if (strcmp(argv[i],"-w")==0) {
              tSet = (short)atoi(argv[i+1]);
          }
          else if (strcmp(argv[i],"-s")==0) {
              slot = (short)atoi(argv[i+1]);
              if (slot<1 || slot>20) {
                  printf("Invalid arguments.  Usage:\n");
                  printf(usage);
                  exit(1);
              }
          }
          else if (strcmp(argv[i],"-c")==0) {
              chan = (short)atoi(argv[i+1]);
              if (chan<1 || chan>8) {
                  printf("Invalid arguments.  Usage:\n");
                  printf(usage);
                  exit(1);
              }
          }
          else {
              printf("Invalid arguments.  Usage:\n");
              printf(usage);
              exit(1);
          }
      }
  }

  // Open connection with a Camac controller
  sock = ccconnect("129.57.160.156",2000);
  if(sock==0)
  {
    printf("Connection failed \n");
    exit(1);
  }
  
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
 
  // READ ALL THRESHOLDS:
  printf("Read All Thresholds:::::::::::::::::::::::::::::\n");
  for(N=1; N<20; N++) {
      for(A=0; A<=7; A++) {
          F = 0;
          resp = CNAF16(sock, N, A, F, &Q, &dataout);
          thresholds[N-1][A] = dataout;
          if (resp != 0)
          {
              printf("ERROR: Negative response from socket server\n");
              printf(" ======> resp=%d, Q=%d, slot=%d, chan=%d, datain=%d\n",resp,Q,N,A+1,datain);
              exit(0);
          }
      }
  }

  // PRINT ALL THRESHOLDS:
  printf("      ");
  for (N=1; N<20; N++) printf("%5d ",N); printf("\n");
  for (A=0; A<=7; A++) {
      printf("%5d ",A+1);
      for (N=1; N<20; N++) printf("%5d ",thresholds[N-1][A]); printf("\n");
  }

  // not setting thresholds, just quit:
  if (tSet<0) exit(0);

  // SET THRESHOLDS:
  printf("Write Thresholds::::::::::::::::::::::::::::::\n");
  for (N=1; N<20; N++) {
      if (slot>0 && N!=slot) continue; 
      for (A=0; A<=7; A++) {
          if (chan>0 && A!=chan-1) continue;
          printf("Writing thresholds slot=%d chan=%d val=%d\n",N,A+1,tSet);
          F=16;
          datain = tSet;
          resp = CNAF16(sock, N, A, F, &Q, &datain);
          if (resp != 0)
          {
              printf("ERROR: Negative response from socket server\n");
              printf(" ======> resp=%d, Q=%d, slot=%d, chan=%d, datain=%d\n",resp,Q,N,A+1,datain);
              return 0;
          }
      }
  }

  // READ ALL THRESHOLDS:
  printf("Read All Thresholds Again :::::::::::::::::::::::::\n");
  for(N=1; N<20; N++) {
      for(A=0; A<=7; A++) {
          F = 0;
          resp = CNAF16(sock, N, A, F, &Q, &dataout);
          thresholds[N-1][A] = dataout;
          if (resp != 0)
          {
              printf("ERROR: Negative response from socket server\n");
              printf(" ======> resp=%d, Q=%d, slot=%d, chan=%d, datain=%d\n",resp,Q,N,A+1,datain);
              exit(0);
          }
      }
  }
  // PRINT ALL THRESHOLDS:
  printf("      ");
  for (N=1; N<20; N++) printf("%5d ",N); printf("\n");
  for (A=0; A<=7; A++) {
      printf("%5d ",A+1);
      for (N=1; N<20; N++) printf("%5d ",thresholds[N-1][A]); printf("\n");
  }

  return 0;

}

