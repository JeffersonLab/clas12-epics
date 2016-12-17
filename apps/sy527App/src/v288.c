/* v288.c - provides interface emulating CAENHVWrapper */



/*#define Linux_vme*/

/* my:*/
 #include "jvme.h"

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

#define SSWAP(x)  ((((x) & 0x00ff) << 8) | (((x) & 0xff00) >> 8))
#define QQ (UINT16)0xfffe
#define OK 0
#define MEK (UINT16)1

/* how many times loop before give up */
//#define TIMEOUT 1111

//NAB:
//#define TIMEOUT 11111
#define TIMEOUT 5111

#define RESET_ERR 101
#define WAIT_ERROR 102

/* the number of words to be transferred for different opcodes */
static int nwords[96] = {
  0, 1, 1, 1, 0, 0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, /*opcodes 0x00-0x0f ( 0-15)*/
  2, 2, 2, 2, 2, 2, 2, 2, 2, 7,-1, 7,-1,-1,-1,-1, /*opcodes 0x10-0x1f (16-31)*/
 -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, /*opcodes 0x20-0x2f (32-47)*/
 -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, /*opcodes 0x30-0x3f (48-63)*/
  1, 1,-1, 1, 1, 1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1, /*opcodes 0x40-0x4f (64-79)*/
  2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1,-1,-1,-1,-1  /*opcodes 0x50-0x5f (80-95)*/
};

/*******************************/
/*******************************/
/***** LOW-level functions *****/
/*******************************/
/*******************************/


/*----------------------------------------------------------*/
/*----------------- active loop delay ----------------------*/
/*----------------------------------------------------------*/
void
v288ActiveLoop(int spas)
{
 /// int jj; my:

#ifdef VXWORKS
  while(spas--) jj++;
#endif
}

/*----------------------------------------------------------*/
/*---------- Send commands to caen function ----------------*/
/*----------------------------------------------------------*/
/*
     addr   - base address of v288 board
     offset - register offset (in bytes) we want to access:
                 0 - base reg
                 2 - stat reg
                 4 - trans reg
                 6 - reset reg
     vmedat - data to write into the register
     spas   -  parameter for delay active loop
 */
int
v288Transmit(UINT32 addr, UINT32 offset, UINT16 vmedat, int spas)
{
  volatile UINT16 *vmeaddress = (volatile UINT16 *) (addr+offset);
  volatile UINT16 *statreg = (volatile UINT16 *) (addr+2);
  int i=0;
  UINT16 q=0;

  /*printf("v288Transmit reached\n");*/

  while(q!=QQ && i<=TIMEOUT)
  {
    /*v288ActiveLoop(spas);*/
    vmeWrite16(vmeaddress, vmedat);
    /*v288ActiveLoop(spas);*/
    q = vmeRead16(statreg);
    i++;
  }
  if(i>TIMEOUT) printf("v288Transmit: error: q=0x%08x, i=%d\n",q,i);
  /*else printf("v288Transmit: info: q=0x%08x, i=%d\n",q,i);*/

  //return((i==TIMEOUT) ? TIMEOUT : OK);
  return((i>TIMEOUT) ? TIMEOUT : OK);
}

/*---------------------------------------------------------*/
/*---- CAEN Wait function -------------------------------- */
/*---------------------------------------------------------*/
int
v288Wait(UINT32 addr, int delay)
{
  volatile UINT16 *v288adr = (volatile UINT16 *) addr;
  volatile UINT16 *statreg = (volatile UINT16 *) (addr+2);
  int i=0;
  UINT16 q=0;
  UINT16 vmedat;

  /*printf("v288Wait reached, delay=%d\n",delay);*/

  while(i<=TIMEOUT && q!=QQ)
  {
    /*v288ActiveLoop(delay);*/
    vmedat = vmeRead16(v288adr);
    /*v288ActiveLoop(delay);*/
    if((q=vmeRead16(statreg)) == QQ)
    {
      /*printf("v288Wait: info: q=0x%08x, i=%d\n",q,i);*/
      return(vmedat);
    }
#ifndef VXWORKS
	usleep(1);
  // NAB:
	//usleep(100);
#endif
    i++;
  }
  printf("v288Wait: error: q=0x%08x, i=%d\n",q,i);

  return(WAIT_ERROR);
}

/*---------------------------------------------------------*/
/*------Reset_restart mod for caenet controller -----------*/ 
/*---------------------------------------------------------*/
int
v288Reset(UINT32 addr)
{
  volatile UINT16 *statreg = (volatile UINT16 *) (addr+2);
  volatile UINT16 *resetreg = (volatile UINT16 *) (addr+6);
  int i=0;
  UINT16 q=0;
#ifdef VXWORKS
  int delay=10000000;
#else
  int delay=1000000000;
#endif

  /*printf("v288Reset reached\n");*/

  // NAB:  Is this 11 iterations optimized / appropriate?
  //       Why is there no delay in this loop?

  while(q!=QQ && i<=11)
  {
    v288ActiveLoop(delay);
    vmeWrite16(resetreg, MEK);
    v288ActiveLoop(delay);
    q = vmeRead16(statreg);
    /*printf("q=0x%08x\n",q);*/
    i++;
  }

  //if(i>11) printf("v288Reset: error: q=0x%08x, i=%d\n",q,i);
  /*else printf("v288Reset: info: q=0x%08x, i=%d\n",q,i);*/

  //return((i==11) ? 11 : OK);

  // NAB:
  //return((i>11) ? i : OK);
  //return i;
  
  if(i>11)
  {
    printf("v288Reset: ERROR: q=0x%08x, i=%d\n",q,i);
    return i;
  }
  else
  {
    printf("v288Reset: INFO: q=0x%08x, i=%d\n",q,i);
    return OK;
  }

}




/*******************************/
/*******************************/
/***** MID-level functions *****/
/*******************************/
/*******************************/

