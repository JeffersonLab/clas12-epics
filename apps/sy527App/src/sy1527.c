
/* sy1527.c - EPICS driver support for CAEN SY1527 HV mainframe */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>

#include "sy1527.h"

#ifdef NO_SMI
#include "smiuirtl.h"
#endif
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

#ifdef USE_CAEN527

#define V0Set   0
#define I0Set   1
#define V1Set   2
#define I1Set   3
#define RUp     4
#define RDWn    5
#define Trip    6
#define SVMax   7
#define VMon    8
#define IMon    9
#define Status  10
#define Pw      11 /* switch power ON/OFF */
#define PwEn    12 /* power ENABLE/DISABLE */
#define TripInt 13
#define TripExt 14
#define Tdrift  15

#else

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

#endif

static int  nA1536param = 16;
static int  nA1520param = 16; // my: 16
static int  nA1535param = 16;

//static char A1520param[MAX_PARAM][MAX_CAEN_NAME] = {
//                "V0Set","I0Set","V1Set","I1Set","RUp","RDWn","Trip","SVMax",
//                "VMon","IMon","Status","Pw","PwEn","TripInt","TripExt","Tdrift"};
static char A1535param[MAX_PARAM][MAX_CAEN_NAME] = {
                "V0Set","I0Set","V1Set","I1Set","RUp","RDWn","Trip","SVMax",
                "VMon","IMon","Status","Pw","POn","TripInt","TripExt","PDwn"};
static char A1520param[MAX_PARAM][MAX_CAEN_NAME] = {
                "V0Set","I0Set","V1Set","I1Set","RUp","RDWn","Trip","SVMax",
                "VMon","IMon","Status","Pw","PwEn","TripInt","TripExt","Tdrift"};
static char A1536param[MAX_PARAM][MAX_CAEN_NAME] = {
                "V0Set","I0Set","V1Set","I1Set","RUp","RDWn","Trip","SVMax",
                "VMon","IMon","Status","Pw","POn","TripInt","TripExt","PDwn"};

#ifdef USE_CAEN527
static int nA944param = 16;
static char A944param[MAX_PARAM][MAX_CAEN_NAME] = {
              "V0Set","I0Set","V1Set","I1Set","Rup","Rdwn","Trip","SVMax",
              "VMon","IMon","Status","Pw","PrOn","PrOff","Pon","Pdwn"};
#endif

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

