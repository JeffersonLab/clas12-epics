
/* sy1527.c - EPICS driver support for CAEN SY1527 HV mainframe */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>

#include "sy1527.h"

#include "smiuirtl.h"
//#include "CAENHVWrapper.h"

/* mainframe threads id's and statistic structures */
static pthread_t idth[MAX_HVPS];
static THREAD stat[MAX_HVPS];

/* mutexes */
static pthread_mutexattr_t mattr;
static pthread_mutex_t global_mutex;       /* to access inter-mainframe info */
static pthread_mutex_t mainframe_mutex[MAX_HVPS]; /* to access one mainframe */

#define LOCK_MAINFRAME(id_m)   pthread_mutex_lock(&mainframe_mutex[id_m])
#define UNLOCK_MAINFRAME(id_m) pthread_mutex_unlock(&mainframe_mutex[id_m])



/* flag to tell mainframe thread it is time to exit */
static int force_exit[MAX_HVPS];

/* mainframes */
int nmainframes = -1;     // the number of active mainframes /// my: static removed
int mainframes[MAX_HVPS]; /* list of active mainframes */
int mainframes_disconnect[MAX_HVPS]; // my_n: indicate connect status  
static HV Demand[MAX_HVPS];
HV Measure[MAX_HVPS];
int is_mainframe_read[MAX_HVPS]; // my: flag to prevent epics value init before reading by driver

// we're going to restart the connection if we hit this error too many times consecutively:
static const int MAXCFEDOWNERR=100;
int NCFEDOWNERR[MAX_HVPS];

/* board-dependent parameter sets */

#define V0Set   0
#define I0Set   1
#define V1Set   2
#define I1Set   3
#define RUp     4
#define RDWn    5
#define Trip    6  // my: set trip time
#define SVMax   7  // my: set software voltage limit
#define VMon    8
#define IMon    9
#define Status  10
#define Pw      11  // my: set on or off
#define PwEn    12 // my: POn and PwEn are the same, so the PwEn is kept here   
#define TripInt 13
#define TripExt 14
#define PDwn  15   // my: PDwn replaced Tdrift

static int  nA1520param = 16; // my: 16
static int  nA1535param = 16;
static int  nA1536HDMparam = 18;

static char A1535param[MAX_PARAM][MAX_CAEN_NAME] = {
                "V0Set","I0Set","V1Set","I1Set","RUp","RDWn","Trip","SVMax",
                "VMon","IMon","Status","Pw","POn","TripInt","TripExt","PDwn"};
static char A1520param[MAX_PARAM][MAX_CAEN_NAME] = {
                "V0Set","I0Set","V1Set","I1Set","RUp","RDWn","Trip","SVMax",
                "VMon","IMon","Status","Pw","PwEn","TripInt","TripExt","Tdrift"};
static char A1536HDMparam[MAX_PARAM][MAX_CAEN_NAME] = {
                "V0Set","I0Set","V1Set","I1Set","RUp","RDWn","Trip","SVMax",
                "VMon","IMon","Status","Pw","POn","TripInt","TripExt","PDwn","ImRange","Pol"};

///----------------- for HV parameters finding ------------------- 

#include <linux/limits.h>
char *g_parr;
int g_parr_index[MAX_PARAM];
FILE *fp_params=NULL;

///---------------------------------------------------------------
/**********************/
/* some usefun macros */

/* check if 'id' is reasonable */
#define CHECK_ID(id_m) \
  if(id_m < 0 || id_m >= MAX_HVPS) \
  { \
    printf("ERROR(sy1527): bad id: 0<=%d<%d is not true\n",id_m,MAX_HVPS); \
    return(CAENHV_SYSERR); \
  }

/* check if that channel is free */
#define CHECK_FREE(id_m) \
  if(Measure[id_m].id != -1) \
  { \
    printf("ERROR(sy1527): communication #%d is not free\n",id_m); \
    return(CAENHV_SYSERR); \
  }

/* check if that channel is opened */
#define CHECK_OPEN(id_m) \
  if(Measure[id_m].id == -1) \
  { \
    printf("ERROR(sy1527): communication #%d is not opened\n",id_m); \
    return(CAENHV_SYSERR); \
  }


/*****************************************************************************/
/**************************** Low level functions ****************************/
/*****************************************************************************/
int
sy1527Measure2Demand(unsigned int id, unsigned int board)
{
  printf("sy1527Measure2Demand: befor: %d %d\n",
      Demand[id].board[board].nchannels,Measure[id].board[board].nchannels);
  memcpy((BOARD *)&Demand[id].board[board].nchannels,
      (BOARD *)&Measure[id].board[board].nchannels,
      sizeof(BOARD));
  printf("sy1527Measure2Demand: after: %d %d\n",
      Demand[id].board[board].nchannels,Measure[id].board[board].nchannels);
  return(CAENHV_OK);
}

