/*****************************************************************************
 *  devLiV450.c
 *
 *  EPICS device handler:
 *     Record type  : long input.
 *     Device model : V450 from Highland Technology
 *     Device type  : 16 channels isolated analog input board with
 *                    4 precision RTD signal conditioners.
******************************************************************************/

#include	<vxWorks.h>
#include	<types.h>
#include	<stdioLib.h>
#include	<string.h>

#include	<alarm.h>
#include	<dbDefs.h>
#include	<dbAccess.h>
#include	<recSup.h>
#include	<recGbl.h>
#include	<devSup.h>
#include	<longinRecord.h>
#include	<epicsExport.h>


static long init_record();
static long read_longin();
int read_V450();

struct {
	long		number;
	DEVSUPFUN	report;
	DEVSUPFUN	init;
	DEVSUPFUN	init_record;
	DEVSUPFUN	get_ioint_info;
	DEVSUPFUN	read_longin;
}devLiV450={
	5,
	NULL,
	NULL,
	init_record,
	NULL,
	read_longin};
epicsExportAddress(dset,devLiV450);

extern int v450_read(unsigned short card, unsigned int data, unsigned long *pval);
/********************************************
 *  init_record
 ********************************************/
static long init_record(struct longinRecord  *pli)
{
 struct vmeio     *pvmeio;

   /* input type must be VME_IO */
   switch (pli->inp.type) 
    {
     case(VME_IO):

      pvmeio = (struct vmeio *)&(pli->inp.value);  
      break;
      
    default:
      recGblRecordError(S_db_badField,(void *)pli,
        "devLiV450(init_record) Illegal INP field");
      return(S_db_badField);

    }

  return(0);
}


/************************************************
 * read_longin
 ************************************************/
static long read_longin(struct longinRecord  *pli)
{
  unsigned short    status;
  unsigned long     data;
  struct vmeio     *pvmeio;

  
  pvmeio = (struct vmeio *)&(pli->inp.value);  

  status = v450_read(pvmeio->card, pvmeio->signal, &data);  

  pli->val = data;

  return(status);
  
}
