/****************************************************************************
 * Program   : drvbrm13.c
 * Programmer: Mike Johnson, David Wetherholt
 * Modified  : 2014 Feb 4
 ****************************************************************************/
/* This file contains the driver functions for the JLAB Beam Raster */
/* Monitor Module.  This module has 12 1-byte registers that are    */
/* shared for writing and reading.                                  */
#include <vxWorks.h>
#include <types.h>
#include <vme.h>
#include <vxLib.h>
#include <cacheLib.h>
#include <stdioLib.h>
#include <drvSup.h>
#include <dbDefs.h>
#include <link.h>
#include <epicsExport.h>

STATUS sysBusToLocalAdrs();
/****************************************************************************/
/* There can be two Beam Raster Monitor Modules in each VME crate           */
/****************************************************************************/
#define BASEADDR1        0x4500  /*** Card 0 */
#define BASEADDR2        0x4600  /*** Card 1 */
#define REGSOFF          20
#define REGS	         40

int DEBUGBRM13 = 0;
unsigned short *brm13_shortAdd[REGS];

/***************************************************************************
 * Init brm13
 ***************************************************************************/
int init_brm13() {
   long mbbid_addrs[] = {BASEADDR1+0x00, BASEADDR1+0x02, BASEADDR1+0x04,
                         BASEADDR1+0x06, BASEADDR1+0x08, BASEADDR1+0x0A,
                         BASEADDR1+0x0C, BASEADDR1+0x0E, 
                         BASEADDR1+0x10, BASEADDR1+0x12,
                         BASEADDR1+0x14, BASEADDR1+0x16, BASEADDR1+0x18,
                         BASEADDR1+0x1A, BASEADDR1+0x1C, BASEADDR1+0x1E,
                         BASEADDR1+0x20, BASEADDR1+0x22, BASEADDR1+0x24,
                         BASEADDR1+0x26, 
                         BASEADDR2+0x00, BASEADDR2+0x02, BASEADDR2+0x04,
                         BASEADDR2+0x06, BASEADDR2+0x08, BASEADDR2+0x0A,
                         BASEADDR2+0x0C, BASEADDR2+0x0E, 
                         BASEADDR2+0x10, BASEADDR2+0x12,
                         BASEADDR2+0x14, BASEADDR2+0x16, BASEADDR2+0x18,
                         BASEADDR2+0x1A, BASEADDR2+0x1C, BASEADDR2+0x1E,
                         BASEADDR2+0x20, BASEADDR2+0x22, BASEADDR2+0x24,
                         BASEADDR2+0x26};
    int i, status;
    short testR;

    if(DEBUGBRM13) {
      printf("BRM13 working with %d byte registers\n",sizeof(testR));
    }

    for (i=0; i < REGS; i++) {
      status = sysBusToLocalAdrs(VME_AM_SUP_SHORT_IO, mbbid_addrs[i],
        &brm13_shortAdd[i]);
      if (status != OK) return ERROR;

      if(DEBUGBRM13) {
        printf("Probing brm13_shortAdd = %p\n", brm13_shortAdd[i]);
      }

      if(vxMemProbe((char *)(brm13_shortAdd[i]), VX_READ, 2,
		(char *)(&testR)) == OK ) {
        printf("BRM13 is present; brm13_shortAdd = %p\n", brm13_shortAdd[i]);
      }
    }
    return(0);
}

int write_brm13(
/**************************************************************************
 * Write BRM
 **************************************************************************/
  register unsigned short card,
  register short signal,
  unsigned long *pval) {

    if (card == 1) signal += REGSOFF;

    /*** Write new output */
    *brm13_shortAdd[signal] = *pval;   /* implicit casting */
    if(DEBUGBRM13)
      printf("signal=%d pval= %ld *brm13_shortAdd = %d brm13_shortAdd = %p\n",
        signal, *pval, *brm13_shortAdd[signal], brm13_shortAdd[signal]);
    return(0);
}

int read_brm13(
/***************************************************************************
 * Read BRM
 ***************************************************************************/
  register unsigned short card,
  register unsigned short signal,
  unsigned long *pval) {
    unsigned short temp;

    if (card == 1) signal += REGSOFF;

    if(DEBUGBRM13) printf("drv_brm13: signal is %d\n", signal);

    cacheInvalidate(DATA_CACHE, brm13_shortAdd[signal], 1);
    temp = *brm13_shortAdd[signal];
    *pval = (unsigned long)temp;

    if(DEBUGBRM13) printf("drvbrm13: temp is %d\n", temp);
    return(0);
}