/* first stage of command sending */
int
v288Send1(UINT32 addr, UINT16 crate, UINT16 code, int delay)
{
  int res = 0;

  if(( res = v288Transmit(addr,0,1,delay))== TIMEOUT )
  {
    printf("v288Send1: set_fatal error: controller identifier code\n");
    return(res);
  }

  if(( res = v288Transmit(addr,0,crate,delay))== TIMEOUT )
  {
    printf("v288Send1: set_fatal error: can't see CAEN crate\n");
    return(res);
  }

  if(( res = v288Transmit(addr,0,code,delay))== TIMEOUT )
  {
    printf("v288Send1: set_error: operation code failed\n");
    return(res);
  }

  return(res);
}

/* second stage of command sending */
int
v288Send2(UINT32 addr, UINT16 value, int delay)
{
  int res = 0;

  if(( res = v288Transmit(addr,0,value,delay))== TIMEOUT )
  {
    printf("v288Send2: error: !!!\n");
    return(res);
  }

  return(res);
}

/* third stage of command sending */
int
v288Send3(UINT32 addr, int delay)
{
  int res = 0;

  if(( res = v288Transmit(addr, 4, MEK, delay)) == TIMEOUT)
  {
    printf("v288Send3: error: transmission register access failed %d \n",res);
  }

  return(res);
}

/* full sending command */
int
v288Send(UINT32 addr, UINT16 crate, UINT16 code, UINT16 *value)
{
  int i, res = 0;
#ifdef VXWORKS
  int delay = 1000;
#else
  int delay = 10000;
#endif

  if(code>95)
  {
    printf("v288Send: ERROR: illegal opcode %d(0x%x)\n",code,code);
    return(-1);
  }

  if(nwords[code]==-1)
  {
    printf("v288Send: ERROR: opcode %d(0x%x) does not exist or was not implemented\n",code,code);
    return(-2);
  }

  res = v288Send1(addr, crate, code, delay);
  if(res != OK)goto error; /// my:
  for(i=0; i<nwords[code]; i++)
  {
    res = v288Send2(addr, value[i], delay);
    if(res != OK)break; /// my:
  }
  if(res != OK)goto error; /// my:
  res = v288Send3(addr, delay);
  if(res != OK)goto error; /// my:
  res = v288Wait(addr, delay);
  if(res == WAIT_ERROR)goto error; /// my:
  goto noerror;
error: 
  //v288Reset(addr);
  // NAB:
  if (v288Reset(addr))
  {
    printf("v288Send:  v288Reset ERROR on %u / %u\n",addr,crate);
  }
noerror:
  return OK; /// my:
  return(res);
}

/* get data */
int
v288Get(UINT32 addr, int nw, UINT16 *buffer)
{
  volatile UINT16 *v288adr = (volatile UINT16 *) addr;
  volatile UINT16 *statreg = (volatile UINT16 *) (addr+2);
  int i, k=0;
  UINT16 q=0;
  UINT16 vmedat;
#ifdef VXWORKS
  int delay = 10000;
#else
 /// int delay = 100000; ///my:
#endif

  i = 0;
  for(;;)
  {
    /*v288ActiveLoop(delay);*/
    vmedat = vmeRead16(v288adr);
    /*v288ActiveLoop(delay);*/
    if( (q=vmeRead16(statreg)) != QQ )
    {
      /*printf("v288Get: q=0x%08x, i=%d - break\n",q,i);*/
      break;
    }

    i++;
    if(k<nw)
    {
      buffer[k++] = vmedat;
	}
    else
    {
      printf("v288Get: ERROR: buffer size %d is not enough !\n",nw);
	}
  }

  return(k);
}


/***************************************************************************/
/***************************************************************************/
/***************************************************************************/

/*
  65: 0      2(Vmon)     0     0    67 <- Vmon is different for diff. channels
  66: nothing
  67: 3500(I0set)     0(???)  7750(V0set) <- all channels 
  68: 0   100  3000  <- all channels

  69:
   900(SVmax)     1  1242
   900     1   200
   900     1  1206
   900     1   164
   900     1  1170
   900     1   128
   900     1  1134
   900     1    92
   900     1    74
   900     1  1080
   900     1    38
   900     1  1044
   900     1     2
   900     1   240
   900     1   222
   900     1  1228
   900     1  1210
   900     1   168
   900     1  1174
   900     1   132
   900     1  1138
   900     1    96
   900     1  1102
   900     1    60

  70:
   25(Rup)    50(Rdwn) 
   25    50 
   25    50 
   ........

  71: nothing
  72: nothing
  73: nothing
  74: nothing

*/


/********************************/
/********************************/
/* CAEN1527-style API functions */
/********************************/
/********************************/


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


#ifdef VXWORKS
#define V288SENDANDGET \
    semTake(v288_mutex, WAIT_FOREVER); \
    v288Send(addr, crate, code, value); \
    tmp = v288Get(addr, 1024, buffer); \
    semGive(v288_mutex)

static SEM_ID v288_mutex;

#else

#define V288SENDANDGET \
    if(pthread_mutex_lock(&v288_mutex)<0) perror("pthread_mutex_lock");\
    v288Send(addr, crate, code, value); \
    tmp = v288Get(addr, 1024, buffer); \
    if(pthread_mutex_unlock(&v288_mutex)<0) perror("pthread_mutex_unlock")

static pthread_mutex_t v288_mutex = PTHREAD_MUTEX_INITIALIZER;

#endif


/*structure to hold mainframe attributes*/
typedef struct hv527
{
  int   id; /* */
  char  name[MAX_NAME];
  char  type[MAX_NAME];
  unsigned long vmeaddr;
  unsigned long CrNum;
  int crnum;
  float scalev[MAX_SLOT];
  float scalei[MAX_SLOT];
} HV527;

static HV527 sy527[MAX_HVPS];