/// ==============   sy1527GetBoard ==========================
int
sy1527GetBoard(unsigned int id, unsigned int board)
{

  int b_status=0;/// b_status_res=0;

  int nXXXXXparam;
  char *XXXXparam[MAX_PARAM];

  char name[MAX_CAEN_NAME];
  int i, ipar, ret, i10;
  unsigned short Slot, ChNum, ChList[MAX_CHAN], Ch;
  float fParValList[MAX_CHAN];
  unsigned long	tipo, lParValList[MAX_CHAN];
  char ParName[MAX_CAEN_NAME];

  CHECK_ID(id);
  CHECK_OPEN(id);
  strcpy(name, Measure[id].name);

  for(i10=0;i10<nmainframes;i10++){
   if(mainframes[i10]==id)break;
  }


  nXXXXXparam = Measure[id].board[board].nparams;
  for(i=0;i<nXXXXXparam;i++) XXXXparam[i]=Measure[id].board[board].parnames[i];

  Slot = board;
  ChNum = Measure[id].board[board].nchannels;

  for(i = 0; i<ChNum; i++)
  {
    Ch = i;
    ChList[i] = (unsigned short)Ch;
  }

  /* loop over parameters */
  for(ipar=0; ipar<nXXXXXparam; ipar++)
  {
    strcpy(ParName,XXXXparam[ipar]); /* Param name */
    tipo = Measure[id].board[board].partypes[ipar];

    if(tipo == PARAM_TYPE_NUMERIC)
      ret = CAENHVGetChParam(name, Slot, ParName, ChNum, ChList, fParValList);
    else
      ret = CAENHVGetChParam(name, Slot, ParName, ChNum, ChList, lParValList);
/*
     int ret1,ret2;
     int retA=CAENHVGetSysProp(Measure[id].name,"FanStat",&ret1);
     int retB=CAENHVGetSysProp(Measure[id].name,"HvPwSM",&ret2);
     printf("NABO2:  FAN=%d/%d PW=%d/%d\n",ret1,retA,ret2,retB);

     // Note:  
     //    FanStat returned 0/-1
    //     HvPwSM  returned 976304689/0 

*/
    if(ret != CAENHV_OK)
    {
      printf("CAENHVGetChParam error: %s (#%d) threadId=%d, brd=%d, (%s) \n\n", CAENHVGetError(name), ret, id, board, ParName);
      mainframes_disconnect[i10]=1; /// my_n: hbeat

      // restart the connection:
      if (ret==5)
      {
        if (++NCFEDOWNERR[id] > MAXCFEDOWNERR)
        {
          printf("@@@@@@@@@@@@@@@@@@@ NABO:  REINITIALIZING\n");
          sy1527Stop(id);
          sleep(10);

          if (sy1527Start(id,Measure[id].IPADDR) != CAENHV_OK)
          {
            printf("@@@@@@@@@@@@@@@@@@ NABO:  REINITIALIZION FAILED.  WAITING 45s and RETRYING.\n");
            sleep(45);
            if (sy1527Start(id,Measure[id].IPADDR) != CAENHV_OK)
            {
              printf("@@@@@@@@@@@@@@@@@@ NABO:  REINITIALIZION FAILED TWICE.  LET PROCSERVE RESTART IT.\n");
              exit(1);
            }
          }
          sy1527GetMap(id);
          sy1527PrintMap(id);
        }
      }
      // only count consecutive errors:
      else NCFEDOWNERR[id]=0;

    }
    else
    {
      if(tipo == PARAM_TYPE_NUMERIC)
      {
        for(i=0; i<ChNum; i++)
          Measure[id].board[board].channel[i].fval[ipar] = fParValList[i];
      }
      else
      {
        for(i=0; i<ChNum; i++)   
        {
          Measure[id].board[board].channel[i].lval[ipar] = lParValList[i];
          if(ipar==Status){
            /// my: smi: accumulates all channels attuses into board status
            b_status = b_status | lParValList[i];
            if(!(lParValList[i] & 0x1))b_status = b_status | BIT_OFF; /// at least one channel in the board is OFF
          }
        }
      }
    }
  }
  return(CAENHV_OK);
}

int
sy1527CrateSmiInit(char *smi_obj_name, unsigned int id){
  int j, j10;
  for(j=0;j<MAX_SLOT;j++){
    for(j10=0;j10<MAX_BOARDPARTS;j10++){
      //   printf("%d %d %d\n",i,j,j10);
      boards_status[id][j][j10]=-1;
    }
  }
  return 0;
}

int
sy1527BoardSmiMonitor(char *epics_name, unsigned int id, unsigned int board, 
unsigned int first_channel, unsigned int chs_number)
{
  char *tmp1, *tmp2=epics_name;
  while((tmp1=strstr(tmp2,"_P"))){
    tmp2=tmp1+1;
  }
  int board_part=first_channel; /// my_n_smi: atoi(tmp2-1+strlen("_P"));

  int b_status=0, b_status_res=0;
  int i, i10;
  // id comes from db here.
  // if not connection: id is absent in mainframes[] (in mainframes[] it is present as -1)
  // if comment in startup.all: id is absent in mainframes[]
  int absent_error=1;
  for(i=0;i<nmainframes;i++){
    if(mainframes[i]==id){absent_error=0;i10=i;break;}

  }
  if(absent_error==0 && mainframes_disconnect[i10]==1)absent_error=3;
  else if(absent_error==0 && Demand[id].board[board].nchannels==0)absent_error=2;

  LOCK_MAINFRAME(id);
  for(i=first_channel; i<first_channel+chs_number; i++)
  {
    /// my: smi: accumulates all channels attuses into board status
    b_status = b_status |  Measure[id].board[board].channel[i].lval[Status];
    if(!(Measure[id].board[board].channel[i].lval[Status] & 0x1))b_status = b_status | BIT_OFF; /// at least one channel in the board is OFF
  }
  /// my:smi
  char smi_obj_name1[150];
  char smi_command[150];
  if(b_status & BIT_ON)b_status_res=BIT_ON;
  if(b_status & (BIT_RAMPUP | BIT_RAMPDOWN ))b_status_res=BIT_RAMPUP;
  if(b_status & BIT_OFF)b_status_res=BIT_OFF;
  if(b_status & (BIT_INTTRIP | BIT_EXTTRIP | BIT_OVERCUR | BIT_OVERVOLT | BIT_UNDERVOLT )) b_status_res=BIT_INTTRIP;
  if(b_status_res==BIT_ON)strcpy(smi_command,"SET_ON");
  else if(b_status_res==BIT_RAMPUP)strcpy(smi_command,"SET_RAMP");
  else if(b_status_res==BIT_OFF)strcpy(smi_command,"SET_OFF");
  else if(b_status_res==BIT_INTTRIP)strcpy(smi_command,"SET_ERROR");
  if(absent_error){
    if(absent_error==1)b_status_res=BIT_CRATE_OFF;
    else if(absent_error==2)b_status_res=BIT_BOARD_NOT_PRESENT;
    else if(absent_error==3)b_status_res=BIT_CRATE_OFF_ON_WAY; 
    strcpy(smi_command,"SET_ERROR");
  }

  if(b_status_res != boards_status[id][board][board_part]){
    sprintf(smi_obj_name1, "CLAS12::%s", epics_name);
    smiui_send_command(smi_obj_name1,  smi_command);
    printf("smi:  smi_obj_name=%s  smi_command=%s id=%d board=%d chas=%d abs_error=%d \n", smi_obj_name1, smi_command, id, board, Demand[id].board[board].nchannels, absent_error);
    boards_status[id][board][board_part]=b_status_res;
  }
  UNLOCK_MAINFRAME(id);
  return(CAENHV_OK);
}

