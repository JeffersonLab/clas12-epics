/* share/src/drv @(#)drvXy560.c	1.3	5/06/93 */
/* static char *sccsID = "@(#)drvVmi3113.c	1.3\t5/06/93"; */
/*
 * subroutines that are used to interface to the vme analog output cards
 *
 * 	Author:      Cengiz Erbas 
 * 	Date:        8-03-93
 *
 *	Experimental Physics and Industrial Control System (EPICS)
 *
 *	Copyright 1991, the Regents of the University of California,
 *	and the University of Chicago Board of Governors.
 *
 *	This software was produced under  U.S. Government contracts:
 *	(W-7405-ENG-36) at the Los Alamos National Laboratory,
 *	and (W-31-109-ENG-38) at Argonne National Laboratory.
 *
 *	Initial development by:
 *		The Controls and Automation Group (AT-8)
 *		Ground Test Accelerator
 *		Accelerator Technology Division
 *		Los Alamos National Laboratory
 *
 *	Co-developed with
 *		The Controls and Computing Group
 *		Accelerator Systems Division
 *		Advanced Photon Source
 *		Argonne National Laboratory
 *
 * Modification Log:
 * -----------------
 * .01 8/03/93		ce	Original version
 */


#include    <vxWorks.h>
#include    <vme.h>
#include    <drvSup.h>
#include    <dbDefs.h>
#include    <dbScan.h>
#include    <module_types.h>
#include    <stdlib.h>
#include    <stdio.h>
#include    <rebootLib.h>
#include    <intLib.h>

#include    <sysLib.h>
#include    <vxLib.h>
#include    <taskLib.h>

/* Xy560 defines */

#define MAX_AI_XY560_CARDS	3
#define XY560_MAXCHAN		32
#define XY560_ADDRESS		0x8800

#define  SOFTWARE_RESET     0x10
#define  INTERRUPT_ENABLE   0x08
#define  SINGLE_CHAN        0x00
#define  SEQUENTIAL_CHAN    0x20
#define  RANDOM_CHAN        0x40
#define  EXTERNAL_TRIGGER   0x60
#define  FAIL_LED_ON        0x00
#define  FAIL_LED_OFF       0x01
#define  PASS_LED_ON        0x02
#define  PASS_LED_OFF       0x00
#define  CHAN_0             0x00
#define  CHAN_GAIN_1        0x00
#define  BUSY               0x80
#define  REQUEST_LEVEL_4    0x04

#define  VME_INT_VECTOR     0x84



/* memory structure of the XyCom 560 Interface */

struct aiXY560{
    struct identification {
        unsigned char reserved1;
        unsigned char data;
    } id[32];
    unsigned char reserved2[65];
    unsigned char csr;
    unsigned char reserved3;
    unsigned char ivr;
    unsigned char reserved4;
    unsigned char cgr;
    unsigned short dat;
};

long	Xy560_io_report();
long	Xy560_init();
int	Xy560_interrupt();

struct {
        long    	number;
        DRVSUPFUN	report;
        DRVSUPFUN       init;
} drvXy560={
        2,
        Xy560_io_report,
        Xy560_init};

LOCAL
unsigned short	**pai_Xy560;

LOCAL
char *Xy560_addr;

static IOSCANPVT *paioscanpvt;

int global;


/*
 * Xy560_init   x
 *
 * intialize the Xy560 board 
 */
