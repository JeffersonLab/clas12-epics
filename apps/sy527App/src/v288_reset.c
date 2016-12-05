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

#ifdef VXWORKS
void
v288test1()
#else
int
main(int argc,char** argv)
#endif
{
  char caenetAddr[100]="sy527_0x100000_3";

#ifndef VXWORKS
  /* Open the default VME windows */
  vmeOpenDefaultWindows();
  if (argc>1) sprintf(caenetAddr,"sy527_0x100000_%s",argv[1]);
#endif

  printf("\nDOING THIS ONE:  %s\n\n",caenetAddr);

  char* Arg=caenetAddr;
  char *ch1,*ch2;
  char arg1[256],arg2[256],arg3[256];
  int addr;
  unsigned long vmeaddr=0;

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

  if (v288Reset(vmeaddr)) printf("v288Reset ERROR\n");
  else printf("v288Reset SUCCESS\n");

  exit(0);
}

#else /* vxWorks or Linux */

void
v288_test_dummy()
{
  return;
}

#endif