///======================================================================================
int
sy1527SetBoard(unsigned int id, unsigned int board)
{
  int nXXXXXparam;
  char *XXXXparam[MAX_PARAM];

  char name[MAX_CAEN_NAME];
  int i, ipar, iparr, ret;
  unsigned short Slot, ChNum, Ch;
  float fParVal;
  unsigned long	tipo, lParVal;
  char ParName[MAX_CAEN_NAME];

  CHECK_ID(id);
  CHECK_OPEN(id);
  strcpy(name, Demand[id].name);

  nXXXXXparam = Demand[id].board[board].nparams;
  for(i=0;i<nXXXXXparam;i++) XXXXparam[i]=Demand[id].board[board].parnames[i];

  Slot = board;
  ChNum = Demand[id].board[board].nchannels;

  /* loop over parameters */
  for(iparr=0; iparr<nXXXXXparam; iparr++)
  {

    /* patch to make sure 'PwEn' always executed before 'Pw' */
    if(iparr == Pw)        ipar = PwEn;
    else if(iparr == PwEn) ipar = Pw;
    else                   ipar = iparr;

    strcpy(ParName,XXXXparam[ipar]); /* Param name */
    tipo = Demand[id].board[board].partypes[ipar];

    /* loop over all channels */
    for(Ch=0; Ch<ChNum; Ch++)
    {
      if(Demand[id].board[board].channel[Ch].setflag[ipar] == 1)
      {
        if(tipo == PARAM_TYPE_NUMERIC)
        {
          fParVal = Demand[id].board[board].channel[Ch].fval[ipar];
          /*printf("Set Value %s: %f\n",ParName,fParVal);*/
          ret = CAENHVSetChParam(name, Slot, ParName, 1, &Ch, &fParVal);
        }
        else
        {
          lParVal = Demand[id].board[board].channel[Ch].lval[ipar];
          printf(">>>>>>>>>>>>>> Set Value parname=%s: value=%ld  ipar=%d iparr=%d channel=%d\n",XXXXparam[ipar],lParVal, ipar, iparr, Ch);
          ret = CAENHVSetChParam(name, Slot, ParName, 1, &Ch, &lParVal);
        }

        if(ret != CAENHV_OK)
        {
          /* set was unsuccessful so return error */
          printf("CAENHVSetChParam error: %s (num. %d)\n",CAENHVGetError(name),ret);
          return(CAENHV_SYSERR);
        }
        else
        {
          /* set was successful so cleanup setflag */
          Demand[id].board[board].channel[Ch].setflag[ipar] = 0;
        }
      }
    }
  }

  return(CAENHV_OK);
}
int
sy1527PrintParams(unsigned int id)
{ 
  unsigned short NrOfSl, NrOfPar, *SerNumList, *NrOfCh;
  char *ModelList, *DescriptionList;
  unsigned char	*FmwRelMinList, *FmwRelMaxList;
  char name[MAX_CAEN_NAME];
  int i, ret,j,k;
  unsigned long tipo;

// important, taken from CEANHVWrapper.h:
#define MAX_PARAM_NAME 10

  char*  parNames1=(char*)NULL;
  char (*parNames2)[MAX_PARAM_NAME];
  char   parNames3[100][MAX_PARAM_NAME];

  CHECK_ID(id);
  CHECK_OPEN(id);
  strcpy(name, Measure[id].name);

  printf("\nENTER  sy1527PrintParams(%d) *************************************\n\n",id);

  ret = CAENHVGetCrateMap(name, &NrOfSl, &NrOfCh, &ModelList,
                          &DescriptionList, &SerNumList,
                          &FmwRelMinList, &FmwRelMaxList );
  if(ret != CAENHV_OK)
  {
    printf("ERROR(sy1527): %s (num. %d)\n\n", CAENHVGetError(name), ret);
    return(CAENHV_SYSERR);
  }
  
  char *m = ModelList;
  char *d = DescriptionList;

  printf("NrofSl=%d\n",NrOfSl);
  for(i=0; i<NrOfSl; i++, m+=strlen(m)+1, d+=strlen(d)+1)
  {
    if(*m == '\0')
    {
      printf("Board %2d: Not Present\n", i);
      continue;
    }
    printf("Board %2d: %s %s  Nr. Ch: %d  Ser. %d   Rel. %d.%d\n",
        i, m, d, NrOfCh[i], SerNumList[i], FmwRelMaxList[i], 
        FmwRelMinList[i]);

    // retrieve parameter names (for first channel only):
    ret=CAENHVGetChParamInfo(name,i,0,&parNames1);
    if (ret!=CAENHV_OK) {
      printf("\nCAENHVGetChParamInfo(%s,%d,%d) ERROR:  %d\n",name,i,0,CAENHV_OK);
      continue;
    }
    parNames2=(char(*)[MAX_PARAM_NAME])parNames1;
    for (j=0;parNames2[j][0];j++) {}
    printf("NrOfPar = %d\n",NrOfPar=j);
    for (j=0; j<NrOfPar; j++) {
      for (k=0; k<MAX_PARAM_NAME;k++) {
        if (!parNames2[j][k]) break;
        parNames3[j][k]=parNames2[j][k];
      }
      parNames3[j][k]='\0';
    }

    // retrieve parameter types:
    for (j=0; j<NrOfPar; j++) {
            printf("\n%s,%d,%d,%s,%s\n",name,i,0,parNames3[j],"Type");
      CAENHVGetChParamProp(name,i,0,parNames3[j],"Type",&tipo);
      if (ret==CAENHV_OK) printf("%s(%d) ",parNames3[j],(int)tipo);
      else printf("\nCAENHVGetChParamProp(%s,%d,%d,%s,%s) ERROR: %d\n",
          name,i,0,parNames3[j],"Type",ret);
    }
    printf("\n");

    if (parNames1!=NULL) free(parNames1);
  
  }
  printf("\nLEAVE  sy1527PrintParams(%d) *************************************\n\n",id);
  return(CAENHV_OK);
}