long Xy560_init()
{
	register unsigned short **pcards_present;
	register unsigned short *base_addr;  
	short			shval;
        int                     status;
	register struct aiXY560 *pcard;
	register short		i;
	register struct aiXY560 *paiXy560;

	base_addr = (unsigned short *)XY560_ADDRESS;

/*	printf ("XY560: %d \n", XY560);
	for (j=0;j<= MAX_AI_TYPES ; j++) printf("%d %x  ",j,ai_addrs[j]);
*/

	printf ("XY560: Base address %hx \n",base_addr);

	pai_Xy560 = (unsigned short  **)
		calloc(MAX_AI_XY560_CARDS, sizeof(struct aiXY560));
	if(!pai_Xy560){
		return ERROR;
	}


	printf ("XY560: MaxCards %d, MaxChan %d \n",
			MAX_AI_XY560_CARDS, XY560_MAXCHAN);

        /*
         *   Initialization for I/O Event Type.
         */
        paioscanpvt = (IOSCANPVT *)calloc(MAX_AI_XY560_CARDS, sizeof(*paioscanpvt));
        if (!paioscanpvt) {
           return ERROR;
        }
        for (i=0; i<MAX_AI_XY560_CARDS; i++) {
            paioscanpvt[i] = NULL;
            scanIoInit(&paioscanpvt[i]);
        }

	pcards_present = pai_Xy560;

        if ((status = sysBusToLocalAdrs(VME_AM_SUP_SHORT_IO, (char *)base_addr, &Xy560_addr)) != OK){ 
           printf("Addressing error in Xy560 driver\n");
           return ERROR;
        }

	pcard = (struct aiXY560 *)((int)Xy560_addr);

        /* mark each card present into the card present array */
        for (i = 0; i < MAX_AI_XY560_CARDS; i++) {

		printf ("XY560: Checking card %d, pcard 0x%x\n",i,pcard); 

                if (vxMemProbe(pcard,VX_READ,1,&shval) == OK) {
                        intConnect((VME_INT_VECTOR * 4), Xy560_interrupt, i);
	                pai_Xy560[i] = (unsigned short *) pcard;
                        *pcards_present = (unsigned short *)pcard;
                        paiXy560 = (struct aiXY560 *)pai_Xy560[i];
			/* External trigger mode */
                        paiXy560->csr = FAIL_LED_OFF | PASS_LED_ON;
                        paiXy560->csr = paiXy560->csr | INTERRUPT_ENABLE;
                        paiXy560->ivr = VME_INT_VECTOR;
			sysIntEnable(REQUEST_LEVEL_4);
                        paiXy560->csr = paiXy560->csr | EXTERNAL_TRIGGER;
                        paiXy560->cgr = CHAN_GAIN_1 | CHAN_0;

		}
                else{
                        *pcards_present = 0;
                        
                 }

		Xy560_addr = Xy560_addr + (int)0x0400;
		pcard = (struct aiXY560 *)((int)Xy560_addr);
		pcards_present += 1;

        }

        /*
         *   Initializing interrupts
         */
        sysIntEnable(REQUEST_LEVEL_4);

	return OK;
}

/*
 * XY560_driver
 *
 * VME VMIC XY560 Digitizer 
 */
long Xy560_driver(card,chan,pval)
register unsigned short card;
register unsigned short chan;
unsigned short 		*pval;
{
	register struct aiXY560	*paiXy560;

        /* check on the card and channel number as kept in module_types.h */

	if ((paiXy560 = (struct aiXY560 *)pai_Xy560[card]) == 0)
		{
	/*	printf ("XY560: Problem with address: Card %d\n", card); */
		return(-1);
		}
	paiXy560->csr = FAIL_LED_OFF | PASS_LED_ON;
        while ((paiXy560->csr & BUSY) != 0) taskDelay(1);
        paiXy560->csr = paiXy560->csr | RANDOM_CHAN;; 
        paiXy560->cgr = CHAN_GAIN_1 | chan;  
        while ((paiXy560->csr & BUSY) != 0) taskDelay(1);

        *pval = paiXy560->dat & 0x0fff; 
	/*

	printf("chan = %d, pval = 0x%x, addrs = 0x%x\n", chan, *pval,paiXy560);
		*/
        paiXy560->csr = paiXy560->csr | INTERRUPT_ENABLE;
        paiXy560->csr = paiXy560->csr | EXTERNAL_TRIGGER;
        paiXy560->cgr = CHAN_GAIN_1 | CHAN_0; 
	paiXy560->csr = FAIL_LED_OFF | PASS_LED_ON;

	return (0);
}


/*
 * Xy560_interrupt
 *
 * VME Xy560 Digitizer Interrupt handler 
 */
int Xy560_interrupt(i)
short i;
{
	register struct aiXY560	*paiXy560;

	if ((paiXy560 = (struct aiXY560 *)pai_Xy560[i]) == 0)
		return(-1);

        global = paiXy560->dat; 
        scanIoRequest(paioscanpvt[i]);
	return (0);
}


/*
 * Xy560_io_report
 *
 * VME Xy560 Digitizer 
 */

long Xy560_io_report(level)
short int level;
 {
    register int i, j;
    unsigned short value;
  
    for (i = 0; i < MAX_AI_XY560_CARDS; i++){
      if (pai_Xy560[i]){   
        printf("AI: Xy560:    card %d\n",i);
          if(level >0){
            for (j=0; j<ai_num_channels[i]; j++) {
              Xy560_driver(i,j,&value);
              printf("channel %d = %x\n", j, value);
            }
          }
          else 
            printf("\n");
      }
    }
	return OK;
 }
                   

long Xy560_getioscanpvt(card,scanpvt)
unsigned short card;
IOSCANPVT *scanpvt;
{
   if ((card <= (unsigned short) MAX_AI_XY560_CARDS) && paioscanpvt[card])
      *scanpvt = paioscanpvt[card];
   return 0;
}
