/*----------------------------------------------------------------------------*
 *  Copyright (c) 2006        Southeastern Universities Research Association, *
 *                            Thomas Jefferson National Accelerator Facility  *
 *                                                                            *
 *    This software was developed under a United States Government license    *
 *    described in the NOTICE file included as part of this distribution.     *
 *                                                                            *
 *    Library for C111C Ethernet Based Camac Controller                       *
 *    Network part                                                            *
 *                                                                            *
 *    Author  :  Vardan Gyurjyan                                              *
 *    Group   :  Data Acquisition                                             *
 *    Version :  1.00                                                         *
 *----------------------------------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h> 
#include <fcntl.h> 
#include <string.h> 
#include <errno.h> 
#include <dirent.h> 
#include <time.h> 
#include <signal.h> 
#include <unistd.h> 
#include <ctype.h> 
#include <netdb.h>
#include <sys/time.h> 
#include <sys/wait.h> 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <sys/stat.h> 
#include <netinet/in.h> 
#include <arpa/inet.h>
#include <sys/ioctl.h>


/****************/
/* NETWORK PART */
/****************/

#include "c111cLib.h"

static int ccsend(int sck, char *buffer, int size);
static int ccrecv(int sck, char *buffer, int size);
//static int ccrecv_t(int sck, char *buffer, int size, int timeout);
static int ccrecv_s(int sck, char *buffer, int size);
//static int ccrecv_st(int sck, char *buffer, int size, int timeout);
//static int ccrecv_sb(int sck, char *buffer, int size);
static int ccsendrecv_s(int sck, char *cmd, char* response, int size);
//static int ccsendrecv_st(int sck, char *cmd, char* response, int size, int timeout);
static int ccflush(int sck);

/*-------------------------------------------------------------- * 
 * Connects to the socket. Hardware provides TCP server socket 
 * listening on the port 2000, TCP binary control sdocket 
 * listening on the port 2001. 
 *---------------------------------------------------------------*/
int
ccconnect(char *ip, int port)
{
  int sc;
  int sockAddrSize;
  struct sockaddr_in server_address;
  //struct hostent *hptr;

  /* create socket */
  if ((sc = socket(AF_INET, SOCK_STREAM, 0)) == 0)
  {
    perror("sockect");
    return 0;
  }

   /* build server socket address */ 
  sockAddrSize = sizeof (struct sockaddr_in); 
  bzero ((char *) &server_address, sockAddrSize); 
 
  server_address.sin_family = AF_INET;
  server_address.sin_port = htons(port);
  server_address.sin_addr.s_addr = inet_addr(ip);
  /*  inet_pton(AF_INET, ip, &server_address.sin_addr);*/
  /*  perror("inet_pton");*/

  /* connect to the server */
  if (connect(sc, (struct sockaddr *) &server_address, sockAddrSize) == -1)
  {
    perror("c111cLib::ccconnect::connect");
    close(sc);
    return 0;
  }
  
  return(sc);
}

/*-------------------------------------------------------------- * 
 * Close the open socket 
 *---------------------------------------------------------------*/
int
ccclose(int sck)
{
  shutdown(sck, 2);
  close(sck);
  return(0);
}

/*-------------------------------------------------------------- * 
 * Check if we can read from the socket 
 *---------------------------------------------------------------*/
static int
isReadable(int sck)
{
  fd_set fd;
  struct timeval tv;
  int data;
  
  FD_ZERO(&fd);
  FD_SET(sck, &fd);
  
  tv.tv_sec = 0;
  tv.tv_usec = 0;
  
  data = select(sck + 1, &fd, NULL, NULL, &tv);
  (void)data;
  
  if (FD_ISSET(sck, &fd))
  {
    return 1;
  }
  else
  {
    return 0;
  }
}

/*-------------------------------------------------------------- * 
 * Check if we can write into the socket 
 *---------------------------------------------------------------*/
static int
isWritable(int sck)
{
  fd_set fd;
  struct timeval tv;
  int data;
  
  FD_ZERO(&fd);
  FD_SET(sck, &fd);
  
  tv.tv_sec = 0;
  tv.tv_usec = 0;
  
  data = select(sck + 1, NULL, &fd, NULL, &tv);
  (void)data;
  
  if (FD_ISSET(sck, &fd))
  {
    return 1;
  }
  else
  {
    return 0;
  }
}

/*-------------------------------------------------------------- * 
 * Send to the socket 
 *---------------------------------------------------------------*/
static int
ccsend(int sck, char *buffer, int size)
{
  if (isWritable(sck)) return send(sck, buffer, size, 0);
  return 0;
}

/*-------------------------------------------------------------- * 
 * Receive from the socket 
 *---------------------------------------------------------------*/