//==================================================================================================
/* */
int
sy1527GetMap(unsigned int id)
{ 
  unsigned short NrOfSl, *SerNumList, *NrOfCh, ChList[MAX_CHAN];
  char *ModelList, *DescriptionList;
  unsigned char	*FmwRelMinList, *FmwRelMaxList;
  char name[MAX_CAEN_NAME];
  int i, j, ret;
  unsigned long tipo;
  char ParName[MAX_CAEN_NAME];

  CHECK_ID(id);
  CHECK_OPEN(id);
  strcpy(name, Measure[id].name);

  printf("\nENTER  sy1527GetMap(%d/%s) *************************************\n\n",id,name);
  
  ret = CAENHVGetCrateMap(name, &NrOfSl, &NrOfCh, &ModelList,
                          &DescriptionList, &SerNumList,
                          &FmwRelMinList, &FmwRelMaxList );
  if(ret != CAENHV_OK)
  {
    printf("ERROR(sy1527): %s (num. %d)\n\n", CAENHVGetError(name), ret);
  }
  else
  {
    char *m = ModelList, *d = DescriptionList;

    printf("Measure MAP:\n\n");// my:
    printf("NrofSl=%d\n",NrOfSl); // my:
    Measure[id].nslots = NrOfSl;
    printf("=========================> %d %d\n",id,Measure[id].nslots); //my:
    Demand[id].nslots = NrOfSl;
    for(i=0; i<NrOfSl; i++, m+=strlen(m)+1, d+=strlen(d)+1)
    {
      if(*m == '\0')
      {
        Measure[id].board[i].nchannels = 0;
        Demand[id].board[i].nchannels = 0;
      }
      else
      {
        strncpy(Measure[id].board[i].modelname,m,MAX_CAEN_NAME-1);
        strncpy(Measure[id].board[i].description,d,MAX_CAEN_NAME-1);
        Measure[id].board[i].nchannels = NrOfCh[i];
        Measure[id].board[i].sernum = SerNumList[i];
        Measure[id].board[i].relmax = FmwRelMaxList[i];
        Measure[id].board[i].relmin = FmwRelMinList[i];
        strncpy(Demand[id].board[i].modelname,m,MAX_CAEN_NAME-1);
        strncpy(Demand[id].board[i].description,d,MAX_CAEN_NAME-1);
        Demand[id].board[i].nchannels = NrOfCh[i];
        Demand[id].board[i].sernum = SerNumList[i];
        Demand[id].board[i].relmax = FmwRelMaxList[i];
        Demand[id].board[i].relmin = FmwRelMinList[i];
        printf("Board %2d: %s %s  Nr. Ch: %d  Ser. %d   Rel. %d.%d\n",
            i, m, d, NrOfCh[i], SerNumList[i], FmwRelMaxList[i], 
            FmwRelMinList[i]);

        /* get params info */
        for(j=0; j<Demand[id].board[i].nchannels; j++)
          ChList[j] = (unsigned short)j;
        if(!strcmp(Measure[id].board[i].modelname,"A1535") ||
            !strcmp(Measure[id].board[i].modelname,"A1536") ||
            !strcmp(Measure[id].board[i].modelname,"A1733") ||
            !strcmp(Measure[id].board[i].modelname,"A1737")) // my: was A1520
        {

          printf("---> found board %s\n",Measure[id].board[i].modelname);
          Measure[id].board[i].nparams = nA1535param;
          Demand[id].board[i].nparams = nA1535param;
          for(j=0; j<Measure[id].board[i].nparams; j++)
          {
            strcpy(Measure[id].board[i].parnames[j],A1535param[j]);
            strcpy(Demand[id].board[i].parnames[j],A1535param[j]);
            strcpy(ParName,Measure[id].board[i].parnames[j]);

            //printf("\n%s,%d,%d,%s,%s\n",name,i,ChList[0],ParName,"Type");
            //strcpy(name,Measure[id].name);

            ret=CAENHVGetChParamProp(name,i,ChList[0],ParName,"Type",&tipo);
            if(ret != CAENHV_OK)
            {
              printf("CAENHVGetChParamProp error: %s (num. %d) ParName=>%s<\n",
                  CAENHVGetError(name),ret,ParName);
              Measure[id].board[i].nchannels = 0;
              Demand[id].board[i].nchannels = 0;
              return(CAENHV_SYSERR);
            }
            else
            {
              Measure[id].board[i].partypes[j] = tipo;
              Demand[id].board[i].partypes[j] = tipo;
            }
          }
        }
        else if( !strcmp(Measure[id].board[i].modelname,"A1520")) // my: was A1520
        {
          printf("---> found board %s\n",Measure[id].board[i].modelname);
          Measure[id].board[i].nparams = nA1520param;
          Demand[id].board[i].nparams = nA1520param;
          for(j=0; j<Measure[id].board[i].nparams; j++)
          {
            strcpy(Measure[id].board[i].parnames[j],A1520param[j]);
            strcpy(Demand[id].board[i].parnames[j],A1520param[j]);

            strcpy(ParName,Measure[id].board[i].parnames[j]);
            ret=CAENHVGetChParamProp(name,i,ChList[0],ParName,"Type",&tipo);
            if(ret != CAENHV_OK)
            {
              printf("CAENHVGetChParamProp error: %s (num. %d) ParName=>%s<\n",
                  CAENHVGetError(name),ret,ParName);
              Measure[id].board[i].nchannels = 0;
              Demand[id].board[i].nchannels = 0;
              return(CAENHV_SYSERR);
            }
            else
            {
              Measure[id].board[i].partypes[j] = tipo;
              Demand[id].board[i].partypes[j] = tipo;
            }
          }
        }
        else if( !strcmp(Measure[id].board[i].modelname,"A1536HDM")) // my: was A1520
        {
          printf("---> found board %s\n",Measure[id].board[i].modelname);
          Measure[id].board[i].nparams = nA1536HDMparam;
          Demand[id].board[i].nparams = nA1536HDMparam;
          for(j=0; j<Measure[id].board[i].nparams; j++)
          {
            strcpy(Measure[id].board[i].parnames[j],A1536HDMparam[j]);
            strcpy(Demand[id].board[i].parnames[j],A1536HDMparam[j]);

            strcpy(ParName,Measure[id].board[i].parnames[j]);
            ret=CAENHVGetChParamProp(name,i,ChList[0],ParName,"Type",&tipo);
            if(ret != CAENHV_OK)
            {
              printf("CAENHVGetChParamProp error: %s (num. %d) ParName=>%s<\n",
                  CAENHVGetError(name),ret,ParName);
              Measure[id].board[i].nchannels = 0;
              Demand[id].board[i].nchannels = 0;
              return(CAENHV_SYSERR);
            }
            else
            {
              Measure[id].board[i].partypes[j] = tipo;
              Demand[id].board[i].partypes[j] = tipo;
            }
          }
        }
        else
        {
          printf("Unknown board =%s\n",Measure[id].board[i].modelname);
          Measure[id].board[i].nchannels = 0;
          Demand[id].board[i].nchannels = 0;
        }
      }
    }
    /*printf("\n");*/
    free(SerNumList);
    free(ModelList);
    free(DescriptionList);
    free(FmwRelMinList);
    free(FmwRelMaxList);
    free(NrOfCh);
  }
  printf("\nLEAVE  sy1527GetMap(%d) *************************************\n\n",id);

  return(CAENHV_OK);
}
//==================================================================================================
int
sy1527PrintMap(unsigned int id)
{
  int i, j;
  CHECK_ID(id);
  CHECK_OPEN(id);
  printf("\n\nMAP for mainframe %d, nslots=%d\n\n",id,Measure[id].nslots);
  for(i=0; i<Measure[id].nslots; i++)
  {
    if(Measure[id].board[i].nchannels == 0)
    {
      printf("Board %2d: Not Present\n", i);
    }
    else
    {
      printf("Board %2d: %s %s  Nr. Ch: %d  Ser. %d   Rel. %d.%d\n",
          i,
          Measure[id].board[i].modelname,
          Measure[id].board[i].description,
          Measure[id].board[i].nchannels,
          Measure[id].board[i].sernum,
          Measure[id].board[i].relmax,
          Measure[id].board[i].relmin);
      printf("  nparams = %d\n",Measure[id].board[i].nparams);
      for(j=0; j<Measure[id].board[i].nparams; j++)
      {
        printf("    >%s<\t\t%ld",
            Measure[id].board[i].parnames[j],Measure[id].board[i].partypes[j]);
        if(Measure[id].board[i].partypes[j]==PARAM_TYPE_NUMERIC)
          printf(" (PARAM_TYPE_NUMERIC)\n");
        else if(Measure[id].board[i].partypes[j]==PARAM_TYPE_ONOFF)
          printf(" (PARAM_TYPE_ONOFF)\n");
        else if(Measure[id].board[i].partypes[j]==PARAM_TYPE_CHSTATUS)
          printf(" (PARAM_TYPE_CHSTATUS)\n");
        else if(Measure[id].board[i].partypes[j]==PARAM_TYPE_BDSTATUS)
          printf(" (PARAM_TYPE_BDSTATUS)\n");
        else
          printf(" (? ? ? UNKNOWN ? ? ?)\n");
      }
    }
  }
  printf("\n");
  return(CAENHV_OK);
}
//==================================================================================================
/* mainframe thread */
void *
sy1527MainframeThread(void *arg)
{
  int id, i, ret, status;

  id=((THREAD *)arg)->threadid;
  printf("[%2d] starts thread +++ ++\n",id);

  while(1)
  {
    sleep(1);
    LOCK_MAINFRAME(id);
    if(force_exit[id])
    {
      pthread_mutex_unlock(&mainframe_mutex[id]);
      break;
    }

    /* sets all existing boards in mainframe 'id' with 'setflag' */
    if(Demand[id].setflag == 1)
    {
      status = CAENHV_OK;
      for(i=0; i<Measure[id].nslots; i++)
      {
        if(Demand[id].board[i].nchannels > 0)
        {
          if(Demand[id].board[i].setflag == 1)
          {
            printf("[%2d] sets board %d\n",id,i); // my:
            ret = sy1527SetBoard(id,i);
            if(ret == CAENHV_OK) Demand[id].board[i].setflag = 0;
            else                 status |= CAENHV_SYSERR;
          }
        }
      }
      if(status == CAENHV_OK) Demand[id].setflag = 0;
    }

    /* gets all existing boards in mainframe 'id' */
    for(i=0; i<Measure[id].nslots; i++)
    {
      /* measure all active boards */
      if(Measure[id].board[i].nchannels > 0)
      {
        /*printf("[%2d] reads out board %d\n",id,i);*/
        ret = sy1527GetBoard(id,i);
      }
    }

    pthread_mutex_unlock(&mainframe_mutex[id]);
    for(i=0; i<nmainframes; i++){
      if(mainframes[i]==id)is_mainframe_read[i]=1;
    }
  }
  printf("[%2d] exit thread\n",id);

  return NULL;
}
//==================================================================================================
/* initialization */
int
sy1527Init()
{
  int i,j,j10;

  nmainframes = 0;
  memset(Measure,0,sizeof(HV)*MAX_HVPS);
  memset(Demand,0,sizeof(HV)*MAX_HVPS);
  for(i=0; i<MAX_HVPS; i++)
  {
    Measure[i].id = -1;
    Demand[i].id = -1;
    mainframes[i] = -1;
    mainframes_disconnect[i] = 0;
    is_mainframe_read[i]=0; // my: flag to prevent epics value init before reading by driver

    for(j=0;j<MAX_SLOT;j++){

      for(j10=0;j10<MAX_BOARDPARTS;j10++){
        boards_status[i][j][j10]=-1;
      }
    }

  }

  /* set mutex attributes */
  pthread_mutexattr_init(&mattr);
  pthread_mutexattr_setpshared(&mattr, PTHREAD_PROCESS_SHARED);

  /* init global mutex */
  pthread_mutex_init(&global_mutex, &mattr);

  return(CAENHV_OK);
}
//===========================================================================
/* open communication with mainframe under logical number 'id',
   do all necessary initialization and start thread */
