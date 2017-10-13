#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <dbAccess.h>
#include <devSup.h>
#include <recGbl.h>
#include <alarm.h>
#include <recSup.h>
#
#include <waveformRecord.h>
#include <epicsExport.h>
#include "amqSupport.h"  //to get the enum of record types (EAi,EWaveform etc)

long init_wf(waveformRecord *prec){
  addPV((void *)prec,EWaveform,prec->inp.text); //save the info for the message handler
  return 0;
}

long read_wf(waveformRecord *prec){
  return 0;
}

struct {
  long num;
  DEVSUPFUN  report;
  DEVSUPFUN  init;
  DEVSUPFUN  init_record;
  DEVSUPFUN  get_ioint_info;
  DEVSUPFUN  read_ai;
} devWaveformMQ = {
  5, /* space for 6 functions */
  NULL,
  NULL,
  init_wf,
  NULL,
  read_wf
};
epicsExportAddress(dset,devWaveformMQ);