/* */
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
/* */
int
sy1527GetBoard(unsigned int id, unsigned int board)
{

  int b_status=0;/// b_status_res=0; /// my: smi

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

  for(i10=0;i10<nmainframes;i10++){ // my_n: hbeat
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

   // if(!strcmp(ParName,"RUp"))printf("RUp type=%d %d\n",tipo,PARAM_TYPE_NUMERIC);
    if(tipo == PARAM_TYPE_NUMERIC)
    {
      ret = CAENHVGetChParam(name, Slot, ParName, ChNum, ChList, fParValList);
//if(!strcmp(ParName,"RUp")){ printf("%s %d %d \n",name, Slot, ChNum);
//printf("RUp f %f\n",fParValList[0]);}
    }
    else
    {
      ret = CAENHVGetChParam(name, Slot, ParName, ChNum, ChList, lParValList);
//if(!strcmp(ParName,"RUp"))printf("RUp l %d\n", lParValList);
    }
    
///-------------- simulator -------
/**
FILE *fps=fopen("/home/clasioc/flags","r");
int flags; 
//printf("pointer=%p\n",fps);
fscanf(fps,"%d",&flags);//printf("%d\n",flags);
//printf("%s\n",name);
if(!strcmp(name,"B_HV009"))
{
 ///printf("%d\n",flags);
 if(flags==1) { printf("==%d\n",flags); ret=4001;}
}
fclose(fps);
*/
///--------------------------------

/*
     int ret1,ret2;
     int retA=CAENHVGetSysProp(Measure[id].name,"FanStat",&ret1);
     int retB=CAENHVGetSysProp(Measure[id].name,"HvPwSM",&ret2);
     printf("NABO2:  FAN=%d/%d PW=%d/%d\n",ret1,retA,ret2,retB);

     // Note:  
     //    FanStat returned 0/-1
    //     HvPwSM  returned 976304689/0 

*/
/*
   // Note: THIS WORKED!
          if (++NCFEDOWNERR[id] > 1000)//MAXCFEDOWNERR)
          {
              NCFEDOWNERR[id]=0;
              printf("@@@@@@@@@@@@@@@@@@@ NABO:  REINITIALIZING\n");
              sy1527Stop(id);
              
              if (sy1527Start(id,Measure[id].IPADDR) != CAENHV_OK)
              {
                  printf("@@@@@@@@@@@@@@@@@@ NABO:  REINITIALIZION FAILED.  WAITING 30s and RETRYING.\n");
                  sleep(35);
                  if (sy1527Start(id,Measure[id].IPADDR) != CAENHV_OK)
                  {
                      printf("@@@@@@@@@@@@@@@@@@ NABO:  REINITIALIZION FAILED TWICE.  LET PROCSERVE RESTART IT.\n");
                      exit(1);
                  }
              }
              sy1527GetMap(id);
              sy1527PrintMap(id);
          }
*/
    if(ret != CAENHV_OK)
    {
     printf("CAENHVGetChParam error: %s (#%d) threadId=%d, brd=%d, (%s) \n\n", CAENHVGetError(name), ret, id, board, ParName);
      mainframes_disconnect[i10]=1; /// my_n: hbeat
    ///  mainframes[i10]=-1;


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
   ///   mainframes_disconnect[i10]=0; /// my_n: hbeat
      /*printf("PARAM VALUE\n");*/
      if(tipo == PARAM_TYPE_NUMERIC)
      {
        for(i=0; i<ChNum; i++)
        {
          // NAB: can we lock this low?
          LOCK_MAINFRAME(id);

          Measure[id].board[board].channel[i].fval[ipar] = fParValList[i];
          /*printf("Slot: %2d  Ch: %3d  %s: %10.2f\n", Slot, ChList[i],
            ParName, fParValList[i]);*/
          
          // NAB: can we lock this low?
          UNLOCK_MAINFRAME(id);
        }
      }
      else
      {
        for(i=0; i<ChNum; i++)   
        {
          // NAB: can we lock this low? 
          LOCK_MAINFRAME(id);
          
          Measure[id].board[board].channel[i].lval[ipar] = lParValList[i];
          if(ipar==Status){
          /// my: smi: accumulates all channels attuses into board status
           b_status = b_status | lParValList[i];
           if(!(lParValList[i] & 0x1))b_status = b_status | BIT_OFF; /// at least one channel in the board is OFF
          }
          /*printf("Slot: %2d  Ch: %3d  %s: %x\n", Slot, ChList[i],
            ParName, lParValList[i]);*/ 
          
          // NAB: can we lock this low?
          UNLOCK_MAINFRAME(id);
        }
      }
    }
  }
  /// my:smi
/*
  char smi_obj_name1[150]; /// temporal
  char smi_obj_name[150]; /// temporal
  char smi_command[150];  /// temporal
  if(b_status & BIT_ON)b_status_res=BIT_ON;
  if(b_status & (BIT_RAMPUP | BIT_RAMPDOWN ))b_status_res=BIT_RAMPUP;
  if(b_status & BIT_OFF)b_status_res=BIT_OFF;
  if(b_status & (BIT_INTTRIP | BIT_EXTTRIP | BIT_OVERCUR | BIT_OVERVOLT | BIT_UNDERVOLT )) b_status_res=BIT_INTTRIP;

  if(b_status_res==BIT_ON)strcpy(smi_command,"SET_ON");
  else if(b_status_res==BIT_RAMPUP)strcpy(smi_command,"SET_ON");  /// temporal !!!
  else if(b_status_res==BIT_OFF)strcpy(smi_command,"SET_OFF");
  else if(b_status_res==BIT_INTTRIP)strcpy(smi_command,"SET_ERROR");

  if(b_status_res != boards_status[id][board]){

   sprintf(smi_obj_name1, CRATE_LABEL, id);
   sprintf(smi_obj_name, "HV_TEST::%s_%d", smi_obj_name1, board);
   smiui_send_command(smi_obj_name,  smi_command);
   printf("smi:  smi_obj_name=%s  smi_command=%s \n", smi_obj_name, smi_command);
   boards_status[id][board]=b_status_res;
  }
*/
  return(CAENHV_OK);
}

