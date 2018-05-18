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
#include <string.h>

#define DEBUG 0 /* 0 - disabled; 1 - enabled */

#define ALL_CHAN 32
static struct dbAddr hist_addr[2]; /* output PV address */
static struct dbAddr inp_addr[ALL_CHAN]; /*  input PV addresses */

/* ------------------------------------------------------------------------ */

void get_pv_addr(char *name, struct dbAddr *paddr){
  
  if (DEBUG) printf("get_pv_addr::Finding address = 0x%x corresponding to name \"%s\"\n",paddr,name);
  dbNameToAddr( name, paddr );
  if (DEBUG) printf("get_pv_addr::Found address = 0x%x corresponding to name \"%s\"\n",paddr,name);
  if( paddr->precord == 0 ) {
    printf("Error in fill_init->get_pv_addr: Cand find %s \n", name );
    exit(1);
  }
}

/* ------------------------------------------------------------------------ */

int fill_init( psub )
     struct subRecord* psub;
{
  long n_chan;
  char name[256];
  const char *pname;
  int i;
  int offset;
  int ihisto;
  pname = name;

  /*
    printf("Initialized Function Summing PV record %s \n",  (char*) ((psub->inpc).value.constantStr) );
  */
  for(ihisto=0; ihisto<2; ihisto++) {
    if (ihisto==0) sprintf(name, "tgp_x");
    if (ihisto==1) sprintf(name, "tgp_y");

    get_pv_addr(name, &(hist_addr[ihisto]));


    n_chan = 32;
    offset = ihisto*16;

    for(i=0; i<n_chan; i++) {
      sprintf(name,"bom_sc_ai_%d", i);
      printf("channel name before get_pv_addr = %s \n",name);
      get_pv_addr(name, &(inp_addr[i]));
    }
  }
  return(0);
}

/* ------------------------------------------------------------------------ */

int fill_proc( psub )
     struct subRecord* psub;
{
  int ihisto;
  long i, n_chan, option;
  double data[1];
  double *buffer;
  void* pfl;
  int status;
  long one = 1;
  int offset;
  option = 0;


  /*struct subRecord* sub_rec;*/
  /*struct dbAddr rec_addr ;*/

  option = 0;
  status = 0;
  pfl=NULL;


  for(ihisto=0; ihisto<2; ihisto++) {
    
    n_chan = 16;
    offset = ihisto*16;
    
    buffer = (double*) malloc( n_chan * sizeof(double) );
    
    /* loop to read the input channels and fill the buffer */
    for(i=0; i<n_chan; i++) {
      /*sub_rec = (subRecord*)inp_addr[i+offset].precord;*/
      data[0] = -1;
      if ( inp_addr[i+offset].precord != NULL ) {
	status |= dbGetField( &inp_addr[i+offset], DBR_DOUBLE, data, &option, &one, pfl );
	if ( status != 0 ) {
	  printf("Error in fill_proc: Can't get data from 0x%x \n", inp_addr[i+offset] );
	  psub->val = 0;
	  return(-3);
	}
	buffer[i] = data[0];
	/*printf("buffer[%ld] = %f\n",i,data[0]);*/
      } else {
	printf("error in proc: precord is null\n");
      }
    }
    
    /* copy buffer into histogram */
    if ( hist_addr[ihisto].precord != NULL ) {
      status |= dbPutField( &hist_addr[ihisto], DBR_DOUBLE, buffer, n_chan );
    }
    else
      status |= 0x100 ;
    free( buffer );
  }

  return(status);
}
