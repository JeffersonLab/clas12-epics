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


static int nA944param = 16;
static char A944param[MAX_PARAM][MAX_NAME] = {
                "V0Set","I0Set","V1Set","I1Set","Rup","Rdwn","Trip","SVMax",
                "VMon","IMon","Status","Pw","PrOn","PrOff","Pon","Pdwn"};

#ifdef VXWORKS
void
v288test1()
#else
int
main(int argc,char** argv)
#endif
{
  unsigned short NrOfSl, *SerNumList, *NrOfCh, ChList[MAX_CHAN];
  char *ModelList, *DescriptionList;
  unsigned char	*FmwRelMinList, *FmwRelMaxList;
  char name[MAX_NAME];
  int i, ret;
  unsigned short Slot, ChNum;
  float fParValList[MAX_CHAN];
  unsigned long	lParValList[MAX_CHAN];
  char ParName[MAX_NAME];
  unsigned long retval;

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
  printf("\n-----------------------------------------------------------------\n");


  char* Arg=caenetAddr;
  int group,ii,jj,id=0;
  char *ch1,*ch2;
  char arg1[256],arg2[256],arg3[256];
  int addr,len;
  unsigned long vmeaddr=0;
  unsigned long vrate=0;

  float V0SET[1024],I0SET[1024],VMAX[1024],TRIP[1024];
  UINT16 NCHAN,ICHAN;
  UINT16 SLOT[1024];
  UINT16 CHAN[1024];

  ushort slot=0;
  ushort channel=0;

  UINT16 code;
  UINT16 crate=0;
  UINT16 value[20];
  UINT16 buffer[1024];
 
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

  code=2;
  value[0] = (slot<<8)+channel;
  v288Send(vmeaddr,crate,code,value);
  len=v288Get(vmeaddr,1024,buffer);

  printf("%d\n",len);
  for (ii=0; ii<len; ii++) printf("[%3d] %5d   0x%04x\n",ii,buffer[ii],buffer[ii]);

  NCHAN=0;

  // read group configurations
  code = 0x40;
  //for (ii=0; ii<16; ii++)
  for (ii=0; ii<1; ii++)
  {
    value[0] = ii;
    v288Send(vmeaddr,crate,code,value);
    len = v288Get(vmeaddr,1024,buffer);
    //printf("%d %d\n",ii,len);
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

  // read group v0set and i0set:
  group = 0;
  value[0] = group;

  code = 0x43;
  ICHAN=0;
  v288Send(vmeaddr,crate,code,value);
  len = v288Get(vmeaddr,1024,buffer);
  for (jj=0; jj<len; jj+=3)
  {
    V0SET[ICHAN] = (float)((buffer[jj]<<16) + buffer[jj+1]);
    I0SET[ICHAN] = buffer[jj+2];
    V0SET[ICHAN] /= 10.;
    I0SET[ICHAN] /= 100.;
    printf("%d:   %d %d %d   %.2f %f\n",jj,buffer[jj],buffer[jj+1],buffer[jj+2],V0SET[ICHAN],I0SET[ICHAN]);
    ICHAN++;
  }

  // read group vmax, trip, and flag;
  code = 0x45;

  // read group rup and rdn:
  code = 0x46;

  // read group statuses:
  code=0x41;

exit(0);


  /* get params info 
  ret = CAENHVGetChParamProp("TestSetup", 3, 1, "VMon", "Type", &retval);
  printf("retval(VMon)=%d\n",retval);
  ret = CAENHVGetChParamProp("TestSetup", 3, 1, "Status", "Type", &retval);
  printf("retval(Status)=%d\n",retval);
  ret = CAENHVGetChParamProp("TestSetup", 3, 1, "Pw", "Type", &retval);
  printf("retval(Pw)=%d\n",retval);
  */


  ChNum = 24; /* # of channels */
  for(i = 0; i<ChNum; i++)
  {
    ChList[i] = (unsigned short)i;
  }


  Slot = 0;
  ChNum = 1;
  for(i=0; i<nA944param; i++)
  {
    ret = CAENHVGetChParamProp("TestSetup", Slot, ChNum, A944param[i], "Type", &retval);
    if(retval == PARAM_TYPE_NUMERIC)
    {
      ret = CAENHVGetChParam("TestSetup", Slot, A944param[i], ChNum, ChList, fParValList);
      printf("CAENHVGetChParam(float): %s = %7.3f\n",A944param[i],fParValList[0]);
    }
    else
    {
      ret = CAENHVGetChParam("TestSetup", Slot, A944param[i], ChNum, ChList, lParValList);
      printf("CAENHVGetChParam(int): %s = %ld\n",A944param[i],lParValList[0]);
    }
  }


  strcpy(ParName,"SVMax");
  Slot = 0;
  ChNum = 1;
  fParValList[0] = 1600.0;
  ret = CAENHVSetChParam("TestSetup", Slot, ParName, ChNum, ChList, fParValList);

  /*
  strcpy(ParName,"Pon");
  ChNum = 1;
  lParValList[0] = 1;
  ret = CAENHVSetChParam("TestSetup", Slot, ParName, ChNum, ChList, lParValList);

  strcpy(ParName,"Pw");
  ChNum = 1;
  lParValList[0] = 1;
  ret = CAENHVSetChParam("TestSetup", Slot, ParName, ChNum, ChList, lParValList);
  */
  return 0;
}

#else /* vxWorks or Linux */

void
v288_test_dummy()
{
  return;
}

#endif
