program harp_scan_generic

/*
  SNL  code to set the {motor_name} motor moving and record
  the scaler data

  The harp starts at its low limit switch (lls) and moves to position A
  and speed_to_a.  Then it moves to position B at speed_to_b.  While moving
  to B the scaler is read out at every scaler_acqt and the results are 
  written to a file.  Once the motor makes it to B, then the motor is 
  retracted.

*/

option -c;
option +r;
option -a;
option +d;

#include "scan.h"
%%#include "epics_b_struct.h"
#define sleep_delay(SltX) taskDelay(SltX*sysClkRateGet())

/* motor records  */

short lls;
assign lls to "{motor_name}.LLS";
monitor lls;

short hls;
assign hls to "{motor_name}.HLS";
monitor hls;

short movn;
assign movn to "{motor_name}.MOVN";
monitor movn;

short spmg;
assign spmg to "{motor_name}.SPMG";
monitor spmg;

short use_or_set;
assign use_or_set to "{motor_name}.SET";

float harp_position;
assign harp_position to "{motor_name}.RBV";
monitor harp_position;

float rmp;
assign rmp to "{motor_name}.RMP";

float harp_speed;
assign harp_speed to "{motor_name}.VELO";

float harp_absolute_move;
assign harp_absolute_move to "{motor_name}.VAL";

float harp_relative_move;
assign harp_relative_move to "{motor_name}.RLV";

string motor_name;
assign motor_name to "name_{motor_name}.VAL";

/* scaler records...need to macro this so "any" scaler record can
   be used.  */

/* long scaler_data[16]; */
/* ================================================================ */

long scaler_datasc1[16];
long scaler_datasc4[16];

assign scaler_datasc1[0] to "scaler_c.S1";
assign scaler_datasc1[1] to "scaler_cS2b.VAL";
assign scaler_datasc1[2] to "scaler_c.S3";
assign scaler_datasc1[3] to "scaler_c.S4";
assign scaler_datasc1[4] to "scaler_c.S5";
assign scaler_datasc1[5] to "scaler_c.S6";
assign scaler_datasc1[6] to "scaler_c.S7";
assign scaler_datasc1[7] to "scaler_c.S8";
assign scaler_datasc1[8] to "scaler_c.S9";
assign scaler_datasc1[9] to "scaler_c.S10";
assign scaler_datasc1[10] to "scaler_c.S11";
assign scaler_datasc1[11] to "scaler_c.S12";
assign scaler_datasc1[12] to "scaler_c.S13";
assign scaler_datasc1[13] to "scaler_c.S14";
assign scaler_datasc1[14] to "scaler_c.S15";
assign scaler_datasc1[15] to "scaler_c.S16";

assign scaler_datasc4[0] to "scaler.S1";
assign scaler_datasc4[1] to "scalerS2b.VAL";
assign scaler_datasc4[2] to "scaler.S3";
assign scaler_datasc4[3] to "scaler.S4";
assign scaler_datasc4[4] to "scaler.S5";
assign scaler_datasc4[5] to "scaler.S6";
assign scaler_datasc4[6] to "scaler.S7";
assign scaler_datasc4[7] to "scaler.S8";
assign scaler_datasc4[8] to "scaler.S9";
assign scaler_datasc4[9] to "scaler.S10";
assign scaler_datasc4[10] to "scaler.S11";
assign scaler_datasc4[11] to "scaler.S12";
assign scaler_datasc4[12] to "scaler.S13";
assign scaler_datasc4[13] to "scaler.S14";
assign scaler_datasc4[14] to "scaler.S15";
assign scaler_datasc4[15] to "scaler.S16";


/* ================================================================ */

float scaler_tp;
assign scaler_tp to "scaler_c.TP";

short scaler_cnt;
assign scaler_cnt to "scaler_c.CNT";
monitor scaler_cnt;

short scaler_mode;
assign scaler_mode to "scaler_c_mode.VAL";

