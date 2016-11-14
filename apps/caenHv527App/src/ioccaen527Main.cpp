
/* Author:  Hovanes Egiyan Date:    10Jul2003 */


#include <stddef.h>
#include <stdlib.h>
#include <stddef.h> 
#include <string.h>
#include <stdio.h>
 
#include "epicsThread.h" 
#include "iocsh.h" 
#include "registryFunction.h"  
#include "ioc_com_def.h"  

extern "C" 
{ 
  long InitChannel(struct bigsubRecord *psub) ;
  long ScanChannel(struct bigsubRecord *psub) ;
};

int main(int argc,char *argv[])
{
  registryFunctionAdd( "InitChannel", (REGISTRYFUNCTION)InitChannel ) ;
  registryFunctionAdd( "ScanChannel", (REGISTRYFUNCTION)ScanChannel ) ;
  if(argc>=2) {    
    iocsh(argv[1]);
    epicsThreadSleep(.2);
  }
  iocsh(NULL);
  return(0);
}
