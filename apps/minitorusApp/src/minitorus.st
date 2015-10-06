
/*-------------------------------------------------------*/
/*-------------------------------------------------------*/
/*              Minitorus Power Supply Control
 *
 *
 * Functions:	This sequence will turn on, off, reset,
 *		and monitor the Dynapower DC PS.  
 *
 *
 * Date:	September 7, 1996
 * Author:	Scott Higgins
 *
 */
/*-------------------------------------------------------*/
/*-------------------------------------------------------*/


program minitoruscontrol ("minitorus=MT")
option +c;               /* Wait for all the channels to connect*/

%%#include <math.h>
%%#include <taskLib.h>
#define NULL 0

/******************************************/
/* Inputs to power supply control control */
/******************************************/

int PSONSET;                     	/* PS on and command (1=ON) (0=OFF) */
assign  PSONSET to "{minitorus}PSONSET";  
monitor PSONSET;

int RESET;                     		/* PS reset command (1=ON) (0=OFF) */
assign RESET to "{minitorus}RESET";  
monitor RESET;

double SETI;                     	/* PS Set Current Value*/
assign SETI to "{minitorus}SETI";  
monitor SETI;
double LSETI;				/* Last Current Setpoint */

int RAMPRATE;                     	/* Ramp Rate 0 - 200 Amps/Sec */
assign RAMPRATE to "{minitorus}RAMPRATE";  
monitor RAMPRATE;

/*************************************/
/* Outputs from Power Supply Control */
/*************************************/

int ALARM;                              /* Mismatch alarm */
assign ALARM to "{minitorus}ALARM";
monitor ALARM;

double IRBCK;				/* Readback current */
assign IRBCK to "{minitorus}IRBCK";
monitor IRBCK;

double ISETRBCK;                         /* Readback set current */
assign ISETRBCK to "{minitorus}ISETRBCK";
monitor ISETRBCK;

double VRBCK;			           /* Voltage Readback */
assign VRBCK to "{minitorus}VRBCK";
monitor VRBCK;

double DACRBCK;                   	/* PS DAC status */
assign DACRBCK to "{minitorus}DACRBCK";  
monitor DACRBCK;

int PSONRBCK;				/* Readback ON command (1=ON) (0=OFF) */
assign PSONRBCK to "{minitorus}PSONRBCK";
monitor PSONRBCK;

int CCMODE;                             /* Computer Control Mode (0=Local) (1=Remote)*/
assign CCMODE to "{minitorus}CCMODE";
monitor CCMODE;

int INHIBIT;                            /* Summary of all Interlocks (0=OK) (1=non OK)*/
assign INHIBIT to "{minitorus}INHIBIT";
monitor INHIBIT;

double INTERLOCKS;                      /* Readback From Hardware */
%% unsigned int INTERLOCK;              /* Readback From Hardware */
assign INTERLOCKS to "{minitorus}INTERLOCKS";
monitor INTERLOCKS;

int IPFAULT;                                /* Input Power Fault (0=OK) (1=non OK)*/
assign IPFAULT to "{minitorus}IPFAULT";
monitor IPFAULT;

int FCFAULT;                                /* Firing Circuit Fault (0=OK) (1=non OK)*/
assign FCFAULT to "{minitorus}FCFAULT";
monitor FCFAULT;

int ZFCTFAULT;                              /* ZFCT Fault (0=OK) (1=non OK)*/
assign ZFCTFAULT to "{minitorus}ZFCTFAULT";
monitor ZFCTFAULT;

int LSODFAULT;                              /* Local Stop/Open Door Fault (0=OK) (1=non OK)*/
assign LSODFAULT to "{minitorus}LSODFAULT";
monitor LSODFAULT;

int OTFAULT;                                /* Xmfr/Thy Overtemp Fault (0=OK) (1=non OK)*/
assign OTFAULT to "{minitorus}OTFAULT";
monitor OTFAULT;

int OCFAULT;                                /* Over Current Fault (0=OK) (1=non OK)*/
assign OCFAULT to "{minitorus}OCFAULT";
monitor OCFAULT;

