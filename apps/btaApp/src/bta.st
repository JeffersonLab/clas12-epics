program bta

option +c;

int  ix ;
int  iy ;


/* Record indicating the top of the hour */
float HourFlag;                           
assign HourFlag to "HL{hall}:bta_master_reset" ;    
monitor HourFlag;

/* Record forcing BTA variables to reset  */
unsigned short  Reset_Flag;
assign Reset_Flag to "HL{hall}:bta_reset_recs" ;
monitor Reset_Flag;

float BeamEvts;
assign BeamEvts to "HL{hall}:bta_bm_evts";
monitor BeamEvts;

#define N_Hours (168)

float DaqEvts;
assign DaqEvts to "HL{hall}:bta_daq_evts";
monitor DaqEvts;

float BeamEvtsHisto[168] ;
assign BeamEvtsHisto to "HL{hall}:bta_bm_evts_h";

float DaqEvtsHisto[168] ;
assign DaqEvtsHisto to "HL{hall}:bta_daq_evts_h";


#define N_BTA_Vars (13)
float BTA_Vars[13];

assign BTA_Vars[0]   to  "HL{hall}:bta_cnt_tot" ;
assign BTA_Vars[1]   to  "HL{hall}:bta_cnt_w_bm" ;
assign BTA_Vars[2]   to  "HL{hall}:bta_cnt_wo_bm" ;
assign BTA_Vars[3]   to  "HL{hall}:bta_cnt_conf_chg" ;
assign BTA_Vars[4]   to  "HL{hall}:bta_cnt_w_bm_w_daq" ;
assign BTA_Vars[5]   to  "HL{hall}:bta_cnt_w_bm_wo_daq" ;
assign BTA_Vars[6]   to  "HL{hall}:bta_cnt_w_bad_state" ;
assign BTA_Vars[7]   to  "HL{hall}:bta_cnt_w_rest_accs" ;
assign BTA_Vars[8]   to  "HL{hall}:bta_cnt_w_sweep" ;
assign BTA_Vars[9]   to  "HL{hall}:bta_cnt_w_sweep_cmpt" ;
assign BTA_Vars[10]  to  "HL{hall}:bta_cnt_w_ctrl_accs" ;
assign BTA_Vars[11]  to  "HL{hall}:bta_cnt_w_powr_prmt" ;
assign BTA_Vars[12]  to  "HL{hall}:bta_cnt_w_bm_prmt" ;

monitor BTA_Vars ;

float CountHisto[13][168] ;
assign CountHisto[0]   to  "HL{hall}:bta_cnt_tot_h" ;
assign CountHisto[1]   to  "HL{hall}:bta_cnt_w_bm_h" ;
assign CountHisto[2]   to  "HL{hall}:bta_cnt_wo_bm_h" ;
assign CountHisto[3]   to  "HL{hall}:bta_cnt_conf_chg_h" ;
assign CountHisto[4]   to  "HL{hall}:bta_cnt_w_bm_w_daq_h" ;
assign CountHisto[5]   to  "HL{hall}:bta_cnt_w_bm_wo_daq_h" ;
assign CountHisto[6]   to  "HL{hall}:bta_cnt_w_bad_state_h" ;
assign CountHisto[7]   to  "HL{hall}:bta_cnt_w_rest_accs_h" ;
assign CountHisto[8]   to  "HL{hall}:bta_cnt_w_sweep_h" ;
assign CountHisto[9]   to  "HL{hall}:bta_cnt_w_sweep_cmpt_h" ;
assign CountHisto[10]  to  "HL{hall}:bta_cnt_w_ctrl_accs_h" ;
assign CountHisto[11]  to  "HL{hall}:bta_cnt_w_powr_prmt_h" ;
assign CountHisto[12]  to  "HL{hall}:bta_cnt_w_bm_prmt_h" ;


float MinuteHisto[13][168] ;
assign MinuteHisto[0]   to  "HL{hall}:bta_sec_tot_h" ;
assign MinuteHisto[1]   to  "HL{hall}:bta_sec_w_bm_h" ;
assign MinuteHisto[2]   to  "HL{hall}:bta_sec_wo_bm_h" ;
assign MinuteHisto[3]   to  "HL{hall}:bta_sec_conf_chg_h" ;
assign MinuteHisto[4]   to  "HL{hall}:bta_sec_w_bm_w_daq_h" ;
assign MinuteHisto[5]   to  "HL{hall}:bta_sec_w_bm_wo_daq_h" ;
assign MinuteHisto[6]   to  "HL{hall}:bta_sec_w_bad_state_h" ;
assign MinuteHisto[7]   to  "HL{hall}:bta_sec_w_rest_accs_h" ;
assign MinuteHisto[8]   to  "HL{hall}:bta_sec_w_sweep_h" ;
assign MinuteHisto[9]   to  "HL{hall}:bta_sec_w_sweep_cmpt_h" ;
assign MinuteHisto[10]  to  "HL{hall}:bta_sec_w_ctrl_accs_h" ;
assign MinuteHisto[11]  to  "HL{hall}:bta_sec_w_powr_prmt_h" ;
assign MinuteHisto[12]  to  "HL{hall}:bta_sec_w_bm_prmt_h" ;

