/****************************************************************************
 * Program   : devLibrm13.c                                                 *
 * Author    : Michael Johnson, David Wetherholt                            *
 * Modified  : 2014 Feb 4                                                   *
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
#include        <longinRecord.h>
#include        <dbScan.h>
#include        <vxLib.h>
#include        <vme.h>
#include        <epicsExport.h>

extern int DEBUGBRM13;
extern int read_brm13();
/* Create the dset for devLibrm13 */
static long init_record();
static long read_longin();

struct {
	long            number;
	DEVSUPFUN       report;
	DEVSUPFUN       init;
	DEVSUPFUN       init_record;
	DEVSUPFUN       get_ioint_info;
	DEVSUPFUN       read_longin;
	DEVSUPFUN       special_linconv;
}devLibrm13={
	6,
	NULL,
	NULL,
	init_record,
	NULL,
	read_longin,
	NULL};
epicsExportAddress(dset,devLibrm13);
static long init_record (struct longinRecord *plongin) {
/********************************************************
 * Init Record
 ********************************************************/

    /* li.inp must be VME_IO */
    switch (plongin->inp.type) {
      case (VME_IO):
        break;
      default :
        recGblRecordError(S_db_badField,(void *)plongin,
          "devLibrm13 (init_record) Illegal INP field");
        return(S_db_badField);
    }
    plongin->udf = FALSE;
    return(0);
}

static long read_longin(struct longinRecord *plongin) {
/**********************************************************
 * Read LongIn
 **********************************************************/
    struct vmeio  *pvmeio_brm13;
    int           status;
    unsigned long value;

    /****** Get value and status */
    pvmeio_brm13 = (struct vmeio *)&(plongin->inp.value);
    status = read_brm13(pvmeio_brm13->card, pvmeio_brm13->signal, &value);

    if(DEBUGBRM13) {
      printf("devLibrm13: signal is %d\n", pvmeio_brm13->signal);
      printf("devLibrm13: status is %d\n", status);
    }

    if(status==0) {
      plongin->val = value;
    } else {
      recGblSetSevr(plongin,READ_ALARM,INVALID_ALARM);
    }
    return(status);
}
