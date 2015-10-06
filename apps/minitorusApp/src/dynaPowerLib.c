/*-------------------------------------------------------*/
/*-------------------------------------------------------*/
/*              Mini-torus Serial Interface
 *                   Low Level Commands
 *
 *
 * Functions: Reads and Writes to the Mini-Torus
 *            Power Supply
 *	      Model Number: PD42-04000103-GKLX-PY57
 *	      S/N: 920177-92018
 *            J/N: 31926
 * Date: Aug 21, 1996
 * Author: Scott Higgins
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

#include <taskLib.h>
#include <stdioLib.h>
#include <string.h>


/***********/
/* Defines */
/***********/

#define STX	2
#define ETX	3
#define EOS	'\0'
#define ACK 	'\006'
#define NACK 	'\021'
#define MAXLEN	1023

/* Command Defines */

#define POWER_OFF       0
#define POWER_ON        1
#define RESET           2
#define SET_IMMEDIATE   3

#define CURRENT         0
#define SETPOINT        1
#define VOLTAGE         2
#define DAC             3
#define INTERLOCKS      4

/* Subroutine Return Defines */

#define TORUS_INIT_ERROR 1        /* Torus Initialization Error */
#define SUCCESS 	 0
#define FAIL 		 1
#define WRITE_ERROR 	 1
#define READ_ERROR 	 1
#define EXTRACT_FAIL 	 1
#define UNKNOWN_CMD	 10


/*********************/
/* Gobal Debug Flags */
/*********************/

int MINI_TORUS_DEBUG = 0;                /* Debug flag for dynaPowerLib.c */
int ReadbackTimeoutCount = 16;		 /* 1 second */
int readDelay = 5;			 /* 1/12 of a second */
char tbuf[1024];			 /* Test Buffer */


/**************/
/* Init Flags */
/**************/

char TorusSerialPortName[] = {"/tyCo/1"};    /* Serial Port Device Name */
int torusFd = 0;                             /* Data Acquistion File Descriptor */
SEM_ID torusIOsync = 0;                      /* Mutually Exclusive Bin Semaphore */
int torusInitialized;                        /* Global Flag Used for Epics call */
					     /* to torusinit */

/*************/
/* Prototype */
/*************/

int torusinit(void);                    /* Intialize Serial Port */
int torus_set(int, double, int);	/* Minit Torus Set */  
int torus_read(int, double*);		/* Minit Torus Read */  
unsigned short calc_crc(char *);	/* Calculate Crc */  
void make_mess(char *, char *);          /* Make a message out of a Command */
int read_mess(char *);          	/* Read a message */
int send_mess(char *);          	/* Send message to Hardware */


/*----------------------------------------------------------*/
/*----------------------------------------------------------*/
/*
 * Name:        torusinit
 *
 * Function:    Create mutually exclusive binary semaphore
 *              for sharing the serial port, Open Serial Port
 *              to mini-torus Power Supply, set baud rate,
 *              flush I/O port.
 *
 * Arguments:   NONE
 *
 * Return:      Error status
*/
/*----------------------------------------------------------*/
/*----------------------------------------------------------*/


