
/**

V.Sytnik 07/2014

*/


#define ALLSET_THROUGH_ONE 0
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <stdio.h>
#include <shareLib.h>
#include <unistd.h>
epicsShareFunc int errlogPrintf(const char *pFormat, ...); ///my:



typedef int BOOL;
typedef int STATUS;

#ifndef ERROR
#define ERROR (-1)
#endif

#ifndef OK
#define OK (0)
#endif


#include <alarm.h> 
#include <dbDefs.h> 
#include <dbAccess.h>
#include <recSup.h>
#include <recGbl.h> 
#include <devSup.h>
#include <boRecord.h>
#include <biRecord.h>
#include <aiRecord.h>
#include <aoRecord.h>
#include <aaoRecord.h>
#include <waveformRecord.h>
#include <epicsExport.h> 
//#include "command.h"

#include "common.h"
#include "CrateMsgTypes.h"

extern int is_mainframe_read[256]; // my: flag to prevent epics value init before reading by driver
extern int nmainframes; // my:
int FLAG_BLOCK_INIT=1; // my:

static long write_ao(struct aoRecord *);
static long init_ao(struct aoRecord *); 
static long read_bi(struct biRecord *); 
static long read_ai(struct aiRecord *); 
static long init_ai(struct aiRecord *); 
static long write_bo(struct boRecord *);
static long init_bo(struct boRecord *);

static long write_aao(struct aaoRecord *);
static long init_aao(struct aaoRecord *); 
static long read_waveform(struct waveformRecord *);
//static long init_waveform(struct waveformRecord *); 
//void IocSetValue(int crate, int slot, int channel, int command, double values[]);

//void block_until_fraimworks_read();/// my:
/* Thses EPICS structures associate the SCALER dev records with the
 * initialization and processing routines defined in this file.  The
 * global structure names are required by epics because of the
 * definitions in the device application's '.dbd' file.
 */

struct
{ long number;
  DEVSUPFUN report;
  DEVSUPFUN init;
  DEVSUPFUN init_record;
  DEVSUPFUN get_ioint_info;
  DEVSUPFUN write_bo;
} devBoSCALERS = {5, NULL, NULL, init_bo, NULL, write_bo};
epicsExportAddress(dset,devBoSCALERS);

struct
{ long number;
  DEVSUPFUN report;
  DEVSUPFUN init;
  DEVSUPFUN init_record;
  DEVSUPFUN get_ioint_info;
  DEVSUPFUN read_bi;
} devBiSCALERS = {5, NULL, NULL, NULL, NULL, read_bi};
epicsExportAddress(dset,devBiSCALERS);

struct
{ long number;
  DEVSUPFUN report;
  DEVSUPFUN init;
  DEVSUPFUN init_record;
  DEVSUPFUN get_ioint_info;
  DEVSUPFUN read_ai;
  DEVSUPFUN special_linconv;
} devAiSCALERS = {6, NULL, NULL, init_ai, NULL, read_ai, NULL};
epicsExportAddress(dset,devAiSCALERS);

/*
struct
{ long number;
  DEVSUPFUN report;
  DEVSUPFUN init;
  DEVSUPFUN init_record;
  DEVSUPFUN read_bi;
  DEVSUPFUN get_ioint_info;
} devBiSCALERS = {5, NULL, NULL, NULL, read_bi, NULL};
epicsExportAddress(dset,devBiSCALERS);
*/
struct
{ long number;
  DEVSUPFUN report;
  DEVSUPFUN init;
  DEVSUPFUN init_record;
  DEVSUPFUN get_ioint_info;
  DEVSUPFUN write_ao;
  DEVSUPFUN special_linconv;
} devAoSCALERS = {6, NULL, NULL, init_ao, NULL, write_ao, NULL};
epicsExportAddress(dset,devAoSCALERS);
///---------------------------------------------------------------
struct
{ long number;
  DEVSUPFUN report;
  DEVSUPFUN init;
  DEVSUPFUN init_record;
  DEVSUPFUN get_ioint_info;
  DEVSUPFUN write_aao;
  DEVSUPFUN special_linconv;
} devAaoSCALERS = {6, NULL, NULL, init_aao, NULL, write_aao, NULL};
epicsExportAddress(dset,devAaoSCALERS);

struct
{ long number;
  DEVSUPFUN report;
  DEVSUPFUN init;
  DEVSUPFUN init_record;
  DEVSUPFUN get_ioint_info;
  DEVSUPFUN read_waveform;
} devWaveformSCALERS = {5, NULL, NULL, NULL, NULL, read_waveform};
epicsExportAddress(dset,devWaveformSCALERS);
///---------------------------------------------------------------



