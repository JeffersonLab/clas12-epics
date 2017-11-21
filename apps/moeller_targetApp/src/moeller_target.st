program moeller_target

option +c;  /* wait for db connections */

/* define target positions */

// Prior to November 2017:
//#define LEFT_FOIL        5.45
//#define EMPTY_POSITION   3.44
//#define RIGHT_FOIL       0.60
//#define ALUMINUM         2.35

// Shifted 0.06 inches beam-left based on Stpan's measurements:
#define LEFT_FOIL        5.39
#define EMPTY_POSITION   3.38
#define RIGHT_FOIL       0.54
#define ALUMINUM         2.29

#define LARGE_POSITIVE  20.00
#define LARGE_NEGATIVE -20.00

/* define command values  */

#define  DO_NOTHING         0
#define  CALIBRATE_CMND     1
#define  MOVE_2_LEFT_CMND  11
#define  MOVE_2_MT_CMND    12
#define  MOVE_2_RIGHT_CMND 13
#define  MOVE_2_AL_CMND    14

#define  CALIBRATE    1
#define  RETRACT      2
#define  RESET        3

/* define status values */

#define  CALIBRATING_STATUS 1
#define  AT_LEFT_STATUS     11
#define  AT_MT_STATUS       12
#define  AT_RIGHT_STATUS    13
#define  AT_AL_STATUS       14
#define  MOVING_STATUS      99

#define  OK                 1
#define  NOT_OK             0
#define  INDETERMINATE     -1

/* monitor signals */

double  command;
assign  command           to "moller_target_command.VAL";
monitor command;

double  status_left;
assign  status_left       to "moller_target_left.VAL";

double  status_empty;
assign  status_empty      to "moller_target_empty.VAL";

double  status_right;
assign  status_right      to "moller_target_right.VAL";

double  status_al;
assign  status_al         to "moller_target_al.VAL";

double  calib_status;
assign  calib_status      to "moller_target_calib.VAL";
monitor calib_status;

short   target_set;
assign  target_set      to "moeller_target.SET";

double  target_off;
assign  target_off      to "moeller_target.OFF";

double  target_rval;
assign  target_rval      to "moeller_target.RVAL";

double  target_rrbv;
assign  target_rrbv      to "moeller_target.RRBV";

double  target_val;
assign  target_val      to "moeller_target.VAL";

double   target_rlv;
assign  target_rlv      to "moeller_target.RLV";

double  target_rbv;
assign  target_rbv      to "moeller_target.RBV";
monitor target_rbv;

short   target_spmg;
assign  target_spmg     to "moeller_target.SPMG";

short   target_hls;
assign  target_hls      to "moeller_target.HLS";
monitor target_hls;

short   target_lls;
assign  target_lls      to "moeller_target.LLS";
monitor target_lls;

short   target_dmov;
assign  target_dmov      to "moeller_target.DMOV";
monitor target_dmov;

float sub_command;
double ldiff;
double rdiff; 
double mtdiff;
int n_moves;
/*--------------------------------------------------------------*/
/* moeller target stepper motor sequencer                       */
/*                                                              */
/*--------------------------------------------------------------*/

ss moller_target
{

  state init 
  {
    when ()
    {
      calib_status = NOT_OK;
      sub_command = 99;
    } state get_command
  }  

/* Now keep probing for commands and take appropriate action */

  state get_command
  {
    when ( command == DO_NOTHING && delay(10) ) 
    {
/*       printf("Moller target cmnd DO_NOTHING\n");   */
    } state check_location

    when ( command == CALIBRATE_CMND )
    {
	sub_command = RETRACT;
        printf("Calibrating the moeller target motor\n"); 
    } state retract

    when (command == MOVE_2_MT_CMND) 
    {
        printf("Moving to empty target position\n");
    } state go_2_empty

    when (command == MOVE_2_LEFT_CMND) 
    {
        printf("Moving to left target position\n");
    } state go_2_left

    when (command == MOVE_2_RIGHT_CMND) 
    {
        printf("Moving to right target position\n");
    } state go_2_right

    when (command == MOVE_2_AL_CMND) 
    {
        printf("Moving to aluminum target position\n");
    } state go_2_AL

  }
  
  state retract
  {
    when ()
    {
	puts("moeller target going to low limit switch");

	if (target_lls != 1) 
        {
	  target_spmg=0;
	  pvPut(target_spmg);

	  target_rlv = LARGE_NEGATIVE;
          pvPut(target_rlv);

	  target_spmg=3;
	  pvPut(target_spmg);
        }

    } state wait_lls 
  }

  state wait_lls
  {
    when (target_lls == 1)
    {
     printf("moller low limit switch hit\n");
    } state reset
  }
  state reset 
    {
      when (delay(1.0))
        {
/*	target_spmg=0;
	pvPut(target_spmg); */

	target_set=1;
	pvPut(target_set);

	target_rval=0.0;
	pvPut(target_rval);

	target_val=0.0;
	pvPut(target_val);

 	target_off=0.0;
	pvPut(target_off); 

	target_set=0;
	pvPut(target_set);
	
/*	target_spmg=3;
	pvPut(target_spmg); */

	command = MOVE_2_MT_CMND;
	pvPut(command);

        calib_status = OK;
	pvPut(calib_status);

        n_moves=0;
		
    } state go_2_empty
  }
  state go_2_empty
  {
     when(delay(1) && target_dmov==1)
     {
	target_val = EMPTY_POSITION;
        pvPut(target_val);
     } state wait_done
  }
  state wait_done
  {
      when(target_dmov==1)
      {
	command = DO_NOTHING;
	pvPut(command);

        n_moves++;

     } state get_command
  }
  state go_2_left
  {
     when()
     {
	target_val = LEFT_FOIL;
        pvPut(target_val);
	
     } state wait_done
  }
  state go_2_right
  {
     when()
     {
	target_val = RIGHT_FOIL;
        pvPut(target_val);
	
     } state wait_done
  }
  state go_2_AL
  {
     when()
     {
	target_val = ALUMINUM;
        pvPut(target_val);
     } state wait_done
  }
  state check_location
  {
     when()
     {

       rdiff =  RIGHT_FOIL     - target_rbv;
       mtdiff = EMPTY_POSITION - target_rbv;
       ldiff =  LEFT_FOIL      - target_rbv;

       if ( rdiff < 0.25 && rdiff > -0.25 )
       {
         status_right = OK;
         status_empty = NOT_OK;
         status_left  = NOT_OK;
       } else if ( mtdiff < 0.25 && mtdiff > -0.25 )
       {
         status_empty = OK;
         status_right = NOT_OK;
         status_left  = NOT_OK;
       } else if ( ldiff < 0.25 && ldiff > -0.25 )
       {
         status_left  = OK; 
         status_empty = NOT_OK;
         status_right = NOT_OK;
       } else
       {
         status_left  = NOT_OK; 
         status_empty = NOT_OK;
         status_right = NOT_OK;
       }
      pvPut(status_left);
      pvPut(status_empty);
      pvPut(status_right);

     if (n_moves > 20) 
     {
        calib_status = NOT_OK;
	pvPut(calib_status);
     }
     } state get_command
  }
}