/* input: SystemName - name we assigned to mainframe (arbitrary)
          LinkType - LINKTYPE_CAENET for sy527
          Arg - sy527_VMEADDRESS_CRATE#
          UserName - irrelevant here
          Passwd - irrelevant here
 */
int
CAENHVInitSystem(const char *SystemName, int LinkType, void *Arg,
                 const char *UserName, const char *Passwd)
{
  int i, addr;
  char arg1[256], arg2[256], arg3[256];
  char *ch1, *ch2;

  if(LinkType != LINKTYPE_CAENET) return(CAENHV_SYSERR);

  /* search for empty slot */
  for(i=0; i<MAX_HVPS; i++)
  {
    if(sy527[i].vmeaddr == 0) /* empty, will use it */
	{
      sy527[i].id = i;
      strcpy(sy527[i].name,SystemName);

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

      /*printf("CAENHVInitSystem: arg's    -> >%s< >%s< >%s<\n",arg1,arg2,arg3);*/

      strcpy(sy527[i].type,arg1);

      addr = strtol(arg2, (char **)NULL, 0); /*0x7fffffff max!!??*/
#ifdef VXWORKS
      sysBusToLocalAdrs(0x39, addr, (char **)&sy527[i].vmeaddr);
#else
      vmeBusToLocalAdrs(0x39, addr, (char **)&sy527[i].vmeaddr);
#endif
      sy527[i].CrNum = strtol(arg3, (char **)NULL, 0);
	  /*
      printf("CAENHVInitSystem: decode's -> >%s< 0x%08x %d\n",
        sy527[i].type,sy527[i].vmeaddr,sy527[i].CrNum);
	  */
      return(CAENHV_OK);
	}
  }

  return(CAENHV_SYSERR); /* no empty slots */
}


#define GET_SYSTEM_ID(myname) \
{ \
  int i; \
  for(i=0; i<MAX_HVPS; i++) \
  { \
    if( !strcmp(myname,sy527[i].name) ) \
    { \
      id = i; \
      crate = sy527[id].CrNum; \
      addr = sy527[id].vmeaddr; \
      /*printf("SYSTEM_ID: name >%s<, id=%d, addr=0x%08x, crate=%d\n", \
		myname,id,addr,crate);*/ \
      break; \
	} \
  } \
}


/* input: SystemName - the same name used in CAENHVInitSystem() call
 */
int
CAENHVDeinitSystem(const char *SystemName)
{
  int i;

  /* search for SystemName and release it if found */
  for(i=0; i<MAX_HVPS; i++)
  {
    if( !strcmp(SystemName,sy527[i].name) )
	{
      sy527[i].vmeaddr = 0;
      strcpy(sy527[i].name,"");

      return(CAENHV_OK);
	}
  }

  return(CAENHV_SYSERR);
}

/* input: SystemName - the same name used in CAENHVDeinitSystem() call
 */
char *
CAENHVGetError(const char *SystemName)
{
  return(CAENHV_OK);
}

/* input: SystemName
   output: NrOfSlot - the number of slots
           NrofChList - the number of channels
           ModelList - 
           DescriptionList - 
           SerNumList - 
           FmwRelMinList - 
           FmwRelMaxList - 
 */