static int
ccrecv(int sck, char *buffer, int size)
{
  return recv(sck, buffer, size, 0);
}

/*-------------------------------------------------------------- * 
 * Receive during the timeout 
 *---------------------------------------------------------------*/
/*
static int
ccrecv_t(int sck, char *buffer, int size, int timeout)
{
  int rp, pos;
  time_t now = time(NULL);
  
  pos = 0;
  buffer[pos] = '\0';
  
  while (pos < size)
  {
    if (isReadable(sck))
    {
      rp = recv(sck, &buffer[pos], 1, 0);
      if (rp < 0) return -1;
      pos++;
    }
    if ((time(NULL) - now) > timeout)
    {
      buffer[pos] = '@';
      return -3;
    }
  }
  return pos;
}
*/

/*-------------------------------------------------------------- * 
 * Receive fixed size data 
 *---------------------------------------------------------------*/
static int
ccrecv_s(int sck, char *buffer, int size)
{
  int rp, pos;
  
  pos = 0;
  buffer[pos] = '\0';
  
  while (pos < size)
  {
    rp = recv(sck, &buffer[pos], 1, 0);
    if (rp > 0)
    {
      buffer[pos + 1] = '\0';
      
      // replace new lines and crs with \0
      if (buffer[pos] == '\n')
      {
	    buffer[pos] = '\0';
	    pos--;
      }
      else if (buffer[pos] == '\r')
      {
	    buffer[pos] = '\0';
	    ccflush(sck);
	    return (pos);
      }
      
      pos++;
      
      if (pos > size) return -2;
    }
    else
    {
      return -1;
    }
  }

  return 0;
}

/*-------------------------------------------------------------- * 
 * Receive fixed size data in specified ammount of time
 *---------------------------------------------------------------*/
/*
static int
ccrecv_st(int sck, char *buffer, int size, int timeout)
{
  int rp, pos;
  time_t now = time(NULL);
  
  pos = 0;
  buffer[pos] = '\0';
  
  while (pos < size)
  {
    if (isReadable(sck))
    {
      rp = recv(sck, &buffer[pos], 1, 0);
      if (rp > 0)
      {
	    buffer[pos + 1] = '\0';
	
	    if (buffer[pos] == '\n')
        {
	      buffer[pos] = '\0';
	      pos--;
	    }
	    else if (buffer[pos] == '\r')
        {
	      buffer[pos] = '\0';
	      ccflush(sck);
	      return (pos);
	    }
	
	    pos++;
	
	    if (pos > size) return -2;
      }
      else
      {
	    return -1;
      }
    }
    
    if ((time(NULL) - now) > timeout)
    {
      buffer[pos] = '@';
      return -3;
    }
  }

  return 0;
}
*/

/*-------------------------------------------------------------- * 
 * Receive fixed sized binary data, 0 the buffer before using
 *---------------------------------------------------------------*/
/*
static int
ccrecv_sb(int sck, char *buffer, int size)
{
  int rp = 0, oflag;
  
  memset(buffer, 0, size);
  
  if (isReadable(sck))
  {
    oflag = fcntl(sck, F_GETFL);
    fcntl(sck, F_SETFL, oflag | O_NONBLOCK);
    rp = recv(sck, buffer, size, 0);
    fcntl(sck, F_SETFL, oflag);
  }

  return rp;
}
*/

/*-------------------------------------------------------------- * 
 * Send and receive fixed size
 *---------------------------------------------------------------*/
static int
ccsendrecv_s(int sck, char *cmd, char* response, int size)
{
  int resp;
  
  if (isWritable(sck) == 0) return 3;
  
  resp = ccsend(sck, cmd, strlen(cmd));
  if (resp <= 0)
  {
    return 1;
  }
  
  resp = ccrecv_s(sck, response, size);
  if (resp <= 0)
  {
    return 2;
  }
  
  return 0;
}

/*-------------------------------------------------------------- * 
 * Send and receive fixed size in timeout
 *---------------------------------------------------------------*/
/*
static int
ccsendrecv_st(int sck, char *cmd, char* response, int size, int timeout)
{
  int resp;
  
  if (isWritable(sck) == 0)
    return 3;
  
  resp = ccsend(sck, cmd, strlen(cmd));
  if (resp <= 0)
  {
    return 1;
  }
  
  resp = ccrecv_st(sck, response, size, timeout);
  if (resp <= 0)
  {
    return 2;
  }
  
  return 0;
}
*/

/*-------------------------------------------------------------- * 
 * Empty the socket
 *---------------------------------------------------------------*/
static int
ccflush(int sck)
{
  char buffer;
  while (isReadable(sck)) ccrecv(sck, &buffer, 1);

  return 0;
}



/**************/
/* CAMAC PART */
/**************/

static int axtoi(char *hexStg);

