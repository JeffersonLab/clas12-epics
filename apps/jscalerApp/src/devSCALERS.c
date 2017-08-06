
#define ALLSET_THROUGH_ONE 0

#define NOWAVEFORMS 1

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <stdio.h>
#include <shareLib.h>
#include <unistd.h>
epicsShareFunc int errlogPrintf(const char *pFormat, ...);

#include <signals.h>

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
#include <waveformRecord.h>
#include <epicsExport.h> 
#include <cantProceed.h>

#include "common.h"
#include "CrateMsgTypes.h"

extern int is_mainframe_read[256]; // my: flag to prevent epics value init before reading by driver
extern int nmainframes;
int FLAG_BLOCK_INIT=1;

static long write_ao(struct aoRecord *);
static long init_ao(struct aoRecord *); 
static long read_bi(struct biRecord *); 
static long read_ai(struct aiRecord *); 
static long init_ai(struct aiRecord *); 
static long write_bo(struct boRecord *);
static long init_bo(struct boRecord *);
static long read_waveform(struct waveformRecord *);

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

struct
{ long number;
  DEVSUPFUN report;
  DEVSUPFUN init;
  DEVSUPFUN init_record;
  DEVSUPFUN get_ioint_info;
  DEVSUPFUN read_waveform;
} devWaveformSCALERS = {5, NULL, NULL, NULL, NULL, read_waveform};
epicsExportAddress(dset,devWaveformSCALERS);


//===============================================================================================
static long
init_bo(struct boRecord  *pbo)
{
  /* Get the card & signal numbers from the record, pointed to by pbo.
     These data items are not used as card/signal, but are defined as
     {card 0-7: chassis, 8-15: slot;  signal 0-7:channel, 8-15:command}.
   */

#ifdef USE_SMI
  struct vmeio *pvmeio = (struct vmeio *) &(pbo->out.value);  
  unsigned short* card    = (unsigned short*) &pvmeio->card;
  unsigned short* signal  = (unsigned short*) &pvmeio->signal;

  unsigned slot = (*card)>>8;
  unsigned chassis = (*card) - ((slot)<<8) ;

  unsigned command = (*signal)>>8;
  unsigned channel = (*signal) - ((command)<<8);

  char tmp[81];
  int retv;
  int first_channel=channel, chs_number=command;
  if(strstr(pbo->desc,"smi"))
  { 
    strncpy(tmp, pbo->name, strlen(pbo->name)-strlen("_BO"));
    tmp[strlen(pbo->name)-strlen("_BO")]=0;

    retv=ScalerBoardSmiMonitor(1, tmp, chassis, slot, first_channel, chs_number);
    pbo->rval = retv; /// means nothing
  }
#endif
  return 0;
}


//===============================================================================================
static long
write_bo(struct boRecord *pbo)
{
#ifdef USE_SMI
  struct vmeio *pvmeio = (struct vmeio *) &(pbo->out.value);  
  unsigned short* card    = (unsigned short*) &pvmeio->card;
  unsigned short* signal  = (unsigned short*) &pvmeio->signal;

  unsigned slot = (*card)>>8;
  unsigned chassis = (*card) - ((slot)<<8) ;

  unsigned command = (*signal)>>8;
  unsigned channel = (*signal) - ((command)<<8);

  int retv;
  int first_channel=channel, chs_number=command;
  if(strstr(pbo->desc,"smi"))
  {
    retv=ScalerBoardSmiControl(pbo->name, chassis, slot,  
    first_channel, chs_number, (unsigned char)pbo->rval);
  }
  else if(strstr(pbo->desc,"crate_fsm_init"))
  { /// for any order of launch of ioc and fsm
    retv=ScalerCrateSmiInit(pbo->name, chassis);
  }
#endif
  return 0;  
}

