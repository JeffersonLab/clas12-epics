program moller_setup

option -c;

#include "moller_setup.h"

float command;
assign command to "moller_command";
monitor command;

float collimator_command;
assign collimator_command to "command1";

float status;
assign status to "moller_system_status";
monitor status;

/* moller quads */

float energy;
assign energy to "MBSY2C_energy";

int dynab_reverse;
assign dynab_reverse to "DYNABREVERSE";

int dynab_forward;
assign dynab_forward to "DYNABFORWARD";

int dynab_on;
assign dynab_on to "DYNABON";

int dynac_on;
assign dynac_on to "DYNACON";

int dynab_off;
assign dynab_off to "DYNABOFF";

int dynac_off;
assign dynac_off to "DYNACOFF";

float dynab_sug_set;
assign dynab_sug_set to "dynab_sug_set";

float dynac_sug_set;
assign dynac_sug_set to "dynac_sug_set";

float dynab_set_i;
assign dynab_set_i to "DYNABSETI";

float dynac_set_i;
assign dynac_set_i to "DYNACSETI";

float dynab_read_i;
assign dynab_read_i to "hallb_sf_xy560_0_14";
monitor dynab_read_i;

float dynac_read_i;
assign dynac_read_i to "hallb_sf_xy560_0_18";
monitor dynac_read_i;

float tagger_current;
assign tagger_current to "TMIRBCK";
monitor tagger_current;

/* moller helmholtz coil */

float helmholtz_command;
assign helmholtz_command to "kepco_command";

float helmholtz_negative;
assign helmholtz_negative to "kepco_negative";
monitor helmholtz_negative;

float helmholtz_positive;
assign helmholtz_positive to "kepco_positive";
monitor helmholtz_positive;

/* target records */

float target_calibrated;
assign target_calibrated to "moller_target_calib";
monitor target_calibrated;

float target_command;
assign target_command to "moller_target_command";

float moller_target_left;
assign moller_target_left to "moller_target_left";
monitor moller_target_left;

float moller_target_right;
assign moller_target_right to "moller_target_right";
monitor moller_target_right;

float moller_target_al;
assign moller_target_al to "moller_target_al";
monitor moller_target_al;

float moller_target_empty;
assign moller_target_empty to "moller_target_empty";
monitor moller_target_empty;

float target_motor;
assign target_motor to "moeller_target.MOVN";
monitor target_motor;

/* SC HIGH Voltage controls  */

float sc_hv_on[5];

int sc_map[5];


assign sc_hv_on[0] to "B/HVON_SET_12_03";
assign sc_hv_on[1] to "B/HVON_SET_12_04";
assign sc_hv_on[2] to "B/HVON_SET_12_06";
assign sc_hv_on[3] to "B/HVON_SET_05_09";
assign sc_hv_on[4] to "B/HVON_SET_05_10";

/* EC high voltage */

float ec_hv_on[8];

/* assign ec_hv_on[0] to "B/HVON_SET_05_01"; replaced by CAEN */
assign ec_hv_on[0] to "B/HVON_SET_01_04";
assign ec_hv_on[1] to "B/HVON_SET_05_02";
assign ec_hv_on[2] to "B/HVON_SET_05_03";
assign ec_hv_on[3] to "B/HVON_SET_05_04";
assign ec_hv_on[4] to "B/HVON_SET_05_05";
assign ec_hv_on[5] to "B/HVON_SET_05_06";
assign ec_hv_on[6] to "B/HVON_SET_05_07";
assign ec_hv_on[7] to "B/HVON_SET_05_08";

/* moller epics polarization records */

float daq_control;
assign daq_control to "moller_accumulate";

float daq_reset;
assign daq_reset to "moller_reset";

string status_string_1;
assign status_string_1 to "moller_system_string_1.VAL";

string status_string_2;
assign status_string_2 to "moller_system_string_2.VAL";

/* OTR records */

int otr1_status;
assign otr1_status to "otr1";