int
sy1527Start(unsigned id_nowused, char *ip_address)
{
  int id;
  char arg[30], userName[20], passwd[30], name[MAX_CAEN_NAME];
  int link, ret;

  printf("\nENTER  sy1527Start(%s) *************************************\n\n",ip_address);

  pthread_mutex_lock(&global_mutex);

  /* do global initialization on first call */
  if(nmainframes == -1) sy1527Init();

  nmainframes++;
  id=id_nowused;

  printf("++++++++++++++++++++++++++++++++++++++++++++++++ nmainframes=%d id=%d\n", nmainframes, id);

  /* lock global mutex to prevent other mainframes to be started
     until we are done with this one */
  /// my: move upward - pthread_mutex_lock(&global_mutex); otherwise many sy1527Init() are possible

  if(nmainframes >= MAX_HVPS)
  {
    printf("ERROR: no more empty slots\n");
    pthread_mutex_unlock(&global_mutex);
    return(CAENHV_SYSERR);
  }

  CHECK_ID(id);
  CHECK_FREE(id);

  sprintf(name, CRATE_LABEL, id);
  printf("System Name set as >%s<\n",name);

  strcpy(arg,ip_address);
  printf("TCP/IP address set as >%s<\n",arg);
  link = LINKTYPE_TCPIP;

  strcpy(userName, "admin");
  strcpy(passwd, "admin");

  ret = CAENHVInitSystem(name, link, arg, userName, passwd);

  printf("my: id_index=%d id=%d name=%s", id, ret, name );
  printf("\nCAENHVInitSystem: %s (num. %d)\n\n", CAENHVGetError(name),ret);

  NCFEDOWNERR[id]=0;

  printf("\n\nRUNNING MODIFIED FOR CFE FIX.!!!!!!!!!!!!!!!!!!!!!!!\n\n");

  if(ret == CAENHV_OK)
  {
    if(strlen(ip_address)>=MAX_CAEN_NAME){printf("too long mainfraime IP: exits now\n");exit(1);}
    strcpy(Measure[id].IPADDR,ip_address);
    Measure[id].id = ret;
    strcpy(Measure[id].name, name); 
    Demand[id].id = ret;
    strcpy(Demand[id].name, name);
    //printf("aaaaaaaaaaaaaaaaaaaaaaa %s\n",Measure[id].name);
  }
  else
  {
    printf("\n CAENHVInitSystem returned %d\n\n",ret);    
    pthread_mutex_unlock(&global_mutex);
    return(CAENHV_SYSERR);
  }

  /* init mainframe mutex */
  pthread_mutex_init(&mainframe_mutex[id], &mattr);

  /* start thread */
  stat[id].threadid = id;
  force_exit[id] = 0;
  if(pthread_create(&idth[id],NULL,sy1527MainframeThread,(void *)&stat[id])!=0)
  {
    printf("ERROR: pthread_create(0x%08lx[%d],...) failure\n",idth[id],id);
    pthread_mutex_unlock(&global_mutex);
    return(CAENHV_SYSERR);
  }
  else
  {
    printf("INFO: pthread_create(0x%08lx[%d],...) done\n",idth[id],id);
  }

  /* register mainframe */
  mainframes[nmainframes-1] = id;

  /* get mainframe map */
  sy1527GetMap(id);

  pthread_mutex_unlock(&global_mutex);
  
  printf("\nLEAVE  sy1527Start(%s) *************************************\n\n",ip_address);

  return(CAENHV_OK);
}
//===========================================================================
/* close communication with mainframe under logical number 'id'
   and stop thread */
