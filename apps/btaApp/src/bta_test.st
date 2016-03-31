program bta_test

option +c;

int iHour ;
int  ix ;
/*
float UnixTime[7][24];
assign UnixTime to "bta_uxtime_h";
monitor UnixTime ;
*/

/* Record indicating the top of the hour */
float ResetFlag;                           
assign ResetFlag to "bta_master_reset" ;    
monitor ResetFlag;

/* Record forcing BTA variables to reset  */
float SetReset;
assign SetReset to "abu_time_reset" ;
monitor SetReset;

/* One of the BTA variables   */
float TotalCount;
assign TotalCount to "tot_count_calc" ;
monitor TotalCount;

/* H-record for Total Count   */
float TotalCountArr[24];
assign TotalCountArr to "total_count_hist" ;

evflag CountsRead; 
sync TotalCount CountsRead;


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
	iHour = 0; 
        SetReset = 0;
	pvPut( SetReset );
     } state check_reset
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
/*  Checks bta_master_reset, which resets at the top of an hour (1sec)  */
/*  Saves the variable into H-records                                   */
/*  Set abu_time_reset to 1                                             */
/*                                                                      */
/*----------------------------------------------------------------------*/
 state check_reset
  {
    when ( ResetFlag == 1 ) 
      {
	pvGet( TotalCountArr );
/*      Reshuffle, push the new reading into H-record */
        for ( ix = 23; ix > 0; ix-- )
          {
            TotalCountArr[ix] = TotalCountArr[ix-1] ;
          }
        TotalCountArr[0] = TotalCount ; 
        pvPut( TotalCountArr ); 
	iHour++ ;
	printf("Total count is %f, Flag is %f, Reset is %f \n",  
		TotalCount, ResetFlag, SetReset );
	printf("Going to Reset \n");
	SetReset = 1;
	pvPut( SetReset );
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
    when ( ( SetReset == 0 ) && ( ResetFlag == 0 ) )
     { 
 	printf("Total count is %f, Flag is %f, Reset is %f \n",  
		TotalCount, ResetFlag, SetReset );
        printf("Returned to no reset \n" );
     } state check_reset 
  }
}







