program reset_motor

/*
  SNL  code to reset the step counter (rrbv)
  value every time the stepper motor hits the limit switch.
  The remaining steps are stored in the "missed_steps" record for
  reference.  Need to generalize this for any motor and any limit
  switch or home switch.
*/

option +c;
option +r;

#include "scan.h"

string motor_name;
assign motor_name to "name_{motor_name}.VAL";

short lls;
assign lls to "{motor_name}.LLS";
monitor lls;

short spmg;
assign spmg to "{motor_name}.SPMG";
monitor spmg;

short use_or_set;
assign use_or_set to "{motor_name}.SET";

int rrbv;
assign rrbv to "{motor_name}.RRBV";
monitor rrbv;

int rval;
assign rval to "{motor_name}.RVAL";

int missed_steps;
assign missed_steps to "{motor_name}_missed_steps.VAL";

ss reset_counter {
   
   state init {
     when () {
       pvGet(motor_name);
       printf("reset_motor %s: initializing  state code\n",motor_name);
     } state wait_lls
   }
   state wait_lls {
     when (lls == LIMIT_SWITCH_ON && rrbv != 0) {
       pvGet(motor_name);
       printf("reset_motor %s: low limit switch hit resetting counters\n",motor_name);
       pvGet(rrbv);
       missed_steps = rrbv;
       pvPut(missed_steps);
       use_or_set = SET;
       pvPut(use_or_set);
     } state stop
   }
   state stop {
     when () {
        printf("reset_motor %s: placed in STOP mode \n",motor_name);
        spmg = STOP;
        pvPut(spmg);
     } state reset_rval
   }
   state reset_rval {
     when (spmg == STOP && delay(0.025)) {
        printf("reset_motor %s: zeroing rval\n",motor_name);
       rval = 0;
       pvPut(rval);
     } state go
   }
   state go {
     when (delay(0.025)) {
        printf("reset_motor %s: placed in GO mode \n",motor_name);
       spmg = GO;
       pvPut(spmg);
     } state use
   }
   state use {
     when (spmg == GO && delay(0.025)) {
        printf("reset_motor %s: placed in USE mode \n",motor_name);
       use_or_set = USE;
       pvPut(use_or_set);
        printf("reset_motor %s: done resetting\n",motor_name);
     } state wait_lls
   }
}
