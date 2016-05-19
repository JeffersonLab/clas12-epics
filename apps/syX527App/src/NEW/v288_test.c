/* v288_test.c */

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
main()
#endif
{


printf("===\n");

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

  /*
  printf("111\n");fflush(stdout);
  usleep(1000000);
  printf("222\n");fflush(stdout);
  exit(0);
  */

#ifndef VXWORKS
  /* Open the default VME windows */
  vmeOpenDefaultWindows();

printf("===\n");
#endif

  ret = CAENHVInitSystem("TestSetup", LINKTYPE_CAENET, "sy527_0x100000_3","","");
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