int OVFAULT;                                /* Over Voltage Fault (0=OK) (1=non OK)*/
assign OVFAULT to "{minitorus}OVFAULT";
monitor OVFAULT;

int GDFAULT;                                /* Ground Fault (0=OK) (1=non OK)*/
assign GDFAULT to "{minitorus}GDFAULT";
monitor GDFAULT;

int PFSHUTDWN;                              /* Power Failure Shutdown (0=OK) (1=non OK)*/
assign PFSHUTDWN to "{minitorus}PFSHUTDWN";
monitor PFSHUTDWN;

int LCWFAULT;                               /* LCW Fault (0=OK) (1=non OK)*/
assign LCWFAULT to "{minitorus}LCWFAULT";
monitor LCWFAULT;

int ESILOCK;                                /* External Safety Interlock (0=OK) (1=non OK)*/
assign ESILOCK to "{minitorus}ESILOCK";
monitor ESILOCK;

int VLWARN;                                 /* Voltage Limit Warning (0=OK) (1=non OK)*/
assign VLWARN to "{minitorus}VLWARN";
monitor VLWARN;

int RESENDCNT;                              /* Number of Times Setpoint is Re-sent */
assign RESENDCNT to "{minitorus}RESENDCNT";
monitor RESENDCNT;

int RDFAILCNT;                                /* Number of Read Fails */
assign RDFAILCNT to "{minitorus}RDFAILCNT";
monitor RDFAILCNT;

int FAILCNT;                                /* Number of Times All Reads Failed */
assign FAILCNT to "{minitorus}FAILCNT";
monitor FAILCNT;

int SERIALSTAT;                             /* Serial Status (0=OK) (1=non OK) */
assign SERIALSTAT to "{minitorus}SERIALSTAT";
monitor SERIALSTAT;

int WAIT;                                   /* Seconds to Wait for Power Supply to Reach Setpoint*/
assign WAIT to "{minitorus}WAIT";
monitor WAIT;

string MSTATUS;                         /* Torus Status Message */
assign MSTATUS to "{minitorus}MSTATUS";

string MSTATE;                          /* Torus State */
assign MSTATE to "{minitorus}MSTATE";

string TSTATUS;                         /* Interlock Trip Status Message */
assign TSTATUS to "{minitorus}TSTATUS";

/*****************/
/* Macro Defines */
/*****************/

int TORUS_STATE_DEBUG = 0;
%%int waitDelay = 7;

#define STATUS(ss)    if (TORUS_STATE_DEBUG) printf("\n%s\n\n",(ss)); \
			 sprintf(MSTATUS,"%s",(ss)); \
			 pvPut(MSTATUS);

#define STATE(ss)    if (TORUS_STATE_DEBUG) printf("\n%s\n\n",(ss)); \
			sprintf(MSTATE,"%s",(ss)); \
			pvPut(MSTATE);

#define TRIPMSG(ss)  if (TORUS_STATE_DEBUG) printf("\n%s\n\n",(ss)); \
		        sprintf(TSTATUS,"%s",(ss)); \
		        pvPut(TSTATUS);

/****************/
/* Mask Defines */
/****************/

#define IPMASK		0x0001  
#define FCMASK		0x0002  
#define ZFCTMASK	0x0004  
#define LSODMASK	0x0008  
#define OTMASK		0x0010  
#define OCMASK		0x0020  
#define OVMASK		0x0040  
#define GDMASK		0x0080  
#define PFSMASK		0x0100  
#define LCWMASK		0x0200  
#define ESIMASK		0x0400  
#define VLWMASK		0x0800  
#define PSMASK		0x1000  
#define CCMASK		0x2000  
#define WRMASK		0x4000  
#define WPMASK		0x8000  

/*******************/
/* Command Defines */
/*******************/

#define POWER_OFF	0
#define POWER_ON	1
#define RESETPS		2
#define SET_IMMEDIATE	3

#define CURRENT		0
#define SETPOINT	1
#define VOLTAGE		2
#define DAC		3
#define INTERLCKS	4

int trd_status;		/* Torus Read Status (0 == SUCCESS) (1 == Fail) */