short display_mode;
assign display_mode to "display_c_mode.VAL";

/* scan specific records */

float command;
assign command to "{motor_name}_command";
monitor command;

float position_a;
assign position_a to "{motor_name}_position_a";
monitor position_a;

float position_b;
assign position_b to "{motor_name}_position_b";
monitor position_b;

float speed_to_a;
assign speed_to_a to "{motor_name}_speed_to_a";

float speed_to_b;
assign speed_to_b to "{motor_name}_speed_to_b";

float scaler_acq_time;
assign scaler_acq_time to "{motor_name}_acq_time";

short   scan_flag;
assign  scan_flag to "{motor_name}_scan_flag.VAL";

string fname;
assign fname to "{motor_name}_scan_flag.ZNAM";

char cfname[1024];
char shortname[1024];
char cmotor_name[1024];

/* file/local variables */

char tmp_rec[24];
char tmp_name[50];
int  tmp_int;
float tmp_f;

short display_mode_init;
short scaler_mode_init;
float scaler_tp_init;
float harp_speed_init;
float harp_position_init;

int fd;
int i;

int delayTime;

int retStatus;

double timeWaited = 0;

%% extern int get_e_name(int, char *);
%% extern int get_r_name(int, char *);
%% extern int scp_clon01(char *, char*, int);