/*---------------------------------------------------------------*
 * Connect to the camac controler
 *---------------------------------------------------------------*/
int
caopen(char *hostname, int *skt)
{
  struct hostent *he;
  struct in_addr ad;
  char *ip;

  ip = (char *)malloc(15);
  he = gethostbyname (hostname);
  if(he)
  {
    //      printf("name: %s\n", he->h_name);
    while (*he->h_aliases) printf("alias: %s\n", *he->h_aliases++);
    while (*he->h_addr_list)
    {
	  bcopy(*he->h_addr_list++, (char *) &ad, sizeof(ad));
	  //  printf("address: %s\n", inet_ntoa(ad));
	  sprintf(ip,"%s",inet_ntoa(ad));
    }
  }
  else
  {
    printf("Unknown host \n");
    return 0;
  }

  *skt = ccconnect(ip,2000);
  free(ip);
  return *skt;
}

/*---------------------------------------------------------------*
 * Connect to the camac controler
 *---------------------------------------------------------------*/
int
caclose(int skt)
{
  return ccclose(skt);
}

/*-------------------------------------------------------------- * 
 * Defines external address
 *---------------------------------------------------------------*/
int
cdreg(int *ext, int b, int sck, int n, int a)
{
  *ext = 0;
  *ext =  (sck<<16) | ( (n<<8) | a);
  return 0;
}

/*-------------------------------------------------------------- * 
 * Short (16) single action
 *---------------------------------------------------------------*/
int
cssa(int f, int ext, short *dat, int *q)
{
  short n,a;
  int sck;
  sck = (ext>>16);
  n=(ext >> 8) & 0x00ff;
  a = (ext & 0x00ff);
  //printf("socket = %d n = %d a = %d \n",sck,n,a);
  return CNAF16(sck,n,a,f,q,dat);
}

/*-------------------------------------------------------------- * 
 * Long (24) single action
 *---------------------------------------------------------------*/
int
cfsa(int f, int ext, short *dat, int *q)
{
  short n,a;
  int sck;
  sck = (ext >> 16);
  n=(ext >> 8) & 0x00ff;
  a = (ext & 0x00ff);
  //printf("socket = %d n = %d a = %d \n",sck,n,a);
  return CNAF24(sck,n,a,f,q,dat);
}

/*-------------------------------------------------------------- * 
 * Crate clear
 *---------------------------------------------------------------*/
int
cccc(int sck)
{
  return CCLEAR(sck);
}

/*-------------------------------------------------------------- * 
 * Crate initialize
 *---------------------------------------------------------------*/
int
cccz(int sck)
{
  return CINIT(sck);
}

/*-------------------------------------------------------------- * 
 * Set/reset crate inhibit 
 *---------------------------------------------------------------*/
int
ccci(int sck,int l)
{
  return CINHIBIT(sck,l);
}

/*-------------------------------------------------------------- * 
 * Test status of previous operation 
 *---------------------------------------------------------------*/
int
ctstat(int sck, int *istat)
{
  short q, x;
  //int cstat;

  CTSTAT(sck, &q, &x);
  // printf("q = %d, x = %d \n",q,x);
  *istat = ( (q << 1) | x ) & 3;
  //printf("q = %d, x = %d istat = %d\n",q,x,*istat);
  return *istat;
}

/*-------------------------------------------------------------- * 
 * Execute a 24 bit CAMAC command; returns Q and DATA
 *---------------------------------------------------------------*/
short
CNAF24(int sck, short N, short A, short F, int *Q, short *DATA)
{
  char send_buff[256], receive_buff[256];
  int retcode = -1; // error
  char *token, steps[] = " \r\0";
  int d;
  
  sprintf(send_buff,"CFSA %d %d %d %x\r", F, N, A, *DATA);
  
  if (ccsendrecv_s(sck, send_buff, receive_buff, 255) != 0)
  {
    return retcode;
  }
  else
  {
    retcode = 0; // ok
  }
  
  // parse the receive_buff
  if (receive_buff != NULL)
  {
    token = strtok(receive_buff, steps);
    // printf(" > coda = %s < \n",token);
    if((token = strtok(NULL, steps))!=NULL)
    {
      //printf(" > Q    = %s < \n",token);
      *Q = atoi(token);
    }
    if((token = strtok(NULL, steps))!=NULL)
    {
      //printf(" > Data = %s < \n",token);
      d = axtoi(token);
      *DATA = d & 0x000000ff;
    }
  }

  return(retcode);
}

/*-------------------------------------------------------------- * 
 * Execute a 16 bit CAMAC command; returns Q and DATA
 *---------------------------------------------------------------*/
