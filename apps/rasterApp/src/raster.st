/******************************************************************************** 
 *										*
 *			    MAGNET CONTROLS SOFTWARE				*
 *										*	
 *		           Hall B Beam Raster Controller 				*
 *										*
 ********************************************************************************/


program rastB

option +c;     /* wait for all channels to connect */

%%#include <math.h>

/**********************/
/* Inputs to Sequence */
/**********************/

double READDELAY;			/* READ DELAY */
assign READDELAY to "RASTREADDELAY";
monitor READDELAY;

int RASTRESET;				/* Reset BSC */
assign RASTRESET to "RASTRESET";
monitor RASTRESET;

double SETPATSIZEX;			/* Set Pattern Size X */
assign SETPATSIZEX to "RASTSETPATTERNX";
monitor SETPATSIZEX;
double LSETPATSIZEX;

double SETPATSIZEY;			/* Set Pattern Size Y */
assign SETPATSIZEY to "RASTSETPATTERNY";
monitor SETPATSIZEY;
double LSETPATSIZEY;

double SETXOFFSET;			/* Set x offset */
assign SETXOFFSET to "RASTSETXOFFSET";
monitor SETXOFFSET;
double LSETXOFFSET;

double SETYOFFSET;			/* Set y offset */
assign SETYOFFSET to "RASTSETYOFFSET";
monitor SETYOFFSET;
double LSETYOFFSET;

int SETCYCLETIME;			/* Set Cycle Time */
assign SETCYCLETIME to "RASTSETCYCLETIME";
monitor SETCYCLETIME;
double LSETCYCLETIME;

int SETFEEDBACK;			/* Set Feedback on(1)/off(0) */
assign SETFEEDBACK to "RASTSETFEEDBACK";
monitor SETFEEDBACK;
double LSETFEEDBACK;

int ENABLECHANGES;			/* device to disable serial writes */
assign ENABLECHANGES to "RASTENABLECHANGES";
monitor ENABLECHANGES;


int SETFCUPGAIN;
assign SETFCUPGAIN to "RASTSETFCUPGAIN";
monitor SETFCUPGAIN;
double LSETFCUPGAIN;

int SETSYNC;
assign SETSYNC to "RASTSETSYNC";
monitor SETSYNC;
double LSETSYNC;

int SETTIMEOUT;				/* Set Timeout 30(0),60(1),90(2) */
assign SETTIMEOUT to "RASTSETTIMEOUT";
monitor SETTIMEOUT;
double LSETTIMEOUT;

int SETRUNSTATUS;			/* Set Run Status on(1)/off(0) */
assign SETRUNSTATUS to "RASTSETRUNSTATUS";
monitor SETRUNSTATUS;
double LSETRUNSTATUS;



/**********************/
/* Output to Sequence */
/**********************/

double PATSIZEX;			/* Read Pattern Size X */
assign PATSIZEX to "RASTPATSIZEX";
monitor PATSIZEX;

double PATSIZEY;			/* Read Pattern Size Y */
assign PATSIZEY to "RASTPATSIZEY";
monitor PATSIZEY;

double XOFFSET;				/* Read XOFFSET */
assign XOFFSET to "RASTXOFFSET";
monitor XOFFSET;

double YOFFSET;				/* Read YOFFSET */
assign YOFFSET to "RASTYOFFSET";
monitor YOFFSET;

int CYCLETIME;				/* Read CYCLETIME */
assign CYCLETIME to "RASTCYCLETIME";
monitor CYCLETIME;

int TIMEOUTSET;				/* Read TIMEOUTSET */
assign TIMEOUTSET to "RASTTIMEOUTSET";
monitor TIMEOUTSET;

int FEEDBACKSET;			/* Read FEEDBACKSET */
assign FEEDBACKSET to "RASTFEEDBACKSET";
monitor FEEDBACKSET;

int RUNSTATUS;				/* Read RUNSTATUS */
assign RUNSTATUS to "RASTRUNSTATUS";
monitor RUNSTATUS;

int READSTATUS;				/* Read READSTATUS */
assign READSTATUS to "RASTREADSTATUS";
monitor READSTATUS;

int FCUPGAIN;				/* Read FCUPGAIN */
assign FCUPGAIN to "RASTFCUPGAIN";
monitor FCUPGAIN;

int RASTSYNC;				/* Read SYNC flag */
assign RASTSYNC to "RASTSYNC";
monitor RASTSYNC;

