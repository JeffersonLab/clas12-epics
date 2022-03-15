/****************************************************************************
 * Program   : devLobrm13.c
 * Author    : Michael Johnson, David Wetherholt
 * Modified  : 2014 Feb 4
 ****************************************************************************/
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
#include        <module_types.h>
#include        <longoutRecord.h>
#include        <dbScan.h>
#include        <vxLib.h>
#include        <vme.h>
#include        <epicsExport.h>


extern int DEBUGBRM13;
/* Create the dset for devLobrm13 */
static long init();
static long init_record();
static long write_longout();

struct {
	long            number;
	DEVSUPFUN       report;
	DEVSUPFUN       init;
	DEVSUPFUN       init_record;
	DEVSUPFUN       get_ioint_info;
	DEVSUPFUN       write_longout;
	DEVSUPFUN       special_linconv;
}devLobrm13={
	6,
	NULL,
        init,
	init_record,
	NULL,
	write_longout,
	NULL};
epicsExportAddress(dset,devLobrm13);
extern int init_brm13();
extern int write_brm13();
static long init(int after) {
/*****************************************************************
 * Init
 *****************************************************************/
   int status = 0;

   if (after == 0) init_brm13();
   return (status);
}

/*****************************************************************
 * Init Record
 *****************************************************************/
static long init_record(struct longoutRecord *plongout) {
   int status = 0;

   /* lo.out must be VME_IO */
   switch (plongout->out.type) {
   case (VME_IO) :
      break;
   default :
      status = S_db_badField;
      recGblRecordError(status,(void *)plongout,
        "devLobrm13 (init_record) Illegal OUT field");
    }
    plongout->udf = FALSE;
    return(status);
}

static long write_longout(struct longoutRecord *plongout) {
/****************************************************************
 * Write LongOut
 ****************************************************************/
    struct vmeio  *pvmeio_brm13;
    int           status;
    unsigned long value;

    pvmeio_brm13 = &(plongout->out.value.vmeio);
    if(DEBUGBRM13)
      printf("pvmeio_brm13->signal = %d\n",pvmeio_brm13->signal);

    value = plongout->val;
    status = write_brm13(pvmeio_brm13->card, pvmeio_brm13->signal,&value);
    if(status!=0) {
      recGblSetSevr(plongout,WRITE_ALARM,INVALID_ALARM);
    }
    return(status);
}