int
sy1527Stop(unsigned id)
{
  char name[MAX_CAEN_NAME];
  int i, j, ret;

  /* lock global mutex to prevent other mainframes to be stoped
     until we are done with this one */
  pthread_mutex_lock(&global_mutex);

  CHECK_ID(id);
  CHECK_OPEN(id);
  strcpy(name, Measure[id].name);

  /* stop thread */
  force_exit[id] = 1;

  ret = CAENHVDeinitSystem(name);

  if(ret == CAENHV_OK)
  {
    printf("\nConnection >%s< closed (num. %d)\n\n", name,ret);
    Measure[id].id = -1;
  }
  else
  {
    printf("\nERROR(sy1527) error: %s (num. %d)\n\n", CAENHVGetError(name), ret);
    pthread_mutex_unlock(&global_mutex);
    return(CAENHV_SYSERR);
  }

  /* unregister mainframe */
  j = -1;
  for(i=0; i<nmainframes; i++)
  {
    if(mainframes[i] == id)
    {
      j = i;
      break;
    }
  }
  if(j==-1)
  {
    printf("ERROR: mainframe %d was not registered\n",id);
    pthread_mutex_unlock(&global_mutex);
    return(CAENHV_SYSERR);
  }
  for(i=j; i<nmainframes; i++) mainframes[i] = mainframes[i+1];
  nmainframes --;

  pthread_mutex_unlock(&global_mutex);

  return(CAENHV_OK);
}


