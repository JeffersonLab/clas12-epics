#include <stdlib.h>
#include <math.h>
#include <vxWorks.h> 
#include <types.h> 
#include <stdioLib.h> 
#include <dbDefs.h>
#include <subRecord.h>
#include <mcaRecord.h>
#include <dbCommon.h>
#include <recSup.h> 
#include <dbFldTypes.h>
#include <dbAccess.h>
#include <link.h>

#include <registryFunction.h>
#include <subRecord.h>
#include <aSubRecord.h>
#include <epicsExport.h>



int bom_sum_init( psub )
     struct subRecord* psub;
{
  /*
  printf("Initialized Function Summing BOM record %s \n",  (char*) ((psub->inpc).value.constantStr) );
  */
  return(0);
}


int bom_sum_proc( psub )
     struct subRecord* psub;
{
  long iChan, n_chan, option;
  char norm_flag;
  long* scaler;
  double sum, current, col_time;
  void* pfl;
  int status;
  char chan_name[256];

  struct mcaRecord* mca_rec;

  struct dbAddr rec_addr ;

  option = 0;
  status = 0;
  pfl=NULL;


  sprintf( chan_name, "%s", (char*) ((psub->inpc).value.constantStr) ) ;
  dbNameToAddr( chan_name, &rec_addr );
  if( rec_addr.precord == 0 ) {
    printf("Error in bom_sum_proc: Cand find %s \n", chan_name );
    psub->val = 0;
    return(-1);
  }
  else {
    n_chan = rec_addr.no_elements ;  
    if ( n_chan < 1 ) {
      printf("Error in bom_sum_proc: No channels in %s \n", chan_name );
      psub->val = 0;
      return(-3);      
    }
    mca_rec = (mcaRecord*)rec_addr.precord;
  }

  scaler = (long*) malloc( (n_chan+1) * sizeof( long ) );

  status |= dbGetField( &(rec_addr), DBR_LONG, scaler, &option, &n_chan, pfl );
  
  if ( status != 0 ) {
    printf("Error in bom_sum_proc: Can't get from 0x%x \n", (struct subRecord*) (rec_addr.precord) );
    psub->val = 0;
    return(-2);
  }

  sum = 0;
  for ( iChan = 0; iChan < n_chan; iChan++ ) {
    sum += (double)scaler[iChan]  ;
  }

  free( scaler );
  
  /* 
     printf("Sum for %s is %f \n", chan_name, sum );  
  */

  norm_flag = psub->b ;
  current   = psub->a ;
  col_time  = psub->d ;

  if( fabs(col_time) < 1.0e-05 ) {
    printf("Error in bom_sum_proc: Collection Time is %f \n", col_time );
    psub->val = 0;
    return(-3);    
  }

  /*
  printf("Col. Time is %f \n", col_time );
  */
  
  if( norm_flag == 1 ) { 
    psub->val = sum / (double) ( col_time ) ;
  }
  else if( ( norm_flag == 2 ) && ( fabs(current) > 1.0e-01 ) ){
    psub->val = sum / (double) ( col_time * current ) ;    
  }
  else if( ( norm_flag == 2 ) && ( fabs(current) < 1.0e-01 ) ){
    psub->val = sum / (double) ( col_time );    
  }  
  else {
    psub->val = sum ;    
  }

  return(0);
}

epicsRegisterFunction(bom_sum_init);
epicsRegisterFunction(bom_sum_proc);





