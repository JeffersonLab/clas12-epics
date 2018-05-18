/*** devAoDVME628.c         ***/
/*** Author: Al Grippo      ***/
/*** Date: 06Feb97          ***/
/* Modified for multi card support.  Richard Dickson  9/4/98 */

#include        <vxWorks.h>
#include        <types.h>
#include        <stdioLib.h>
#include        <memLib.h>
#include        <string.h>

#include        <alarm.h>
#include        <cvtTable.h>
#include        <dbDefs.h>
#include        <dbAccess.h>
#include        <dbAccessDefs.h>
#include        <recSup.h>
#include        <devSup.h>
#include        <recGbl.h>
#include        <link.h>
#include        <module_types.h>
#include        <aoRecord.h>

#include        <dbScan.h>
#include        <vxLib.h>
#include        <vme.h>

#include        <epicsExport.h>

extern int DVME628_Initialized;

/* Create the dset for devAoDVME628 */
static long init();
static long init_record();
static long write_ao();
static long special_linconv();

int init_DVME628(void);
int write_DVME628(register unsigned short card,
		  register unsigned short signal,
				    unsigned long *pval);

struct {
	long            number;
	DEVSUPFUN       report;
	DEVSUPFUN       init;
	DEVSUPFUN       init_record;
	DEVSUPFUN       get_ioint_info;
	DEVSUPFUN       write_ao;
	DEVSUPFUN       special_linconv;
}devAoDVME628={
	6,
	NULL,
        init,
	init_record,
	NULL,
	write_ao,
	special_linconv};
epicsExportAddress(dset,devAoDVME628);

/*****************************************************************
 * Init
 *****************************************************************/
static long init(after)
   int after;
{
   int status = 0;

   if (!DVME628_Initialized)  {
      DVME628_Initialized = 1;
      status = init_DVME628();
   }

   return (status);
}

/*****************************************************************
 * Init Record
 *****************************************************************/
static long init_record(pao)
   struct aoRecord *pao;
{
   int status = 0;

   /* ao.out must be VME_IO */
   switch (pao->out.type) {
   case (VME_IO) :
      break;
   default :
      status = S_db_badField;
      recGblRecordError(status,(void *)pao,
        "devAoDVME628 (init_record) Illegal OUT field");
    }

    /* set linear conversion slope */
    pao->eslo = (pao->eguf - pao->egul)/4095.0;

    return(status);
}

/****************************************************************
 * Write Ao
 ****************************************************************/
static long write_ao(pao)
   struct aoRecord *pao;
{
   struct vmeio *pvmeio_DVME628;
   int status;
   unsigned long value;
   int DEBUGDVME628 = 0;

   pvmeio_DVME628 = (struct vmeio *)&(pao->out.value);
   if(DEBUGDVME628)
      printf("pvmeio_DVME628->signal = %d, value = %ld\n",pvmeio_DVME628->signal,
                                                                value); 

   value = pao->rval;
   status = write_DVME628(pvmeio_DVME628->card, pvmeio_DVME628->signal, &value);
   if(status==0) {
      pao->rbv = value;
   } else {
      recGblSetSevr(pao,WRITE_ALARM,INVALID_ALARM);
   }
   return(status);
}

/******************************************************************
 * special_linconv
 ******************************************************************/
static long special_linconv(pao,after)
    struct aoRecord	*pao;
    int after;
{

    if(!DVME628_Initialized) return(0);
    /* set linear conversion slope*/
    pao->eslo = (pao->eguf - pao->egul)/4095.0;
    return(0);
}