/*****************************************************************************/
/**************************** High level functions ***************************/
/*****************************************************************************/
/*** CAN BE BOARD-DEPENDANT STUFF HERE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ***/
/*****************************************************************************/

/* some useful macros */
#define SET_FVALUE(prop_name_m, value_m) \
  Demand[id].board[board].channel[chan].fval[prop_name_m] = value_m; \
  Demand[id].board[board].channel[chan].setflag[prop_name_m] = 1; \
  Demand[id].board[board].setflag = 1; \
  Demand[id].setflag = 1

#define SET_LVALUE(prop_name_m, value_m) \
  Demand[id].board[board].channel[chan].lval[prop_name_m] = value_m; \
  Demand[id].board[board].channel[chan].setflag[prop_name_m] = 1; \
  Demand[id].board[board].setflag = 1; \
  Demand[id].setflag = 1

#define GET_FVALUE(prop_name_m, value_m) \
  value_m = Measure[id].board[board].channel[chan].fval[prop_name_m];

#define GET_LVALUE(prop_name_m, value_m) \
  value_m = Measure[id].board[board].channel[chan].lval[prop_name_m]

/* loop over all available channels and set them on or off */
int
sy1527SetMainframeOnOff(unsigned int id, unsigned int on_off)
{
  int i, board, chan;

  pthread_mutex_lock(&global_mutex);

  // check if it is active 

  for(i=0; i<nmainframes; i++)
  {
    if(mainframes[i] == id)
    {
      /* loop over all channels in all boards and set it to 'on_off' */
      for(board=0; board<Measure[id].nslots; board++)
      {
        for(chan=0; chan<Measure[id].board[board].nchannels; chan++)
        {
          SET_LVALUE(Pw, on_off);
        }
      }
    }
  }

  pthread_mutex_unlock(&global_mutex);

  return(CAENHV_OK);
}

/* loop over all available channels and set them on or off */
int
sy1527SetBoardOnOff(unsigned int id, unsigned int board, unsigned int on_off)
{
  int i, chan;

  pthread_mutex_lock(&global_mutex);

  // check if it is active 

  for(i=0; i<nmainframes; i++)
  {
    /*printf("-> check mainframe %d\n",i);*/
    if(mainframes[i] == id)
    {
      /* loop over all channels in all boards and set it to 'on_off' */
      for(chan=0; chan<Measure[id].board[board].nchannels; chan++)
      {
        printf("-> set channel %d to %d\n",chan, on_off);
        SET_LVALUE(Pw, on_off);
      }
    }
  }

  pthread_mutex_unlock(&global_mutex);

  return(CAENHV_OK);
}


int
sy1527BoardSmiControl(char *smi_obj_name, unsigned int id, unsigned int board, 
    unsigned int first_channel, unsigned int chs_number, unsigned int onoff)
{
  pthread_mutex_lock(&global_mutex);
  int chan;
  char *tmp1, *tmp22;
  char tmp2[81], tmp3[81+strlen("caput -w 6   ")];

  strcpy(tmp2,smi_obj_name);
  tmp22=tmp2;
  while((tmp1=strstr(tmp22,"_Cf"))) tmp22=tmp1+1;
  tmp2[strlen(tmp2)-strlen(tmp22)-1]=0;

  for(chan=first_channel; chan < first_channel+chs_number; chan++)  /// my_n_smi
  {
    sprintf(tmp3,"caput -w 6 %s_Ch%d_pwonoff %d", tmp2,chan, onoff);
    system(tmp3);
    // CAEN_HVload(id, board, chan, "CHONOFF", value ); /// my:
    /// SET_LVALUE(Pw, onoff); // now previous caput replaced this line: this is for case when whole board is on/off
    /// and we need to see pwonoff value of each channel in gui.
  }

  pthread_mutex_unlock(&global_mutex);
  return CAENHV_OK;

}

///=======================================================================================
int
sy1527GetHeartBeat(unsigned int id, unsigned int board,
                           unsigned int chan){
// id comes from db here.
// if not connection: id is absent in nmainframes[] (in mainframes[] it is present as -1)
// if comment in startup.all: id is absent in nmainframes[]
  int i, i10, absent_error=1;
  for (i=0; i<nmainframes; i++)
  {
    if (mainframes[i]==id)
    {
      absent_error=0;
      i10=i;
      break;
    }
  }
  if (absent_error==0)
  {
    if      (mainframes_disconnect[i10]==1)        absent_error=3;
    else if (Demand[id].board[board].nchannels==0) absent_error=2;
  }

  return absent_error;
}

///=======================================================================================

int
sy1527GetMainframeStatus(unsigned int id, int *active, int *onoff, int *alarm)
{
  int i, board, chan;
  unsigned int u;
  int retv=-1;

  pthread_mutex_lock(&global_mutex);

  *active = *onoff = *alarm = 0;

  /* check if it is active */
  for(i=0; i<nmainframes; i++)
  {
    if(mainframes[i] == id)
    {
      *active = 1;

      /* check if it is ON: loop over all boards and channels */
      /* and if at least one channel is ON, report mainframe  */
      /* status as ON, overwise report it as OFF */

      for(board=0; board<Measure[id].nslots; board++)
      {
        for(chan=0; chan<Measure[id].board[board].nchannels; chan++)
        {
          /* check on/off status */
          GET_LVALUE(Pw, u);
          if(u) *onoff = 1;

          /* check I-tripped bit */
          GET_LVALUE(Status, u);
          if(u & 0x200) *alarm = 1;
        }
      }
      retv=CAENHV_OK; // my:
    }
  }
  ///smiui_send_command("", "");
  pthread_mutex_unlock(&global_mutex);

  return retv;
}

/* sets demand voltage for one channel */
int
sy1527SetChannelDemandVoltage(unsigned int id, unsigned int board,
                              unsigned int chan, float u)
{
  LOCK_MAINFRAME(id);
  SET_FVALUE(V0Set, u);
  UNLOCK_MAINFRAME(id);
  return(0);
}