float UnixTime;
assign UnixTime to "{ioc}:unixtime" ;
monitor UnixTime;

float UnixTimeHisto[168];
assign UnixTimeHisto to "HL{hall}:bta_uxtime_h" ;

/*-------------------------------------------------------------*/
/*                                                             */
/*                                                             */
/* State set to control BTA reset and archiving                */
/*                                                             */
/*                                                             */
/*-------------------------------------------------------------*/

ss bta
{	
 state init 
  {
    when()
     {
        Reset_Flag = 0;
	pvPut( Reset_Flag );
     } state connect_pvs
  } 

 state connect_pvs
  {
    when ( pvAssignCount() !=  pvConnectCount() )
     {
      printf("Some channels are not connected \n");
     } state connect_pvs

    when ( pvAssignCount() == pvConnectCount() )
     {
      printf("All Channels are Connected \n");
     }  state check_reset 
  }


/*----------------------------------------------------------------------*/
/*                                                                      */
/*  Checks HL{hall}:bta_master_reset, which resets at the top of        */
/*           an hour (1sec)                                             */
/*  Saves the variable into H-records                                   */
/*  Set abu_time_reset to 1                                             */
/*                                                                      */
/*----------------------------------------------------------------------*/
 state check_reset
  {
 
/* Waiting until the hour is compete to set the reset flag */
    when ( HourFlag == 1 ) 
      {
/*  Loop through all time related H-records  */
	
	for ( ix = 0; ix < N_BTA_Vars; ix++ )
	 { 
/*     Get the current vectors       */
	   pvGet( BTA_Vars[ix]  );
	   pvGet( CountHisto[ix]  );
	   pvGet( MinuteHisto[ix]  );
/*         Reshuffle, push the new reading into H-record */
           for ( iy = (N_Hours-1); iy > 0; iy-- )
            {
	      CountHisto[ix][iy]   =  CountHisto[ix][iy-1] ;
              MinuteHisto[ix][iy]  =  MinuteHisto[ix][iy-1] ;      
            }

/*   Check that there were enough total counts in this hour  */

	   if ( BTA_Vars[0] > 5000 )
	    { 
	      CountHisto[ix][0]  = BTA_Vars[ix] ;
	      MinuteHisto[ix][0] = 3600.*BTA_Vars[ix]  / BTA_Vars[0] ;
            }
	   else
	    {
	      CountHisto[ix][0]  = 0. ;
	      MinuteHisto[ix][0] = 0. ;
            }
/* Put the histogram vectors back   */  
           pvPut( CountHisto[ix]  ); 
           pvPut( MinuteHisto[ix]  ); 		
         }
/* Deal with the event statistic and nuix time  H-records   */

/* Get current vectors                */
       	pvGet(  BeamEvts );
       	pvGet(  DaqEvts );	
       	pvGet(  BeamEvtsHisto );
       	pvGet(  DaqEvtsHisto );	
        pvGet(  UnixTime     );
        pvGet(  UnixTimeHisto ) ;
        for ( iy = (N_Hours-1); iy > 0; iy-- )
          {
	    BeamEvtsHisto[iy]   =  BeamEvtsHisto[iy-1] ;
	    DaqEvtsHisto[iy]    =  DaqEvtsHisto[iy-1] ;
	    UnixTimeHisto[iy]   =  UnixTimeHisto[iy-1] ;
          }

/* Check for minimal total number of counts  */

        if ( BTA_Vars[0] > 5000 )
	 {	
           BeamEvtsHisto[0]   =  BeamEvts ;
           DaqEvtsHisto[0]    =  DaqEvts ;
	   UnixTimeHisto[0]   =  UnixTime ;
         }
	else	
         {
           BeamEvtsHisto[0]   =  0 ;
           DaqEvtsHisto[0]    =  0 ;
	   UnixTimeHisto[0]   =  0 ;
         }
/* Put histogram vectors back */ 
       	pvPut(  BeamEvtsHisto ) ;
       	pvPut(  DaqEvtsHisto  ) ;
	pvPut(  UnixTimeHisto ) ;

	printf("Total count is %f, Hour Flag is %f, Reset Flag is %d \n",  
		BTA_Vars[0], HourFlag, Reset_Flag );
	printf("Going to Reset \n");
	Reset_Flag = 1;
	pvPut( Reset_Flag );
      } state check_unreset
  }

/*-----------------------------------------------------------------*/
/*                                                                 */
/* Check if Reset is disabled and Reset Flag s down                */
/*  and return to check reset                                      */
/*                                                                 */
/*-----------------------------------------------------------------*/
 state check_unreset
  {
    
    when (  Reset_Flag == 0  &&  HourFlag == 0  )
     { 
 	printf("Total count is %f, Hour Flag is %f, Reset Flag is %d \n",  
		BTA_Vars[0], HourFlag, Reset_Flag );
        printf("Returned to no reset \n" );
     } state check_reset 

/*
    when (  HourFlag != 0   ||  Reset_Flag != 0  )
     {
	pvGet( Reset_Flag );  
	printf("Still Waiting \n");
 	printf("Total count is %f, Hour Flag is %f, Reset Flag is %d \n",  
		BTA_Vars[0], HourFlag, Reset_Flag );
   
     } state check_unreset
*/ 
  }
}







