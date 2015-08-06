/*
 In this file we define the IOC commands
  for initializzing, starting and stopping
  CAEN HV chassis. 
*/


#ifndef IOC_COMMS_CAEN
#define IOC_COMMS_CAEN

extern "C" 
{
#include <pthread.h>
#include "sy1527.h"
#include "sy1527epics.h"
} ;
#include <iostream> 
using namespace std;

/* Define Arguments descriptors for "Start and Atop Commands */
static const iocshArg StartArgs[2] = { {"Chassis Number", iocshArgInt }, 
				       {"Chassis IP    ", iocshArgString } };
static const iocshArg StopArgs[1]  = { {"Chassis Number", iocshArgInt} } ;


/* Define the array of the pointers to the Arguments descriptors for Start and Stop command */
static const iocshArg* const  StartArgs_ptr[2] = { &StartArgs[0], &StartArgs[1] };
static const iocshArg* const  StopArgs_ptr[2]  = { &StopArgs[0] , &StopArgs[1]  };

/* Define arguments structures for Init, Start and Stop Commans */
static const iocshFuncDef Init_commDef  = {"Init_CAEN",  0, 0 };
static const iocshFuncDef Start_commDef = {"Start_CAEN", 2, StartArgs_ptr };
static const iocshFuncDef Stop_commDef  = {"Stop_CAEN",  1, StopArgs_ptr  };


/* Initializing function */
static void  runInit_CAEN( const iocshArgBuf* args ) 
{
  cout << "Initializing CAEN Application " << endl;
  sy1527Init(); 
}


/* Start function */
static void  runStart_CAEN( const iocshArgBuf* args ) 
{
  cout << "Starting CAEN Application for chassis " << args[0].ival << 
    " at " << args[1].sval << endl;
  sy1527Start( (unsigned) args[0].ival, args[1].sval ) ;

  sy1527GetMap( args[0].ival  );
  sy1527PrintMap( args[0].ival  );
}

/* Stop Function */
static void  runStop_CAEN( const iocshArgBuf* args ) 
{
  cout << "Stopping CAEN Application for chassis " << args[0].ival << endl;
  sy1527Stop( (unsigned) args[0].ival ) ;
}

/* Define a class whos constructor registers Init, Start and Stop commands */
class IocShellComReg { 
 public:
  IocShellComReg( ) { 
    iocshRegister( &Init_commDef , runInit_CAEN ); 
    iocshRegister( &Start_commDef, runStart_CAEN ); 
    iocshRegister( &Stop_commDef, runStop_CAEN );     
  }
};

/*
  Define a dummy global variable to register Init, Start and Stop Commands  
  before the execution starts 
*/
static IocShellComReg dummyObj;

#endif


