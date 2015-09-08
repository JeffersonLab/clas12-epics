/*-------------------------------------------------------*/
/*-------------------------------------------------------*/
/*             	    Hall B Raster Control
 *                   Software Library 
 *
 *
 * Functions: Reads and Writes to Hall B's
 *	      Raster Controller
 * Date: August 4, 1998  
 * Author: Scott Higgins 
 *
 *  Major revision:  Sept. 2000 apf and F. Barbosa 
 *
*/
/*-------------------------------------------------------*/
/*-------------------------------------------------------*/


/************/
/* Includes */
/************/

#include <vxWorks.h>
#include <ioLib.h>
#include <tyLib.h>
#include <ctype.h>
#include <selectLib.h>
#include <semLib.h>
#include <string.h>

/***********/
/* Defines */
/***********/

/* Command Defines */

#include "rast.h"

/*********************/
/* Gobal Debug Flags */
/*********************/

int BSC_DEBUG = 0;                               /* Debug flag for rastLib.c */
int bscReadbackTimeoutCount = 10;		 /* 5/6 of a second */
int bscreadDelay = 5;			         /* 1/12 of a second */


/**************/
/* Init Flags */
/**************/

char BscSerialPortName[] = {"/tyIP/0"};   /* Serial Port Device Name  */
/* char BscSerialPortName[] = {"/tyCo/1"}; */  /* Serial Port Device Name  */
int bscFd = 0;                            /* Data Acquistion File Descriptor  */
SEM_ID bscIOsync = 0;                     /* Mutually Exclusive Bin Semaphore  */
int bscInitialized;                        /* Global Flag Used for Epics call */
					    /* to bscinit */

/*************/
/* Prototype */
/*************/

int bscinit(void);                      /* Intialize Serial Port */
int bsc_set(int, int, int);             /* Bsc Set */  
int bsc_read(int, int *);	        /* Bsc Read */  
int bsc_read_mess(char *);        	/* Read a message */
int bsc_send_mess(char *);        	/* Send message to Hardware */
int getbits(unsigned x, int p, int n);  /* bit unpacker */
int setbits(unsigned x, int p, int n, unsigned y); /* bit packer */

/*----------------------------------------------------------*/
/*----------------------------------------------------------*/
/*
 * Name:        bscinit
 *
 * Function:    Create mutually exclusive binary semaphore
 *              for sharing the serial port, Open Serial Port
 *              to Bsc Shore Power Supply, set baud rate,
 *              flush I/O port. Do this for three serial ports
 *
 * Arguments:   NONE
 *
 * Return:      Error status
*/
/*----------------------------------------------------------*/
/*----------------------------------------------------------*/


int bscinit(void)
{

	/********************/
	/* Create Semaphore */
	/********************/

	if ((bscIOsync = semBCreate(SEM_Q_FIFO, SEM_FULL)) == NULL) {
	    printf("bscinit(): Could not create binary semaphore \n");
	    return(BSC_INIT_ERROR); 
	}
	semTake(bscIOsync, WAIT_FOREVER);   /* Take control of Serial Port */

	/********************/
	/* Open Serial Port */
	/********************/

	if ((bscFd = open(BscSerialPortName,O_RDWR,0777)) == ERROR) {
	    printf("bscinit(): Could not open %s\n",BscSerialPortName);
	    semDelete(bscIOsync);
	    return(BSC_INIT_ERROR); 
	}

	/*****************/
	/* Set Baud Rate */
	/*****************/

	if (ioctl(bscFd, FIOBAUDRATE, 9600) == ERROR ) {
	    printf("bscinit(): Could not set baud rate \n");
	    close(bscFd);
	    semDelete(bscIOsync);
	    return(BSC_INIT_ERROR); 
	}

	/****************/
	/* Set Raw Mode */
	/****************/
	
	if (ioctl(bscFd, FIOSETOPTIONS, OPT_RAW) == ERROR ) {
	    printf("bscinit(): Could not set raw mode \n");
	    close(bscFd);
	    semDelete(bscIOsync);
	    return(BSC_INIT_ERROR); 
	}


	/******************/
	/* Flush I/O Port */
	/******************/

	if (ioctl(bscFd, FIOFLUSH, 0) == ERROR ) {
	    printf("bscinit(): Could not Flush I/O Buffer \n");
	    close(bscFd);
	    semDelete(bscIOsync);
	    return(BSC_INIT_ERROR); 
	}

	semGive(bscIOsync);	/* Free Serial Port Control  */

	bscInitialized = 1;	/* Set Bsc Initialization Flag */
	printf("bsc_init: Finished!\n");
	return(SUCCESS); 
}