int EXTINHIBIT;				/* Read EXTINHIBIT */
assign EXTINHIBIT to "RASTEXTINHIBIT";
monitor EXTINHIBIT;

int BEAMSTATUS;				/* Read BEAMSTATUS */
assign BEAMSTATUS to "RASTBEAMSTATUS";
monitor BEAMSTATUS;

string RASTSTATUS;                  /* Rast Status */
assign RASTSTATUS to "RASTSTATUS";

/*****************/
/* String Macros */
/*****************/


#define STATUS(ss)    sprintf(RASTSTATUS,"%s",(ss)); \
		      pvPut(RASTSTATUS);


/* Command Defines */

#include "rast.h"

%% extern int bscinit(void);                      /* Intialize Serial Port */
%% extern int bsc_set(int, int, int);             /* Bsc Set */
%% extern int bsc_read(int, int *);               /* Bsc Read */
%% extern int getbits(unsigned x, int p, int n);  /* bit unpacker  */
%% extern int setbits(unsigned x, int p, int n, unsigned y);  /* bit packer  */

int    tempval = 0;
int    temp_int = 0;
short  tempword = 0;
int status = 0;
unsigned int temp_unsigned;


/*------------------------------------------------------------*/
/*------------------------ Raster Set ------------------------*/
/*------------------------------------------------------------*/

