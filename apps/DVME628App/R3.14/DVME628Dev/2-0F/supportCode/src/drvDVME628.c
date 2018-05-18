/*****   drvDVME628.c            *****/
/*****   Author: Al Grippo       *****/
/*****   Date:   06Feb97         *****/
/* Modified for multi card support.  Richard Dickson  9/4/98 */

#include        <vxWorks.h>
#include	<types.h>
#include        <vme.h>
#include        <cacheLib.h>
#include        <stdioLib.h>
#include        <stdio.h>
#include        <sysLib.h>
#include        <taskLib.h>
#include        <intLib.h>
#include        <vxLib.h>
#include        <drvSup.h>

#include	<dbDefs.h>
#include	<link.h>
#include        <iocsh.h>

#include        <epicsExport.h>

/****************************************************************************/
/* The DVME628 has 8 12-bit inputs that will be provided by 16-bit writes. */
/****************************************************************************/

#define CARDS		  3
#define C1BASEADDR        0x9400
#define C2BASEADDR        0x9800
#define C3BASEADDR        0x9B00
#define CHANS	          8 

int DEBUGDVME628 = 0;
int DVME628_Initialized = 0;
volatile unsigned short *dvme_shortAdd[CARDS][CHANS];

/***************************************************************************/
/* Init DVME628                                                            */
/***************************************************************************/
int init_DVME628(void){
   int chan_addrs[CARDS][CHANS] =
                                 {{C1BASEADDR+160, C1BASEADDR+162, C1BASEADDR+164,
                                   C1BASEADDR+166, C1BASEADDR+168, C1BASEADDR+170,
	                           C1BASEADDR+172, C1BASEADDR+174 },

                                  {C2BASEADDR+160, C2BASEADDR+162, C2BASEADDR+164,
                                   C2BASEADDR+166, C2BASEADDR+168, C2BASEADDR+170,
	                           C2BASEADDR+172, C2BASEADDR+174 },

                                  {C3BASEADDR+160, C3BASEADDR+162, C3BASEADDR+164,
                                   C3BASEADDR+166, C3BASEADDR+168, C3BASEADDR+170,
	                           C3BASEADDR+172, C3BASEADDR+174 }};
   int status, chan, card;
   char *dvme_shortaddr;
   char testV = 0;

   for (card=0; card<CARDS; card++){
     /***********************************************************************/
     /* Get the access addresses for each channel                           */
     /* Tell card we are using short supervisory access                     */
     /***********************************************************************/
     for (chan=0;chan<CHANS;chan++){
        status = sysBusToLocalAdrs(VME_AM_SUP_SHORT_IO, (char *)chan_addrs[card][chan], &dvme_shortaddr);
        if (status != OK){
           printf("Addressing error in DVME628 driver Card #%d Channel #%d\n",card, chan);
  	 DVME628_Initialized = 0;
           return ERROR;
        }
        dvme_shortAdd[card][chan] = (unsigned short *)dvme_shortaddr;
        if(vxMemProbe(dvme_shortaddr, VX_READ, 1, &testV) == OK ){
              printf("DVME628 is present; dvme_shortAdd = %p\n",
                    dvme_shortAdd[card][chan]);
        } 
     }
   }

   return(0);
}

/**************************************************************************/
/* Write DVME628                                                          */
/**************************************************************************/
int write_DVME628(card, signal, pval)
unsigned short card;
unsigned short signal;
unsigned long   *pval;
{
   unsigned short dvmeout;
   /* write new output - shift left 4 bits since only 12 bit DAC */
   dvmeout = (*pval << 4);   /* implicit casting */
   *dvme_shortAdd[card][signal] = dvmeout;
   if(DEBUGDVME628)
      printf("card = %d signal = %d pval= %ld *dvme_shortAdd = %d dvme_shortAdd = %p\n", 
           card, signal, *pval, dvmeout, dvme_shortAdd[card][signal]);
           /* Note: cannot print *dvme_shortAdd directly, since the DAC
              registers are write-only */

   return(0);
}
