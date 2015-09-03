program frwd_scaler_restart

option +c;

#define SLEEP_TIME                 60  /* 1 minute  */
#define SLEEP_TIME_WRONG_MODE     300  /* 5 minutes */
#define DEFAULT_DISPLAY_MODE        2  /* 1=hertz 2=norm 0=raw */


short sc_CNT;
assign sc_CNT to "{frwd_scaler}frwd_scaler.CNT";
monitor sc_CNT;

short sc_mode;
assign sc_mode to "{frwd_scaler}frwd_scaler_mode.VAL";

short sc_display_mode;
assign sc_display_mode to "{frwd_scaler}frwd_display_mode.VAL";
monitor sc_display_mode;
float sc_rate;
assign sc_rate to "{frwd_scaler}frwd_scaler.RATE";

float sc_TP;
assign sc_TP to "{frwd_scaler}frwd_scaler.TP";

/*--------------------------------------------------------------*/
/* This is to automatically restart the scaler if it is iddle   */
/* for more than SLEEP_TIME seconds                             */
/*--------------------------------------------------------------*/
ss frwd_scaler_restart
{
  state wait
  {
    when(sc_CNT==0)
    {
      ;
    } state restart_scaler_stopped
    when( sc_display_mode != DEFAULT_DISPLAY_MODE)
    {
    ;
    } state restart_wrong_mode
  }

  state restart_scaler_stopped
  {
    when( delay(SLEEP_TIME) )
    {
	printf("frwd_scaler: NOT COUNTING\n");
     ;
    } state restarting
  }

  state restart_wrong_mode
  {
    when( delay(SLEEP_TIME_WRONG_MODE) )
    {
	printf("frwd_scaler: IN WRONG MODE\n");
     ;
    } state restarting
  }
  state restarting
  {
    when()
    {
	printf("frwd_scaler: resetting scaler to default settings\n");
	sc_CNT  = 1;
	sc_mode = 1;
	sc_display_mode = DEFAULT_DISPLAY_MODE;  /* 1=hertz  2=norm */
	sc_rate = 10;
	sc_TP = 2;
	pvPut(sc_display_mode);
	pvPut(sc_mode);
	pvPut(sc_CNT);
	pvPut(sc_rate);
	pvPut(sc_TP);

    } state wait
  
    when (sc_CNT)
    {
      ;
    } state wait
  }
}