/* state code  */
ss harp_scan_snc {
   
   state init {
     when () {

/* ========================================================= */

   if(  ( ! (strcmp(motor_name,"harp_2c21"))) ||  ( ! (strcmp(motor_name,"harp_tagger"))) )
   {

   }
   if(  ( ! (strcmp(motor_name,"harp_2H02A"))) )
   {
       pvStopMonitor( scaler_cnt );
       pvAssign(scaler_tp, "scaler.TP"); 
       pvAssign(scaler_cnt, "scaler.CNT"); 
       pvAssign(scaler_mode, "scaler_mode.VAL"); 
       pvAssign(display_mode, "display_mode.VAL"); 
       pvMonitor( scaler_cnt );
       timeWaited = 0.0;
       while( ( (	!pvAssigned (scaler_tp  ) || !pvConnected(scaler_tp  ) ) || 
	        (	!pvAssigned (scaler_cnt  ) || !pvConnected(scaler_cnt  ) ) || 
	        (	!pvAssigned (scaler_mode  ) || !pvConnected(scaler_mode ) ) ||
	        (	!pvAssigned (display_mode  ) || !pvConnected(display_mode ) ) )
	     && (timeWaited < 10) ) {
		printf( "Scaler Connect: waiting %f \n", timeWaited );
		timeWaited = timeWaited + 1.0;
                epicsThreadSleep( 1.0 );
       }
       if( timeWaited >= 10 ) { 
	printf( "Error : Timed out waiting for scaler to connect \n" );
       }
   }

/* ========================================================= */



        harp_relative_move = 0.0;
        pvPut(harp_relative_move);
       pvGet(motor_name);
	for (tmp_int = 0;  (get_e_rec(tmp_int,tmp_rec)); tmp_int++) {
	   tmp_float[tmp_int] = 0.0;
           pvAssign(tmp_float[tmp_int], tmp_rec);
           pvGet(tmp_float[tmp_int]);
           tmp_f = tmp_float[tmp_int];
        }
       printf("harp_scan: %s initializing  state code\n", motor_name);
     } state wait_command
   }
   state wait_command {
     when (command == SCAN) {

        printf("harp_scan: %s command = %f\n",motor_name, command);

        scan_flag = 1;
        pvPut(scan_flag);


/* ========================================================= */

   if(  ( ! (strcmp(motor_name,"harp_2c21"))) ||  ( ! (strcmp(motor_name,"harp_tagger"))) )
   {

   }
   if(  ( ! (strcmp(motor_name,"harp_2H02A"))) )
   {
       pvStopMonitor( scaler_cnt );
       pvAssign(scaler_tp, "scaler.TP"); 
       pvAssign(scaler_cnt, "scaler.CNT"); 
       pvAssign(scaler_mode, "scaler_mode.VAL"); 
       pvAssign(display_mode, "display_mode.VAL"); 
       pvMonitor( scaler_cnt );
       timeWaited = 0.0;
       while( ( (	!pvAssigned (scaler_tp  ) || !pvConnected(scaler_tp  ) ) || 
	        (	!pvAssigned (scaler_cnt  ) || !pvConnected(scaler_cnt  ) ) || 
	        (	!pvAssigned (scaler_mode  ) || !pvConnected(scaler_mode ) ) ||
	        (	!pvAssigned (display_mode  ) || !pvConnected(display_mode ) ) )
	     && (timeWaited < 10) ) {
		printf( "Scaler Connect: waiting %f \n", timeWaited );
		timeWaited = timeWaited + 1.0;
                epicsThreadSleep( 1.0 );
       }
       if( timeWaited >= 10 ) { 
	printf( "Error : Timed out waiting for scaler to connect \n" );
       }
   }

/* ========================================================= */


/* store old values so the hardware can be restored post scan  */
        pvGet(harp_speed);
        harp_speed_init = harp_speed;

        pvGet(scaler_tp);
        scaler_tp_init = scaler_tp;

        pvGet(scaler_mode);
        scaler_mode_init = scaler_mode;

        pvGet(display_mode);
        display_mode_init = display_mode;

	pvGet(harp_position);
        harp_position_init = harp_position;

/* open the file */
	strcpy(cmotor_name,motor_name);
        fd = open_file(&cfname,&cmotor_name, &shortname);
	strcpy(fname,cfname);
        pvPut(fname);

/* retract the harp to low limit switch */
	pvGet(speed_to_a);
	harp_speed = speed_to_a;
	pvPut(harp_speed);

	harp_absolute_move = -5.;
	pvPut(harp_absolute_move);
	command = 0;
        pvPut(command);
     } state wait_lls
   }
   state wait_lls {    
     when (lls == LIMIT_SWITCH_ON) {
        printf("harp_scan: %s wait_lls state low limit swithc hit\n",motor_name);
     } state start_move_to_a
   }
   state start_move_to_a {    
     when (delay(0.5)) {
        printf("harp_scan: %s starting move to a position\n",motor_name);
	pvGet(speed_to_a);
	harp_speed = speed_to_a;
	pvPut(harp_speed);

	pvGet(position_a);
        harp_absolute_move = position_a;
        pvPut(harp_absolute_move);
     } state write_beam_conf
   }
   state write_beam_conf {
     when () {
      /*write magnet settings to the file*/
        printf( "Debigging\n" );
	for (tmp_int = 0;  (get_e_rec(tmp_int,tmp_rec) && get_e_name(tmp_int,tmp_name)); tmp_int++) {
	   retStatus = pvAssign(tmp_float[tmp_int], tmp_rec);
	   printf( "Return from pvAssign is %d for variable number %d \n", retStatus, tmp_int );

	   timeWaited = 0.0;
	   while( (	!pvAssigned ( tmp_float[tmp_int] ) 
	            ||  !pvConnected( tmp_float[tmp_int] ) ) 
	          && (timeWaited < 2) ) {
		printf( "waiting %f \n", timeWaited );
		timeWaited = timeWaited + 1.0;
                epicsThreadSleep( 1.0 );
	   }
	printf( "Connected or timed out\n" );
/*	delayTime = 1 * sysClkRateGet(); */
/*	taskDelay( delayTime ); */
/*	printf( "record name is <%s>\n",tmp_rec );  */
           pvGet(tmp_float[tmp_int]);
           tmp_f = tmp_float[tmp_int];
           printf("# %50s: %24s: %f\n",tmp_name, tmp_rec,tmp_f); 
           fdprintf(fd,"# %50s: %24s: %f\n",tmp_name, tmp_rec,tmp_f); 
        }
     } state start_scan
   }
   state start_scan {
     when (harp_position >= (position_a - DELTA) && movn == DONE) {

        printf("harp_scan: %s start scan state moving to %f\n", 
                 motor_name,position_b);
/* set up the scaler */
        scaler_mode = ONESHOT;
        pvPut(scaler_mode);
	pvGet(scaler_acq_time);
        scaler_tp = scaler_acq_time;
        pvPut(scaler_tp);
        scaler_cnt = DONE;
        pvPut(scaler_cnt);

/* set up the motor */
	pvGet(speed_to_b);
	harp_speed = speed_to_b;
	pvPut(harp_speed);

	pvGet(position_b);
        harp_absolute_move = position_b;
        pvPut(harp_absolute_move);

        scaler_cnt = COUNT;
        pvPut(scaler_cnt);
        printf( "Will go to write scaler (daq_write) \n" );
     } state daq_write
   }
   state daq_write {
     when (scaler_cnt == DONE && harp_position > position_a && harp_position < position_b) {
/*       printf( "Count done \n" ); */
       pvGet(rmp);
       fdprintf(fd,"%f ", harp_position);

/* ========================================== */

       if(  ( ! (strcmp(cmotor_name,"harp_2c21"))) ||  ( ! (strcmp(cmotor_name,"harp_tagger"))) )
       {
	       for (i=0;i<16;i++) {
	          pvGet(scaler_datasc1[i]);
	          fdprintf(fd,"%d ", scaler_datasc1[i]);
	       }
       }
       if(  ( ! (strcmp(motor_name,"harp_2H02A"))) )
       {
/*	printf("Writing scalers for harp_2H02A \n" ); */
	       for (i=0;i<16;i++) {
	          pvGet(scaler_datasc4[i]);
	          fdprintf(fd,"%d ", scaler_datasc4[i]);
	       }
       }
/*
       for (i=0;i<16;i++) {
          pvGet(scaler_data[i]);
          fdprintf(fd,"%d ", scaler_data[i]);
       }
*/

/* ========================================== */

       fdprintf(fd,"%f ", rmp);
       fdprintf(fd,"\n");

/* start the scaler again */
       scaler_cnt = COUNT;
       pvPut(scaler_cnt);
     } state daq_write

     when (hls == LIMIT_SWITCH_ON) {
       printf("end of harp_{motor_name} scan\n");
     } state end_scan
     when (harp_position >= (position_b -DELTA) && movn == DONE) {
       printf("end of harp_{motor_name} scan\n");
     } state end_scan
   }
   state end_scan {
     when () {
       spmg = 0;
       pvPut(spmg);

       pvGet(speed_to_a);
       harp_speed = speed_to_a;
       pvPut(harp_speed);

       harp_absolute_move = -100.0;
       pvPut(harp_absolute_move);

       spmg = 3;
       pvPut(spmg);

/*close the file  and scp to mcc*/
      if ((fd > 0) && (fd != ioGlobalStdGet(1)) ) {
         close(fd);
         scp_clon01(shortname, motor_name, 5);
      }

     } state restore_hardware
   }
   state restore_hardware {
     when(lls == LIMIT_SWITCH_ON) {
        harp_speed = harp_speed_init;
        pvPut(harp_speed);

        scaler_tp = scaler_tp_init;
        pvPut(scaler_tp);

        scaler_mode = scaler_mode_init;
        pvPut(scaler_mode);

        display_mode = display_mode_init;
        pvPut(display_mode);

        scaler_cnt = COUNT;
        pvPut(scaler_cnt);
/*
        harp_absolute_move = harp_position_init;
        pvPut(harp_absolute_move);
*/
	scan_flag = 0;
	pvPut(scan_flag);
     } state wait_command
   }
}
/* ---------------------------------------------------------------------- */
/* C functions                                                            */
/* ---------------------------------------------------------------------- */