int
CAENHVGetCrateMap(const char *SystemName, unsigned short *NrOfSlot,
                  unsigned short **NrofChList, char **ModelList,
                  char **DescriptionList, unsigned short **SerNumList,
                  unsigned char **FmwRelMinList, unsigned char **FmwRelMaxList)
{
  int id=0; /// my:
  UINT16 crate=0, code, value[20], buffer[1024]; /// my:
  int tmp=0;
  int i, ii;
  UINT32 addr=0, Vmax; /// my:
  UINT16 bitmap, Imax, Rampmin, Rampmax, Vres, Ires, Vdec, Idec;
  unsigned short  *u1, *u2;
  char *bname, Iunits[3];
  UINT8 *b8 = (UINT8 *)buffer, *c1, *c2;
  char *m, *d;
  float paw_10[] = {1., 10., 100.};

  GET_SYSTEM_ID(SystemName);

  code = 4; /*returns crate occupation (bitmap)*/
  V288SENDANDGET;
  bitmap = buffer[0];
  /*printf("v288Get returns %d\n",tmp);*/

  // NAB:  how much time is being wasted scanning slots without boards?

  *NrOfSlot = 10; /* sy527 has 10 slots */
  /*printf("\nCrate bitmap 0x%04x, NrOfSlot=%d\n\n",bitmap,*NrOfSlot);*/


  /* allocate memory for output parameters */
  *NrofChList = calloc(*NrOfSlot,sizeof(unsigned short));
  *SerNumList = calloc(*NrOfSlot,sizeof(unsigned short));
  *FmwRelMinList = calloc(*NrOfSlot,sizeof(unsigned char));
  *FmwRelMaxList = calloc(*NrOfSlot,sizeof(unsigned char));

  *ModelList = calloc((*NrOfSlot)*256,sizeof(char));
  *DescriptionList = calloc((*NrOfSlot)*256,sizeof(char));

  u1 = *NrofChList;
  u2 = *SerNumList;
  c1 = *FmwRelMinList;
  c2 = *FmwRelMaxList;
  m = *ModelList;
  d = *DescriptionList;

  /* get crate information */
  code = 3;
  for(i=0; i<(*NrOfSlot); i++, m+=strlen(m)+1, d+=strlen(d)+1)
  {
    if( !((bitmap>>i)&0x1) )
    {
      strcpy(m,"");
      continue; /*skip empty slots*/
	}
    /*printf("\n   Slot number %d ==================== (bitmap=0x%08x)\n",i,bitmap);*/
    value[0] = i; /*slot number(from 0)*/

    /* send command and get data */
    V288SENDANDGET;
    /*printf("v288Get returns %d\n",tmp);*/
    if(tmp<=0) continue;

#ifndef VXWORKS
    for(ii=0; ii<tmp; ii++) buffer[ii] = SSWAP(buffer[ii]);
#endif
    /* print results 
    for(ii=0; ii<tmp; ii++) printf("[%3d] %5d   0x%04x\n",ii,buffer[ii],buffer[ii]);
    */

    bname = (char *)&buffer[0];
    strncpy(m,bname,5); /* max 5 characters */
    m[5] = '\0'; /* in case of 5-char name 'm' will not be null-terminated, so do it */
    /*printf("Board name: >%5.5s< (len=%d)\n",bname,strlen(m));*/

    strcpy(d,"n/a");

    tmp = b8[5];
    if(tmp==0) strcpy(Iunits,"A ");
    else if(tmp==1) strcpy(Iunits,"mA");
    else if(tmp==2) strcpy(Iunits,"uA");
    else if(tmp==3) strcpy(Iunits,"nA");
    /*printf("[%2d] Current units: %s\n",i,Iunits);*/

#ifndef VXWORKS
    buffer[3] = SSWAP(buffer[3]);
#endif

    u2[i] = buffer[3];
    /*printf("Serial number %d\n",buffer[3]);*/

    c2[i] = b8[8];
    c1[i] = b8[9];
    /*printf("Software version %2d.%02d\n",b8[8],b8[9]);*/

    u1[i] = (unsigned short)b8[30];
    /*printf("Num. of Channels %d (%d 0x%08x)\n",b8[30],u1[i],&u1[i]);*/


    Vmax = (b8[35]<<24)+(b8[36]<<16)+(b8[37]<<8)+b8[38];
    Imax = (b8[39]<<8)+b8[40];
    Rampmin = (b8[41]<<8)+b8[42];
    Rampmax = (b8[43]<<8)+b8[44];
    Vres = (b8[45]<<8)+b8[46];
    Ires = (b8[47]<<8)+b8[48];
    Vdec = (b8[49]<<8)+b8[50];
    Idec = (b8[51]<<8)+b8[52];

    sy527[id].scalev[i] = paw_10[Vdec];
    sy527[id].scalei[i] = paw_10[Idec];

    //printf("Scale Factors:  I=%.0f V=%.0f\n",sy527[id].scalei[i],sy527[id].scalev[i]);

    /*
    printf("Vmax=%d V\n",Vmax);
    printf("Imax=%d %s\n",Imax,Iunits);
    printf("Rampmin=%d V/sec\n",Rampmin);
    printf("Rampmax=%d V/sec\n",Rampmax);
	*/
	/*
    printf("\n");
    printf("[%2d] Vres=%d*0.01 V\n",i,Vres);
    printf("[%2d] Ires=%d*0.01 %s\n",i,Ires,Iunits);
    printf("[%2d] Vdec=%d significant figures after the decimal point\n",i,Vdec);
    printf("[%2d] Idec=%d significant figures after the decimal point\n",i,Idec);
    printf("\n");
	*/
  }

  return(CAENHV_OK);
}


#define V288SENDANDGETBIG \
    if(pthread_mutex_lock(&v288_mutex)<0) perror("pthread_mutex_lock");\
    v288Send(addr, crate, code, value); \
    tmp = v288Get(addr, 2048, buffer); \
    if(pthread_mutex_unlock(&v288_mutex)<0) perror("pthread_mutex_unlock")

/*
   CAENHVGetGroupList

   input:
      group - group number
            - 0 is all channels in mainframe
            - doc says only 16 groups are allowed (0-15)

   output:
      slot - array of slot numbers
      chan - array of channel numbers

   return value:
      number of channels in the group
 */
int
CAENHVGetGroupList(
    const char* SystemName, ushort group,
    int *slot, int* chan)
{
  const int wpc=2; // words per channel
  int tmp,jj,id=0;
  UINT32 addr=0;
  UINT16 code=0,crate=0,value[20],buffer[2048];
 
  GET_SYSTEM_ID(SystemName);
  
  int nchan=0;
  value[0] = group;

  // Read channel list:
  code = 0x40;
  V288SENDANDGETBIG;
  for (jj=0; jj<tmp; jj++)
  {
    // should this be a break?
    if (buffer[jj] == 0xFFFF) continue;

    // the first 6 words are group name, ignore them:
    if (jj<6) continue;
   
    // word pairs:
    //  - first is slot/channel
    //  - second is on/off priority for group operations, ignore it
    //      - 0x0101 by default for group-0
    //      - two bytes are on and off priorities
    if (jj%wpc==0)
    {
      slot[nchan] = buffer[jj] >> 8;
      chan[nchan] = buffer[jj] & 0xFF;
      nchan++;
    }
  }
  return nchan;
}

// NAB:  going to have to sort out slot-based scale factors
int
CAENHVGetGroupFast(
    const char* SystemName, ushort group,
    float* vmon, float* imon, float* smax, int* stat,
    float* vset, float* iset)
{
  int wpc; // words per channel
  int tmp,jj,id=0,nchan=0;
  UINT32 addr=0;
  UINT16 code=0,crate=0,value[20],buffer[2048];
  GET_SYSTEM_ID(SystemName);
  value[0] = group;
  
  // Read IMON, VMON, and STAT:
  code = 0x41;
  wpc = 5;
  V288SENDANDGETBIG;
  nchan = tmp/wpc;
  if (nchan<=0 || nchan>MAX_CHAN*MAX_SLOT)
  {
    printf("CAENHVGetGroupFast:  V0SET/I0SET:  #CHAN ERROR:  %d/%d==%d\n",tmp,wpc,nchan);
    return 0;
  }
  for (jj=0; jj<tmp; jj+=wpc)
  {
    vmon[jj/wpc] = (float)((buffer[jj]<<16) + buffer[jj+1]);
    smax[jj/wpc] = buffer[jj+2];
    imon[jj/wpc] = buffer[jj+3];
    stat[jj/wpc] = buffer[jj+4];
  }

  // Read V0SET and I0SET:
  code = 0x43;
  wpc = 3;
  V288SENDANDGETBIG;
  if (tmp/wpc != nchan)
  {
    printf("CAENHVGetGroupFast:  V0SET/I0SET:  #CHAN ERROR:  %d!=%d\n",tmp/wpc,nchan);
    return 0;
  }
  for (jj=0; jj<tmp; jj+=wpc)
  {
    //ss = slot[jj/wpc];
    vset[jj/wpc] = (float)((buffer[jj]<<16) + buffer[jj+1]);
    iset[jj/wpc] = buffer[jj+2];
    //vset[jj/wpc] /= (float)sy527[id].scalev[ss];
    //iset[jj/wpc] /= (float)sy527[id].scalei[ss];
  }
  return nchan;
}

