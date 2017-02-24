/* drvV450.c */

/* This code provides EPICS support for the Highlab V450 ADC
 * Customized for Hall B SVT Slow Controls
 *
 * Converted by sergey & peter from VMIVME3122 ADC Driver by Steve Hartman
 *
 * Steve Hartman <hartman@fel.duke.edu>, Duke FEL Laboratory
 * Copyright (c) 2005 Duke University
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

#include <vxWorks.h>
#include <sysLib.h>
#include <vxLib.h>
#include <types.h>
#include <stdioLib.h>
#include <stdlib.h>
#include <vme.h>
#include <epicsVersion.h>
#include <taskLib.h>
#if (EPICS_VERSION==3) && (EPICS_REVISION>=14)
	#include <epicsExport.h>
#endif

#include <dbDefs.h>
#include <drvSup.h>

#include <drvV450.h>

#define GAIN	GAIN_1X
#define SCAN	AUTO_SCAN 

#define NUM_CHANNELS 16 /* number of channels in board */

int DEBUGV450;

/* these can be changed in st.cmd before iocInit if necessary */
unsigned int numV450cards = 11;       /* number of cards in SVT crate - Changed from 9 to 11 on 6-20-2014*/
unsigned int v450_base = 0xC000;    /* base address of card 0 - Addresses increment by 0x1000 */

long v450_init(void);
long v450_report(int);

struct {
  long	number; /* the number of following elements */
	DRVSUPFUN	report;
	DRVSUPFUN	init;
} drvV450={
	2,
	v450_report,
	v450_init};

#if (EPICS_VERSION==3) && (EPICS_REVISION>=14)
	epicsExportAddress(drvet,drvV450);
#endif

static int v450_addr;
static unsigned short **pai_v450;

/* initialize the v450 analog input card */
long
v450_init(void)
{
  unsigned short **boards_present;
  short shval;
  long status;
  int i;
  v450 *board;
  
  

  pai_v450 = (unsigned short **)calloc(numV450cards,sizeof(*pai_v450));
  if(!pai_v450)
  {
	printf("V450Config: failed to allocate space\n");
	return(ERROR);
  }

  boards_present = pai_v450;

  if ( (status = sysBusToLocalAdrs(VME_AM_STD_SUP_DATA,(char *)v450_base,(char **)&v450_addr)) != OK)
  {
	printf("Addressing error in V450Config\n");
	return(ERROR);
  }
  else
  {
    printf("Board address = 0x%08x\n",(int)v450_addr);
  }

  board = (( v450 *)((int)v450_addr));

  for (i=0; i<numV450cards; i++, board++, boards_present++)
  {
    printf("[%d] probing board at 0x%08x ---> ",i,(int)board);

	if (vxMemProbe((char *)board,VX_READ,sizeof(short),(char *)&shval) == OK)
    {
	  *boards_present = (unsigned short *)board;

      /* board initialization */     
      board->CTL0 = 0x100A;  /* set Channel 0 to +/-12V @ 4.17 samples /Sec */
      board->CTL1 = 0x100A;  /* set Channel 1 to +/-12V @ 4.17 samples /Sec */
      board->CTL2 = 0x100A;  /* set Channel 2 to +/-12V @ 4.17 samples /Sec */
      board->CTL3 = 0x100A;  /* set Channel 3 to +/-12V @ 4.17 samples /Sec */
      board->CTL4 = 0x100A;  /* set Channel 4 to +/-12V @ 4.17 samples /Sec */
      board->CTL5 = 0x100A;  /* set Channel 5 to +/-12V @ 4.17 samples /Sec */
      board->CTL6 = 0x100A;  /* set Channel 6 to +/-12V @ 4.17 samples /Sec */
      board->CTL7 = 0x100A;  /* set Channel 7 to +/-12V @ 4.17 samples /Sec */
      board->CTL8 = 0x100A;  /* set Channel 8 to +/-12V @ 4.17 samples /Sec */
      board->CTL9 = 0x100A;  /* set Channel 9 to +/-12V @ 4.17 samples /Sec */
      board->CTL10 = 0x100A;  /* set Channel 10 to +/-12V @ 4.17 samples /Sec */
      board->CTL11 = 0x100A;  /* set Channel 11 to +/-12V @ 4.17 samples /Sec */
      board->CTL12 = 0x100A;  /* set Channel 12 to +/-12V @ 4.17 samples /Sec */
      board->CTL13 = 0x100A;  /* set Channel 13 to +/-12V @ 4.17 samples /Sec */
      board->CTL14 = 0x100A;  /* set Channel 14 to +/-12V @ 4.17 samples /Sec */
      board->CTL15 = 0x100A;  /* set Channel 15 to +/-12V @ 4.17 samples /Sec */
      
      board->rtda = rtd_on;   	/* Enable RTD A @ 100 ohm platinum, ISO 385 curve */
      board->rtdb = rtd_on;	/* Enable RTD B @ 100 ohm platinum, ISO 385 curve */
      board->rtdc = rtd_on;	/* Enable RTD C @ 100 ohm platinum, ISO 385 curve */
      board->rtdd = rtd_on;	/* Enable RTD D @ 100 ohm platinum, ISO 385 curve */
      
      taskDelay(1);

			   
      printf("memprobe found a V450 board at this address\n");
      
	}
    else
	{
      printf("Error in memprobe - No V450 found at this address\n");
	}
	
  }/*end of board initialization */
   
  return(OK);
}