%%#include <time.h>
%%#include <vxWorks.h>
%%#include <stdio.h>
%%#include <string.h>
%%#include <bootLib.h>
%%#include <ioLib.h>
%%#include <remLib.h>
%%#include <envLib.h>
%%#include <errnoLib.h>

/* Max Environment variable length (bytes) */ 
%%#define EGR_MAX_ENV_LENGTH     8192

/* Default port for cmd deamon on remote host (/etc/services) */
%%#define EGR_HOST_DEFAULT_PORT   514

%{

int get_e_rec(int i, char *tmp_char) 
{
int iret=0;
     if (strcmp(hallb_string[i].epics_name,"EOL") != 0) {
        strcpy(tmp_char, hallb_string[i].epics_name); 
        iret = 1;
     } else {
        iret = 0;
     } 
     return iret;
}
int get_e_name(int i, char *tmp_char) 
{
int iret=0;
     if (strcmp(hallb_string[i].real_name,"EOL") != 0) {
        strcpy(tmp_char, hallb_string[i].real_name); 
        tmp_char = hallb_string[i].real_name;
	iret = 1;
     } else {
        iret = 0;
     }
     return iret;
}
int open_file(char *fname, char *motor_name, char *shortname)
/* ------------------------------------------------------------------------ */
{
  int fd;
  time_t calTime;
  struct tm *lclTimePtr;
  char fileDate[18];
  char thename[150];

    time( &calTime );
    lclTimePtr = localtime( &calTime );

/* add an hour because of DST and ioc time one hour behind */

/*    lclTimePtr->tm_hour++; */

    fileDate[0] = '\0'; 
    thename[0] = '\0';
    shortname[0] ='\0'; 

    strftime(&fileDate[0], 18, "%m-%d-%y_%H:%M:%S", lclTimePtr);

    strcpy( fname, fileDate );

    strcpy(shortname, motor_name);
    strcat(shortname, "_");
    strcat(shortname, fname);
    strcat(shortname, ".txt" );

/*    strcpy(thename, "/home/epics/data/e_scans/"); */
    strcpy(thename, "/home/epics/DATA/HARP_SCANS/");
    strcat(thename, motor_name);
    strcat(thename, "/");

    strcat(thename, shortname);


    printf("creating : %s\n",thename);

    fd = creat(thename,0);
    if (fd == ERROR)
    {
      printf("Can't open %s\n",thename);
      fd = ioGlobalStdGet(1);
    }
    printf("fd = %d\n",fd);

  return fd;
}


/* External declarations */
extern void printErrno(int);
extern BOOT_PARAMS sysBootParams;

STATUS
scp_clon01(char *harpscan_file, char* mot_name,  int sleep_time)
{

  int rfd;

  char rhost[BOOT_HOST_LEN], ruser[BOOT_USR_LEN];
  char rstring[512];

  /* Get remote host info */
  strcpy(rhost,sysBootParams.hostName);

  /* Get remote user info */
  strcpy(ruser,sysBootParams.usr);

  /* Construct the remote command */
  sprintf(rstring,"sleep %i;scp /home/epics/DATA/HARP_SCANS/%s/%s epics@opsll.acc.jlab.org:/usr/opsdata/harpData/HallB/%s  &",
      sleep_time, mot_name, harpscan_file, harpscan_file);

   printf("SCP CMD: %s\n", rstring);

  /* Set local user to the same as remote user*/
  iam(ruser,NULL);

  printf("host = %s  user = %s     cmd = %s\n",rhost,ruser,rstring);

  /* Issue the remote command */
  rfd = rcmd(rhost,EGR_HOST_DEFAULT_PORT,ruser,ruser,rstring,0);

  if(rfd > 0) {  /* Read the result */

    printf("harp_scan_generic: file scp to mcc opsll\n");


  } else {  /* PrintDe the error */
    printf("harp_scan_generic: ERROR: ");
    printErrno(errno);
    return(ERROR);
  }

  /* Close file descriptor */
  close(rfd);

  return(OK);

}

}%