int
CAENHVGetGroupSlow(
    const char* SystemName, ushort group,
    float* vmax, float* trip, float* rup, float* rdn,
    int* flag)
{
  int wpc; // words per channel
  int tmp,jj,id=0,nchan=0;
  UINT32 addr=0;
  UINT16 code=0,crate=0,value[20],buffer[2048];
  
  GET_SYSTEM_ID(SystemName);

  value[0] = group;

  // Read VMAX, TRIP, and FLAG:
  code = 0x45;
  wpc = 3;
  V288SENDANDGETBIG;
  nchan = tmp/wpc;
  if (nchan<=0 || nchan>MAX_CHAN*MAX_SLOT)
  {
    printf("CAENHVGetGroupFast:  V0SET/I0SET:  #CHAN ERROR:  %d/%d==%d\n",tmp,wpc,nchan);
    return 0;
  }
  for (jj=0; jj<tmp; jj+=wpc)
  {
    vmax[jj/wpc] = buffer[jj];
    trip[jj/wpc] = buffer[jj+1];
    flag[jj/wpc] = buffer[jj+2];
  }

  // Read RAMPUP and RAMPDN:
  code = 0x46;
  wpc = 2;
  V288SENDANDGETBIG;
  if (tmp/wpc != nchan)
  {
    printf("CAENHVGetGroupSlow:  RUP/RDN:  #CHAN ERROR:  %d!=%d\n",tmp/wpc,nchan);
    return 0;
  }
  for (jj=0; jj<tmp; jj+=wpc)
  {
    rup[jj/wpc] = buffer[jj];
    rdn[jj/wpc] = buffer[jj+1];
  }

  return nchan;
}

/*
   CAENHVGetGroupParam

   input:
      group - group number
            - 0 is all channels in mainframe
            - doc says only 16 groups are allowed (0-15)
   output:
      slot,chan,vmon,imon,vset,iset,vmax,smax,trip,rup,rdn,flag,stat

   return value:
      number of channels in the group
  
  Stops at the first sign of error and returns 0.
 */
int
CAENHVGetGroupParam(
    const char* SystemName, ushort group,
    int* slot, int* chan,
    float* vmon, float* imon,
    float* vset, float* iset,
    float* vmax, float* smax,
    float* trip, float* rup, float* rdn,
    int* flag, int* stat)
{
  int wpc; // words per channel
  int tmp,ss,jj,id=0,nchan=0;
  UINT32 addr=0;
  UINT16 code=0,crate=0,value[20],buffer[2048];
  
  GET_SYSTEM_ID(SystemName);

  value[0] = group;

  // Start by reading channel list:
  nchan = 0;
  code = 0x40;
  wpc = 2;
  V288SENDANDGETBIG;
  for (jj=0; jj<tmp; jj++)
  {
    // should this be a break?
    if (buffer[jj] == 0xFFFF) continue;

    // the first 6 words are group name, let's ignore them:
    if (jj<6) continue;
   
    // word pairs:
    //  - first of pair is slot/channel
    //  - second of pair is on/off priority for group operations, ignore it
    //      - 0x0101 by default for group-0
    //      - two bytes are on and off priorities
    if (jj%wpc==0)
    {
      slot[nchan] = buffer[jj] >> 8;
      chan[nchan] = buffer[jj] & 0xFF;
      nchan++;
    }
  }

  if (nchan<=0 || nchan>MAX_SLOT*MAX_CHAN) 
  {
    printf("CAENHVGetGroupParam:  #CHAN ERROR:  %d\n",nchan);
    return 0;
  }

  // Read V0SET and I0SET:
  code = 0x43;
  wpc = 3;
  V288SENDANDGETBIG;
  if (tmp/wpc != nchan)
  {
    printf("CAENHVGetGroupParam:  V0SET/I0SET:  #CHAN ERROR:  %d!=%d\n",tmp/wpc,nchan);
    return 0;
  }
  for (jj=0; jj<tmp; jj+=wpc)
  {
    ss = slot[jj/wpc];
    vset[jj/wpc] = (float)((buffer[jj]<<16) + buffer[jj+1]);
    iset[jj/wpc] = buffer[jj+2];
    vset[jj/wpc] /= (float)sy527[id].scalev[ss];
    iset[jj/wpc] /= (float)sy527[id].scalei[ss];
  }

  // Read VMAX, TRIP, and FLAG:
  code = 0x45;
  wpc = 3;
  V288SENDANDGETBIG;
  if (tmp/wpc != nchan)
  {
    printf("CAENHVGetGroupParam:  VMAX/TRIP/FLAG:  #CHAN ERROR:  %d!=%d\n",tmp/wpc,nchan);
    return 0;
  }
  for (jj=0; jj<tmp; jj+=wpc)
  {
    vmax[jj/wpc] = buffer[jj];
    trip[jj/wpc] = buffer[jj+1];
    flag[jj/wpc] = buffer[jj+2];
  }

  // Read RAMPUP and RAMPDN:
  code = 0x46;
  wpc = 2;
  V288SENDANDGETBIG;
  if (tmp/wpc != nchan)
  {
    printf("CAENHVGetGroupParam:  RUP/RDN:  #CHAN ERROR:  %d!=%d\n",tmp/wpc,nchan);
    return 0;
  }
  for (jj=0; jj<tmp; jj+=wpc)
  {
    rup[jj/wpc] = buffer[jj];
    rdn[jj/wpc] = buffer[jj+1];
  }

  // Read VMON, IMON, VMAX, and STAT:
  code = 0x41;
  wpc = 5;
  V288SENDANDGETBIG;
  if (tmp/wpc != nchan)
  {
    printf("CAENHVGetGroupParam:  VMON/IMON/STAT:  #CHAN ERROR:  %d!=%d\n",tmp/wpc,nchan);
    return 0;
  }
  for (jj=0; jj<tmp; jj+=wpc)
  {
    ss = slot[jj/wpc];
    vmon[jj/wpc] = (float)((buffer[jj]<<16) + buffer[jj+1]);
    smax[jj/wpc] = buffer[jj+2];
    imon[jj/wpc] = buffer[jj+3];
    stat[jj/wpc] = buffer[jj+4];
    vmon[jj/wpc] /= (float)sy527[id].scalev[ss];
    imon[jj/wpc] /= (float)sy527[id].scalei[ss];
  }

  // success, just return #channels:
  return nchan;
}