#ifdef USE_SMI
/// my_n_smi ======================================================================================
int sy1527CrateSmiInit ///  my: smi  my_n_smi
(char *smi_obj_name, unsigned int id){

int j, j10;

    for(j=0;j<MAX_SLOT;j++){

     for(j10=0;j10<MAX_BOARDPARTS;j10++){
   //   printf("%d %d %d\n",i,j,j10);
      boards_status[id][j][j10]=-1;
     }
    }

return 0;
}

/// my: smi ======================================================================================
int sy1527BoardSmiMonitor(
char *epics_name, unsigned int id, unsigned int board, 
unsigned int first_channel, unsigned int chs_number)
{

  char *tmp1, *tmp2=epics_name; /// temporal
  while((tmp1=strstr(tmp2,"_P"))){
   tmp2=tmp1+1; /// my_n_smi: not used
  }
  int board_part=first_channel; /// my_n_smi: atoi(tmp2-1+strlen("_P"));

  int b_status=0, b_status_res=0; /// my: smi
  int i, i10;
///-------- my_n:
// id comes from db here.
// if not connection: id is absent in mainframes[] (in mainframes[] it is present as -1)
// if comment in startup.all: id is absent in mainframes[]
int absent_error=1;
for(i=0;i<nmainframes;i++){
 if(mainframes[i]==id){absent_error=0;i10=i;break;}

}
if(absent_error==0 && mainframes_disconnect[i10]==1)absent_error=3;
else if(absent_error==0 && Demand[id].board[board].nchannels==0)absent_error=2;

///--------

  LOCK_MAINFRAME(id);
  for(i=first_channel; i<first_channel+chs_number; i++)   /// my_n_smi
  {
          
    /// my: smi: accumulates all channels attuses into board status
    b_status = b_status |  Measure[id].board[board].channel[i].lval[Status];
    if(!(Measure[id].board[board].channel[i].lval[Status] & 0x1))b_status = b_status | BIT_OFF; /// at least one channel in the board is OFF
         
          /*printf("Slot: %2d  Ch: %3d  %s: %x\n", Slot, ChList[i],
            ParName, lParValList[i]);*/ 
  }
 /// my:smi
 char smi_obj_name1[150]; /// temporal
  char smi_command[150];  /// temporal
  if(b_status & BIT_ON)b_status_res=BIT_ON;
  if(b_status & (BIT_RAMPUP | BIT_RAMPDOWN ))b_status_res=BIT_RAMPUP;
  if(b_status & BIT_OFF)b_status_res=BIT_OFF;
  if(b_status & (BIT_INTTRIP | BIT_EXTTRIP | BIT_OVERCUR | BIT_OVERVOLT | BIT_UNDERVOLT )) b_status_res=BIT_INTTRIP;

  if(b_status_res==BIT_ON)strcpy(smi_command,"SET_ON");
  else if(b_status_res==BIT_RAMPUP)strcpy(smi_command,"SET_RAMP");  /// temporal !!!
  else if(b_status_res==BIT_OFF)strcpy(smi_command,"SET_OFF");
  else if(b_status_res==BIT_INTTRIP)strcpy(smi_command,"SET_ERROR");
  if(absent_error){
    if(absent_error==1)b_status_res=BIT_CRATE_OFF;
    else if(absent_error==2)b_status_res=BIT_BOARD_NOT_PRESENT;
    else if(absent_error==3)b_status_res=BIT_CRATE_OFF_ON_WAY; 
    strcpy(smi_command,"SET_ERROR"); // my_n:
    //printf(">>> %s %d\n", epics_name, absent_error );
  }

  if(b_status_res != boards_status[id][board][board_part]){

 //  sprintf(smi_obj_name1, CRATE_LABEL, id);
 //  sprintf(smi_obj_name, "HV_TEST::%s_%d", smi_obj_name1, board);
 //  strncpy(smi_obj_name1, smi_obj_name, strlen(smi_obj_name) - strlen("_monitor"));
 //  smi_obj_name1[strlen(smi_obj_name) - strlen("_monitor")]=0;
   sprintf(smi_obj_name1, "CLAS12::%s", epics_name);
   smiui_send_command(smi_obj_name1,  smi_command);
   printf("smi:  smi_obj_name=%s  smi_command=%s id=%d board=%d chas=%d abs_error=%d \n", smi_obj_name1, smi_command, id, board, Demand[id].board[board].nchannels, absent_error);
   boards_status[id][board][board_part]=b_status_res;
  }
  UNLOCK_MAINFRAME(id);
  return(CAENHV_OK);
}
#endif