int otr2_status;
int otr2_init_status;
assign otr2_status to "otr2";

int otr1_command;
assign otr1_command to "otr1";

int otr2_command;
assign otr2_command to "otr2";

int i_sc_hv;
int i_ec_hv;

ss moller_conf {
    state init {
      when () {
	printf("Moller setup state code initialized\n");
	status = STATE_INIT;
	pvPut(status);
        sc_map[0] = 3;
        sc_map[1] = 4;
        sc_map[2] = 6;
        sc_map[3] = 9;
        sc_map[4] = 10;
      } state get_command
    }
    state get_command {
	when (command == CONFIGURE_LEFT_NEG) {
           strcpy(status_string_1,"Starting Moller Hardware configuration");
           pvPut(status_string_1);
           strcpy(status_string_2,"MAKE SURE DC HV IS OFF!!!");
           pvPut(status_string_2);
	   printf("starting moller run--- left target negative helmholtz\n");
           i_sc_hv = 5;
           i_ec_hv = 8;
        } state get_tagger_status

	when (command == CONFIGURE_LEFT_POS) {
	   printf("starting moller run---left target positive helmholtz\n");
           i_sc_hv = 5;
           i_ec_hv = 8;
        } state get_tagger_status

	when (command == CHANGE_HELM_POS) {
	   printf("changing helmholtz polarity to POS---\n");
        } state change_helm_pos

	when (command == CHANGE_HELM_NEG) {
	   printf("changing helmholtz polarity to NEG---\n");
        } state change_helm_neg

        when (command == BACKOUT) {
           printf("ending moller run.....\n");
        } state stop_daq

        when (command == DO_NOTHING && status < 10 && delay(10)) {
           strcpy(status_string_1,
            "First: Turn DCHV OFF & Tune beam to");   
/*            "First: Turn DCHV OFF ");     */
           pvPut(status_string_1);
           strcpy(status_string_2,
/*            "Then: Configure Hardware");  */
            "TAGGER DUMP....THEN: Conf. Hardware");    
           pvPut(status_string_2);
        } state get_command
        when (command == DO_NOTHING && status > 10 && delay(10)) {
	   ;
        } state get_command
    }

    state get_tagger_status {
/*      when(tagger_current >= 0) {   */
      when(tagger_current > 200) {   
           strcpy(status_string_1,"Tagger Magnet Energized-GOOD!");
           pvPut(status_string_1);
           strcpy(status_string_2,"Make sure DVHV is off!!!!!");
           pvPut(status_string_2);
      } state get_otr_status
/*      when (tagger_current < 0) {   */
      when (tagger_current < 200) {   
        strcpy(status_string_1,"Tagger Magnet NOT Energized!!!");
        pvPut(status_string_1);
        strcpy(status_string_2,"Tell MCC to tune beam to TAGGER DUMP");
        pvPut(status_string_2);
        status = STATE_INIT;
        pvPut(status);
        command = DO_NOTHING;
        pvPut(command);
      } state get_command
    }

    state get_otr_status {
      when () {
           strcpy(status_string_1,"Checking status of OTR2");
           pvPut(status_string_1);
        pvGet(otr2_status);
        otr2_init_status = otr2_status;
	if (otr2_init_status == 0) {
           strcpy(status_string_2,"OTR2 was found retracted");
        } else {
           strcpy(status_string_2,"OTR2 was found inserted");
        }
        pvPut(status_string_2);
      } state sc_hv_down
    }

    state sc_hv_down {
      when (i_sc_hv <= 0) {
          sprintf(status_string_2,"Done with SC mainframes...");
          pvPut(status_string_2);
      } state ec_hv_down
      when (delay(7)) {
       i_sc_hv--;
       sprintf(status_string_1,"Turning off SC %i mainframe",sc_map[i_sc_hv]);
       pvPut(status_string_1);
       sprintf(status_string_2,"HV alarms will sound...waiting 7secs");
       pvPut(status_string_2);
       sc_hv_on[i_sc_hv] = OFF;
       if (pvConnected(sc_hv_on[i_sc_hv])) {
         pvPut(sc_hv_on[i_sc_hv]);
       } else {
         sprintf(status_string_1,"SC mainframe %i not responding",sc_map[i_sc_hv]);
         pvPut(status_string_1);
       }
      } state sc_hv_down
    }
    state ec_hv_down {
      when (i_ec_hv <= 0) {
           strcpy(status_string_1,"Make sure DC HV is OFF!!!");
           pvPut(status_string_1);
           strcpy(status_string_2,"Ramping Helmholtz-NEG polarity");
           pvPut(status_string_2);
           i_ec_hv = 8;
           i_sc_hv = 5;
      } state set_helmholtz
      when (delay(7)) {
       sprintf(status_string_1,"Turning off EC %i mainframe",i_ec_hv);
       pvPut(status_string_1);
       sprintf(status_string_2,"HV alarms will sound...waiting 7secs");
       pvPut(status_string_2);
       i_ec_hv--;
       ec_hv_on[i_ec_hv] = OFF;
       if (pvConnected(ec_hv_on[i_ec_hv])) {
          pvPut(ec_hv_on[i_ec_hv]);
       } else {
         sprintf(status_string_1,"EC mainframe %i not responding",i_ec_hv+1);
         pvPut(status_string_1);
       }
      } state ec_hv_down
    }
    state collimator_on_axis {
      when (delay(2)) {
         collimator_command = 10;
         pvPut(collimator_command);	
      } state set_helmholtz
    } 
    state set_helmholtz {
      when (command == CONFIGURE_LEFT_NEG) {
           strcpy(status_string_1,
            "Make sure DC HV is OFF!!!");
           pvPut(status_string_1);
           strcpy(status_string_2,
            "Ramping Helmholtz-NEG polarity");
           pvPut(status_string_2);
         helmholtz_command = NEGATIVE;
         pvPut(helmholtz_command);
      } state check_motor
      when (command == CONFIGURE_LEFT_POS) {
           strcpy(status_string_1,
            "Make sure DC HV is OFF!!!");
           pvPut(status_string_1);
           strcpy(status_string_2,
            "Ramping Helmholtz-POS polarity");
           pvPut(status_string_2);
         helmholtz_command = POSITIVE;
         pvPut(helmholtz_command);
      } state check_motor
    }

    state check_motor {
      when (target_calibrated == OK && 
            target_motor == DONE) {
           strcpy(status_string_1,
            "LAST CHANCE to turn DC HV OFF!!!");
           pvPut(status_string_1);
      } state insert_target
      when (target_calibrated != OK && target_motor == DONE) {
           strcpy(status_string_1,
            "LAST CHANCE to turn DC HV OFF!!!");
           pvPut(status_string_1);
           strcpy(status_string_2,
            "Calibrating target motor");
           pvPut(status_string_2);
	target_command = CALIBRATE;
        pvPut(target_command);
      } state wait_motor
      when (target_motor != DONE  && delay(10)) {
        ;
      } state wait_motor
    }

    state wait_motor {
      when (delay(5) && target_motor == DONE) {
             ;
      } state check_motor
      when (delay(10) && target_motor != DONE) {
           ;
      } state wait_motor
    }
    state insert_target {
       when (delay(5) && command == CONFIGURE_LEFT_NEG) {
                strcpy(status_string_2,"Moving to LEFT target");
                pvPut(status_string_2);
	        target_command = LEFT;
                pvPut(target_command);
       } state set_quads
       when (delay(5) && command == CONFIGURE_LEFT_POS) {
                strcpy(status_string_2,"Moving to LEFT target");
                pvPut(status_string_2);
	        target_command = LEFT;
                pvPut(target_command);
       } state set_quads
       when (delay(5) && command == CONFIGURE_RIGHT_NEG) {
                strcpy(status_string_2,"Moving to RIGHT target");
                pvPut(status_string_2);
	        target_command = RIGHT;
                pvPut(target_command);
       } state set_quads
       when (delay(5) && command == CONFIGURE_RIGHT_POS) {
                strcpy(status_string_2,"Moving to RIGHT target");
                pvPut(status_string_2);
	        target_command = RIGHT;
                pvPut(target_command);
       } state set_quads
    }
    state insert_otr1 {
      when () {
           strcpy(status_string_2,"Inserting OTR1");
           pvPut(status_string_2);
           otr1_command = 1;
           pvPut(otr1_command);
      } state set_quads 
    }
    state set_quads {
	when () {
	   dynab_set_i = 0;
           pvPut(dynab_set_i);
	   dynac_set_i = 0;
           pvPut(dynac_set_i);
        } state dynab_switch
    }
    state dynab_switch {
       when (dynab_read_i < 20.0 && dynac_read_i < 20 ) {
           pvGet(energy);
	   printf("Beam energy %f\n", energy);
           if (energy < 2000.) {
              strcpy(status_string_2,"Upstream quad polarity: reverse");
              pvPut(status_string_2);
              dynab_reverse = ON;
              pvPut(dynab_reverse);
	      printf("%s %i\n",status_string_2, dynab_reverse);
           } else { 
              strcpy(status_string_2,"Upstream quad polarity: forward");
              pvPut(status_string_2);
              dynab_forward = ON;
              pvPut(dynab_forward);
	      printf("%s %i\n",status_string_2, dynab_forward);
           }
       } state quad_on
    }
    state quad_on {
       when (delay(5) && dynab_read_i < 20.0 && dynac_read_i < 20) {
           dynab_on = ON;
           pvPut(dynab_on);
           dynac_on = ON;
           pvPut(dynac_on);
       } state quad_set_current
    }
    state quad_set_current {
       when (delay(5)) {
           strcpy(status_string_1,"Turning on Moller Quads");
           pvPut(status_string_1);
           pvGet(dynab_sug_set);
           pvGet(dynac_sug_set);
           
           dynab_set_i = dynab_sug_set;
           pvPut(dynab_set_i);

           dynac_set_i = dynac_sug_set;
           pvPut(dynac_set_i);
       } state daq_disable
    }
    state daq_disable {
      when (delay(5)) {
         daq_control = DISABLED;
         pvPut(daq_control);
      } state take_data
    }
    state take_data {
       when (delay(10) && target_motor == DONE && 
             (helmholtz_negative == ON || helmholtz_positive == ON)) {
         strcpy(status_string_1,"Moller Hardware CONFIGURED");
         pvPut(status_string_1);
         strcpy(status_string_2,"EPICS daq started");
         pvPut(status_string_2);
         daq_control = ENABLED;
         pvPut(daq_control);
         daq_reset = ON;
         pvPut(daq_reset);
         command = DO_NOTHING;
         pvPut(command);
	 status = CONFIGURED_NEG_LEFT;
	 pvPut(status);
       } state get_command
    }

    state stop_daq {
      when () {
         strcpy(status_string_1,"All done? disabling EPICS DAQ");
         pvPut(status_string_1);
         strcpy(status_string_2,"Making LogBook Entry");
         pvPut(status_string_2);
	moller_oplog_remote();
         strcpy(status_string_2,"Backing out Moller Hardware");
         pvPut(status_string_2);
        daq_control = DISABLED;
        pvPut(daq_control);
        target_command = EMPTY;
        pvPut(target_command);      
        dynab_set_i = 0;
        pvPut(dynab_set_i);
        dynac_set_i = 0;
        pvPut(dynac_set_i);
        helmholtz_command = OFF;
        pvPut(helmholtz_command);
      } state quad_ps_off
    }
    state quad_ps_off {
       when (delay(10) && dynab_read_i < 20.0 && dynac_read_i < 20) {
           dynab_off = ON;
           pvPut(dynab_off);
           dynac_off = ON;
           pvPut(dynac_off);
         strcpy(status_string_1,"Waiting for empty target position");
         pvPut(status_string_1);
       } state hv_on
    }
    state  retract_otr1 {
	when () {
          strcpy(status_string_2,"Retracting OTR1");
          otr1_command = 0;
          pvPut(status_string_2);
          pvPut(otr1_command);
        } state hv_on
    }
    state collimator_home {
      when (delay(2)) {
         strcpy(status_string_2,"Retracting Collimator");
         collimator_command = 5;
         pvPut(collimator_command);	
      } state hv_on
    }
    state hv_on {
       when(delay(10) && moller_target_empty == ON) {
         strcpy(status_string_1,"Turning SC & EC HV on");
         pvPut(status_string_1);
         strcpy(status_string_2,"You can turn DC HV back on");
         pvPut(status_string_2);
       } state sc_hv_on
    }
    state sc_hv_on {
      when (i_sc_hv <= 0) {
          sprintf(status_string_2,"Done turning on SC mainframes");
          pvPut(status_string_2);
      } state ec_hv_on
      when (delay(7)) {
       i_sc_hv--;
       sprintf(status_string_1,"Turning ON SC %i mainframe",sc_map[i_sc_hv]);
       pvPut(status_string_1);
       sprintf(status_string_2,"HV alarms will sound...waiting 7secs");
       pvPut(status_string_2);
       sc_hv_on[i_sc_hv] = ON;
       if (pvConnected(sc_hv_on[i_sc_hv])) {
          pvPut(sc_hv_on[i_sc_hv]);
       } else {
         sprintf(status_string_1,"SC mainframe %i not responding",sc_map[i_sc_hv]);
         pvPut(status_string_1);
       }
      } state sc_hv_on
    }
    state ec_hv_on {
      when (i_ec_hv <= 0) {
         strcpy(status_string_1,"You can turn DC HV on now");
         pvPut(status_string_1);
         strcpy(status_string_2,"moller hardware disabled...");
         pvPut(status_string_2);
         command = DO_NOTHING;
         pvPut(command);
	 status = WAITING;
	 pvPut(status);      
         i_ec_hv = 8;
         i_sc_hv = 5;
      } state insert_pause
      when (delay(7)) {
        sprintf(status_string_1,"Turning ON EC %i mainframe",i_ec_hv);
        pvPut(status_string_1);
        sprintf(status_string_2,"HV alarms will sound...waiting 7secs");
        pvPut(status_string_2);
        i_ec_hv--;
        ec_hv_on[i_ec_hv] = ON;
        if (pvConnected(ec_hv_on[i_ec_hv])) {
          pvPut(ec_hv_on[i_ec_hv]);
        } else {
          sprintf(status_string_1,"EC mainframe %i not responding",i_ec_hv+1);
          pvPut(status_string_1);
        }
      } state ec_hv_on
    }
    state insert_pause {
      when (delay(30)) {
        ;
      } state get_command
    }
    state change_helm_pos {
	when() {
         strcpy(status_string_1,"Changing Helmholtz polarity to POS");
         pvPut(status_string_1);
         strcpy(status_string_2,"Disabling EPICS daq, waiting...");
         pvPut(status_string_2);
          daq_control = DISABLED;
          pvPut(daq_control);
          helmholtz_command = POSITIVE;
          pvPut(helmholtz_command);
        } state take_data
    }
    state change_helm_neg {
	when() {
         strcpy(status_string_1,"Changing Helmholtz polarity to NEG");
         pvPut(status_string_1);
         strcpy(status_string_2,"Disabling EPICS daq, waiting...");
         pvPut(status_string_2);
          daq_control = DISABLED;
          pvPut(daq_control);
          helmholtz_command = NEGATIVE;
          pvPut(helmholtz_command);
        } state wait_helmholtz 
    }
    state wait_helmholtz {
        when(helmholtz_negative == ON || helmholtz_positive == ON) {
          strcpy(status_string_2,"Helmholtz Magnet set---GO!!");
          pvPut(status_string_2);
        } state take_data
    }
}