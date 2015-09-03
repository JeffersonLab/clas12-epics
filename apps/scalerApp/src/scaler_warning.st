program scaler_warning

option +c;


double halo;
assign halo  to  "{scaler}scaler_warning.VAL";
monitor halo;

double  O_thr;
assign  O_thr to "{scaler}orange_threshold.VAL";
monitor O_thr;

double  R_thr;
assign  R_thr to "{scaler}red_threshold.VAL";
monitor R_thr;

short O_alert;
assign O_alert to "{scaler}orange_alert.VAL";

short R_alert;
assign R_alert to "{scaler}red_alert.VAL";

short R_alert_memory;
assign R_alert_memory to "{scaler}red_alert_memory.VAL";


/*--------------------------------------------------------------*/
/*                                                              */
/*--------------------------------------------------------------*/
ss scaler_warning
{
  state normal
  {
    when(halo>O_thr)
    {
      O_alert = TRUE;
      pvPut(O_alert);
    } state orange
  }
  
  state orange
  {
    when(halo<O_thr)
    {
      O_alert = FALSE;
      pvPut(O_alert);

    } state normal

    when(halo>R_thr)
    {
      R_alert = TRUE;
      pvPut(R_alert);

      R_alert_memory = TRUE;
      pvPut(R_alert_memory);

      O_alert = FALSE;
      pvPut(O_alert);
    } state red
  }

  state red
  {
    when(halo<R_thr)
    {
      R_alert = FALSE;
      pvPut(R_alert);

      O_alert = TRUE;
      pvPut(O_alert);
    } state orange
  }
}


