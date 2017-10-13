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
#include <aiRecord.h>
#include <epicsExport.h>
#include "amqSupport.h"  //to get the enum of record types (EAi,EWaveform etc)

long init_ai(aiRecord *prec){
  addPV((void *)prec,EAi,prec->inp.text); //save the info for the message handler
  return 0;
}

long read_ai(aiRecord *prec){
  return 2;         //ret = 2 to prevent conversion from rval to val
}

struct {
  long num;
  DEVSUPFUN  report;
  DEVSUPFUN  init;
  DEVSUPFUN  init_record;
  DEVSUPFUN  get_ioint_info;
  DEVSUPFUN  read_ai;
  DEVSUPFUN  special_linconv;
} devAiMQ = {
  6, /* space for 6 functions */
  NULL,
  NULL,
  init_ai,
  NULL,
  read_ai,
  NULL
};
epicsExportAddress(dset,devAiMQ);