/* returns demand voltage for one channel */
float
sy1527GetChannelDemandVoltage(unsigned int id, unsigned int board,
                              unsigned int chan)
{
  float u;
  LOCK_MAINFRAME(id);
  GET_FVALUE(V0Set, u);
  UNLOCK_MAINFRAME(id);
  return(u);
}

/* sets maximum voltage for one channel */
int
sy1527SetChannelMaxVoltage(unsigned int id, unsigned int board,
                           unsigned int chan, float u)
{
  LOCK_MAINFRAME(id);
  SET_FVALUE(SVMax, u);
  UNLOCK_MAINFRAME(id);
  return(0);
}

/* returns maximum voltage for one channel */
float
sy1527GetChannelMaxVoltage(unsigned int id, unsigned int board,
                           unsigned int chan)
{
  float u;
  LOCK_MAINFRAME(id);
  GET_FVALUE(SVMax, u);
  UNLOCK_MAINFRAME(id);
  return(u);
}

/* sets maximum current for one channel */
int
sy1527SetChannelMaxCurrent(unsigned int id, unsigned int board,
                           unsigned int chan, float u)
{
  LOCK_MAINFRAME(id);
  SET_FVALUE(I0Set, u);
  UNLOCK_MAINFRAME(id);
  return(0);
}

/* returns maximum current for one channel */
float
sy1527GetChannelMaxCurrent(unsigned int id, unsigned int board,
                           unsigned int chan)
{
  float u;
  LOCK_MAINFRAME(id);
  GET_FVALUE(I0Set, u);
  UNLOCK_MAINFRAME(id);
  return(u);
}

/* returns measured voltage for one channel */
float
sy1527GetChannelMeasuredVoltage(unsigned int id, unsigned int board,
                                unsigned int chan)
{
  float u;
  LOCK_MAINFRAME(id);
  GET_FVALUE(VMon, u);
  UNLOCK_MAINFRAME(id);
  return(u);
}

/* returns measured current for one channel */
float
sy1527GetChannelMeasuredCurrent(unsigned int id, unsigned int board,
                                unsigned int chan)
{
  float u;
  LOCK_MAINFRAME(id);
  GET_FVALUE(IMon, u);
  UNLOCK_MAINFRAME(id);
  return(u);
}

/* sets Ramp-up speed for one channel */
int
sy1527SetChannelRampUp(unsigned int id, unsigned int board, unsigned int chan,
                       float u)
{

  LOCK_MAINFRAME(id);
  SET_FVALUE(RUp, u);
  UNLOCK_MAINFRAME(id);
  return(0);
}

/* returns Ramp-up speed for one channel */
float
sy1527GetChannelRampUp(unsigned int id, unsigned int board, unsigned int chan)
{
  float u;
  LOCK_MAINFRAME(id);
  GET_FVALUE(RUp, u);
  UNLOCK_MAINFRAME(id);
  return(u);
}

/* sets Ramp-down speed for one channel */
int
sy1527SetChannelRampDown(unsigned int id, unsigned int board,
                         unsigned int chan, float u)
{
  LOCK_MAINFRAME(id);
  SET_FVALUE(RDWn, u);
  UNLOCK_MAINFRAME(id);
  return(0);
}

/* returns Ramp-down speed for one channel */
float
sy1527GetChannelRampDown(unsigned int id, unsigned int board,
                         unsigned int chan)
{
  float u;
  LOCK_MAINFRAME(id);
  GET_FVALUE(RDWn, u);
  UNLOCK_MAINFRAME(id);
  return(u);
}

/* sets on/off status for one channel */
int
sy1527SetChannelOnOff(unsigned int id, unsigned int board,
                      unsigned int chan, unsigned int u)
{
  LOCK_MAINFRAME(id);
  SET_LVALUE(Pw, u);
  UNLOCK_MAINFRAME(id);
  return(0);
}

/* returns on/off status for one channel */
unsigned int
sy1527GetChannelOnOff(unsigned int id, unsigned int board,
                      unsigned int chan)
{
  unsigned int u;
  LOCK_MAINFRAME(id);
  GET_LVALUE(Pw, u);
  UNLOCK_MAINFRAME(id);
  return(u);
}

float
sy1527GetChannelTripTime(unsigned int id, unsigned int board,
                         unsigned int chan)
{
  float u; 
  LOCK_MAINFRAME(id);
  u=Measure[id].board[board].channel[chan].fval[Trip];
  UNLOCK_MAINFRAME(id);
  return u;
}




#define SET_LVALUE1(prop_name_m, value_m) \
printf("SET_LVALUE1: id=%d board=%d chan=%d\n",id,board,chan); \
printf("SET_LVALUE1: prop=%d value=%d\n",prop_name_m, value_m); \
  Demand[id].board[board].channel[chan].lval[prop_name_m] = value_m; \
  Demand[id].board[board].channel[chan].setflag[prop_name_m] = 1; \
  Demand[id].board[board].setflag = 1; \
  Demand[id].setflag = 1


/* sets enable/disable for one channel */
int
sy1527SetChannelEnableDisable(unsigned int id, unsigned int board,
                              unsigned int chan, unsigned int u)
{
  LOCK_MAINFRAME(id);
  SET_LVALUE1(PwEn, u);
  UNLOCK_MAINFRAME(id);
  return(0);
}

/* returns enable/disable for one channel */
unsigned int
sy1527GetChannelEnableDisable(unsigned int id, unsigned int board,
                              unsigned int chan)
{
  unsigned int u;
  LOCK_MAINFRAME(id);
  GET_LVALUE(PwEn, u);
  UNLOCK_MAINFRAME(id);
  return(u);
}

/* returns status for one channel */
unsigned int
sy1527GetChannelStatus(unsigned int id, unsigned int board,
                       unsigned int chan)
{
  unsigned int u;
  LOCK_MAINFRAME(id);
  GET_LVALUE(Status, u);
  UNLOCK_MAINFRAME(id);
  return(u);
}