/*----------------------------------------------------------*/
/*----------------------------------------------------------*/
/*
 * Name:        bsc_send_mess
 *
 * Function:  	Send message to the RS232 Port 
 *
 * Arguments:   char *output;	Message to Hardware. Ex: "MODE1"  
 *		
 * Return:      Error Status
*/
/*----------------------------------------------------------*/
/*----------------------------------------------------------*/

int bsc_send_mess(char *output)
{

	int msgSize = 0;		/* Number of bytes to write */
	int bytesSent = 0;		/* Number of bytes written */

	/*****************/
	/* Write Message */
	/*****************/

	msgSize = strlen(output);


	bytesSent = write(bscFd, output, msgSize);   /* Write Message */


	if (BSC_DEBUG > 1)
		printf("\nbsc_send_mess(): Message Size: <%d> Actual Sent <%d>\n",
			msgSize,bytesSent);

	if (bytesSent != msgSize) {
		if (BSC_DEBUG > 1) {
			printf("\nbsc_send_mess(): Message Size: <%d> != Actual Sent <%d>\n", msgSize,bytesSent);
		}
		return(WRITE_ERROR);
	}
	return(SUCCESS);
}


/*----------------------------------------------------------*/
/*----------------------------------------------------------*/
/*
 * Name:        bsc_read_mess
 *
 * Function:  	Read message from the RS232 Port 
 *
 * Arguments:   char *input;	Char buffer to hold message 
 *		
 * Return:      Error Status
*/
/*----------------------------------------------------------*/
/*----------------------------------------------------------*/

int bsc_read_mess(char *input)
{

	int i = 0; 
	int j = 0;
	int NumUnRead = -1; 		/* Number of unread bytes in Read Buffer */
	int Count = 0;

	/*****************/
	/* Read Responce */
	/*****************/

	if (BSC_DEBUG > 1) { 
		printf("Message: %s  FD: %d\n",input,bscFd);
	}

	do {
      		taskDelay(bscreadDelay);
		ioctl(bscFd, FIONREAD, (int)&NumUnRead);
		if ((NumUnRead + i) > MAXLEN)
			break;
		if (NumUnRead != 0) {
			read(bscFd, &input[i], NumUnRead);
			i = i + NumUnRead;
		}
		Count++;
		j = (i > 0) ? i - 1 : 0;

	} while((input[j] != '\r') && (Count < bscReadbackTimeoutCount) );

	input[j] = EOS;		/* After each Message is a \r */
				/* Put EOS where the \r is	*/
	if (BSC_DEBUG > 1) { 
		printf("\nread_mess() Input: %s Count: %d NumRead: %d\n", input, Count, i);
	
	}

	return (Count == bscReadbackTimeoutCount) ? READ_ERROR : SUCCESS;


}

/*----------------------------------------------------------*/
/*----------------------------------------------------------*/
/*
 * Name:        bsc_set
 *
 * Function:    This Subroutine is called to set the 
 *		Bsc Shore Power Supply. The Commands
 *		supported are Current Setpoint and Mode Setpoint
 *
 * Arguments:   int command;	Which Command (0)
 * 		int value;	Value being set
 *
 * Return:      Error status
*/
/*----------------------------------------------------------*/
/*----------------------------------------------------------*/

