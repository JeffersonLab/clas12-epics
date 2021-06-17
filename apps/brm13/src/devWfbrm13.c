#include        <vxWorks.h>
#include        <types.h>
#include        <stdioLib.h>
#include        <memLib.h>
#include        <string.h>
#include        <alarm.h>
#include        <cvtTable.h>
#include        <dbDefs.h>
#include        <dbAccess.h>
#include        <recGbl.h>
#include        <recSup.h>
#include        <devSup.h>
#include        <link.h>
#include        <waveformRecord.h>
#include        <dbScan.h>
#include        <vxLib.h>
#include        <vme.h>
#include        <epicsExport.h>

extern int DEBUGBRM13;
extern int read_brm13();

static long init_record();
static long read_wf();

struct {
	long            number;
	DEVSUPFUN       report;
	DEVSUPFUN       init;
	DEVSUPFUN       init_record;
	DEVSUPFUN       get_ioint_info;
	DEVSUPFUN       read_wf;
}devWfbrm13={
	5,
	NULL,
	NULL,
	init_record,
	NULL,
	read_wf};
epicsExportAddress(dset,devWfbrm13);
static long init_record (waveformRecord *pwaveform) {
/********************************************************
 * Init Record
 ********************************************************/

    /* li.inp must be VME_IO */
    switch (pwaveform->inp.type) {
      case (VME_IO):
        break;
      default :
        recGblRecordError(S_db_badField,(void *)pwaveform,
          "devWfbrm13 (init_record) Illegal INP field");
        return(S_db_badField);
    }
    pwaveform->udf = FALSE;
    return(0);
}

static long read_wf(waveformRecord *pwaveform) {
 /**********************************************************
 * Read Record
 **********************************************************/
    struct vmeio  *pvmeio_brm13;
    int           status = OK;
    unsigned long value;
    int           conv_value;

    waveformRecord *wf = (waveformRecord*)pwaveform;
    pvmeio_brm13 = (struct vmeio *)&(wf->inp.value);

    wf->rarm = 0;
    for (wf->nord = 0; wf->nord < wf->nelm; wf->nord++) {
      /****** Get value and status */
      status = read_brm13(pvmeio_brm13->card, pvmeio_brm13->signal, &value);
      if (status != OK)
	break;
      
      /* convert register 12-bit 2's complement value */
      if (value >= 2048) {
	conv_value = -((~value & 0x0FFF) + 1);
      }
      else {
	conv_value = value;
      }
      
      switch (wf->ftvl)
	{
	case DBF_DOUBLE:
	  ((epicsFloat64*)wf->bptr)[wf->nord] = (epicsFloat64)conv_value;
	  break;
	case DBF_FLOAT:
	  ((epicsFloat32*)wf->bptr)[wf->nord] = (epicsFloat32)conv_value;
	  break;
	case DBF_LONG:
	  ((epicsInt32*)wf->bptr)[wf->nord] = (epicsInt32)conv_value;
	  break;
	case DBF_SHORT:
	  ((epicsInt16*)wf->bptr)[wf->nord] = (epicsInt16)conv_value;
	  break;
	default:
	  recGblRecordError(S_db_badField,(void *)wf,
          "read_wf: Can't convert waveform data type");
	  status = ERROR;
	  break;
	}
    }
    if(DEBUGBRM13) {
      printf("devWfbrm13: signal is %d\n", pvmeio_brm13->signal);
      printf("devWfbrm13: status is %d\n", status);
    }

    if(status == OK) {
      // do nothing
    } else {
      recGblSetSevr(pwaveform,READ_ALARM,INVALID_ALARM);
    }

    return(status);
}
