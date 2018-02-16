/*-------------------------------------------------------*/
/*              Xycom 240 Bo Device Support
 *
 * Functions: Bo Device Support For the Xycom 240
 *            Digital I/O Card. Writes to Hardware
 *
 * Date: April 8, 1997
 * Author: Scott higgins
 *
 * Overview: This device support uses the vme_io
 * 	     structure as follows
 *	     card:   card # 0-1
 *	     signal: port # 0-7
 *	     parm:   bit # 0-7
 *           Exception To The Rules:
 *                   If signal is set to 8 the parm field
 *		     is a mask to set the ports up as inputs
 *	             or outputs. 
 *
 */
/*-------------------------------------------------------*/
/*-------------------------------------------------------*/

#include	<vxWorks.h>
#include	<types.h>
#include	<stdlib.h>
#include	<stdioLib.h>
#include	<string.h>

#include	<alarm.h>
#include	<dbDefs.h>
#include    <recGbl.h>
#include	<dbAccess.h>
#include    <recSup.h>
#include	<devSup.h>
#include	<module_types.h>
#include	<boRecord.h>
#include    <epicsExport.h>

extern int errVerbose;
extern int Xycom240M_Initialized;
extern int init_Xy240M();
extern int config_Xy240M(short, int);
extern int write_Xy240M(short, short, long, long);

/* Create the dset for devBoXy240M */
static long init();
static long init_record();
static long write_bo();

struct {
	long		number;
	DEVSUPFUN	report;
	DEVSUPFUN	init;
	DEVSUPFUN	init_record;
	DEVSUPFUN	get_ioint_info;
	DEVSUPFUN	write_bo;
}devBoXy240M={
	5,
	NULL,
	init,
	init_record,
	NULL,
	write_bo};

epicsExportAddress(dset,devBoXy240M);

static long init(after)
int after;
{
        int status = 0;
        if (!Xycom240M_Initialized) {
                Xycom240M_Initialized = 1; /* If init fails it will reset to 0 */
                status = init_Xy240M();
        }

        return(status);
}

static long init_record(pbo)
    struct boRecord	*pbo;
{
    struct vmeio *pvmeio;
    int	status;
    unsigned int bit, port_mask;

    /* bo.out must be an VME_IO */
    switch (pbo->out.type) {
    case (VME_IO) :
	pvmeio = (struct vmeio *)&(pbo->out.value);
	if (pvmeio->signal < 8) {		/* Initialize Bit Mask */
		bit = atoi((char *)pvmeio->parm);
        	pbo->mask = 1;
        	pbo->mask <<= bit;
		status = write_Xy240M(pvmeio->card,pvmeio->signal,pbo->mask,pbo->rval);
	}
	else if (pvmeio->signal == 8) {		/* Initialize Cards Port Direction Register */
		port_mask = atoi((char *)pvmeio->parm);
		config_Xy240M(pvmeio->card,port_mask);
	}
	else {
		recGblRecordError(S_db_badField,(void *)pbo,
			"devBoXy240M (init_record) Illegal OUT field (Signal > 8)");
		return(S_db_badField);
	}
	break;
    default :
	recGblRecordError(S_db_badField,(void *)pbo,
		"devBoXy240M (init_record) Illegal OUT field");
	return(S_db_badField);
    }
    return(0);
}

static long write_bo(pbo)
    struct boRecord	*pbo;
{
	struct vmeio 	*pvmeio;
	int	    	status;

	
	pvmeio = (struct vmeio *)&(pbo->out.value);
	status = write_Xy240M(pvmeio->card,pvmeio->signal,pbo->mask,pbo->rval);
	if(status!=0) {
                if(recGblSetSevr(pbo,WRITE_ALARM,INVALID_ALARM) && errVerbose
		&& (pbo->stat!=WRITE_ALARM || pbo->sevr!=INVALID_ALARM))
			recGblRecordError(-1,(void *)pbo,"write_Xy240M Error");
		return(2);
	}
	return(0);
}