int torusinit(void)
{

	/********************/
	/* Create Semaphore */
	/********************/

	if ((torusIOsync = semBCreate(SEM_Q_FIFO, SEM_FULL)) == NULL) {
	    printf("torusinit(): Could not create binary semaphore\n");
	    return(TORUS_INIT_ERROR); 
	}

	semTake(torusIOsync, WAIT_FOREVER);   /* Take control of Serial Port */

	/********************/
	/* Open Serial Port */
	/********************/

	if ((torusFd = open(TorusSerialPortName,O_RDWR,0777)) == ERROR) {
	    printf("torusinit(): Could not open %s\n",TorusSerialPortName);
	    semDelete(torusIOsync);
	    return(TORUS_INIT_ERROR); 
	}

	/*****************/
	/* Set Baud Rate */
	/*****************/

	if (ioctl(torusFd, FIOBAUDRATE, 9600) == ERROR ) {
	    printf("torusinit(): Could not set baud rate\n");
	    close(torusFd);
	    semDelete(torusIOsync);
	    return(TORUS_INIT_ERROR); 
	}

	/****************/
	/* Set Raw Mode */
	/****************/

	if (ioctl(torusFd, FIOSETOPTIONS, OPT_RAW) == ERROR ) {
	    printf("torusinit(): Could not set raw mode\n");
	    close(torusFd);
	    semDelete(torusIOsync);
	    return(TORUS_INIT_ERROR); 
	}



	/******************/
	/* Flush I/O Port */
	/******************/

	if (ioctl(torusFd, FIOFLUSH, 0) == ERROR ) {
	    printf("torusinit(): Could not Flush I/O Buffer\n");
	    close(torusFd);
	    semDelete(torusIOsync);
	    return(TORUS_INIT_ERROR); 
	}

	semGive(torusIOsync);	/* Free Serial Port Control */
	torusInitialized = 1;	/* Set Torus Initialization Flag */
	return(SUCCESS); 
}


/*----------------------------------------------------------*/
/*----------------------------------------------------------*/
/*
 * Name:        calc_crc
 *
 * Function:    Calculate Crc for length plus the Message
 *		*** Important *** CRC must use shorts.
 *
 * Arguments:   char *mess;   String of length and Message
 *
 * Return:      5 digit crc.
*/
/*----------------------------------------------------------*/
/*----------------------------------------------------------*/

unsigned short calc_crc(char *mess)
{

	unsigned short shifter;
	unsigned short flag;
	unsigned short accum = 0;
	short i;
	short len;

	len = strlen(mess);
	for (i = 0; i < len; i++)
	    for (shifter = 0x80; shifter; shifter >>= 1) {
	        flag = (accum & 0x8000);
		accum <<= 1;
		accum |= ((shifter & mess[i]) ? 1 : 0);
		if (flag)
		    accum ^= 0x1021;
	    }
	return accum;
}


void num2ascii(unsigned short num, char *buf, int max)
{

	int i;
	for (i = 0; max; i++) {
		buf[i] = (num / max) + '0';
		num %= max;
		max /= 10;
	}
	buf[i] = EOS;
}


/*----------------------------------------------------------*/
/*----------------------------------------------------------*/
/*
 * Name:        make_mess
 *
 * Function:  	Make message to pass to the hardware. 
 *		SDDDDS...SDDDDDS
 *		||__||___||___||___ ETX - end character '^C'
 *              | |   |    |_______ 5 digit CRC of length and message (ASCII)
 *		| |   |____________ message itself
 *		| |________________ 4 digit length (ASCII)
 *		|__________________ STX - start character '^B'
 *
 * Arguments:   char *mess;	Message to Hardware. Ex: "POWER_ON"  
 *		char *buf;	Formated string -> hardware
 *		
 * Return:      NULL
*/
/*----------------------------------------------------------*/
/*----------------------------------------------------------*/

void make_mess(char *mess, char *buf)
{
	unsigned short crc;
	int len;

	buf[0] = STX;
	len = strlen(mess);			/* Length of Message */
	num2ascii(len,buf+1,1000);
	strcpy(buf + 5,mess);
	len += 5;
	buf[len] = EOS;
	crc = calc_crc(buf + 1);		/* Get CRC */
	num2ascii(crc,buf+len,10000);
	len +=5;
	buf[len++] = ETX;
	buf[len] = EOS;			/* Terminate String */

	if (MINI_TORUS_DEBUG) 
		printf("Message After Crc: %s\n",buf); 

}