//===============================================================================================
static long
init_bo(struct boRecord  *pbo)
{
  /* Get the card & signal numbers from the record, pointed to by pbo.
     These data items are not used as card/signal, but are defined as
     {card 0-7: chassis, 8-15: slot;  signal 0-7:channel, 8-15:command}.
   */
 //usleep(100000); 

  struct vmeio *pvmeio = (struct vmeio *) &(pbo->out.value);  
  unsigned short* card    = (unsigned short*) &pvmeio->card;
  unsigned short* signal  = (unsigned short*) &pvmeio->signal;

  unsigned slot = (*card)>>8;
  unsigned chassis = (*card) - ((slot)<<8) ;

  unsigned command = (*signal)>>8;
  unsigned channel = (*signal) - ((command)<<8);

  ///printf("chassis=%d\n", chassis);
 
  char tmp[81]; /// temporal
  int retv;
  int first_channel=channel, chs_number=command;
#ifdef USE_SMI
  if(strstr(pbo->desc,"smi"))
  { 
    strncpy(tmp, pbo->name, strlen(pbo->name)-strlen("_BO"));
    tmp[strlen(pbo->name)-strlen("_BO")]=0;

    retv=ScalerBoardSmiMonitor(1, tmp, chassis, slot, first_channel, chs_number);
    pbo->rval = retv; /// means nothing
  }
  else
  {
   /// we never should be here for SCALERS
  }
#endif

  return 0;
}


//===============================================================================================
static long
write_bo(struct boRecord *pbo)
{
  /* Get the card & signal numbers from the record, pointed to by pbo.
     These data items are not used as card/signal, but are defined as
     {card 0-7: chassis, 8-15: slot;  signal 0-7:channel, 8-15:command}.
   */

  struct vmeio *pvmeio = (struct vmeio *) &(pbo->out.value);  
  unsigned short* card    = (unsigned short*) &pvmeio->card;
  unsigned short* signal  = (unsigned short*) &pvmeio->signal;

  unsigned slot = (*card)>>8;
  unsigned chassis = (*card) - ((slot)<<8) ;

  unsigned command = (*signal)>>8;
  unsigned channel = (*signal) - ((command)<<8);

  int retv;
  int first_channel=channel, chs_number=command;
#ifdef USE_SMI
  if(strstr(pbo->desc,"smi"))
  {
    //sscanf(pbo->desc, "%s %d %d", tmp1, first_board, bds_number);
    //sscanf(pbo->desc, "%s %d %d", tmp1, first_board, bds_number);

    retv=ScalerBoardSmiControl(pbo->name, chassis, slot,  
    first_channel, chs_number, (unsigned char)pbo->rval);
  }
  else if(strstr(pbo->desc,"crate_fsm_init"))
  { /// for any order of launch of ioc and fsm
    retv=ScalerCrateSmiInit(pbo->name, chassis);
  }
  else
  {
	;
  }
#endif

  return 0;  

}

//===============================================================================================

static long init_ai(struct aiRecord *pai) { return 0; }
static long read_ai(struct aiRecord *pai)
{
  double values[200];

  struct vmeio *pvmeio = (struct vmeio *) &(pai->inp.value);  

  unsigned short* card    = (unsigned short*) &pvmeio->card;
  unsigned short* signal  = (unsigned short*) &pvmeio->signal;

  unsigned int slot = (*card)>>8;
  unsigned int chassis = (*card) - ((slot)<<8) ;

  unsigned int command = (*signal)>>8;
  unsigned int channel = (*signal) - ((command)<<8);

  if (command<2) {
      IocGetValue(chassis,slot,channel,JLAB_SET_THRESHOLD,values);
      pai->rval = values[command];
  }
  else {
    printf("read_ai:  ERROR, no command: %d\n",command);
  }

  return 0;  
}
//===============================================================================================
static long init_ao(struct aoRecord  *pao)
{
  double values[200];

  struct vmeio *pvmeio = (struct vmeio *) &(pao->out.value);  

  unsigned short* card    = (unsigned short*) &pvmeio->card;
  unsigned short* signal  = (unsigned short*) &pvmeio->signal;

  unsigned int slot = (*card)>>8;
  unsigned int chassis = (*card) - ((slot)<<8) ;

  unsigned int command = (*signal)>>8;
  unsigned int channel = (*signal) - ((command)<<8);

  if (command<2) {
      IocGetValue(chassis,slot,channel,JLAB_SET_THRESHOLD,values);
      pao->rval = values[command];
  }
  else {
    printf("read_ai:  ERROR, no command: %d\n",command);
  }

  return 0;  
}
static long write_ao(struct aoRecord *pao)
{
  double values[200];

  double threshType,threshValue;

  struct vmeio *pvmeio = (struct vmeio *) &(pao->out.value);  

  unsigned short* card    = (unsigned short*) &pvmeio->card;
  unsigned short* signal  = (unsigned short*) &pvmeio->signal;

  unsigned int slot = (*card)>>8;
  unsigned int chassis = (*card) - ((slot)<<8) ;

  unsigned int command = (*signal)>>8;
  unsigned int channel = (*signal) - ((command)<<8);

  if (command<2) {
      threshType = command;
      threshValue = pao->val;
      values[0] = threshType;
      values[1] = threshValue;
      IocSetValue(chassis,slot,channel,JLAB_SET_THRESHOLD,values);
  }
  else {
    printf("write_ao:  ERROR, no command: %d\n",command);
  }

  return 0;  
}


