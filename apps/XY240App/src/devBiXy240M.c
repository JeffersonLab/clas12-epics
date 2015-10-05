/*-------------------------------------------------------*/
/*              Xycom 240 Bi Device Support
 *
 * Functions: Bi Device Support For the Xycom 240
 *            Digital I/O Card. Reads From Hardware
 *
 * Date: April 8, 1997
 * Author: Scott higgins
 *
 * Overview: This device support uses the vme_io
 *           structure as follows
 *           card:   card # 0-1
 *           signal: port # 0-7
 *           parm:   bit # 0-7
 *           Exception To The Rules:
 *                   If signal is set to 8 the parm field
 *                   is a mask to set the ports up as inputs
 *                   or outputs.
 */
/*-------------------------------------------------------*/
/*-------------------------------------------------------*/

#include	<vxWorks.h>
#include	<types.h>
#include    <stdlib.h>
#include	<stdioLib.h>
#include	<string.h>

#include	<alarm.h>
#include	<dbDefs.h>
#include    <recGbl.h>
#include	<dbAccess.h>
#include	<recSup.h>
#include	<devSup.h>
#include	<module_types.h>
#include	<biRecord.h>


extern int errVerbose;
extern int Xycom240M_Initialized;
extern int init_Xy240M();
extern int config_Xy240M(short, int);
extern int read_Xy240M(short, short, long, long*);

/* Create the dset for devBiXy240M */
static long init();
static long init_record();
static long read_bi();

struct {
	long		number;
	DEVSUPFUN	report;
	DEVSUPFUN	init;
	DEVSUPFUN	init_record;
	DEVSUPFUN	get_ioint_info;
	DEVSUPFUN	read_bi;
}devBiXy240M={
	5,
	NULL,
	init,
	init_record,
	NULL,
	read_bi};


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

static long init_record(pbi)
    struct biRecord	*pbi;
{
    struct vmeio *pvmeio;
    unsigned int bit,port_mask;

    /* bi.inp must be an VME_IO */
    switch (pbi->inp.type) {
    case (VME_IO) :
	pvmeio = (struct vmeio *)&(pbi->inp.value);
	if (pvmeio->signal < 8) {              /* Initialize Bit Mask */
		bit = atoi((char *)pvmeio->parm);
        	pbi->mask = 1;
        	pbi->mask <<= bit;
        }
        else if (pvmeio->signal == 8) {        /* Initialize Cards Port Direction Register */
                port_mask = atoi((char *)pvmeio->parm);
                config_Xy240M(pvmeio->card,port_mask);
        }
	else {
		recGblRecordError(S_db_badField,(void *)pbi,
			"devBiXy240M (init_record) Illegal INP field (Signal > 8)");
		return(S_db_badField);
	}
	break;
    default :
	recGblRecordError(S_db_badField,(void *)pbi,
		"devBiXy240M (init_record) Illegal INP field");
	return(S_db_badField);
    }
    return(0);
}

static long read_bi(pbi)
    struct biRecord	*pbi;
{
	struct vmeio 	*pvmeio;
	int	    	status;
	unsigned long   value;

	
	pvmeio = (struct vmeio *)&(pbi->inp.value);
	status = read_Xy240M(pvmeio->card,pvmeio->signal,pbi->mask,&value);
	if(status==0) {
		pbi->rval = value;
		return(0);
	} else {
                if(recGblSetSevr(pbi,READ_ALARM,INVALID_ALARM) && errVerbose
		&& (pbi->stat!=READ_ALARM || pbi->sevr!=INVALID_ALARM))
			recGblRecordError(-1,(void *)pbi,"read_Xy240M Error");
		return(2);
	}
}