/*
   input:
      ChNum - the number of channels
      ChList - list of channels (length=ChNum)

   output:
      ParValList - list of values (length=ChNum)
 */
int
CAENHVGetChParam(const char *SystemName, ushort slot, const char *ParName,
                 ushort ChNum, const ushort *ChList, void *ParValList)
{
  int id=0; /// my:
  UINT16 crate=0, code, value[20]; /// my:
  UINT16 buffer[1024];
  static UINT16 buffer1[MAX_CHAN][MAX_V288GET], buffer2[MAX_CHAN][MAX_V288GET];
  int i, ich, tmp=0;
  UINT32 addr=0; /// my:
  char *ch;
  int V0set, V1set, I0set, I1set, SVmax, Rup, Rdwn, Trip, Flag;
  int Vmon, HVmax, Imon, Status;
  float *fval = ParValList;
  int *ival = ParValList;

  GET_SYSTEM_ID(SystemName);

  /*printf("CAENHVGetChParam reached\n");*/

  /* loop over 'ChNum' channels */
  for(ich=0; ich<ChNum; ich++)
  {

    /* hack to speed things up: read hardware ONLY if 'V0Set' is requested;
       we assume that parameters are requested in the same order starting from 'V0Set' */
    if( !strcmp(ParName,"V0Set") )
    //if( 1 )
    {
      value[0] = (slot<<8) + ChList[ich];

      /* gets preseted channel parameters */
      code = 2;
      V288SENDANDGET;
      if(tmp > MAX_V288GET)
      {
        printf("WARN: v288Get(1) returned %d, cut to %d\n",tmp,MAX_V288GET);
        tmp = MAX_V288GET;
      }
      for(i=0; i<tmp; i++) buffer1[ich][i] = buffer[i];
      /*printf("v288Get returns %d\n",tmp);*/
      /*for(i=0; i<tmp; i++) printf("[%3d] %5d   0x%04x\n",i,buffer1[ich][i],buffer1[ich][i]);*/
      /*printf("\n");*/

      /* gets status channel parameters */
      code = 1;
      V288SENDANDGET;
      if(tmp > MAX_V288GET)
      {
        printf("WARN: v288Get(2) returned %d, cut to %d\n",tmp,MAX_V288GET);
        tmp = MAX_V288GET;
      }
      for(i=0; i<tmp; i++) buffer2[ich][i] = buffer[i];
      /*printf("v288Get returns %d\n",tmp);*/
      /*for(i=0; i<tmp; i++) printf("[%3d] %5d   0x%04x\n",i,buffer2[ich][i],buffer2[ich][i]);*/
      /*printf("\n");*/
    }

    ch = (char *)&buffer1[ich][0];
    /*printf("Channel name >%s<\n",ch);*/

    V0set = (buffer1[ich][6]<<16) + buffer1[ich][7];
    V1set = (buffer1[ich][8]<<16) + buffer1[ich][9];
    I0set = buffer1[ich][10];
    I1set = buffer1[ich][11];
    SVmax = buffer1[ich][12];
    Rup = buffer1[ich][13];
    Rdwn = buffer1[ich][14];
    Trip = buffer1[ich][15];
    Flag = buffer1[ich][17]; /*what about 16 ??*/

    Vmon = (buffer2[ich][0]<<16) + buffer2[ich][1];
    HVmax = buffer2[ich][2];
    Imon = buffer2[ich][3];
    Status = buffer2[ich][4];

    /*
    printf("V0set=%d\n",V0set);
    printf("V1set=%d\n",V1set);
    printf("I0set=%d\n",I0set);
    printf("I1set=%d\n",I1set);
    printf("SVmax=%d\n",SVmax);
    printf("Rup=%d\n",Rup);
    printf("Rdwn=%d\n",Rdwn);
    printf("Trip=%d\n",Trip);
    printf("Flag=%d\n",Flag);
    printf("Vmon=%d\n",Vmon);
    printf("HVmax=%d\n",HVmax);
    printf("Imon=%d\n",Imon);
    */

    /* HAVE TO REPORT SOME OF FOLLOWING !!!
    printf("Status=%d\n",Status);
    if(Status&0x0001) printf("Status: Channel Present\n");
    else              printf("Status: Channel not Present\n");
    if(Status&0x0020) printf("Status: Internal Trip\n");
    if(Status&0x0040) printf("Status: Kill\n");
    if(Status&0x0100) printf("Status: Vmax\n");
    if(Status&0x0200) printf("Status: External Trip\n");
    if(Status&0x0400) printf("Status: Overvoltage\n");
    if(Status&0x0800) printf("Status: Undervoltage\n");
    if(Status&0x1000) printf("Status: Overcurrent\n");
    if(Status&0x2000) printf("Status: Down\n");
    if(Status&0x4000) printf("Status: Up\n");
    if(Status&0x8000) printf("Status: Channel On\n");
    else              printf("Status: Channel Off\n");
	*/

    if(      !strcmp(ParName,"V0Set") )  fval[ich] = ((float)V0set)/sy527[id].scalev[slot];
    else if( !strcmp(ParName,"I0Set") )  fval[ich] = ((float)I0set)/sy527[id].scalei[slot];
    else if( !strcmp(ParName,"V1Set") )  fval[ich] = ((float)V1set)/sy527[id].scalev[slot];
    else if( !strcmp(ParName,"I1Set") )  fval[ich] = ((float)I1set)/sy527[id].scalei[slot];
    else if( !strcmp(ParName,"Rup") )    fval[ich] = (float)Rup;
    else if( !strcmp(ParName,"Rdwn") )   fval[ich] = (float)Rdwn;
    else if( !strcmp(ParName,"Trip") )   fval[ich] = (float)Trip;
    else if( !strcmp(ParName,"SVMax") )  fval[ich] = (float)SVmax;
    else if( !strcmp(ParName,"VMon") )   fval[ich] = ((float)Vmon)/sy527[id].scalev[slot];
    else if( !strcmp(ParName,"IMon") )   fval[ich] = ((float)Imon)/sy527[id].scalei[slot];
    else if( !strcmp(ParName,"Status") ) ival[ich] = (int)Status;
    else if( !strcmp(ParName,"Pw") )     ival[ich] = 0;
    else if( !strcmp(ParName,"PrOn") )   ival[ich] = 0;
    else if( !strcmp(ParName,"PrOff") )  ival[ich] = 0;
    else if( !strcmp(ParName,"Pon") )    ival[ich] = 0;
    else if( !strcmp(ParName,"Pdwn") )   fval[ich] = 0.0;
    else                                 fval[ich] = 0.0;
  }



  return(CAENHV_OK);
}