//===============================================================================================
static long init_ai(struct aiRecord *pai) { return 0; }
static long read_ai(struct aiRecord *pai)
{
  struct vmeio *pvmeio = (struct vmeio *) &(pai->inp.value);  

  unsigned short* card    = (unsigned short*) &pvmeio->card;
  unsigned short* signal  = (unsigned short*) &pvmeio->signal;

  unsigned int slot = (*card)>>8;
  unsigned int chassis = (*card) - ((slot)<<8) ;

  unsigned int command = (*signal)>>8;
  unsigned int channel = (*signal) - ((command)<<8);

#ifdef NOWAVEFORMS
  double *values;
  int ret,len;
  // thresholds:
  if (command==FADCTET || command==TDCTET || command==TRGTET) { 
      values = (double *) malloc(sizeof(double)*2);
      if (!IocGetValue(chassis,slot,channel,JLAB_SET_THRESHOLD,values))
          pai->rval = values[(command & 0xF)-1];
      else
          recGblSetSevr(pai,READ_ALARM,INVALID_ALARM); 
      free(values);
  }
  // counts:
  else if (command==FADCCNT ||
           command==GTDCCNT || command==GTRGCNT ||
           command==TDCCNT  || command==TRGCNT) {
    ret=IocGetWaveformLength(chassis, slot, channel, &len);
    if (ret==0) {
        if (len > (command & 0xF)-3) {
            values = (double *) malloc(sizeof(double)*len);
            IocReadWaveform(chassis, slot, channel, len, values);
            pai->rval = values[(command & 0xF)-3];
            free(values);
        }
        else recGblSetSevr(pai,READ_ALARM,INVALID_ALARM); 
            //printf("read_ai:  ERROR, bad scaler array: %u/%u/%u/%x\n",chassis,slot,channel,command);
    }
    else recGblSetSevr(pai,READ_ALARM,INVALID_ALARM); 
        //printf("read_ai:  ERROR, bad slot status: %u/%u/%u/%x\n",chassis,slot,channel,command);
  }
  else if (command==SSPNSFIB || command==SSPNDFIB) {
      values = (double*) malloc(sizeof(double)*2);
      if (!IocGetValue(chassis,slot,channel,JLAB_GET_NFIBERS,values))
          pai->rval = values[(command & 0xF)-3];
      else
          recGblSetSevr(pai,READ_ALARM,INVALID_ALARM); 
      free(values);
  }
  else printf("read_ai:  ERROR, no command:  %u/%u/%u/%x\n",chassis,slot,channel,command);
#else
  double values[200];
  if (command<2) {
      IocGetValue(chassis,slot,channel,JLAB_SET_THRESHOLD,values);
      pai->rval = values[command];
  }
  else printf("read_ai:  ERROR, no command: %d\n",command);
#endif

  return 0;  
}
//===============================================================================================
static long init_ao(struct aoRecord  *pao)
{
  double values[20];

  struct vmeio *pvmeio = (struct vmeio *) &(pao->out.value);  

  unsigned short* card    = (unsigned short*) &pvmeio->card;
  unsigned short* signal  = (unsigned short*) &pvmeio->signal;

  unsigned int slot = (*card)>>8;
  unsigned int chassis = (*card) - ((slot)<<8) ;

  unsigned int command = (*signal)>>8;
  unsigned int channel = (*signal) - ((command)<<8);

#ifdef NOWAVEFORMS
  if (command==FADCTET || command==TDCTET || command==TRGTET) { 
      IocGetValue(chassis,slot,channel,JLAB_SET_THRESHOLD,values);
      pao->rval = values[(command & 0xF)-1];
  }
  else printf("init_ao:  ERROR, no command:  %u/%u/%u/%x\n",chassis,slot,channel,command);
#else
  if (command<2) {
      IocGetValue(chassis,slot,channel,JLAB_SET_THRESHOLD,values);
      pao->rval = values[command];
  }
  else printf("init_ao:  ERROR, no command: %u/%u/%u/%d\n",chassis,slot,channel,command);
#endif
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

#ifdef NOWAVEFORMS
  if (command==FADCTET || command==TDCTET || command==TRGTET) { 
      threshType = (command & 0xF) - 1;
      threshValue = pao->val;
      values[0] = threshType;
      values[0] = threshValue;
      IocSetValue(chassis,slot,channel,JLAB_SET_THRESHOLD,values);
  }
  else printf("write_ao:  ERROR, no command:  %u/%u/%u/%x\n",chassis,slot,channel,command);
#else
  if (command<2) {
      threshType = command;
      threshValue = pao->val;
      values[0] = threshType;
      values[1] = threshValue;
      IocSetValue(chassis,slot,channel,JLAB_SET_THRESHOLD,values);
  }
  else printf("write_ao:  ERROR, no command: %d\n",command);
#endif
  return 0;  
}