int bsc_set(int command, int value, int value2)
{

	char sbuf[32];	        /* String Buffer */
	int status = 0;
	unsigned int temp = 0;
	unsigned int temp2 = 0;

	/*************************************/
	/* Take Semaphore and Flush I/O Port */
	/*************************************/

	semTake(bscIOsync, WAIT_FOREVER);          /* Take Serial Port Control */
	ioctl (bscFd, FIOFLUSH, 0);                /* Clear tty I/O buffers */

	/*******************/
	/* Perform Command */
	/*******************/

	switch(command)
	{
		case SET_RESET: 
			sprintf(sbuf,"WRS\r");
			status = bsc_send_mess(sbuf);
		break;
		case SET_SIZE_X: 
			temp = (unsigned int)value;
			sprintf(sbuf,"WSX%04d\r",temp);
			status = bsc_send_mess(sbuf);
		break;
		case SET_SIZE_XY: 
			temp = (unsigned int)value;
			temp2 = (unsigned int)value2;
			sprintf(sbuf,"WSB%04d,%04d\r",temp,temp2);
			status = bsc_send_mess(sbuf);
		break;
		case SET_SIZE_Y: 
			temp = (unsigned int)value;
			sprintf(sbuf,"WSY%04d\r",temp);
			status = bsc_send_mess(sbuf);
		break;
		case SET_OFFSET_X: 
			if (value < 0 ) {
  			  temp = -1*value;
			  sprintf(sbuf,"WOX-%04d\r",temp);
                        } else {
  			  temp =  value;
			  sprintf(sbuf,"WOX+%04d\r",temp);
			}
			status = bsc_send_mess(sbuf);
		break;
		case SET_OFFSET_Y: 
			if (value < 0 ) {
  			  temp = -1*value;
			  sprintf(sbuf,"WOY-%04d\r",temp);
                        } else {
  			  temp =  value;
			  sprintf(sbuf,"WOY+%04d\r",temp);
			}
			status = bsc_send_mess(sbuf);
		break;
		case SET_OFFSET_XY: 
			if (value < 0 && value2 < 0) {
  			  temp = -1*value;
  			  temp2 = -1*value2;
			  sprintf(sbuf,"WOB-%04d,-%04d\r",temp,temp2);
                        } else if (value < 0 && value2 > 0) {
  			  temp = -1*value;
  			  temp2 = +1*value2;
			  sprintf(sbuf,"WOB-%04d,+%04d\r",temp,temp2);
                        } else if (value > 0 && value2 < 0) {
  			  temp = +1*value;
  			  temp2 = -1*value2;
			  sprintf(sbuf,"WOB+%04d,-%04d\r",temp,temp2);
                        } else if (value > 0 && value2 > 0) {
  			  temp = +1*value;
  			  temp2 = +1*value2;
			  sprintf(sbuf,"WOB+%04d,+%04d\r",temp,temp2);
                        } 
			status = bsc_send_mess(sbuf);
		break;
		case SET_CYCLETIME: 
			temp = (unsigned int)value;
			sprintf(sbuf,"WCY%d\r",temp);
			status = bsc_send_mess(sbuf);
		break;
		case SET_BYTEWORD: 
			temp = (unsigned int)value;
			if (BSC_DEBUG) 
				printf("Byte Word: %u\n",temp);
			  sprintf(sbuf,"WSE%03d\r",temp);
			  /*                          printf("Byte Word CMD:%u:%s:\n",temp,sbuf); */
                          status = bsc_send_mess(sbuf);
		break;
		default:
			status = UNKNOWN_CMD;
		break;
	}

	/******************/
	/* Free Semaphore */
	/******************/

	semGive(bscIOsync);                          /* Free Serial Port Control */

	if (BSC_DEBUG) {
		printf("\nbsc_set: Set Parameters\n");
		printf("	bsc_set: Command %s\n",sbuf);
		printf("	bsc_set: Status %d\n",status);
	}
	
	return(status);
}

/*----------------------------------------------------------*/
/*----------------------------------------------------------*/
/*
 * Name:        bsc_read
 *
 * Function:    This Subroutine is called to read the 
 *		Bsc.
 *
 * Arguments:   int command;	Which Command (0-3)
 * 		double value;	Value being read
 *
 * Return:      Error status
*/
/*----------------------------------------------------------*/
/*----------------------------------------------------------*/

