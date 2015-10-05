/*-------------------------------------------------------*/
/*              Xycom 240 Driver Support
 *
 * Functions: Driver Support For the Xycom 240 Digital I/O
 *          Card. Initialize, Read, Write. 
 *            
 * Date: April 9, 1996
 * Author: Scott Higgins
 *
 */
/*-------------------------------------------------------*/
/*-------------------------------------------------------*/

#include    <vxWorks.h>
#include    <types.h>
#include    <vme.h>
#include    <cacheLib.h>
#include    <stdioLib.h>
#include    <drvSup.h>
#include    <sysLib.h>
#include    <vxLib.h>


#define BASEADDR1       0xa000
#define BASEADDR2       0xa400
#define CARD_INIT       0x3
#define NO_CARDS        2
#define NO_REGS         10 
#define PORTDIR_REG     8 

int DEBUGXYCOM240M = 0;
int Xycom240M_Initialized = 0;
unsigned long BASEADDR[] = {BASEADDR1,BASEADDR2};
unsigned short *xy240M_shortAdd[NO_CARDS][NO_REGS];


/*---------------------------- Init Xycom 240 --------------------------------*/

int init_Xy240M()
{
    unsigned long reg_addr[] = { 0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D, 0x8E, 0x8F, 0x87, 0x81}; 
    int status, i, j;
    int card_found = 0;
    char testV = 0;
    unsigned long addr;
    char *shortaddr;

    /***************************************************/
    /* Get the access address for all register chunks  */
    /* Tell card we are using short supervisory access */
    /***************************************************/

    for (i = 0; i < NO_CARDS; i++) {
        card_found = 0;
        for (j = 0; j < NO_REGS; j++) {
            addr = BASEADDR[i] + reg_addr[j];
            status = sysBusToLocalAdrs(VME_AM_SUP_SHORT_IO, (char *)addr, &shortaddr);
            if (status != OK) {
                printf("Addressing error in Xycom240M driver Register #%d\n",j);
                Xycom240M_Initialized = 0;
                return ERROR;
            }
            
            xy240M_shortAdd[i][j] = (unsigned short *)shortaddr;
            if (vxMemProbe(shortaddr, VX_READ, 1, &testV) == OK ) {
                if (!card_found) { /* If card had not been previously detected */
                    printf("Xycom 240 card #%d is present\n",i);
                    card_found = 1;
                }
                else if (j == 9) {
                    *xy240M_shortAdd[i][9] = CARD_INIT;
                    if(DEBUGXYCOM240M) {
                        printf("init_Xy240M: Init control register");
                        printf("init_Xy240M: xy240M_shortAdd[%d][9]: %p\n",i,xy240M_shortAdd[i][9]);
                    }
                }
            }
            else if (DEBUGXYCOM240M) {
                printf("Xycom 240 card #%d reg#%d not responding\n",i,j);
            }
        }
    }
    return(0);
}


/*---------------------------- Xycom 240 Config --------------------------------*/

int config_Xy240M(card, val)
register unsigned short card;
int val;
{

    /*******************************/
    /* Set Port Direction Register */
    /*******************************/

    if (!Xycom240M_Initialized)
        return(1);

    *xy240M_shortAdd[card][PORTDIR_REG] = val;   /* implicit casting */

    if(DEBUGXYCOM240M)
        printf("drvXy240M: card = %d *xy240M_shortAdd = %d xy240M_shortAdd = %p\n", 
                card, *xy240M_shortAdd[card][PORTDIR_REG], xy240M_shortAdd[card][PORTDIR_REG]);
    return(0);
}

/*---------------------------- Xycom 240 Write --------------------------------*/

int write_Xy240M(card, port, mask, val)
register unsigned short card;
register unsigned short port;
unsigned long mask;
unsigned long val;
{
    /********************/
    /* Write new output */
    /********************/

    if (val) 
        *xy240M_shortAdd[card][port] |= mask;         /* Set Bit On */
    else
        *xy240M_shortAdd[card][port] &= (~mask & 0xff);   /* Set Bit Off */
        

    if(DEBUGXYCOM240M == 2)
        printf("drvXy240M: card = %d port = %d mask = %lx val= %lu *xy240M_shortAdd = %x xy240M_shortAdd = %p\n", 
                card, port, mask, val, *xy240M_shortAdd[card][port], xy240M_shortAdd[card][port]);

    return(0);
}

/*---------------------------- Xycom 240 Read --------------------------------*/

int read_Xy240M(card, port, mask, val)
register unsigned short card;
register unsigned short port;
unsigned long mask;
unsigned long *val;
{
   unsigned short temp;

    if(DEBUGXYCOM240M == 3)
        printf("drvXy240M: card = %d port = %d mask = %lx val= %lu *xy240M_shortAdd = %x xy240M_shortAdd = %p\n", 
                card, port, mask, *val, *xy240M_shortAdd[card][port], xy240M_shortAdd[card][port]);
        /*cacheInvalidate(DATA_CACHE, (void *)xy240M_shortAdd[card][port], 2);*/
    temp = *xy240M_shortAdd[card][port];
    *val = (unsigned long)((temp & mask) !=0); /* This will force a binary value */
    if(DEBUGXYCOM240M == 3)
        printf("drvXy240M: card = %d port = %d mask = %lx val= %lu *xy240M_shortAdd = %x xy240M_shortAdd = %p\n", 
                card, port, mask, *val, *xy240M_shortAdd[card][port], xy240M_shortAdd[card][port]);
    return(0);
}