//===============================================================================================
static long
read_bi(struct biRecord *pbi)
{
#ifdef USE_SMI
  struct vmeio *pvmeio = (struct vmeio *) &(pbi->inp.value);  

  unsigned short* card    = (unsigned short*) &pvmeio->card;
  unsigned short* signal  = (unsigned short*) &pvmeio->signal;

  unsigned int slot = (*card)>>8;
  unsigned int chassis = (*card) - ((slot)<<8) ;

  unsigned int command = (*signal)>>8;
  unsigned int channel = (*signal) - ((command)<<8);

  int retv;
  int first_channel=channel, chs_number=command;
  if(strstr(pbi->desc,"smi"))
  {
    retv=ScalerBoardSmiMonitor(0, pbi->name, chassis, slot, first_channel, chs_number);
    pbi->rval = retv; /// means nothing
  }
#endif

  return 0;  
}


//===============================================================================================
static long
read_waveform(struct waveformRecord *pwi)
{
  struct vmeio *pvmeio = (struct vmeio *) &(pwi->inp.value);  

  unsigned short* card    = (unsigned short*) &pvmeio->card;
  unsigned short* signal  = (unsigned short*) &pvmeio->signal;

  unsigned slot = (*card)>>8;
  unsigned chassis = (*card) - ((slot)<<8) ;

  unsigned command = (*signal)>>8;
  unsigned channel = (*signal) - ((command)<<8);

  int len, len_com;
  double *values;
  int ret_status=1;

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

//    for (pwi->nord=0; pwi->nord<pwi->nelm; pwi->nord++) {
//        ((double*)pwi->bptr)[pwi->nord] = (double)rand()/RAND_MAX * 1e8;
//    }
//    return OK;
    
    if (command==SSPSCAL)
        ret_status = IocGetWaveformLength(chassis, slot, channel, &len);
    else if (command==SSPDATA) 
        ret_status = IocGetWaveformLengthSSPData(chassis, slot, channel, &len);
    else
        ret_status = IocGetWaveformLength(chassis, slot, channel, &len);

    //fprintf(stderr,"read_waveform:  %x/%x/%x/%x %d/%d\n",
    //        slot,chassis,command,channel,ret_status,len);

    if (ret_status==0) {
        values = (double *) malloc(sizeof(double)*len);
        if (command==SSPSCAL)
            IocReadWaveform(chassis, slot, channel, len, values);
        else if (command==SSPDATA)
            IocReadWaveformSSPData(chassis, slot, channel, len, values);
        else
            IocReadWaveform(chassis, slot, channel, len, values);   
        len_com=len;
    }
    else len_com=pwi->nelm;

    for (pwi->nord = 0; pwi->nord < len_com; pwi->nord++)
    {
        if (ret_status==0) 
            ((double*)pwi->bptr)[pwi->nord] = values[pwi->nord];
        else
            ((double*)pwi->bptr)[pwi->nord] = ret_status;
    }
    if (ret_status==0) free(values);
  }
  return OK;
}

//===============================================================================================