short
CNAF16(int sck, short N, short A, short F, int *Q, short *DATA)
{
  char send_buff[256], receive_buff[256];
  int retcode = -1; // error
  char *token, steps[] = " \r\0";
  int d;

  sprintf(send_buff,"CSSA %d %d %d %x\r", F, N, A, *DATA);
  
  if (ccsendrecv_s(sck, send_buff, receive_buff, 255) != 0)
  {
    return retcode;
  }
  else
  {
    retcode = 0; // ok
  }
  
  // parse the receive_buff
  if (receive_buff != NULL)
  {
    //printf(" > buffer = %s < \n",receive_buff);
    token = strtok(receive_buff, steps);
    //printf(" > coda = %s < \n",token);
    if((token = strtok(NULL, steps))!=NULL)
    {
      // printf(" > Q    = %s < \n",token);
      *Q = atoi(token);
    }
    if((token = strtok(NULL, steps))!=NULL)
    {
      //    printf(" > Data = %s < \n",token);
      d = axtoi(token);
      *DATA = d & 0x000000ff;
    }
  }

  return(retcode);
}

/*-------------------------------------------------------------- * 
 * Returns Q and X values from last access on bus
 *---------------------------------------------------------------*/
short
CTSTAT(int sck, short *Q, short *X)
{
  char send_buff[256], receive_buff[256];
  int retcode = -1; // error
  char *token, steps[] = " \r\0";

  sprintf(send_buff,"CTSTAT\r");
  
  if (ccsendrecv_s(sck, send_buff, receive_buff, 255) != 0)
  {
    return retcode;
  }
  else
  {
    retcode = 0; // ok
  }
   
  // parse the receive_buff
  if (receive_buff != NULL)
  {
    // printf(" > buffer = %s < \n",receive_buff);
    token = strtok(receive_buff, steps);
    // printf(" > coda = %s < \n",token);
    if((token = strtok(NULL, steps))!=NULL)
    {
      *Q = atoi(token);
      // printf(" > Q = %d < \n",*Q);
    }
    if((token = strtok(NULL, steps))!=NULL)
    {
      *X = atoi(token);
      // printf(" > X = %d < \n", *X);
    }
  }

  return(retcode);
}

/*-------------------------------------------------------------- * 
 * Generate dataway init
 *---------------------------------------------------------------*/
short
CINIT(int sck)
{
  int retcode;
  char send_buff[256], receive_buff[256];

  sprintf(send_buff, "CCCZ\r");
  retcode = ccsendrecv_s(sck, send_buff, receive_buff, 255);
  (void)retcode;

  return( atoi(receive_buff) );
}

/*-------------------------------------------------------------- * 
 * Generate crate clear
 *---------------------------------------------------------------*/
short
CCLEAR(int sck)
{
  int retcode;
  char send_buff[256], receive_buff[256];

  sprintf(send_buff, "CCCC\r");
  retcode = ccsendrecv_s(sck, send_buff, receive_buff, 255);
  (void)retcode;

  return( atoi(receive_buff) );
}

/*-------------------------------------------------------------- * 
 * Change dataway inhibit to specified value(0 or 1)
 *---------------------------------------------------------------*/
short
CINHIBIT(int sck, int I)
{
  int retcode;
  char send_buff[256], receive_buff[256];

  sprintf(send_buff, "CCCI %d\r",I);
  retcode = ccsendrecv_s(sck, send_buff, receive_buff, 255);
  (void)retcode;

  return( atoi(receive_buff) );
}

/*---------------------------------------------------------------*
Function gets the hex string and returns decimal value as an integer
 *---------------------------------------------------------------*/
static int
axtoi(char *hexStg)
{
  int n = 0;         // position in string
  int m = 0;         // position in digit[] to shift
  int count;         // loop index
  int intValue = 0;  // integer value of hex string
  int digit[5];      // hold values to convert
  while (n < 4)
  {
    if (hexStg[n]=='\0') break;
    if (hexStg[n] > 0x29 && hexStg[n] < 0x40 ) //if 0 to 9
	{
      digit[n] = hexStg[n] & 0x0f;            //convert to int
	}
     else if (hexStg[n] >='a' && hexStg[n] <= 'f') //if a to f
	 {
       digit[n] = (hexStg[n] & 0x0f) + 9;      //convert to int
	 }
     else if (hexStg[n] >='A' && hexStg[n] <= 'F') //if A to F
	 {
       digit[n] = (hexStg[n] & 0x0f) + 9;      //convert to int
	 }
     else break;
    n++;
  }
  count = n;
  m = n - 1;
  n = 0;
  while(n < count)
  {
    // digit[n] is value of hex digit at position n
    // (m << 2) is the number of positions to shift
    // OR the bits into return value
    intValue = intValue | (digit[n] << (m << 2));
    m--;   // adjust the position to set
    n++;   // next digit to process
  }

  return(intValue);
}
