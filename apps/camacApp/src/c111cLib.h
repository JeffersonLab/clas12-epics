/*---------------------------------------------------------------------------*
 *  Copyright (c) 2006        Southeastern Universities Research Association, *
 *                            Thomas Jefferson National Accelerator Facility  *
 *                                                                            *
 *    This software was developed under a United States Government license    *
 *    described in the NOTICE file included as part of this distribution.     *
 *                                                                            *
 *    Library for C111C Ethernet Based Camac Controller                       *
 *    Network part function prototypes                                        *
 *                                                                            *
 *    Author  :  Vardan Gyurjyan                                              *
 *    Group   :  Data Acquisition                                             *
 *    Version :  1.00                                                         *
 *----------------------------------------------------------------------------*/

int ccconnect(char *ip, int port);
int ccclose(int sck);

int caopen(char *hostname, int *skt);
int caclose(int skt);
int cdreg(int *ext, int b, int sck, int n, int a);
int cssa(int f, int ext, short *dat, int *q);
int cfsa(int f, int ext, short *dat, int *q);
int cccc(int sck);
int cccz(int sck);
int ccci(int sck, int l);
int ctstat(int sck, int *istat);
short CNAF24(int sck, short N, short A, short F, int *Q, short *DATA);
short CNAF16(int sck, short N, short A, short F, int *Q, short *DATA);
short CTSTAT(int sck, short *Q, short *X);
short CINIT(int sck);
short CCLEAR(int sck);
short CINHIBIT(int sck, int I);
