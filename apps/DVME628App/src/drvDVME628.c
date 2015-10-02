/*****   drvDVME628.c            *****/
/*****   Author: Al Grippo       *****/
/*****   Date:   06Feb97         *****/

/**
 * Ported to EPICS 3.14+
 *
 * Author: Wesley Moore
 * Date:   Oct 2015
 */

#include    <vxWorks.h>
#include	<types.h>
#include    <vme.h>
#include    <cacheLib.h>
#include    <stdioLib.h>
#include    <drvSup.h>
#include    <sysLib.h>
#include    <vxLib.h>

#include	<dbDefs.h>
#include	<link.h>


/****************************************************************************/
/* The DVME628 has 8 12-bit inputs that will be provided by 16-bit writes. */
/****************************************************************************/

#define BASEADDR        0x9400
#define CHANS	         8 

int DEBUGDVME628 = 0;
unsigned short *dvmeao_shortAdd[CHANS];

/***************************************************************************/
/* Init DVME628                                                            */
/***************************************************************************/
int init_DVME628(){
   long chan_addrs[] = {BASEADDR+160, BASEADDR+162, BASEADDR+164,
               BASEADDR+166, BASEADDR+168, BASEADDR+170,
	       BASEADDR+172, BASEADDR+174 };
   int status, i;
   char *shortaddr;
   char testV = 0;

   /***********************************************************************/
   /* Get the access addresses for each channel                           */
   /* Tell card we are using short supervisory access                     */
   /***********************************************************************/
   for (i=0;i<CHANS;i++){
      status = sysBusToLocalAdrs(VME_AM_SUP_SHORT_IO, (char *)chan_addrs[i], &shortaddr);
      if (status != OK){
         printf("Addressing error in DVME628 driver Channel #%d\n",i);
         return ERROR;
      }
      dvmeao_shortAdd[i] = (unsigned short *)shortaddr;
      if(vxMemProbe(shortaddr, VX_READ, 1, &testV) == OK ){
	 if(DEBUGDVME628){
            printf("DVME628 is present; shortAdd = %p\n",
                  dvmeao_shortAdd[i]);
         }
      } 
   }

   return(0);
}

/**************************************************************************/
/* Write DVME628                                                          */
/**************************************************************************/
int write_DVME628(signal, pval)
unsigned short signal;
unsigned long   *pval;
{
   unsigned short dvmeout;
   /* write new output - shift left 4 bits since only 12 bit DAC */
   dvmeout = (*pval << 4);   /* implicit casting */
   *dvmeao_shortAdd[signal] = dvmeout;
   if(DEBUGDVME628)
      printf("signal = %d pval= %ld *dvmeao_shortAdd = %d dvmeao_shortAdd = %p\n", 
           signal, *pval, dvmeout, dvmeao_shortAdd[signal]);
           /* Note: cannot print *dvmeao_shortAdd directly, since the DAC
              registers are write-only */

   return(0);
}
