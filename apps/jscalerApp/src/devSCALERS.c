
#define NOWAVEFORMS 1

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <stdio.h>
#include <shareLib.h>
#include <unistd.h>

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
#include <biRecord.h>
#include <aiRecord.h>
#include <aoRecord.h>
#include <waveformRecord.h>
#include <epicsExport.h> 
#include <cantProceed.h>

#include "common.h"
#include "CrateMsgTypes.h"

extern int is_mainframe_read[256];
extern int nmainframes;
int FLAG_BLOCK_INIT=1;

static long write_ao(struct aoRecord *);
static long init_ao(struct aoRecord *); 
static long read_ai(struct aiRecord *); 
static long init_ai(struct aiRecord *); 
static long read_waveform(struct waveformRecord *);

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
    }
    else recGblSetSevr(pai,READ_ALARM,INVALID_ALARM); 
  }
  // SSP # fibers:
  else if (command==SSPNSFIB || command==SSPNDFIB) {
      values = (double*) malloc(sizeof(double)*2);
      if (!IocGetValue(chassis,slot,channel,JLAB_GET_NFIBERS,values))
          pai->rval = values[(command & 0xF)-3];
      else
          recGblSetSevr(pai,READ_ALARM,INVALID_ALARM); 
      free(values);
  }
  // SSP temperatures/voltages:
  else if (command==SSPTEMP1 || 
           command==SSPTEMP2 || 
           command==SSPTEMP3 ||
           command==SSPVOLT1 || 
           command==SSPVOLT2 || 
           command==SSPVOLT3 || 
           command==SSPVOLT4 || 
           command==SSPVOLT5 || 
           command==SSPVOLT6) {
      ret=IocGetWaveformLengthSSPData(chassis, slot, channel, &len);
      if (len > (command & 0xF) - 5) {
          values = (double*) malloc(sizeof(double)*len);
          IocReadWaveformSSPData(chassis,slot,channel,len,values);
          pai->rval = values[(command & 0xF) - 5];
          free(values);
      }
      else recGblSetSevr(pai,READ_ALARM,INVALID_ALARM); 
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
read_waveform(struct waveformRecord *pwi)
{
  struct vmeio *pvmeio = (struct vmeio *) &(pwi->inp.value);  

  unsigned short* card    = (unsigned short*) &pvmeio->card;
  unsigned short* signal  = (unsigned short*) &pvmeio->signal;

  unsigned slot = (*card)>>8;
  unsigned chassis = (*card) - ((slot)<<8) ;

  unsigned command = (*signal)>>8;
  unsigned channel = (*signal) - ((command)<<8);

  int len, len_com;//,ii;
  double *values;
  int ret_status=1;

  {
    pwi->rarm = 0;

// simulator:
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

    //fprintf(stderr,"read_waveform:  %x/%x/%x/%d %d/%d\n",
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
        //for (ii=0;ii<len;ii++) printf("--------- %f\n",values[ii]);
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