%%extern int torusinit(void);               /* Intialize Serial Port */
%%extern int torus_set(int, double, int);	/* Minit Torus Set */  
%%extern int torus_read(int, double*);		/* Minit Torus Read */  

/*-----------------------------------------------------------------*/
/*-------------------- Power Supply Sequence ----------------------*/
/*-----------------------------------------------------------------*/

ss control 
{

    /*------------------------- State Init ------------------------*/

    state init 
    { 

	/*-------------------*/
	/* Init Power Supply */
	/*-------------------*/

	when ()		
        {
%%		torusinit();
		RAMPRATE = 10.0;
		pvPut(RAMPRATE);
	} state remote_wait
    }


    /*------------------ Wait For Remote Mode --------------------*/

    state remote_wait
    {

	/*----------------*/
	/* In Remote Mode */
	/*----------------*/

	when (CCMODE)
	{
	   ;
	} state on_or_off

	/*--------------------*/
	/* Not In Remote Mode */
	/*--------------------*/

	when (!CCMODE && delay(2))
	{
		STATUS("NOT IN REMOTE MODE");
        } state remote_wait

    }


    state on_or_off 
    {
       when(delay(2) && PSONRBCK) {
          STATUS("REMOTE MODE PS ON");
	  printf("mini-torus PS initializing...found ON\n");
	  PSONSET = 1;
	  pvPut(PSONSET);
       } state on
       when(delay(2) && !(PSONRBCK)) {
          STATUS("REMOTE MODE PS OFF");
	  printf("mini-torus PS initializing...found OFF\n");
	  PSONSET = 0;
	  pvPut(PSONSET);
       } state off
    }
    /*---------------------- Magnet Off ------------------------*/

    state off 
    { 

	/*--------------------*/
	/* Not In Remote Mode */
	/*--------------------*/

	when (!CCMODE)
	{
		STATUS("NOT IN REMOTE MODE");

        } state remote_wait

 
	/*-------------------------------*/
	/* Turn Supply On if No INHIBITS */
	/*-------------------------------*/
       
	when (PSONSET && !INHIBIT)
	{
		SETI = 0.0;
		pvPut(SETI);
%%		torus_set(SET_IMMEDIATE,SETI,RAMPRATE);
		LSETI = 0.0;
%%		torus_set(RESETPS,NULL,NULL);
%%		torus_set(POWER_ON,NULL,NULL);
		STATUS("Setting PS ON");
	} state wait_on

	/*--------------------------------------*/
	/* Set PSONCMD OFF Because of  INHIBITS */
	/*--------------------------------------*/

	when (PSONSET && INHIBIT)
	{
		STATUS("INHIBIT");
	} state turn_off

	/*------------------------*/
	/* Reset the Power Supply */
	/*------------------------*/
	  
	when (RESET) 
	{
%%		torus_set(RESETPS,NULL,NULL);
	        RESET = 0;
	        pvPut(RESET);
		STATUS("RESETING PS");
	} state off

	/*-----------------------*/
	/* Send Off Again to PS  */
	/* if it didn't turn off */
	/*-----------------------*/

	when (((IRBCK > 1.0) || (PSONRBCK)) && delay(2))
	{
		SETI = 0.0;
		pvPut(SETI);
%%		torus_set(SET_IMMEDIATE,SETI,10.0);
		LSETI = 0.0;
%%		torus_set(POWER_OFF,NULL,NULL);
		PSONSET = 0;
		pvPut(PSONSET);
		STATUS("Setting PS OFF");
	} state off

    }

    /*-------------------- Wait For PS To Turn On ------------------------*/

    state wait_on
    {

	/*----------*/
	/* PS IS ON */
	/*----------*/

	when(PSONRBCK)
	{
		STATUS("PS ON");
		SETI = 0.0;
		pvPut(SETI);
%%		torus_set(SET_IMMEDIATE,SETI,RAMPRATE);
		SETI = 0.0;
		pvPut(SETI);
%%		torus_set(SET_IMMEDIATE,SETI,RAMPRATE);
		SETI = 0.0;
		pvPut(SETI);
%%		torus_set(SET_IMMEDIATE,SETI,RAMPRATE);

	} state on

	/*-----------------------------*/
	/* Power Supply Not Turning On */
	/*-----------------------------*/

	when (!PSONRBCK && delay(10))
	{
		SETI = 0.0;
		pvPut(SETI);
%%		torus_set(SET_IMMEDIATE,SETI,RAMPRATE);
		LSETI = 0.0;
%%		torus_set(POWER_OFF,NULL,NULL);
		PSONSET = 0;
		pvPut(PSONSET);
		STATUS("PS Would Not Come On");
	} state off

    }


    /*---------------------- Power Supply On --------------------------*/

    state on
    {

	/*--------------------*/
	/* Not In Remote Mode */
	/*--------------------*/

	when (!CCMODE)
	{
                printf("mini-t: on state failed CCMODE\n");
		STATUS("NOT IN REMOTE MODE");

        } state remote_wait

	/*----------------------------*/
	/* User Requested Off or Trip */	
	/*----------------------------*/

	when(INHIBIT || !PSONSET || !PSONRBCK)
	{
		STATUS("Turn PS OFF");
	} state turn_off

	/*-----------------------------------*/
	/* Inhibit Reseting the Power Supply */
	/*-----------------------------------*/
	  
	when (RESET) 
	{
	        RESET = 0;
	        pvPut(RESET);
		STATUS("No Reset When PS ON");
	} state on


	/*-------------*/
	/* Set Current */
	/*-------------*/

	when (SETI != LSETI)
	{
%%		torus_set(SET_IMMEDIATE,SETI,RAMPRATE);
		RESENDCNT = 0;
		STATUS("New Setpoint");
	} state wait_setcurrent

	/*-----------*/
	/* Set Alarm */
	/*-----------*/

        when (delay(2)) 
        {

		if (((fabs(SETI - (IRBCK + 5.0))) > (0.03 * SETI))
		     && (IRBCK > 1.0)) {
			ALARM = 1;
			pvPut(ALARM);
		}
		else {
			ALARM = 0;
			pvPut(ALARM);
		}
        } state on

    }

    /*---------------- Wait for Setpoint To get To Hardware ----------------------*/

    state wait_setcurrent
    {

	/*----------------------------*/
	/* User Requested Off or Trip */	
	/*----------------------------*/

	when(INHIBIT || !PSONSET || !PSONRBCK)
	{
		STATUS("Turn PS OFF");
	} state turn_off

	/*------------------*/
	/* Resent Maxed OUT */
	/*------------------*/

	when (RESENDCNT == 4) 
	{
		SETI = LSETI;
		pvPut(SETI);
		STATUS("Setpoint Not Going to PS");
	} state on

	/*-----------------------------------------*/
	/* If SetPoint didnt reach hardware Resend */
	/*-----------------------------------------*/

	when ((((fabs(SETI - ISETRBCK)) > 0.5) || ((fabs(SETI - DACRBCK)) > 0.5)) 
                && delay(3))
	{
%%		torus_set(SET_IMMEDIATE,SETI,RAMPRATE);
		RESENDCNT++;
		pvPut(RESENDCNT);
		STATUS("Resend Setpoint");
	} state wait_setcurrent

	/*-------------------------------------------------*/
	/* If SetPoint reached hardware Wait For Readback  */
	/*-------------------------------------------------*/

	when (((fabs(SETI - ISETRBCK)) < 0.5) || ((fabs(SETI - DACRBCK)) < 0.5))
	{
		STATUS("Wait Current");
		WAIT = fabs(SETI - LSETI)/RAMPRATE + 10.0;
		pvPut(WAIT);
	} state wait_current
    }


    /*-------------------- Wait for Setpoint = Readback --------------------------*/

    state wait_current
    {

	/*----------------------------*/
	/* User Requested Off or Trip */	
	/*----------------------------*/

	when(INHIBIT || !PSONSET || !PSONRBCK)
	{
		STATUS("Turn PS OFF");
	} state turn_off

	/*------------*/
	/* Magnet Set */
	/*------------*/

        when (((fabs(SETI - (IRBCK + 5.0))) < (0.03 * SETI)) ||
		((IRBCK < 2.0) && (SETI < 2.0))) 
        {
		LSETI = SETI;
		STATUS("Magnet Set");
        } state on


	/*--------------------------------*/
	/* Readback Not Reaching Setpoint */
	/*--------------------------------*/

	when (delay(WAIT))
	{
		LSETI = SETI;
		STATUS("Readback Not Reaching Setpoint");
	} state on

    }

    /*-------------------- State Turn Off --------------------------*/

    state turn_off
    {

	when(1)
	{

		if (!PSONSET) { 
			STATUS("User Request PS OFF");
		}
		else if (IPFAULT) { 
			STATUS("Input Power Fault");
		}
		else if (FCFAULT) {
			STATUS("Firing Circuit Fault");
		}
		else if (ZFCTFAULT) {
			STATUS("ZFCT Fault");
		}
		else if (LSODFAULT) {
			STATUS("Local/Open Door Fault");
		}
		else if (OTFAULT) {
			STATUS("Xmfr/Thy Temp Fault");
		}
		else if (OCFAULT) {
			STATUS("Over Current Fault");
		}
		else if (OVFAULT) {
			STATUS("Over Voltage Fault");
		}
		else if (GDFAULT) {
			STATUS("Ground Fault");
		}
		else if (PFSHUTDWN) {
			STATUS("Power Failure Shutdown");
		}
		else if (LCWFAULT) {
			STATUS("LCW Fault");
		}
		else if (ESILOCK) {
			STATUS("External Safety Interlock");
		}
		else  {
			STATUS("Unknown Fault");
		}

		SETI = 0.0;
		pvPut(SETI);
%%		torus_set(SET_IMMEDIATE,SETI,10.0);
		LSETI = 0.0;
%%		torus_set(POWER_OFF,NULL,NULL);
		PSONSET = 0;
		pvPut(PSONSET);

	} state off
    }

}

