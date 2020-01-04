program scaler_d_restart

option +c;

#define SLEEP_TIME     30

short sc_CNT;
assign sc_CNT to "{scaler_d}scaler_d.CNT";
monitor sc_CNT;

short sc_mode;
assign sc_mode to "{scaler_d}scaler_d_mode.VAL";

short sc_display_mode;
assign sc_display_mode to "{scaler_d}display_d_mode.VAL";

float sc_rate;
assign sc_rate to "{scaler_d}scaler_d.RATE";

float sc_TP;
assign sc_TP to "{scaler_d}scaler_d.TP";

/*--------------------------------------------------------------*/
/* This is to automatically restart the scaler if it is iddle   */
/* for more than SLEEP_TIME seconds                             */
/*--------------------------------------------------------------*/
ss scaler_d_restart
{
  state wait
  {
    when(sc_CNT==0)
    {
      ;
    } state restarting
  }

  state restarting
  {
    when((delay(SLEEP_TIME)) && (sc_CNT==0))
    {
      if (sc_CNT==0)
      {
	printf("restarting\n");
	sc_CNT  = 1;
	sc_mode = 1;
	sc_display_mode = 1;  /* 1=hertz 2=norm */
	sc_rate = 10;
	sc_TP = 2;
	pvPut(sc_display_mode);
	pvPut(sc_mode);
	pvPut(sc_CNT);
	pvPut(sc_rate);
	pvPut(sc_TP);
      }
    } state wait
  
    when (sc_CNT)
    {
      ;
    } state wait
  }
}