int
CAENHVSetGroupOnOff(const char* SystemName, ushort group,ushort onoff)
{
  int tmp,id=0;
  UINT32 addr=0;
  UINT16 code=0,crate=0,value[20],buffer[2048];
  
  GET_SYSTEM_ID(SystemName);

  value[0] = group;

  if (onoff) code = 0x5A;
  else       code = 0x5B;
  V288SENDANDGETBIG;

  return (CAENHV_OK);
}

int
CAENHVSetGroupParam(const char* SystemName, ushort group, 
                    const char* ParName,float fval)
{
  int tmp,id=0;
  UINT32 addr=0;
  UINT16 code=0,crate=0,value[20],buffer[1024];

  // Groups must be of similar cards due to scale factors.
  // Need to attach a slot number to the group.
  int slot = 0;

  GET_SYSTEM_ID(SystemName);

  value[0] = group;

  if(!strcmp(ParName,"V0Set") )
  {
    code = 0x52;
    value[1] = (int)(fval*sy527[id].scalev[slot]);
    printf("CAENHVSetGroupParam:  %.2f %d\n",fval,value[1]);
  }
  else if( !strcmp(ParName,"I0Set") )
  {
    code = 0x54;
    value[1] = (int)(fval*sy527[id].scalei[slot]);
  }
  else if( !strcmp(ParName,"V1Set") )
  {
    code = 0x53;
    value[1] = (int)(fval*sy527[id].scalev[slot]);
  }
  else if( !strcmp(ParName,"I1Set") )
  {
    code = 0x55;
    value[1] = (int)(fval*sy527[id].scalei[slot]);
  }
  else if( !strcmp(ParName,"Rup") )
  {
    code = 0x57;
    value[1] = (int)(fval);
  }
  else if( !strcmp(ParName,"Rdwn") )
  {
    code = 0x58;
    value[1] = (int)(fval);
  }
  else if( !strcmp(ParName,"Trip") )
  {
    code = 0x59;
    value[1] = (int)(fval);
  }
  else if( !strcmp(ParName,"SVMax") )
  {
    code = 0x56;
    value[1] = (int)(fval);
  }
  else if ( !strcmp(ParName,"Pw"))
  {
    if (fval < 0.5) code = 0x5B; // OFF
    else            code = 0x5A; // ON
  }
  else
  {
    printf("CAENHVSetGroupParam:  ERROR:  ParName:  %s\n",ParName);
    return (CAENHV_SYSERR);
  }

  printf("CAENHVSetGroupParam:  0x%x %d %d\n",code,value[0],value[1]);

  V288SENDANDGET;

  return (CAENHV_OK);
}

