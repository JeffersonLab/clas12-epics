#define Linux_vme

#if defined(VXWORKS) || defined(Linux_vme)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#ifdef VXWORKS
#include <vxWorks.h>
#include <taskLib.h>
#include <semLib.h>
IMPORT  STATUS sysBusToLocalAdrs(int, char *, char **);
#else
#include <unistd.h>
#include <pthread.h>
#define UINT32 unsigned int
#define UINT16 unsigned short
#define UINT8 unsigned char
#endif

#include "v288.h"


#define MAX_NAME  81
#define MAX_SLOT  16 /* sy527 has 10 slots, but 16 should be fine for memory allocation */
#define MAX_CHAN  48
#define MAX_PARAM 100

#define MAX_HVPS        256
#define CAENHV_OK       0
#define CAENHV_SYSERR   1

#define LINKTYPE_TCPIP              0
#define LINKTYPE_RS232              1
#define LINKTYPE_CAENET             2

#define PARAM_TYPE_NUMERIC          0
#define PARAM_TYPE_ONOFF            1
#define PARAM_TYPE_CHSTATUS         2
#define PARAM_TYPE_BDSTATUS         3

#define MAX_V288GET 50

#define DEBUG 0

#ifdef VXWORKS
void
v288test1()
#else
int
main(int argc,char** argv)
#endif
{
  unsigned short NrOfSl, *SerNumList, *NrOfCh;
  char *ModelList, *DescriptionList;
  unsigned char	*FmwRelMinList, *FmwRelMaxList;
  char name[MAX_NAME];
  int i, ret;

  char caenetAddr[100]="sy527_0x100000_3";

#ifndef VXWORKS
  /* Open the default VME windows */
  vmeOpenDefaultWindows();

printf("===\n");
if (argc>1)
{
  sprintf(caenetAddr,"sy527_0x100000_%s",argv[1]);
}
#endif

  printf("\nDOING THIS ONE:  %s\n\n",caenetAddr);

  ret = CAENHVInitSystem("TestSetup", LINKTYPE_CAENET, caenetAddr,"","");
  printf("=== ret= %d\n", ret);

  ret = CAENHVGetCrateMap("TestSetup",&NrOfSl, &NrOfCh, &ModelList,
                          &DescriptionList, &SerNumList,
                          &FmwRelMinList, &FmwRelMaxList );
  printf("=== ret= %d\n", ret);

  if(ret != CAENHV_OK)
  {
    printf("ERROR(sy527): %s (num. %d)\n\n", CAENHVGetError(name), ret);
  }
  else
  {
    char *m = ModelList, *d = DescriptionList;

    printf("The number of slots = %d\n",NrOfSl);
    for(i=0; i<NrOfSl; i++, m+=strlen(m)+1, d+=strlen(d)+1)
    {
      if(*m == '\0')
      {
        printf("Board %2d: Not Present\n", i);
      }
      else
      {
        printf("Board %2d: %s %s  Nr. Ch: %d  Ser. %2d   Rel. %d.%d\n",
                i, m, d, NrOfCh[i], SerNumList[i], FmwRelMaxList[i], 
                FmwRelMinList[i]);
      }
    }
  }
  
  free(SerNumList);
  free(ModelList);
  free(DescriptionList);
  free(FmwRelMinList);
  free(FmwRelMaxList);
  free(NrOfCh);
  

  printf("\n-----------------------------------------------------------------\n");
  printf("\n      START GROUP STUFF                      \n");
  printf("\n-----------------------------------------------------------------\n\n");

#define BUFSIZE 2048

  char* Arg=caenetAddr;
  int group,ii,jj;
  char *ch1,*ch2;
  char arg1[256],arg2[256],arg3[256];
  int addr,len,res;
  unsigned long vmeaddr=0;

  ushort slot=0;
  ushort channel=0;

  UINT16 code;
  UINT16 crate=0;
  UINT16 value[20];
  UINT16 buffer[BUFSIZE];
 
  ch1 = (char *)Arg;
  ch2 = arg1;
  while(*ch1 != '_') *ch2++ = *ch1++;
  *ch2 = '\0';

  ch1++;
  ch2 = arg2;
  while(*ch1 != '_') *ch2++ = *ch1++;
  *ch2 = '\0';

  ch1++;
  ch2 = arg3;
  while(*ch1 != '\0') *ch2++ = *ch1++;
  *ch2 = '\0';

  addr = strtol(arg2,(char**)NULL,0);
  vmeBusToLocalAdrs(0x39,addr,(char**)&vmeaddr);
  crate = strtol(arg3,(char**)NULL,0);

  float VSET[1024]={},ISET[1024]={},VMAX[1024]={},TRIP[1024]={};
  float RUP[1024]={},RDN[1024]={},FLAG[1024]={},STAT[1024]={};
  float VMON[1024]={},IMON[1024]={},SMAX[1024]={};
  UINT16 NCHAN=0,SLOT[1024]={},CHAN[1024]={};

/*
  // add channel to group-1:
  code = 0x50;
  group = 1;
  value[0] = group;
  value[1] = 0x0000;
  res = v288Send(vmeaddr,crate,code,value);
  len = v288Get(vmeaddr,BUFSIZE,buffer);
  value[0] = group;
  value[1] = 0x0101;
  res = v288Send(vmeaddr,crate,code,value);
  len = v288Get(vmeaddr,BUFSIZE,buffer);
*/
/*
  // set group-0 v0set:
  code = 0x52;
  value[0] = 0;
  value[1] = 210; // <-- this is 10x voltage
  res = v288Send(vmeaddr,crate,code,value);
  len = v288Get(vmeaddr,BUFSIZE,buffer);
*/
/*
  // set group-0 ON:
  code = 0x5A;
  value[0] = 0;
  res = v288Send(vmeaddr,crate,code,value);
  len = v288Get(vmeaddr,BUFSIZE,buffer);
*/
/*
  // set group-0 OFF:
  code = 0x5B;
  value[0] = 0;
  res = v288Send(vmeaddr,crate,code,value);
  len = v288Get(vmeaddr,BUFSIZE,buffer);
*/


  // read group configurations
  code = 0x40;
  //for (ii=0; ii<16; ii++)
  for (ii=0; ii<16; ii++)
  {
    value[0] = ii;
    res = v288Send(vmeaddr,crate,code,value);
    len = v288Get(vmeaddr,BUFSIZE,buffer);
    printf("GROUP-%d:         %d %d\n",ii,len,(len-6)/2);
    for (jj=0; jj<len; jj++)
    {

      if (buffer[jj] == 0xFFFF) continue;
      if (jj<6) continue;

      if (jj>5 && jj%2==0)
      {
        slot    = buffer[jj] >> 8;
        channel = buffer[jj] & 0xFF;

        printf("group=%d  [%3d] %5d   0x%04x",ii,jj,buffer[jj],buffer[jj]);
        printf("      slot=%d chan=%d pri=%d",slot,channel,buffer[jj+1]);
        printf("\n");

        SLOT[NCHAN]=slot;
        CHAN[NCHAN]=channel;
        NCHAN++;

      }
    }
  }

  // read group parameters
  if (0)
  {
    group = 0;
    value[0] = group;

    // read group v0set and i0set:
    code = 0x43;
    res = v288Send(vmeaddr,crate,code,value);
    len = v288Get(vmeaddr,BUFSIZE,buffer);
    printf("VSET/ISET:       %d %d\n",len,len/3);
    for (jj=0; jj<len; jj+=3)
    {
      VSET[jj/3] = (float)((buffer[jj]<<16) + buffer[jj+1]);
      ISET[jj/3] = buffer[jj+2];
      VSET[jj/3] /= 10.;
      ISET[jj/3] /= 100.;
      if (DEBUG) printf("%d:   %d %d %d   %.2f %f\n",jj,buffer[jj],buffer[jj+1],buffer[jj+2],VSET[jj/3],ISET[jj/3]);
    }

    // read group vmax, trip, and flag;
    code = 0x45;
    res = v288Send(vmeaddr,crate,code,value);
    len = v288Get(vmeaddr,BUFSIZE,buffer);
    printf("VMAX/TRIP/FLAG:  %d %d\n",len,len/3);
    for (jj=0; jj<len; jj+=3)
    {
      VMAX[jj/3] = buffer[jj];
      TRIP[jj/3] = buffer[jj+1];
      FLAG[jj/3] = buffer[jj+2];
      if (DEBUG) printf("%d:   %d %d %d   %.2f %f %f\n",jj,buffer[jj],buffer[jj+1],buffer[jj+2],VMAX[jj/3],TRIP[jj/3],FLAG[jj/3]);
    }

    // read group rup and rdn:
    code = 0x46;
    res = v288Send(vmeaddr,crate,code,value);
    len = v288Get(vmeaddr,BUFSIZE,buffer);
    printf("RUP/RDN:         %d %d\n",len,len/2);
    for (jj=0; jj<len; jj+=2)
    {
      RUP[jj/2] = buffer[jj];
      RDN[jj/2] = buffer[jj+1];
      if (DEBUG) printf("%d:   %d %d   %f %f\n",jj,buffer[jj],buffer[jj+1],RUP[jj/2],RDN[jj/2]);
    }

    // read group channel status:
    code = 0x41;
    res = v288Send(vmeaddr,crate,code,value);
    len = v288Get(vmeaddr,BUFSIZE,buffer);
    printf("VMON/IMON/STAT:  %d %d\n",len,len/5);
    for (jj=0; jj<len; jj+=5)
    {
      VMON[jj/5] = (float)((buffer[jj]<<16) + buffer[jj+1]);
      SMAX[jj/5] = buffer[jj+2];
      IMON[jj/5] = buffer[jj+3];
      STAT[jj/5] = buffer[jj+4];
      VMON[jj/5] /= 10;
      IMON[jj/5] /= 100;
      if (DEBUG) printf("%d:   %d %d %d %d %d  %.2f %f %f %f\n",jj,
          buffer[jj],buffer[jj+1],buffer[jj+2],buffer[jj+3],buffer[jj+4],
          VMON[jj/5],IMON[jj/5],SMAX[jj/5],STAT[jj/5]);
    }


    printf("\nGROUP-%d SUMMARY::::::::::::::::::::::::::::::\n\n",group);

    // print all values by channel:
    for (jj=0; jj<NCHAN; jj++)
    {
      printf("(%d,%d):  ",SLOT[jj],CHAN[jj]);
      printf("(%.2f,%.0f,%.0f) ",VMON[jj],IMON[jj],STAT[jj]);
      printf("(%.2f,%.2f,%.0f,%.0f,%.0f,%.0f) ",VSET[jj],ISET[jj],VMAX[jj],SMAX[jj],RUP[jj],RDN[jj]);
      printf("\n");
    }
  }


  exit(0);


}

#else /* vxWorks or Linux */

void
v288_test_dummy()
{
  return;
}

#endif