/*----------------------------------------------------------*/
/*----------------------------------------------------------*/
/*
 * Name:        send_mess
 *
 * Function:  	Send message to the RS232 Port 
 *
 * Arguments:   char *output;	Message to Hardware. Ex: "POWER_ON"  
 *		
 * Return:      Error Status
*/
/*----------------------------------------------------------*/
/*----------------------------------------------------------*/

int send_mess(char *output)
{

	int msgSize = 0;		/* Number of bytes to write */
	int bytesSent = 0;		/* Number of bytes written */

	/*****************/
	/* Write Message */
	/*****************/

	msgSize = strlen(output);


	bytesSent = write(torusFd, output, msgSize);   /* Write Message */


	if (MINI_TORUS_DEBUG)
		printf("\nsend_mess(): Message Size: <%d> Actual Sent <%d>\n",
			msgSize,bytesSent);

	if (bytesSent != msgSize) {
		if (MINI_TORUS_DEBUG) {
			printf("\nsend_mess(): Message Size: <%d> != Actual Sent 
			<%d>\n", msgSize,bytesSent);
		}
		return(WRITE_ERROR);
	}
	return(SUCCESS);
}


/*----------------------------------------------------------*/
/*----------------------------------------------------------*/
/*
 * Name:        read_mess
 *
 * Function:  	Read message from the RS232 Port 
 *
 * Arguments:   char *input;	Char buffer to hold message 
 *		
 * Return:      Error Status
*/
/*----------------------------------------------------------*/
/*----------------------------------------------------------*/

int read_mess(char *input)
{

	int i = 0; 
	int j = 0;
	int NumUnRead = -1; 		/* Number of unread bytes in Read Buffer */
	int Count = 0;

	/*****************/
	/* Read Responce */
	/*****************/

	do {
      		taskDelay(readDelay);
		ioctl(torusFd, FIONREAD, (int)&NumUnRead);
		if ((NumUnRead + i) > MAXLEN)
			break;
		if (NumUnRead != 0) {
			read(torusFd, &input[i], NumUnRead);
			i = i + NumUnRead;
		}
		Count++;
		j = (i > 0) ? i - 2 : 0;

	} while((input[j] != ETX) && (Count < ReadbackTimeoutCount) );

	input[j] = EOS;
	if (MINI_TORUS_DEBUG) { 
		printf("\nread_mess() Input: %s Count: %d NumRead: %d\n", input, Count, i);
	
	}

	return (Count == ReadbackTimeoutCount) ? READ_ERROR : SUCCESS;


}

/*----------------------------------------------------------*/
/*----------------------------------------------------------*/
/*
 * Name:        extract_mess
 *
 * Function:  	Extract Message and length from the string buffer
 *
 * Arguments:   char *in;	Buffer holding the message 
 * 		char *mess;	Message 
 * 		int length;	Length 
 *		
 * Return:      Error Status
*/
/*----------------------------------------------------------*/
/*----------------------------------------------------------*/

int extract_mess(char *in, char *mess, int *length)
{

	unsigned short crc;
	unsigned short crc2;
	char tbuf[1024];		/* Temporary Buffer */
	char input[1024];		/* Temporary Buffer */
	int len;			/* Message length */

	strcpy(input,&in[1]);
	if (input[0] != STX)		/* Make sure 1st char is STX */
		return(EXTRACT_FAIL);
	
	strcpy(tbuf,&input[1]);
	tbuf[4] = EOS;
	sscanf(tbuf,"%d",length);	/* Extract Message Length */
	len = *length;
	if (len < 0) 
		return(EXTRACT_FAIL);
	strcpy(mess,&input[5]);		/* Extract Message */
	mess[len] = EOS;		/* Terminate Message */
	strcpy(tbuf,&input[len+5]);
	tbuf[5] = EOS;
	sscanf(tbuf,"%hu",&crc);	/* Extract Message CRC */
	strcpy(tbuf,&input[1]);
	tbuf[len+4] = EOS;
	crc2 = calc_crc(tbuf);		/* Check Crc */
	if (MINI_TORUS_DEBUG)
		printf("\nextract_mess() crc: %hu, crc2: %hu,len: %d, mess: %s\n",
			crc,crc2,len,mess);

	return(crc2 != crc);
}


/*----------------------------------------------------------*/
/*----------------------------------------------------------*/
/*
 * Name:        torus_set
 *
 * Function:    This Subroutine is called to set the 
 *		Mini-torus Power Supply. The Commands
 *		supported are Power_on, Power_off, Reset,
 *		Current Setpoint.
 *
 * Arguments:   int command;	Which Command (0-3)
 * 		double value;	Value being set
 *		int ramprate;   Value 0-200 Amps/Sec
 *
 * Return:      Error status
*/
/*----------------------------------------------------------*/
/*----------------------------------------------------------*/

int torus_set(int command, double value, int ramprate)
{

	char tbuf[1024];	/* Temporary String Buffer */
	char sbuf[1024];	/* String Buffer */
	int status = 0;

	switch(command)
	{
		case POWER_OFF: 
			make_mess("POWER_OFF",sbuf);
			semTake(torusIOsync, WAIT_FOREVER);          /* Take Serial Port Control */
			ioctl (torusFd, FIOFLUSH, 0);                /* Clear tty I/O buffers */
			status = send_mess(sbuf);
			semGive(torusIOsync);                          /* Free Serial Port Control */
		break;
		case POWER_ON: 
			make_mess("POWER_ON",sbuf);
			semTake(torusIOsync, WAIT_FOREVER);          /* Take Serial Port Control */
			ioctl (torusFd, FIOFLUSH, 0);                /* Clear tty I/O buffers */
			status = send_mess(sbuf);
			semGive(torusIOsync);                          /* Free Serial Port Control */
		break;
		case RESET: 
			make_mess("RESET",sbuf);
			semTake(torusIOsync, WAIT_FOREVER);          /* Take Serial Port Control */
			ioctl (torusFd, FIOFLUSH, 0);                /* Clear tty I/O buffers */
			status = send_mess(sbuf);
			semGive(torusIOsync);                          /* Free Serial Port Control */
		break;
		case SET_IMMEDIATE: 
			sprintf(tbuf,"%s%.2f,%d","SET_IMMEDIATE,",value,ramprate);
			make_mess(tbuf,sbuf);
			semTake(torusIOsync, WAIT_FOREVER);          /* Take Serial Port Control */
			ioctl (torusFd, FIOFLUSH, 0);                /* Clear tty I/O buffers */
			status = send_mess(sbuf);
			semGive(torusIOsync);                          /* Free Serial Port Control */
		break;
		default:
			status = UNKNOWN_CMD;
		break;
	}

	if (MINI_TORUS_DEBUG) 
		printf("torus_set: Command %s, status %d\n",sbuf,status);
	
	return(status);
}

/*----------------------------------------------------------*/
/*----------------------------------------------------------*/
/*
 * Name:        torus_read
 *
 * Function:    This Subroutine is called to read the 
 *		Mini-torus Power Supply. The Read Commands
 *		supported are Current, Setpoint, Voltage,
 *		Dac, Interlocks
 *
 * Arguments:   int command;	Which Command (0-3)
 * 		double value;	Value being read
 *
 * Return:      Error status
*/
/*----------------------------------------------------------*/
/*----------------------------------------------------------*/

int torus_read(int command, double *value)
{

	char wbuf[1024];	/* String Write Buffer */
	char rbuf[1024];	/* String Read Buffer */
	char mess[1024];        /* Read Message */
	char tempstr[1024];     /* Temp String */
	int status = 0;
	int retVal = 0;	 	/* Return value of sscanf */
	int temp = 0;
	int len = 0;
	int i = 0;

	wbuf[1023] = EOS;
	rbuf[1023] = EOS;
	mess[1023] = EOS;

	switch(command)
	{
		case CURRENT: 
			make_mess("GET_DATA?,CURRENT",wbuf); 	     
			semTake(torusIOsync, WAIT_FOREVER);          /* Take Serial Port Control */
			ioctl (torusFd, FIOFLUSH, 0);                /* Clear tty I/O buffers */
			status = send_mess(wbuf);
			if (!status) 
				status = read_mess(rbuf);
			semGive(torusIOsync);                          /* Free Serial Port Control */
			if (!status) {
				status = extract_mess(rbuf,mess,&len);
				if (!status) {
					retVal = sscanf(mess,"%lf",value);
					if (!retVal)
						status = FAIL;
				}
			}

			   
		break;
		case SETPOINT: 
			make_mess("GET_DATA?,SETPOINT",wbuf);
			semTake(torusIOsync, WAIT_FOREVER);          /* Take Serial Port Control */
			ioctl (torusFd, FIOFLUSH, 0);                /* Clear tty I/O buffers */
			status = send_mess(wbuf);
			if (!status)
				status = read_mess(rbuf);
			semGive(torusIOsync);                          /* Free Serial Port Control */
			if (!status) {
				status = extract_mess(rbuf,mess,&len);
				if (!status) {
					if (strcmp("NONE",mess) == 0) {
						*value = 0.0;	
					}
					else {
						strcpy(tempstr,&mess[3]);
						for(i = 0; i< MAXLEN; i++) 
							if (tempstr[i] == ',') 
								break;
						tempstr[i] = EOS;
						retVal = sscanf(tempstr,"%lf",value);
						if (!retVal)
							status = FAIL;
					}
				}
			}	
		break;
		case VOLTAGE: 
			make_mess("GET_DATA?,VOLTAGE",wbuf);
			semTake(torusIOsync, WAIT_FOREVER);          /* Take Serial Port Control */
			ioctl (torusFd, FIOFLUSH, 0);                /* Clear tty I/O buffers */
			status = send_mess(wbuf);
			if (!status)
				status = read_mess(rbuf);
			semGive(torusIOsync);                          /* Free Serial Port Control */
			if (!status) {
				status = extract_mess(rbuf,mess,&len);
				if (!status) {
					retVal = sscanf(mess,"%lf",value);
					if (!retVal)
						status = FAIL;
				}
			}	
		break;
		case DAC: 
			make_mess("GET_DATA?,DAC",wbuf);
			semTake(torusIOsync, WAIT_FOREVER);          /* Take Serial Port Control */
			ioctl (torusFd, FIOFLUSH, 0);                /* Clear tty I/O buffers */
			status = send_mess(wbuf);
			if (!status)
				status = read_mess(rbuf);
			semGive(torusIOsync);                          /* Free Serial Port Control */
			if (!status) {
				status = extract_mess(rbuf,mess,&len);
				if (!status) {
					retVal = sscanf(mess,"%lf",value);
					if (!retVal)
						status = FAIL;
				}
			}	
		break;
		case INTERLOCKS: 
			make_mess("GET_DATA?,INTERLOCKS",wbuf);
			semTake(torusIOsync, WAIT_FOREVER);          /* Take Serial Port Control */
			ioctl (torusFd, FIOFLUSH, 0);                /* Clear tty I/O buffers */
			status = send_mess(wbuf);
			if (!status)
				status = read_mess(rbuf);
			semGive(torusIOsync);                          /* Free Serial Port Control */
			if (!status) {
				status = extract_mess(rbuf,mess,&len);
				if (!status) {
					retVal = sscanf(mess,"%x",&temp);
					if (!retVal)
						status = FAIL;
					else
						*value = temp;
				}
			}	
		break;
		default:
			status = UNKNOWN_CMD;
		break;
	}

	if (MINI_TORUS_DEBUG) 
		printf("torus_read: Command %s Read %s, status %d\n",wbuf,rbuf,status);
	
	return(status);
}
