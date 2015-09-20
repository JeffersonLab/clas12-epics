program scaler_restart

option +c;

#define SLEEP_TIME                 60  /* 1 minute  */
#define SLEEP_TIME_WRONG_MODE     300  /* 5 minutes */
#define DEFAULT_DISPLAY_MODE        1  /* 0=Counts, 1=Cts/s */


short sc_CNT;
assign sc_CNT to "{scaler}.CNT";
monitor sc_CNT;

short sc_mode;
assign sc_mode to "{scaler}.CONT";

short sc_display_mode;
assign sc_display_mode to "{scaler}_calc_ctrl";
monitor sc_display_mode;

float sc_rate;
assign sc_rate to "{scaler}.RATE";

float sc_TP;
assign sc_TP to "{scaler}.TP";

/*--------------------------------------------------------------*/
/* This is to automatically restart the scaler if it is iddle   */
/* for more than SLEEP_TIME seconds                             */
/*--------------------------------------------------------------*/
ss scaler_restart
{
  state wait {
    when(sc_CNT==0) {
    } state restart_scaler_stopped
    
    when( sc_display_mode != DEFAULT_DISPLAY_MODE) {
    } state restart_wrong_mode
  }

  state restart_scaler_stopped {
    when( delay(SLEEP_TIME) ) {
	    printf("scaler: NOT COUNTING\n");
    } state restarting
  }

  state restart_wrong_mode {
    when( delay(SLEEP_TIME_WRONG_MODE) ) {
    	printf("scaler: IN WRONG MODE\n");
    } state restarting
  }
  
  state restarting {
    when() {
	    printf("scaler: resetting scaler to default settings\n");
	    sc_CNT  = 1;
	    sc_mode = 1;
	    sc_display_mode = DEFAULT_DISPLAY_MODE;  /* 1=hertz */
	    sc_rate = 10;
	    sc_TP = 2;
	    pvPut(sc_display_mode);
	    pvPut(sc_mode);
    	pvPut(sc_CNT);
	    pvPut(sc_rate);
	    pvPut(sc_TP);
    } state wait
  
    when (sc_CNT) {
    } state wait
  }
}

