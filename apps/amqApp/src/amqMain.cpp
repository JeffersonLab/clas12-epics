/* amqMain.cpp */
/* Author:  Ken Livingston Date:    Oct 2017 */

#include <stddef.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdio.h>

#include "epicsExit.h"
#include "epicsThread.h"
#include "iocsh.h"
#include "amqSupport.h"


//setup for funcs to be available at the IOC prompt 
static const iocshArg InitArgs[2] = {{"Message Broker",iocshArgString},{"Topic",iocshArgString}};
static const iocshArg* const  InitArgs_ptr[2] = { &InitArgs[0], &InitArgs[1] };
static const iocshFuncDef Init_commDef  = {"ConnectMQ",  2, InitArgs_ptr };
static const iocshFuncDef Start_commDef  = {"StartMQ",  0, 0 };


int main(int argc,char *argv[])
{
    if(argc>=2) {    
        iocsh(argv[1]);
        epicsThreadSleep(.2);
    }
    iocsh(NULL);
    epicsExit(0);
    return(0);
}

static void runInit(const iocshArgBuf *args){
  initConsumer(args[0].sval,args[1].sval);
  //fprintf(stderr,"Called AMQ Init: %s %s\n", args[0].sval, args[1].sval); 
}

static void runStart(const iocshArgBuf *args){
  startConsumer();
  //fprintf(stderr,"Called AMQ Init: %s %s\n", args[0].sval, args[1].sval); 
}

static int doRegister(void){
  iocshRegister(&Init_commDef, runInit);
  iocshRegister(&Start_commDef, runStart);
  return 1;
}

//calling this here makes the abve functions available before iocinit is called.
static int done = doRegister();