ss rastBset {

    /*------- Init Hall B Beam Scan Controller  --------------*/

    state init {

	/*-------------------*/
	/* Init Power Supply */
	/*-------------------*/

	when (1) 
	{
%%		bscinit();
/*
 %%		bsc_set(SET_RESET,0,0); 
*/
		STATUS("Init BSC");
		LSETPATSIZEX = SETPATSIZEX = 1000;
		pvPut(SETPATSIZEX);
		LSETPATSIZEY = SETPATSIZEY = 1000;
		pvPut(SETPATSIZEY);
		/* Reset X and Y offsets to 0 */
		LSETXOFFSET = SETXOFFSET = 0.0;
		pvPut(SETXOFFSET);
		LSETYOFFSET = SETYOFFSET = 0.0;
		pvPut(SETYOFFSET);
		/* Reset Cycle Time */
		LSETCYCLETIME = SETCYCLETIME = 5.0;
		pvPut(SETCYCLETIME);
		/* Reset FCup Gain */
		LSETFCUPGAIN = SETFCUPGAIN = 1;
		pvPut(SETFCUPGAIN);
		/* Reset beam SYNC On */
		LSETSYNC = SETSYNC = 0;
		pvPut(SETSYNC);
		/* Reset Feedback On */
		LSETFEEDBACK = SETFEEDBACK = 0;
		pvPut(SETFEEDBACK);
		/* Reset Timeout */
		LSETTIMEOUT = SETTIMEOUT = 1;
		pvPut(SETTIMEOUT);
		/* Reset Run of Bsc ON */
		LSETRUNSTATUS = SETRUNSTATUS = 1;
		pvPut(SETRUNSTATUS);
	} state set
    }

    /*---------------------- State Set BSC  ----------------------*/

    state set {

	/*-------*/
	/* RESET */
	/*-------*/

	when (RASTRESET) 
	{
%%		bsc_set(SET_RESET,0,0);

		/* Reset Pattern Size for X and Y to 0 */
		LSETPATSIZEX = SETPATSIZEX = 0;
		pvPut(SETPATSIZEX);
		LSETPATSIZEY = SETPATSIZEY = 0;
		pvPut(SETPATSIZEY);

		/* Reset X and Y offsets to 0 */
		LSETXOFFSET = SETXOFFSET = 0.0;
		pvPut(SETXOFFSET);
		LSETYOFFSET = SETYOFFSET = 0.0;
		pvPut(SETYOFFSET);

		RASTRESET = 0;
		pvPut(RASTRESET);
	} state set

	/*------------------*/
	/* Set Pattern Size */
	/*------------------*/

	when ((SETPATSIZEX != LSETPATSIZEX) && 
              (SETPATSIZEY != LSETPATSIZEY) &&
              (ENABLECHANGES))	{
		LSETPATSIZEX = SETPATSIZEX;
		LSETPATSIZEY = SETPATSIZEY;
		pvPut(SETPATSIZEX);
		pvPut(SETPATSIZEY);
%%		bsc_set(SET_SIZE_XY, (int) SETPATSIZEX, SETPATSIZEY);
		STATUS("Set X and Y Amplitude");
	} state set

	when ((SETPATSIZEX != LSETPATSIZEX) &&
              (SETPATSIZEY == LSETPATSIZEY) && 
              (ENABLECHANGES))	{
		LSETPATSIZEX = SETPATSIZEX;
		pvPut(SETPATSIZEX);
%%		bsc_set(SET_SIZE_X, (int) SETPATSIZEX, 0);
		STATUS("Set X Amplitude");
	} state set

	when ((SETPATSIZEY != LSETPATSIZEY) && 
              (SETPATSIZEX == LSETPATSIZEX) && 
              (ENABLECHANGES))	{
		LSETPATSIZEY = SETPATSIZEY;
		pvPut(SETPATSIZEY);
%%		bsc_set(SET_SIZE_Y, (int) SETPATSIZEY,0);
		STATUS("Set Y Amplitude");
	} state set
	/*---------------------*/
	/* Set X and Y Offsets */
	/*---------------------*/

           /*   simulataneous X Y offsets broken in hardware   */
/*
	when ((SETXOFFSET != LSETXOFFSET) && 
              (SETYOFFSET != LSETYOFFSET) &&
              (ENABLECHANGES)) 	{
		pvPut(SETXOFFSET);
		pvPut(SETYOFFSET);
%%	        bsc_set(SET_OFFSET_XY, (int) SETXOFFSET,SETYOFFSET);
	        LSETXOFFSET = SETXOFFSET;
	        LSETYOFFSET = SETYOFFSET;
	        STATUS("Set XY offset");
	} state set
*/
	when ((SETXOFFSET != LSETXOFFSET) && 
/*               (SETYOFFSET == LSETYOFFSET) &&    */
              (ENABLECHANGES)) 	{
		pvPut(SETXOFFSET);
%%	        bsc_set(SET_OFFSET_X, (int) SETXOFFSET,0);
	        LSETXOFFSET = SETXOFFSET;
	        STATUS("Set X offset");
	} state set

	when ((SETYOFFSET != LSETYOFFSET) && 
/*              (SETXOFFSET == LSETXOFFSET) &&  */
              (ENABLECHANGES) && delay(2)) 	{
		pvPut(SETYOFFSET);
%%	        bsc_set(SET_OFFSET_Y, (int) SETYOFFSET,0);
	        LSETYOFFSET = SETYOFFSET;
	        STATUS("Set Y offset");
	} state set

	/*----------------*/
	/* Set Cycle Time */
	/*----------------*/

	when (SETCYCLETIME != LSETCYCLETIME) 
	{
		if (SETCYCLETIME > 10) {
			SETCYCLETIME = 10;
		}
		else if (SETCYCLETIME < 1) {
			SETCYCLETIME = 1;
		}
		pvPut(SETCYCLETIME);
%%        	bsc_set(SET_CYCLETIME, (int) SETCYCLETIME,0);
		LSETCYCLETIME = SETCYCLETIME;
		STATUS("Set Cycle Time");
	} state set


	/*------------------------------------------------------*/
	/* Set Feedback, Timeout, Fcupgain, sync and Run Status */
	/*------------------------------------------------------*/

	when (((SETFEEDBACK != LSETFEEDBACK) || (SETTIMEOUT != LSETTIMEOUT) || 
	       (SETRUNSTATUS != LSETRUNSTATUS) || (SETFCUPGAIN != LSETFCUPGAIN) ||
               (SETSYNC != LSETSYNC))) 
	{
		if (SETFEEDBACK != LSETFEEDBACK) {
			STATUS("Set Feedback");
		}
		else if (SETTIMEOUT != LSETTIMEOUT) {
			STATUS("Set Timeout");
		}
		else if (SETFCUPGAIN != LSETFCUPGAIN) {
			STATUS("Set Fcup Gain");
		}
		else if (SETSYNC != LSETSYNC) {
			STATUS("Set Sync");
		}
		else if (SETRUNSTATUS != LSETRUNSTATUS) {
			STATUS("Set Run Status");
		}
		LSETFEEDBACK = SETFEEDBACK;
		LSETTIMEOUT = SETTIMEOUT;
		LSETRUNSTATUS = SETRUNSTATUS;
                LSETFCUPGAIN = SETFCUPGAIN;
                LSETSYNC = SETSYNC;
	        temp_int = setbits(temp_int,6,1,SETFCUPGAIN);
	        temp_int = setbits(temp_int,5,1,SETFEEDBACK);
	        temp_int = setbits(temp_int,4,2,SETTIMEOUT);
	        temp_int = setbits(temp_int,2,1,1);
	        temp_int = setbits(temp_int,1,1,SETSYNC);
	        temp_int = setbits(temp_int,0,1,SETRUNSTATUS);
/*                printf("rast.st::rast_set  Setting byteword %i\n", temp_int); */
%%		bsc_set(SET_BYTEWORD,temp_int,0);
	} state set


    }
}