int
v450_read(unsigned short card, unsigned int signal, unsigned long *pval) 
/* For SVT slow Controls - signals 0-20 are valid and vme cards 0-8 */
/* signals = (0-15) ADC-HFCB temps - (Ch16=RTDA, Ch17=RTDB, Ch18=RTDC,Ch19=RTDD,Ch20=TMPR) */
{
  float vout;
  float tempc;
  float tempf;
  float hfcbtemp;
  register v450 *paiVMI;
  
  
  if (( paiVMI = ( v450 *)pai_v450[card]) == 0)
  {
    printf("v450_read error. \n"); /* can't read from module */
    return(ERROR);
  }
 
 if (signal <= 15 )  /* if signal name is 0 to 15, we're reading ADC channels (0-15) */
 {   
  /* for full 32bit resolution - correct register locking, read high 2 bytes, then low 2 bytes (32 bits)*/
  *pval = (paiVMI->data[signal*2])<<16;   /* high bytes */  
  *pval += paiVMI->data[signal*2+1];      /* low bytes */
  
  /* For debug & Demo, convert and print vout */
 vout = (*pval) * 12.5 / 2147483648;   /* (32 bits) voltage range +/-12.5 V  / 2 power 31 (page 14 of V450 manual) */
 hfcbtemp = ((vout*1000.0)-2100)/-10.9;
 if(DEBUGV450)printf(" Card=%2d - ADC Channel=%2d - vout=%.3fV - HFCB Temp= %.2fC\n",card,signal,vout, hfcbtemp);
  
 } 
   
   if (signal <= 16 <= 20 )  /* if signal name is 16 to 20, we're reading RTD Temps (Ch16=RTDA, Ch17=RTDB, Ch18=RTDC,Ch19=RTDD,Ch20=TMPR)  */
   {
     
      switch (signal)  {

      
	case 16: /*  Read RTD A  */	  
	*pval = paiVMI->tmpa;
	tempc = (*pval) / 16.0;    /* temp from VME board is in degrees C x 16  */
	tempf = ((9.0/5.0)*tempc)+32.0;
	//printf(" Card=%2d - RTD A = %.2fC / %.2fF \n",card,tempc,tempf);
	break;
              
	case 17:  /*  Read RTD B  */
	*pval = paiVMI->tmpb;
	tempc = (*pval) / 16.0;   /* temp from VME board is in degrees C x 16  */
	tempf = ((9.0/5.0)*tempc)+32.0;
	//printf(" Card=%2d - RTD B = %.2fC / %.2fF \n",card,tempc,tempf);
	break;
	       
	case 18: /*  Read RTD C  */
	*pval = paiVMI->tmpc;
	tempc = (*pval) / 16.0;  /* temp from VME board is in degrees C x 16  */
	tempf = ((9.0/5.0)*tempc)+32.0;
	//printf(" Card=%2d - RTD C = %.2fC / %.2fF \n",card,tempc,tempf);
	break;
	       
	case 19: /*  Read RTD D  */
	*pval = paiVMI->tmpd;
	tempc = (*pval) / 16.0;  /* temp from VME board is in degrees C x 16  */
	tempf = ((9.0/5.0)*tempc)+32.0;
	//printf(" Card=%2d - RTD D = %.2fC / %.2fF \n",card,tempc,tempf);
	break;
	      
	case 20: /*  Read TMPR - VME Board Temp  */
	*pval = paiVMI->tmpr;
	tempc = (*pval) / 16.0;  /* temp from VME board is in degrees C x 16  */
	tempf = ((9.0/5.0)*tempc)+32.0;
	//printf(" Card=%2d - VME Board Temp = %.2fC / %.2fF \n",card,tempc,tempf);
	break;
	
      }
     
   }
   if (signal == 36 )  /* Special designator to read the board serial no.)  */
   {
     *pval = paiVMI->serial;
   }
   
   
  return(OK);
}


long
v450_report(int level)
{
  int i;
  v450 *paiVMI;

  for (i = 0; i < numV450cards; i++)
  {
	if (pai_v450[i])
    {
	  printf("  ai: V450 card number %d is present\n",i);
	  if ( level > 0 )
      {
		paiVMI = (v450 *)pai_v450[i];
			printf("Address = %p, Board serial# = %2d, ", paiVMI,paiVMI->serial);
        if( level > 1 ) printf(" VXI mfr ID = %x, Mod type = %d, ", paiVMI->vximfr, paiVMI->vxitype);
        if( level > 1 ) printf(" ROM ID = %d, ROM Rev = %c, ", paiVMI->romid, paiVMI->romrev);
			printf("\n   tmpa = %d, tmpb = %d, tmpc = %d, tmpd = %d, tmpr = %d \n\n",
			       paiVMI->tmpa,paiVMI->tmpb,paiVMI->tmpc,paiVMI->tmpd,paiVMI->tmpr);
	  }

	}
  }

  return(OK);
}
