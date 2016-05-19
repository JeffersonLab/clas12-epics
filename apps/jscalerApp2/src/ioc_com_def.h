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
//#include "sy1527.h"
//#include "sy1527epics1.h"
} ;
//#include <iostream.h> 

#include "jscalers.h"
extern ScalersSlowControl *scalersslowcontrol;

/* Define Arguments descriptors for "Start and Atop Commands */
static const iocshArg StartArgs[2] = { {"Chassis Number", iocshArgInt }, 
				       {"Chassis IP    ", iocshArgString } };
static const iocshArg StopArgs[1]  = { {"Chassis Number", iocshArgInt} } ;

///------------------------------
static const iocshArg genStartArgs = { "generic arguments", iocshArgArgv };
///------------------------------


///iocshArgPdbbase

/* Define the array of the pointers to the Arguments descriptors for Start and Stop command */
static const iocshArg* const  StartArgs_ptr[2] = { &StartArgs[0], &StartArgs[1] };
static const iocshArg* const  StopArgs_ptr[2]  = { &StopArgs[0] , &StopArgs[1]  };
///------------------------------
static const iocshArg* const  genStartArgs_ptr[]={&genStartArgs};
///------------------------------


/* Define arguments structures for Init, Start and Stop Commans */

static const iocshFuncDef Start_commDef = {"Start_CAEN", 2, StartArgs_ptr };
static const iocshFuncDef Stop_commDef  = {"Stop_CAEN",  1, StopArgs_ptr  };
///------------------------------
static const iocshFuncDef Init_commDef  = {"Init_SCALERS",  0, 0 };
static const iocshFuncDef genStart_commDef = {"Start_SCALERS_CRATE", sizeof(genStartArgs_ptr)/sizeof(genStartArgs_ptr[0]), genStartArgs_ptr };
///------------------------------

/* Initializing function */
static void  runInit_SCALERS( const iocshArgBuf* args ) 
{
  cout << "Initializing SCALERS Application " << endl;
  scalersslowcontrol= new ScalersSlowControl();

}


/* Start function */
static void  runStart_CAEN( const iocshArgBuf* args ) 
{

}
///------------------------------
static void  runStart_SCALERS_CRATE( const iocshArgBuf* args ) 
{

//double a[10];
//a[0]= *(((double *) (args[1].vval))+0);

char *new_args[args->aval.ac+1];
int id=-1;
string hostname;
//int number_of_slots;
///int *board_types;
///board_types = new int[number_of_slots];

for ( int i=1; i<args->aval.ac; i++ ){
 new_args[i-1] = args->aval.av[i];
 // printf("========1========= %s %s\n",args->aval.av[i], new_args[i-1]);

 if(i==1)id=atoi(new_args[i-1]);
 else if(i==2)hostname=string(new_args[i-1]);
/// else if(i==3)number_of_slots=atoi(new_args[i-1]);
/// else if(i>3)board_types[i-4]=atoi(new_args[i-1]);
}


// printf("========1=========2 %d %s %d %d %d \n",id, hostname.c_str()  , number_of_slots, board_types[0],board_types[1]);

// scalersslowcontrol->vmecrates[id]=new VmeChassis(id, hostname  , number_of_slots, board_types);
scalersslowcontrol->vmecrates[id]=new VmeChassis(id, hostname );

///delete board_types;

}
///------------------------------


/* Stop Function */
static void  runStop_CAEN( const iocshArgBuf* args ) 
{
  //cout << "Stopping CAEN Application for chassis " << args[0].ival << endl;

}

/* Define a class whos constructor registers Init, Start and Stop commands */
class IocShellComReg { 
 public:
  IocShellComReg( ) { 
    iocshRegister( &Start_commDef, runStart_CAEN ); 
    iocshRegister( &Stop_commDef, runStop_CAEN );     
///------------------------------
    iocshRegister( &Init_commDef , runInit_SCALERS ); 
    iocshRegister( &genStart_commDef, runStart_SCALERS_CRATE ); 
///------------------------------
  }
};

/*
  Define a dummy global variable to register Init, Start and Stop Commands  
  before the execution starts 
*/
static IocShellComReg dummyObj;

#endif