//===============================================================================================
static long
read_bi(struct biRecord *pbi)
{
  /* Get the card & signal numbers from the record, pointed to by pbo.
     These data items are not used as card/signal, but are defined as
     {card 0-7: chassis, 8-15: slot;  signal 0-7:channel, 8-15:command}.
     Note that slot and channel numbers are not used in this situation.
   */

  struct vmeio *pvmeio = (struct vmeio *) &(pbi->inp.value);  


  unsigned short* card    = (unsigned short*) &pvmeio->card;
  unsigned short* signal  = (unsigned short*) &pvmeio->signal;

  unsigned int slot = (*card)>>8;
  unsigned int chassis = (*card) - ((slot)<<8) ;

  unsigned int command = (*signal)>>8;
  unsigned int channel = (*signal) - ((command)<<8);

//  printf("read_bi chassis=%d %s\n", chassis, pbi->name); 
 // printf("read_bi chassis=%d\n", chassis); 
  int retv;
  int first_channel=channel, chs_number=command;
#ifdef USE_SMI
  if(strstr(pbi->desc,"smi"))
  {
    //printf("read_bi chassis=%d %s\n", chassis, pbi->name); 
    retv=ScalerBoardSmiMonitor(0, pbi->name, chassis, slot, first_channel, chs_number);
    pbi->rval = retv; /// means nothing
  }
  else
  {
	;
  }
#endif

  return 0;  
}



//===============================================================================================
//===============================================================================================
static long
init_aao(struct aaoRecord  *paao)
{
  double values[200]; ///??? 
  int i;

  struct vmeio *pvmeio = (struct vmeio *) &(paao->out.value);

  unsigned short* card    = (unsigned short*) &pvmeio->card;
  unsigned short* signal  = (unsigned short*) &pvmeio->signal;

  unsigned slot = (*card)>>8;
  unsigned chassis = (*card) - ((slot)<<8) ;

  unsigned command = (*signal)>>8;
  unsigned channel = (*signal) - ((command)<<8);

  block_until_crate_read(chassis);

//printf("1nelm=%d %d %p %p %s \n", paao->nelm,paao->nord,(double *) paao->val , (double *) paao->bptr, paao->name );
  IocGetValue( chassis,  slot,  channel,  command, values);
//printf("2nelm=%d %d %p %p %s \n", paao->nelm,paao->nord,(double *) paao->val , (double *) paao->bptr, paao->name );
  if(!(paao->bptr))        
  paao->bptr = callocMustSucceed(paao->nelm, dbValueSize(paao->ftvl), "aao: buffer calloc failed");

 
  if(command==JLAB_SET_THRESHOLD /*&& strstr(paao->name,"B_SCALERS000_Sl13_Ch15")*/ ){
 // paao->val=(double *)malloc(sizeof(double)*10);
     //      paao->bptr = callocMustSucceed(paao->nelm, dbValueSize(paao->ftvl),
     //           "aao: buffer calloc failed");

 
   //printf("nelm=%d %d %p %p %s %d %d\n", paao->nelm,paao->nord,(double *) paao->val , (double *) paao->bptr, paao->name, (int)values[0], (int)values[1] );
   //((double *)(paao->bptr))[0]=1;


  ((double*)paao->bptr)[0]=-1; /// undefined type of threshold last set (does not need initialization)
  ((double*)paao->bptr)[1]=values[0];
  ((double*)paao->bptr)[2]=values[1];

  }
  else if(command==JLAB_SET_READ_MODE){
   for(i=0;i<MODE_PARS_NUMBER;i++){
    ((double*)paao->bptr)[i]=values[i];
   }


  }
   paao->nord=paao->nelm;
 return 0;

}