int bsc_read(int command, int *value)
{

	char sbuf[32];	/* String Write Buffer */
	char rbuf[32];	/* String Read Buffer */
	int status = 0;
        int tmp_value = 0;
	int retVal = 0;	 	/* Return value of sscanf */

	/*************************************/
	/* Take Semaphore and Flush I/O Port */
	/*************************************/

	semTake(bscIOsync, WAIT_FOREVER);          /* Take Serial Port Control */
	ioctl (bscFd, FIOFLUSH, 0);                /* Clear tty I/O buffers */

	/*******************/
	/* Perform Command */
	/*******************/

	switch(command)
	{
		case READ_SIZE_X: 
			sprintf(sbuf,"RSX\r");
			status = bsc_send_mess(sbuf);
			if ((status = bsc_read_mess(rbuf)) == FAIL)
				break;
			if (strncmp(rbuf,"RSX",3) != 0) {
				status = FAIL;
				break;
			}
			retVal = sscanf(&rbuf[3],"%d",value);
			if (retVal) 
				status = SUCCESS;
			else 
				status = FAIL;
		break;
		case READ_SIZE_Y: 
			sprintf(sbuf,"RSY\r");
			status = bsc_send_mess(sbuf);
			if ((status = bsc_read_mess(rbuf)) == FAIL)
				break;
			if (strncmp(rbuf,"RSY",3) != 0) {
				status = FAIL;
				break;
			}
			retVal = sscanf(&rbuf[3],"%d",value);
			if (retVal) 
				status = SUCCESS;
			else 
				status = FAIL;
		break;
		case READ_OFFSET_X: 
			sprintf(sbuf,"ROX\r");
			status = bsc_send_mess(sbuf);
			if ((status = bsc_read_mess(rbuf)) == FAIL)
				break;
			if (strncmp(rbuf,"ROX",3) != 0) {
				status = FAIL;
				break;
			}
			retVal = sscanf(&rbuf[3],"%d ",value);
			if (retVal) 
				status = SUCCESS;
			else 
				status = FAIL;
		break;
		case READ_OFFSET_Y: 
			sprintf(sbuf,"ROY\r");
			status = bsc_send_mess(sbuf);
			if ((status = bsc_read_mess(rbuf)) == FAIL)
				break;
			if (strncmp(rbuf,"ROY",3) != 0) {
				status = FAIL;
				break;
			}
			retVal = sscanf(&rbuf[3],"%d",value);
			if (retVal) 
				status = SUCCESS;
			else 
				status = FAIL;
		break;
		case READ_CYCLETIME: 
			sprintf(sbuf,"RCY\r");
			status = bsc_send_mess(sbuf);
			if ((status = bsc_read_mess(rbuf)) == FAIL)
				break;
			if (strncmp(rbuf,"RCY",3) != 0) {
				status = FAIL;
				break;
			}
			retVal = sscanf(&rbuf[3],"%d",value);
			if (retVal) 
				status = SUCCESS;
			else 
				status = FAIL;
		break;
		case READ_BYTEWORD: 
			sprintf(sbuf,"RSE\r");
			status = bsc_send_mess(sbuf);
			if ((status = bsc_read_mess(rbuf)) == FAIL)
				break;
			if (strncmp(rbuf,"RSE",3) != 0) {
				status = FAIL;
				break;
			}
			retVal = sscanf(&rbuf[3],"%d",value);
			status = SUCCESS;
		break;
		case READ_STATUS: 
			sprintf(sbuf,"RST\r");
			status = bsc_send_mess(sbuf);
			if ((status = bsc_read_mess(rbuf)) == FAIL)
				break;
			if (strncmp(rbuf,"RST",3) != 0) {
				status = FAIL;
				break;
			}
			retVal = sscanf(&rbuf[3],"%d",value);
			status = SUCCESS;
		break;
		default:
			status = UNKNOWN_CMD;
		break;
	}

	/******************/
	/* Free Semaphore */
	/******************/

	semGive(bscIOsync);                          /* Free Serial Port Control */

	if (BSC_DEBUG == 2) {
		if (status == FAIL) 
			printf("\nbsc_read: FAILED\n");
		if (status == SUCCESS)
			printf("\nbsc_read: Success\n");
		printf("	bsc_read: Command %s\n",sbuf);
		printf("	bsc_read: Read %s\n",rbuf);
		printf("	bsc_read: Status %d\n",status);
	}

	return(status);
}
int getbits(unsigned x, int p, int n) {
	return (x >> (p+1-n)) & ~(~0 << n);
}
int setbits(unsigned x, int p, int n, unsigned y) {
   return (x & ~((~(~0 << n)) << (p+1-n))) + ((y & ~(~0 << n)) << (p+1-n)); 
}
