/**************************************************************************************
*
*  moller_oplog_remote.c  -  execute a script on clon01 to make a Moeller log entry 
*
*  Author: Hovanes Egiyan
*          Jefferson Lab 
*          Mar 2003
*
*  Revision  1.0 - Initial Revision 
*
*  Inputs:       None
*
*  Returns:    Nothing 
*/

#include <vxWorks.h>
#include <stdio.h>
#include <string.h>
#include <bootLib.h>
#include <ioLib.h>
#include <remLib.h>
#include <envLib.h>
#include <errnoLib.h>

/* Max Environment variable length (bytes) */ 
#define EGR_MAX_ENV_LENGTH     8192

/* Default port for cmd deamon on remote host (/etc/services) */
#define EGR_HOST_DEFAULT_PORT   514

/* External declarations */
extern void printErrno(int);
extern BOOT_PARAMS sysBootParams;

STATUS
moller_oplog_remote( )
{

  int rfd;

  char rhost[BOOT_HOST_LEN], ruser[BOOT_USR_LEN];
  char rstring[1024];

  /* Get remote host info */
  strcpy(rhost,sysBootParams.hostName);

  /* Get remote user info */
  /*  strcpy(ruser,sysBootParams.usr); */
  strcpy(ruser,"clasrun");

  /* Construct the remote command */
  sprintf(rstring,"/home/hovanes/EPICS/app/moller_setup/scripts/moller_oplog.pl 'Auto'  >& /dev/null/ &");
  /* Set local user to the same as remote user*/
  /*  iam(ruser,NULL);  */

  printf("host = %s  user = %s     cmd = %s\n",rhost,ruser,rstring); 

  /* Issue the remote command */
  rfd = rcmd(rhost,EGR_HOST_DEFAULT_PORT,ruser,ruser,rstring,0);

  if(rfd > 0) {  /* Read the result */

    printf("moller_oplog_remote: command successful\n");


  } else {  /* Print the error */
    printf("moller_oplog_remote: ERROR: ");
    printErrno(errno);
    return(ERROR);
  }

  /* Close file descriptor */
  close(rfd);

  return(OK);

}