//===============================================================================================
static long
write_aao(struct aaoRecord *paao)
{
 // Get the card & signal numbers from the record, pointed to by pbo.
  //   These data items are not used as card/signal, but are defined as
  //   {card 0-7: chassis, 8-15: slot;  signal 0-7:channel, 8-15:command}.
  //   Note that slot and channel numbers are not used in this situation.

double values[32]; ///??? 

  struct vmeio *pvmeio = (struct vmeio *) &(paao->out.value);  

  unsigned short* card    = (unsigned short*) &pvmeio->card;
  unsigned short* signal  = (unsigned short*) &pvmeio->signal;

  unsigned slot = (*card)>>8;
  unsigned chassis = (*card) - ((slot)<<8) ;

  unsigned command = (*signal)>>8;
  unsigned channel = (*signal) - ((command)<<8);

//printf("======== %f %f ===========2 \n",((double*)paao->bptr)[0], ((double*)paao->bptr)[1]);
  // printf("222 nelm=%d %d %p %p %s\n", paao->nelm,paao->nord,(double *) paao->val , (double *) paao->bptr, paao->name);


  if(command==JLAB_SET_THRESHOLD){
   values[0]=((double*)paao->bptr)[0]; /// threshold type is written here
   if(values[0]==SCALER_PARTYPE_THRESHOLD)values[1]=((double*)paao->bptr)[1];
   else values[1]=((double*)paao->bptr)[2]; /// SCALER_PARTYPE_THRESHOLD2
 
  }
  else if(command==JLAB_SET_READ_MODE){
   values[0]=((double*)paao->bptr)[0];
   values[1]=((double*)paao->bptr)[1];
   values[2]=((double*)paao->bptr)[2];
   values[3]=((double*)paao->bptr)[3];
  }

  // printf("2partype=%f buffer[0]=%f \n",values[0], values[1]);
  IocSetValue( chassis,  slot,  channel,  command, values);



 return 0;
}

//===============================================================================================
/*
static long init_waveform(struct waveformRecord  *pao)
{


 return 0;

}
*/

//===============================================================================================
static long
read_waveform(struct waveformRecord *pwi)
{
  // Get the card & signal numbers from the record, pointed to by pbo.
  //   These data items are not used as card/signal, but are defined as
  //   {card 0-7: chassis, 8-15: slot;  signal 0-7:channel, 8-15:command}.
  //   Note that slot and channel numbers are not used in this situation.
   
  struct vmeio *pvmeio = (struct vmeio *) &(pwi->inp.value);  


  unsigned short* card    = (unsigned short*) &pvmeio->card;
  unsigned short* signal  = (unsigned short*) &pvmeio->signal;

  unsigned slot = (*card)>>8;
  unsigned chassis = (*card) - ((slot)<<8) ;

  unsigned command = (*signal)>>8;
  unsigned channel = (*signal) - ((command)<<8);

 
  int len, len_com;
  double *values;
  int ret_status;

#ifdef USE_SMI
  if(strstr(pwi->desc,"smi"))
  {
    ///retv=sy1527BoardSmiMonitor(pbi->name, chassis, slot, channel, command);
    /// pbi->rval = retv; /// means nothing
  }
  else
#endif
  {
    pwi->rarm = 0;
    ///if(pwi->ftvl==DBF_ULONG)
    ///{
    //pwi->val=(unsigned long*) malloc(40);/// first=0; printf("p=%p\n",pwi->val);}
    ///IocReadWaveform(chassis, slot, channel, &len, values);
    // *((unsigned long*) (pwi->val))=5;
    ret_status=IocGetWaveformLength(chassis, slot, channel, &len);

    //if(chassis==0 && slot==4 && channel==0)printf("ret_status=%d len=%d %d\n", ret_status, pwi->nelm, len);

    ///-------------------- if(len<=0)return OK;
    //values = (unsigned long *) malloc(sizeof(long)*len);

    if(ret_status==0)
    {
      values = (double *) malloc(sizeof(double)*len);
      IocReadWaveform(chassis, slot, channel, len, values);
      len_com=len;
    }
    else
	{
      len_com=pwi->nelm;
	}
 
    for (pwi->nord = 0; pwi->nord < len_com; pwi->nord++)
    {
      /// *((unsigned long*) (pwi->bptr+pwi->nord))=5;
    
      //    ((unsigned long*)pwi->bptr)[pwi->nord]=values[pwi->nord];
      if(ret_status==0){ ((double*)pwi->bptr)[pwi->nord]=values[pwi->nord]; }
      else ((double*)pwi->bptr)[pwi->nord]=ret_status;

      ///((unsigned long*)pwi->bptr)[pwi->nord]=5;
 
      /// if(len!=0){
      ///   printf("%08lx %d %d %d len=%d val=%p\n", values[pwi->nord],chassis, slot, channel, len, pwi->val);
   /// }
  

   //printf("READ_BI ======================================== name=%s %d %d %d\n",pbi->name,chassis,slot, result); //my:
   // Show error if the requested chassis does not exist.
   
 
     } ///for
     if(ret_status==0)free(values);

  } /// else
  
  return OK;
}

//===============================================================================================



///=======================================================================================================
///=======================================================================================================
///=======================================================================================================
///=======================================================================================================
///=======================================================================================================
///=======================================================================================================
