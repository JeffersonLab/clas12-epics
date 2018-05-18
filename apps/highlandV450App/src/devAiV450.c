/* devAiV450.c */

/*  */

/* Copyright (c) 2005 Duke University
 *
 * Steve Hartman <hartman@fel.duke.edu>, Duke FEL Laboratory
 * Version 1.0
 * Please check <www.fel.duke.edu/epics> for the most recent version.
 *
 * This code provides EPICS support for the VMIVME-3122 High-Performance
 * 16-bit ADC board.
 * 
 */

/*
 This library is free software; you can redistribute it and/or
 modify it under the terms of the GNU Lesser General Public
 License as published by the Free Software Foundation; either
 version 2.1 of the License, or (at your option) any later version.

 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 Lesser General Public License for more details.

 You should have received a copy of the GNU Lesser General Public
 License along with this library; if not, write to the Free Software
 Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307
 USA
*/

#include <stdioLib.h>
#include <vme.h>
#include <epicsVersion.h>
#if (EPICS_VERSION==3) && (EPICS_REVISION>=14)
	#include <epicsExport.h>
#endif

#include <dbDefs.h>
#include <dbAccess.h>
#include <recSup.h>
#include <recGbl.h>
#include <devSup.h>
#include <link.h>
#include <alarm.h>
#include <aiRecord.h>


extern int v450_read(unsigned short card, unsigned int data, unsigned long *pval);

static long init_record();
static long read_ai();
static long special_linconv();

struct {
	long		number;  /* the number of following elements */
	DEVSUPFUN	report;
	DEVSUPFUN	init;
	DEVSUPFUN	init_record;
	DEVSUPFUN	get_ioint_info;
	DEVSUPFUN	read_ai;
	DEVSUPFUN	special_linconv;
} devAiV450={
	6,
	NULL,
	NULL,
	init_record,
	NULL,
	read_ai,
	special_linconv};

#if (EPICS_VERSION==3) && (EPICS_REVISION>=14)
	epicsExportAddress(dset,devAiV450);
#endif


static long init_record(pai)
struct aiRecord	*pai;
{

	/* ai.inp must be an VME_IO */
	switch (pai->inp.type) {
	case (VME_IO) :
		pai->udf = FALSE;
		break;
	default :
		recGblRecordError(S_db_badField,(void *)pai,
		    "devAiV450 (init_record) Illegal INP field");
		return(S_db_badField);
	}

	/* set linear conversion slope*/
	pai->eslo = (pai->eguf - pai->egul)/65535.0; /* 16-bit */

	return(0);
}

static long read_ai(pai)
struct aiRecord	*pai;
{
	unsigned long value;
	struct vmeio *pvmeio;
	int status=0;

	pvmeio = (struct vmeio *)&(pai->inp.value);

	status=v450_read(pvmeio->card,pvmeio->signal,&value);

	if ( status == 0 ) {
        // hack, prolly not the right place for this, NAB (January 2018)
        if (pvmeio->signal>=16 && pvmeio->signal<=20) 
            value=(short)value;
		pai->rval = value;
    }
	else
		recGblSetSevr(pai,READ_ALARM,INVALID_ALARM);

	return(status);
}

static long special_linconv(pai,after)
    struct aiRecord     *pai;
    int after;
{
    if(!after) return(0);
    /* set linear conversion slope*/
    pai->eslo = (pai->eguf - pai->egul)/65535.0; /* 16-bit */
    return(0);
}