/*----------------------------------------------------------------------*/
/*------------------- Read Beam Scan Controller  -----------------------*/
/*----------------------------------------------------------------------*/


ss rastBread {

    state rastread {
	
	when(delay(READDELAY))
	{
                READSTATUS=0;
                pvPut(READSTATUS);                
		if ((status = bsc_read(READ_SIZE_X,&tempval)) == SUCCESS) {
			PATSIZEX = tempval;
			pvPut(PATSIZEX);
		}
		if ((status = bsc_read(READ_SIZE_Y,&tempval)) == SUCCESS) {
			PATSIZEY = tempval;
			pvPut(PATSIZEY);
		}
		if ((status = bsc_read(READ_OFFSET_X,&tempval)) == SUCCESS) { 
			XOFFSET = tempval;
			pvPut(XOFFSET);
		}
		if ((status = bsc_read(READ_OFFSET_Y,&tempval)) == SUCCESS) { 
			YOFFSET = tempval;
			pvPut(YOFFSET);
		}
		if ((status = bsc_read(READ_CYCLETIME,&tempval)) == SUCCESS) {
			CYCLETIME = tempval;
			pvPut(CYCLETIME);
		}
		if ((status = bsc_read(READ_BYTEWORD,&tempval)) == SUCCESS) { 
			temp_unsigned = tempval;
/*	                printf("RSE STATUS word: %u\n",temp_unsigned); */
			tempword = getbits(temp_unsigned,0,1);
			if (tempword == 0) {
			        RASTSYNC = OFF;
			} else {
				RASTSYNC = ON;
			}
			pvPut(RASTSYNC);

			tempword = getbits(temp_unsigned,3,2);
			if (tempword == 0) {
				TIMEOUTSET = 30;
			}
			else if (tempword == 1) {
				TIMEOUTSET = 60;
			}
			else if (tempword == 2) {
				TIMEOUTSET = 90;
			}
			pvPut(TIMEOUTSET);
			tempword = getbits(temp_unsigned,4,1);
			if (tempword == 0) {
				FEEDBACKSET = OFF;
			}
			else {
				FEEDBACKSET = ON;
			}
			pvPut(FEEDBACKSET);
			tempword = getbits(temp_unsigned,5,1);
			if (tempword == 0) {
				FCUPGAIN = LOW;
			}
			else {
				FCUPGAIN = HIGH;
			}
			pvPut(FCUPGAIN);

	                READSTATUS=1;
                        pvPut(READSTATUS);
		} else {
	          READSTATUS=0;
                  pvPut(READSTATUS);
                }
		if ((status = bsc_read(READ_STATUS,&tempval)) == SUCCESS) { 
			temp_unsigned = tempval;
			tempword = getbits(temp_unsigned,0,1);
/*	                printf("RST STATUS word: %u\n",temp_unsigned); */
			if (tempword == 0) {
				RUNSTATUS = OFF;
			}
			else {
				RUNSTATUS = ON;
			}
			pvPut(RUNSTATUS);
			tempword = getbits(temp_unsigned,1,1);
			if (tempword == 0) {
				EXTINHIBIT = ON;
			}
			else {
				EXTINHIBIT = OFF;
			}
			pvPut(EXTINHIBIT);
			tempword = getbits(temp_unsigned,2,1);
			if (tempword == 0) {
				BEAMSTATUS = OFF;
			}
			else {
				BEAMSTATUS = ON;
			}
			pvPut(BEAMSTATUS);
	                READSTATUS=1;
                        pvPut(READSTATUS);
		} else {
	                READSTATUS=0;
                        pvPut(READSTATUS);                
                }
	} state rastread
    }
}