int
CAENHVSetChParam(const char *SystemName, ushort slot, const char *ParName,
                 ushort ChNum, const ushort *ChList, void *ParValue)
{
  int id=0; /// my:
  int ich, bit, tmp=0;
  UINT16 crate=0, code, value[20], buffer[1024]; /// my:
  UINT32 addr=0; /// my:
  float *fval = ParValue;
  int *ival = ParValue;

  //usleep(120000); /// my: inserted although VME access is synchronized (probably: no way to switch frequently)

  // NAB: try this instead:
  usleep(48000);
  //usleep(12000);
  //usleep(1200);
  //usleep(120);
  //usleep(12);

  // NAB:  ^ that is a critical parameter
  // too small and writes are missed, too large and unnecessarily block the scan thread
  // i haven't figured out how writes can be missed, regardless the value


  GET_SYSTEM_ID(SystemName);
  /*printf("CAENHVSetChParam reached\n");*/

  /* loop over 'ChNum' channels */
  for(ich=0; ich<ChNum; ich++)
  {
    value[0] = (slot<<8) + ChList[ich];

    if(      !strcmp(ParName,"V0Set") )
    {
      code = 0x10;
      value[1] = (int)(fval[ich]*sy527[id].scalev[slot]);
    }
    else if( !strcmp(ParName,"I0Set") )
    {
      code = 0x12;
      value[1] = (int)(fval[ich]*sy527[id].scalei[slot]);
    }
    else if( !strcmp(ParName,"V1Set") )
    {
      code = 0x11;
      value[1] = (int)(fval[ich]*sy527[id].scalev[slot]);
    }
    else if( !strcmp(ParName,"I1Set") )
    {
      code = 0x13;
      value[1] = (int)(fval[ich]*sy527[id].scalei[slot]);
    }
    else if( !strcmp(ParName,"Rup") )
    {
      code = 0x15;
      value[1] = (int)(fval[ich]);
    }
    else if( !strcmp(ParName,"Rdwn") )
    {
      code = 0x16;
      value[1] = (int)(fval[ich]);
    }
    else if( !strcmp(ParName,"Trip") )
    {
      code = 0x17;
      value[1] = (int)(fval[ich]);
    }
    else if( !strcmp(ParName,"SVMax") )
    {
      code = 0x14;
      value[1] = (int)(fval[ich]);
    }
    /*else if( !strcmp(ParName,"VMon") )
      {
      ;
      }*/
    /*else if( !strcmp(ParName,"IMon") )
      {
      ;
      }*/
    /*else if( !strcmp(ParName,"Status") )
      {
      ;
      }*/
    /* NOTE: few following parameters are set using 'Flag' bits (code=0x18) */
    /* flag bit 3 (mask bit 11) (Pw) - Power,
       flag bit 6 (mask bit 14) (on/off) - enable,
       flag bit 7 (mask bit 15) (Pwon) -
     (if mask bit=0, parameter maintain old value, if =1, parameter take value from flag)
     */
    else if( !strcmp(ParName,"Pw") ) /* bit 'Power' ??? */
    {
      code = 0x18;
      bit = ival[ich] & 0x1; /* can be 0 or 1 */
      value[1] = ((bit<<3) | (1<<11));
      ///  printf("Pw: 0x%04x\n",value[1]);
    }
    /*else if( !strcmp(ParName,"PrOn") )
      {
      ;
      }*/
    /*else if( !strcmp(ParName,"PrOff") )
      {
      ;
      }*/
    else if( !strcmp(ParName,"Pon") ) /* bit 'Power-on enable' ??? */
    {
      code = 0x18;
      bit = ival[ich] & 0x1; /* can be 0 or 1 */
      value[1] = ((bit<<6) | (1<<14));
      //printf("Pon: 0x%04x\n",value[1]);
    }
    /*else if( !strcmp(ParName,"Pdwn") )
      {
      ;
      }*/
    else
    {
      printf("CAENHVSetChParam: ERROR: unknown ParName >%s<\n",ParName);
      continue;
    }

    V288SENDANDGET;
    /*printf("v288Get returns %d\n",tmp);*/
  }

  return(CAENHV_OK);
}

/* here only PropName='Type' is supported; for input 'ParName' it will
return one of four values through 'retval' */

int
CAENHVGetChParamProp(const char *SystemName, ushort slot, ushort ChNum,
                     const char *ParName, const char *PropName, void *retVal)
{
  int id, crate;
  unsigned int addr;
  unsigned long *retval = retVal;

  /* expecting 'Type' only */
  if(strncmp(PropName,"Type",4))
  {
    printf("Only PropName 'Type' currently supported\n");
    return(CAENHV_SYSERR);
  }

  GET_SYSTEM_ID(SystemName);
  /*printf("CAENHVGetChParamProp reached\n");*/

  /*A944*/
  if(!strncmp(ParName,"V0Set",5))       *retval = PARAM_TYPE_NUMERIC;
  else if(!strncmp(ParName,"I0Set",5))  *retval = PARAM_TYPE_NUMERIC;
  else if(!strncmp(ParName,"V1Set",5))  *retval = PARAM_TYPE_NUMERIC;
  else if(!strncmp(ParName,"I1Set",5))  *retval = PARAM_TYPE_NUMERIC;
  else if(!strncmp(ParName,"Rup",3))    *retval = PARAM_TYPE_NUMERIC;
  else if(!strncmp(ParName,"Rdwn",4))   *retval = PARAM_TYPE_NUMERIC;
  else if(!strncmp(ParName,"Trip",4))   *retval = PARAM_TYPE_NUMERIC;
  else if(!strncmp(ParName,"SVMax",5))  *retval = PARAM_TYPE_NUMERIC;
  else if(!strncmp(ParName,"VMon",4))   *retval = PARAM_TYPE_NUMERIC;
  else if(!strncmp(ParName,"IMon",4))   *retval = PARAM_TYPE_NUMERIC;
  else if(!strncmp(ParName,"Status",6)) *retval = PARAM_TYPE_CHSTATUS;
  else if(!strncmp(ParName,"Pw",2))     *retval = PARAM_TYPE_ONOFF;
  else if(!strncmp(ParName,"PrOn",4))   *retval = PARAM_TYPE_ONOFF;
  else if(!strncmp(ParName,"PrOff",5))  *retval = PARAM_TYPE_ONOFF;
  else if(!strncmp(ParName,"Pon",3))    *retval = PARAM_TYPE_ONOFF;
  else if(!strncmp(ParName,"Pdwn",4))   *retval = PARAM_TYPE_NUMERIC;
  else
  {
    *retval = PARAM_TYPE_NUMERIC;
    return(CAENHV_SYSERR);
  }

  return(CAENHV_OK);
}



/**************************************************************************/
/**************************************************************************/
/**************************************************************************/
/**************************************************************************/
/**************************************************************************/




#else /* vxWorks or Linux */

void
v288_dummy()
{
  return;
}

#endif