/*-----------------------------------------------------------------*/
/*-------------------- Power Supply Sequence ----------------------*/
/*-----------------------------------------------------------------*/
 
ss  monitoring 
{
    state monitoring 
    {
	when(delay(2))
	{
		/* Reset Read Fail Counter */
		RDFAILCNT = 0;
		pvPut(RDFAILCNT);

		/**************************/
		/* Read From Power Supply */
		/**************************/

%%		trd_status = torus_read(CURRENT,&IRBCK); 
		if (trd_status) {
			RDFAILCNT = RDFAILCNT + 1;
		}
		else {
			pvPut(IRBCK);
		}
		taskDelay(waitDelay);


%%		trd_status = torus_read(SETPOINT,&ISETRBCK); 
		if (trd_status) {
			RDFAILCNT = RDFAILCNT + 1;
		}
		else {
			pvPut(ISETRBCK);
		}
		taskDelay(waitDelay);


%%		trd_status = torus_read(VOLTAGE,&VRBCK); 
		if (trd_status) {
			RDFAILCNT = RDFAILCNT + 1;
		}
		else {
			pvPut(VRBCK);
		}
		taskDelay(waitDelay);

%%		trd_status = torus_read(DAC,&DACRBCK); 
		if (trd_status) {
			RDFAILCNT = RDFAILCNT + 1;
		}
		else {
			pvPut(DACRBCK);
		}
		taskDelay(waitDelay);

%%		trd_status = torus_read(INTERLCKS,&INTERLOCKS); 
		if (trd_status) {
			RDFAILCNT = RDFAILCNT + 1;
		}
		else {
			pvPut(INTERLOCKS);
		}
		taskDelay(waitDelay);

		/***************************/
		/* Calculate Serial Status */
		/***************************/

		if (RDFAILCNT > 4) {			/* All Reads Failed */
			FAILCNT = FAILCNT + 1;
			pvPut(FAILCNT);
		}

		if (RDFAILCNT < 1) {
			SERIALSTAT = 0;
			pvPut(SERIALSTAT);
		}
		else if (FAILCNT >= 5) {
			SERIALSTAT = 1;
			pvPut(SERIALSTAT);
			if (FAILCNT > 100000) {
				FAILCNT = 100000;
				pvPut(FAILCNT);
			}
		}

		/************************/
		/* Calculate Interlocks */
		/************************/
			

%%		INTERLOCK = (unsigned int)INTERLOCKS;

		/* Set IPFAULT */
		if (INTERLOCK & IPMASK) 
		{
			IPFAULT = 1;
			pvPut(IPFAULT);
		}
		else {
			IPFAULT = 0;
			pvPut(IPFAULT);
		}

		/* Set FCFAULT */
		if (INTERLOCK & FCMASK) 
		{
			FCFAULT = 1;
			pvPut(FCFAULT);
		}
		else {
			FCFAULT = 0;
			pvPut(FCFAULT);
		}

		/* Set ZFCTFAULT */
		if (INTERLOCK & ZFCTMASK) 
		{
			ZFCTFAULT = 1;
			pvPut(ZFCTFAULT);
		}
		else {
			ZFCTFAULT = 0;
			pvPut(ZFCTFAULT);
		}

		/* Set LSODFAULT */
		if (INTERLOCK & LSODMASK) 
		{
			LSODFAULT = 1;
			pvPut(LSODFAULT);
		}
		else {
			LSODFAULT = 0;
			pvPut(LSODFAULT);
		}

		/* Set OTFAULT */
		if (INTERLOCK & OTMASK) 
		{
			OTFAULT = 1;
			pvPut(OTFAULT);
		}
		else {
			OTFAULT = 0;
			pvPut(OTFAULT);
		}

		/* Set OCFAULT */
		if (INTERLOCK & OCMASK) 
		{
			OCFAULT = 1;
			pvPut(OCFAULT);
		}
		else {
			OCFAULT = 0;
			pvPut(OCFAULT);
		}

		/* Set OVFAULT */
		if (INTERLOCK & OVMASK) 
		{
			OVFAULT = 1;
			pvPut(OVFAULT);
		}
		else {
			OVFAULT = 0;
			pvPut(OVFAULT);
		}

		/* Set GDFAULT */
		if (INTERLOCK & GDMASK) 
		{
			GDFAULT = 1;
			pvPut(GDFAULT);
		}
		else {
			GDFAULT = 0;
			pvPut(GDFAULT);
		}

		/* Set PFSHUTDWN */
		if (INTERLOCK & PFSMASK) 
		{
			PFSHUTDWN = 1;
			pvPut(PFSHUTDWN);
		}
		else {
			PFSHUTDWN = 0;
			pvPut(PFSHUTDWN);
		}

		/* Set LCWFAULT */
		if (INTERLOCK & LCWMASK) 
		{
			LCWFAULT = 1;
			pvPut(LCWFAULT);
		}
		else {
			LCWFAULT = 0;
			pvPut(LCWFAULT);
		}

		/* Set ESILOCK */
		if (INTERLOCK & ESIMASK) 
		{
			ESILOCK = 1;
			pvPut(ESILOCK);
		}
		else {
			ESILOCK = 0;
			pvPut(ESILOCK);
		}

		/* Set VLWARN */
		if (INTERLOCK & VLWMASK) 
		{
			VLWARN = 1;
			pvPut(VLWARN);
		}
		else {
			VLWARN = 0;
			pvPut(VLWARN);
		}

		/* Set PSONRBCK */
		if (INTERLOCK & PSMASK) 
		{
			PSONRBCK = 1;
			pvPut(PSONRBCK);
		}
		else {
			PSONRBCK = 0;
			pvPut(PSONRBCK);
		}

		/* Set CCMODE */
		if (INTERLOCK & CCMASK) 
		{
			CCMODE = 1;
			pvPut(CCMODE);
		}
		else {
			CCMODE = 0;
			pvPut(CCMODE);
		}

		/* Set Status of INHIBIT */
		if (IPFAULT || FCFAULT || ZFCTFAULT || LSODFAULT || OTFAULT || OCFAULT ||
		    OVFAULT || GDFAULT || PFSHUTDWN || LCWFAULT || ESILOCK) {
			INHIBIT = 1;
			pvPut(INHIBIT);
		}
		else {
			INHIBIT = 0;
			pvPut(INHIBIT);
		}

        } state monitoring
    }
}

