/* devAiXy566.c */
/* share/src/dev @(#)devAiXy566.c	1.13     5/07/93 */

/* devAiXy566.c - Device Support Routines */
/*
 *      Author:      Cengiz Erbas 
 *      Date:        8-03-93
 *
 *      Experimental Physics and Industrial Control System (EPICS)
 *
 *      Copyright 1991, the Regents of the University of California,
 *      and the University of Chicago Board of Governors.
 *
 *      This software was produced under  U.S. Government contracts:
 *      (W-7405-ENG-36) at the Los Alamos National Laboratory,
 *      and (W-31-109-ENG-38) at Argonne National Laboratory.
 *
 *      Initial development by:
 *              The Controls and Automation Group (AT-8)
 *              Ground Test Accelerator
 *              Accelerator Technology Division
 *              Los Alamos National Laboratory
 *
 *      Co-developed with
 *              The Controls and Computing Group
 *              Accelerator Systems Division
 *              Advanced Photon Source
 *              Argonne National Laboratory
 *
 * Modification Log:
 * -----------------
 *      ...
 */

#include	<vxWorks.h>
/* #include	<types.h>
   #include	<stdioLib.h> */
#include	<stdlib.h>
#include	<stdio.h>
#include	<string.h>

#include	<alarm.h>
#include	<cvtTable.h>
#include	<dbDefs.h>
#include    <recGbl.h>
#include	<dbAccess.h>
#include    <recSup.h>
#include	<devSup.h>
#include	<link.h>
#include	<dbScan.h>
#include	<module_types.h>
#include	<aiRecord.h>
#include    <epicsExport.h>

extern int Xy560_driver(short, short, short*);
extern int Xy560_getioscanpvt(short, IOSCANPVT*);

static long init_record();
static long get_ioint_info();
static long read_ai();
static long special_linconv();

struct {
	long		number;
	DEVSUPFUN	report;
	DEVSUPFUN	init;
	DEVSUPFUN	init_record;
    DEVSUPFUN   get_ioint_info;
	DEVSUPFUN	read_ai;
	DEVSUPFUN	special_linconv;
} devAiXy560={
	6,
	NULL,
	NULL,
	init_record,
	get_ioint_info,
	read_ai,
	special_linconv};
epicsExportAddress(dset,devAiXy560);

static long init_record(pai)
    struct aiRecord	*pai;
{
    unsigned short value;
    struct vmeio *pvmeio;
    long status;

    /* ai.inp must be an VME_IO */
    switch (pai->inp.type) {
    case (VME_IO) :
		break;
    	default :
		recGblRecordError(S_db_badField,(void *)pai,
			"devAiXy560 (init_record) Illegal INP field");
		return(S_db_badField);
    }

    /* set linear conversion slope*/
    pai->eslo = (pai->eguf -pai->egul)/4095.0;

    /* call driver so that it configures card */
    pvmeio = (struct vmeio *)&(pai->inp.value);
    if( (status=Xy560_driver(pvmeio->card,pvmeio->signal,&value)) ) {
		recGblRecordError(status,(void *)pai,
			"devAiXy560 (init_record) Xy560_driver error");
		return(status);
    }
    return(0);
}

static long get_ioint_info(int cmd, struct aiRecord *pai,IOSCANPVT *ppvt)
{
    Xy560_getioscanpvt(pai->inp.value.vmeio.card,ppvt);
    return(0);
}

static long read_ai(pai)
    struct aiRecord	*pai;
{
	unsigned short value;
	struct vmeio *pvmeio;
	long status;
	pvmeio = (struct vmeio *)&(pai->inp.value);
	status=Xy560_driver(pvmeio->card,pvmeio->signal,&value);
        if(status==-1) {
			status = 2; /*don't convert*/
            recGblSetSevr(pai,READ_ALARM,INVALID_ALARM);
			return(status);
        }else if(status==-2) {
            status=0;
            recGblSetSevr(pai,HW_LIMIT_ALARM,INVALID_ALARM);
        }
	if(status!=0) return(status);
	pai->rval = value;
	return(status);
}

static long special_linconv(pai,after)
    struct aiRecord	*pai;
    int after;
{

    if(!after) return(0);
    /* set linear conversion slope*/
    pai->eslo = (pai->eguf -pai->egul)/4095.0;
    return(0);
}