///======================================================================================
/* */
int
sy1527SetBoard(unsigned int id, unsigned int board)
{
  int nXXXXXparam;
  char *XXXXparam[MAX_PARAM];

  char name[MAX_CAEN_NAME];
  int i, ipar, iparr, ret;
  unsigned short Slot, ChNum, Ch; //ChList[MAX_CHAN];
  float fParVal;///, fparval[MAX_CHAN];
  unsigned long	tipo, lParVal;///, lparval[MAX_CHAN];
  char ParName[MAX_CAEN_NAME];

  CHECK_ID(id);
  CHECK_OPEN(id);
  strcpy(name, Demand[id].name);

  nXXXXXparam = Demand[id].board[board].nparams;
  for(i=0;i<nXXXXXparam;i++) XXXXparam[i]=Demand[id].board[board].parnames[i];

  Slot = board;
  ChNum = Demand[id].board[board].nchannels;
  //for(i = 0; i<ChNum; i++) ChList[i] = (unsigned short)i;

  /* loop over parameters */
  for(iparr=0; iparr<nXXXXXparam; iparr++)
  {

   // printf("iparr=%d n=%d\n", iparr, nXXXXXparam);
	/* patch to make sure 'PwEn' always executed before 'Pw' */
    if(iparr == Pw)        ipar = PwEn;
    else if(iparr == PwEn) ipar = Pw;
    else                   ipar = iparr;

    strcpy(ParName,XXXXparam[ipar]); /* Param name */
    tipo = Demand[id].board[board].partypes[ipar];


    //fprintf(stderr,"sy1527SetBoard:  %d %d %s\n",id,board,ParName);

    /* will be good to do it this way, but is does not work
    if(tipo == PARAM_TYPE_NUMERIC)
    {
      for(Ch=0; Ch<ChNum; Ch++)
      {
        fparval[Ch] = Demand[id].board[board].channel[Ch].fval[ipar];
	fparval[Ch] = 1.0*Ch+1.0;
        printf("Value %s: %f\n",ParName,fparval[Ch]);
      }
      ret = CAENHVSetChParam(name, Slot, ParName, ChNum, ChList, fparval);
    }
    else
    {
      for(Ch=0; Ch<ChNum; Ch++)
      {
        lparval[Ch] = Demand[id].board[board].channel[Ch].lval[ipar];
        printf("Value %s: %ld\n",ParName,lparval[Ch]);
      }
      ret = CAENHVSetChParam(name, Slot, ParName, ChNum, ChList, lparval);
    }

    if(ret != CAENHV_OK)
    {
      printf("CAENHVSetChParam: %s (num. %d)\n",CAENHVGetError(name),ret);
      return(CAENHV_SYSERR);
    }
    */

    /* loop over all channels */
    for(Ch=0; Ch<ChNum; Ch++)
    {
      if(Demand[id].board[board].channel[Ch].setflag[ipar] == 1)
      {
        //fprintf(stderr,"sy1527SetBoard:  %d\n",Ch);
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

  /*
  char *ParNameList, *plist;
  CAENHVGetChParamInfo(name,0,1,&ParNameList);
  plist=ParNameList;
  for(i=0;i<10;i++){
    if(*plist == '\0'){printf("NULL %d\n",i);break;}
    //if(ParNameList[i])
    printf("param=%s %d\n",plist, i);
    plist+=strlen(plist)+1;
    //else printf("param number %d is NULL\n", i);
  }
  */

  /*  
  char **ParNameList;
  CAENHVGetChParamInfo(name,1,0,ParNameList);
  //  plist=ParNameList;
  for(i=0;i<10;i++){
    // if(*plist == '\0'){printf("NULL %d\n",i);break;}
    if(ParNameList[i])
    printf("param=%s %d\n",ParNameList[i], i);
    //    plist+=strlen(plist)+1;
    //else printf("param number %d is NULL\n", i);
  }
  */

  /*
  char *ParNameList, (*parnamelist)[100];
  CAENHVGetChParamInfo(name,0,0,&ParNameList);
  parnamelist=( char (*)[100])ParNameList;
  int nj=0;
  for(nj=0;parnamelist[nj][0];nj++);
  printf("nj=%d\n",nj);
  //  plist=ParNameList;
  // for(i=0;i<10;i++){
    // if(*plist == '\0'){printf("NULL %d\n",i);break;}
  //  if(ParNameList[i])
  //  printf("param=%s %d\n",ParNameList[i], i);
    //    plist+=strlen(plist)+1;
    //else printf("param number %d is NULL\n", i);
    // }
    */


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
        /*printf("Board %2d: Not Present\n", i);*/
      }
      else
      {

///----------------- HV parameters finding piece ------------------- 
/*
 // printf("name================================================%s\n",name);
  int retv;
  retv=CAENHVGetChParamInfo(name,i,0,&g_parr);

  int nj=0;
  int ni=0;
  int index=0;
 while(1){

 if(!((nj)%10)){
  if((*(g_parr+nj))==0){
   g_parr_index[index++]=ni;
  // printf("%s\n",g_parr+ni);
   break;
  }
  else{
   if(nj!=0){
    // printf("%s\n",g_parr+ni);
     g_parr_index[index++]=ni;
     ni=nj;
   }
  }
 }
 nj++;
 //printf("%c %d\n",*(parr+nj), *(parr+nj));
 }

 int found=0;
 char tmp[PATH_MAX];

 strcpy(tmp,getenv("HOME"));
 strcat(tmp,"/.hv_params");
 if(!fp_params){
  fp_params = fopen(tmp,"w+");
  if(fp_params)
  fprintf(fp_params, "This file contains not found parameters: \n");
  fflush(fp_params);
 }

 // printf("nj================================================%d i=%d retv=%d %d\n",nj, i, retv,sizeof(A1520param));

 for(ni=0; ni < nA1520param; ni++){
  found=0;
  for(nj=0;nj<index;nj++){
   if(!strcmp(A1520param[ni],g_parr+g_parr_index[nj]))found=1;
  }
  if(!found){
   if(fp_params)
   fprintf(fp_params, "parameter %s: NOT FOUND. CRATE=%s SLOT=%d \n",A1520param[ni], name, i);
   printf("parameter %s: NOT FOUND. CRATE=%s SLOT=%d \n",A1520param[ni], name, i);
   printf("found parameters are:\n");
   for(nj=0;nj<index;nj++){
    printf("%s \n",g_parr+g_parr_index[nj]);
   }
   //exit(1);
  }
 }
  // if(fp_params)
  // fprintf(fp_params, "all parameters are found in crate:%s the slot: %d\n",name, i);
*/
///----------------- end of HV parameters finding piece ------------------- 

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
        if(!strcmp(Measure[id].board[i].modelname,"A1535") || !strcmp(Measure[id].board[i].modelname,"A1733") ) // my: was A1520
        {
          printf("---> found board %s\n",Measure[id].board[i].modelname);
          Measure[id].board[i].nparams = nA1535param;
          Demand[id].board[i].nparams = nA1535param;
          for(j=0; j<Measure[id].board[i].nparams; j++)
          {
            strcpy(Measure[id].board[i].parnames[j],A1535param[j]);
            strcpy(Demand[id].board[i].parnames[j],A1535param[j]);

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
          Measure[id].board[i].nparams = nA1536param;
          Demand[id].board[i].nparams = nA1536param;
          for(j=0; j<Measure[id].board[i].nparams; j++)
          {
            strcpy(Measure[id].board[i].parnames[j],A1536param[j]);
            strcpy(Demand[id].board[i].parnames[j],A1536param[j]);

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
#ifdef USE_CAEN527
        else if(strstr(Measure[id].board[i].modelname,"A944") || strstr(Measure[id].board[i].modelname,"A934") ) // my:
        {

          if(strstr(Measure[id].board[i].modelname,"A944") )printf("found board A944\n"); //my:
          else if(strstr(Measure[id].board[i].modelname,"A934") )printf("found board A934\n"); //my:

          Measure[id].board[i].nparams = nA944param;
          Demand[id].board[i].nparams = nA944param;
          for(j=0; j<Measure[id].board[i].nparams; j++)
          {
            strcpy(Measure[id].board[i].parnames[j],A944param[j]);
            strcpy(Demand[id].board[i].parnames[j],A944param[j]);

            strcpy(ParName,Measure[id].board[i].parnames[j]);
            ret=CAENHVGetChParamProp(name,i,ChList[0],ParName,"Type",&tipo);
            if(ret != CAENHV_OK)
            {
              printf("CAENHVGetChParamProp: %s (num. %d) ParName=>%s<\n",
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
#endif
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


    // free(ParNameList); // my:

  }

  return(CAENHV_OK);
}
//==================================================================================================
/* */
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

    // NAB:  can we do this at a lower level?
    //LOCK_MAINFRAME(id);
    
    if(force_exit[id])
    {
      //pthread_mutex_unlock(&mainframe_mutex[id]);
      break;
    }

    /***** talk to mainframe here *****/

    // NAB:  try it here (separately for write and read queues):
    LOCK_MAINFRAME(id);
    
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
            printf("[%2d] sets board %d\n",id,i);

            ret = sy1527SetBoard(id,i);
            if(ret == CAENHV_OK) Demand[id].board[i].setflag = 0;
            else                 status |= CAENHV_SYSERR;
            printf("[%2d] DONE sets board %d\n",id,i);
          }
        }
      }
      if(status == CAENHV_OK) Demand[id].setflag = 0;
    }
    // NAB: try it here:
    UNLOCK_MAINFRAME(id);
    
    /* gets all existing boards in mainframe 'id' */
    for(i=0; i<Measure[id].nslots; i++)
    {
      /* measure all active boards */
      if(Measure[id].board[i].nchannels > 0)
      {
        // NAB:  move lock into here:
        ret = sy1527GetBoard(id,i);
      }
    }
    /**********************************/

    // NAB:  can we do this at a lower level?
    //pthread_mutex_unlock(&mainframe_mutex[id]);

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

#ifdef USE_CAEN527
  vmeOpenDefaultWindows();
#endif

  nmainframes = 0;
  memset(Measure,0,sizeof(HV)*MAX_HVPS); ///my: *MAX_HVPS
  memset(Demand,0,sizeof(HV)*MAX_HVPS); ///my: *MAX_HVPS
  for(i=0; i<MAX_HVPS; i++)
  {
    Measure[i].id = -1;
    Demand[i].id = -1;
    mainframes[i] = -1;
    mainframes_disconnect[i] = 0; // my_n:
    is_mainframe_read[i]=0; // my: flag to prevent epics value init before reading by driver

    // int mbp=MAX_BOARDPARTS;
    // printf("MAXBOARDPARTS=%d\n",mbp);
    for(j=0;j<MAX_SLOT;j++)
    {
      for(j10=0;j10<MAX_BOARDPARTS;j10++)
      {
       //printf("%d %d %d\n",i,j,j10);
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
  int id; ///my:
  char arg[30], userName[20], passwd[30], name[MAX_CAEN_NAME];
  int link, ret;

  pthread_mutex_lock(&global_mutex);

  /* do global initialization on first call */
  if(nmainframes == -1) sy1527Init();

  nmainframes++;///my:
  ///id=nmainframes-1;///my:

  ///if((id+1)>nmainframes)nmainframes=id+1;
  id=id_nowused;///nmainframes-1;///my:

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

/// my:  sprintf(name,"sy1527_%03d",id);
  sprintf(name, CRATE_LABEL, id); /// my:
  printf("System Name set as >%s<\n",name);

  strcpy(arg,ip_address);
  printf("TCP/IP address set as >%s<\n",arg);

#ifdef USE_CAEN527
  link = LINKTYPE_CAENET;
  strcpy(userName, "user");
  strcpy(passwd, "user");
#else
  link = LINKTYPE_TCPIP;
  strcpy(userName, "admin");
  strcpy(passwd, "admin");
#endif

  ret = CAENHVInitSystem(name, link, arg, userName, passwd);

  printf("my: id_index=%d id=%d name=%s", id, ret, name );
  printf("\nCAENHVInitSystem error: %s (num. %d)\n\n", CAENHVGetError(name),ret);

  NCFEDOWNERR[id]=0;

  printf("\n\nRUNNING MODIFIED FOR CFE FIX.!!!!!!!!!!!!!!!!!!!!!!!\n\n");

  if(ret == CAENHV_OK)
  {
    if(strlen(ip_address)>=MAX_CAEN_NAME){printf("too long mainfraime IP: exits now\n");exit(1);} /// my:
    strcpy(Measure[id].IPADDR,ip_address); /// my:
    Measure[id].id = ret;
    strcpy(Measure[id].name, name); 
    Demand[id].id = ret;
    strcpy(Demand[id].name, name); 
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
  mainframes[nmainframes-1] = id; /// my: removed nmainframes++
  ///mainframes[id] = id;

  printf("====================== 111111111111\n");
  /* get mainframe map */
  sy1527GetMap(id);
  printf("====================== 222222222222\n");

  pthread_mutex_unlock(&global_mutex);

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

  // NAB:  shouldn't we do this? :
  // UNLOCK_MAINFRAME(id);

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
//===================================================================================
/* loop over all available channels and set them on or off */
int
sy1527SetMainframeOnOff(unsigned int id, unsigned int on_off)
{
  int i, board, chan;

  pthread_mutex_lock(&global_mutex);

 // check if it is active 

//printf("hjhjhjhjhjhjhhjh nmainframes,id, mainframes[i] %d %d %d\n",nmainframes,id, mainframes[i]);
  for(i=0; i<nmainframes; i++)
  {
    /*printf("-> check mainframe %d\n",i);*/
    if(mainframes[i] == id)
    {
//printf("hjhjhjhjhjhjhhjh 2\n");
      /*printf("-> mainframe %d has id=%d, so loop over %d boards\n",
        i,id,Measure[id].nslots);*/
      /* loop over all channels in all boards and set it to 'on_off' */

      for(board=0; board<Measure[id].nslots; board++)
      {
        /*printf("-> slot %d: nchannels=%d\n",
          board,Measure[id].board[board].nchannels);*/
        for(chan=0; chan<Measure[id].board[board].nchannels; chan++)
        {
         /// printf("-> set channel %d to %d\n",chan, on_off); /// my:
          SET_LVALUE(Pw, on_off);
        }
      }
    }
  }

  pthread_mutex_unlock(&global_mutex);

  return(CAENHV_OK);
}

/// my: smi ============================================================================
/* loop over all available channels and set them on or off */
int
sy1527SetBoardOnOff(unsigned int id, unsigned int board, unsigned int on_off)
{
  int i, chan;

  pthread_mutex_lock(&global_mutex);

 // check if it is active 

//printf("hjhjhjhjhjhjhhjh nmainframes,id, mainframes[i] %d %d %d\n",nmainframes,id, mainframes[i]);
  for(i=0; i<nmainframes; i++)
  {
    /*printf("-> check mainframe %d\n",i);*/
    if(mainframes[i] == id)
    {
//printf("hjhjhjhjhjhjhhjh 2\n");
      /*printf("-> mainframe %d has id=%d, so loop over %d boards\n",
        i,id,Measure[id].nslots);*/
      /* loop over all channels in all boards and set it to 'on_off' */

      /// for(board=0; board < Measure[id].nslots; board++)
      ///{
        /*printf("-> slot %d: nchannels=%d\n",
          board,Measure[id].board[board].nchannels);*/
        for(chan=0; chan<Measure[id].board[board].nchannels; chan++)
        {
          printf("-> set channel %d to %d\n",chan, on_off); /// my:
          SET_LVALUE(Pw, on_off);
        }
      ///}
    }
  }

  pthread_mutex_unlock(&global_mutex);

  return(CAENHV_OK);
}

/// my: smi ============================================================================


#ifdef USE_SMI
int
sy1527BoardSmiControl (char *smi_obj_name, unsigned int id, unsigned int board, 
                       unsigned int first_channel, unsigned int chs_number, unsigned int onoff){
pthread_mutex_lock(&global_mutex);
    int chan;

  // float value=onoff;
  char *tmp1, *tmp22;
  char tmp2[81], tmp3[81+strlen("caput -w 6   ")]; /// temporal
   
  strcpy(tmp2,smi_obj_name);
  tmp22=tmp2;
  while((tmp1=strstr(tmp22,"_Cf"))){ /// my_n_smi
   tmp22=tmp1+1;
  }
  tmp2[strlen(tmp2)-strlen(tmp22)-1]=0;

        /*printf("-> slot %d: nchannels=%d\n",
          board,Measure[id].board[board].nchannels);*/
    for(chan=first_channel; chan < first_channel+chs_number; chan++)  /// my_n_smi
    {
      sprintf(tmp3,"caput -w 6 %s_Ch%d_pwonoff %d", tmp2,chan, onoff);
      system(tmp3);
     // CAEN_HVload(id, board, chan, "CHONOFF", value ); /// my:
     // printf("-> %s\n",tmp3); /// my:
     /// printf("-> set channel %d to %d\n",chan, onoff); /// my:
      /// SET_LVALUE(Pw, onoff); // now previous caput replaced this line: this is for case when whole board is on/off
      /// and we need to see pwonoff value of each channel in gui.
    }

pthread_mutex_unlock(&global_mutex);
return CAENHV_OK;

}
#endif

///=======================================================================================
int /// my_n: adding heart beat
sy1527GetHeartBeat(unsigned int id, unsigned int board,
                           unsigned int chan){

///-------- my_n:
// id comes from db here.
// if not connection: id is absent in nmainframes[] (in mainframes[] it is present as -1)
// if comment in startup.all: id is absent in nmainframes[]
int i, i10, absent_error=1;
for(i=0;i<nmainframes;i++){
 if(mainframes[i]==id){absent_error=0;i10=i;break;}
}
///--------
if(absent_error==0 && mainframes_disconnect[i10]==1)absent_error=3;
else if(absent_error==0 && Demand[id].board[board].nchannels==0)absent_error=2;


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
//printf("===========================================id=%d board=%d chan=%d\n",id,board,chan);
  LOCK_MAINFRAME(id);
  GET_FVALUE(RUp, u);
  UNLOCK_MAINFRAME(id);
 //printf("===========================================id=%d board=%d chan=%d value=%f\n",id,board,chan,u);
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

/// my:

float
sy1527GetChannelTripTime(unsigned int id, unsigned int board,
                         unsigned int chan)
{
  float u; 
  LOCK_MAINFRAME(id);
  //GET_FVALUE(Trip, u);
u=Measure[id].board[board].channel[chan].fval[Trip];
//printf("trip time  %f %d %f\n", u, //Measure[id].board[board].channel[chan].lval[Trip],Measure[id].board[board].channel[chan].fval[Trip]);
  UNLOCK_MAINFRAME(id);

//printf("trip time  %f\n", u);
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

