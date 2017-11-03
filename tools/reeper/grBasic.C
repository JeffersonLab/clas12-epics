//Demo script to scan some EPICS variables
//Part of the (GRIM)REEPER package
//(GRIM)REEPER Implements Macros to Read EPICS Events and Plot Everything in ROOT

//#include "reeper.h"

GrimReeper* gr = NULL; 

void grBasic(int sim = 1){

  gr = new GrimReeper();
   
  //Optional - use a testioc if you don't have real PVs
  if(sim)gr->simIOC();  
  
  
  //Add all the PVs to be readback (These are from the simulation)
  // Time is compuslory as PV0    // 0
  gr->addPV("PV23004");               // 1
  gr->addPV("colliX");                // 2
  gr->addPV("BigScaler");             // 3
  gr->addPV("Fcup");                  // 4
  gr->addPV("PMT1");                  // 5
  gr->addPV("Xsetting");              // 6 
  gr->addPV("Ysetting");              // 7 

  gr->printPVs();

  //make some graphs using makeGraph(int y,int x, const char *fit,double min, double max),
  //                       where y,x are indices of PVs (see above, fit is a fit function min,max are fit range)
  //                       A single letter is for fit is passed as a draw option "C" or "L" normally.
  //             y-axis    v     x-axis                  fitfunc     fitrange    
  gr->makeGraph( "PV23004",      "Time",                   "pol3"                     );   // 0
  gr->makeGraph( "colliX",       "Time",                   "C"                        );   // 1
  gr->makeGraph( "BigScaler",    "Time"                                               );   // 2
  gr->makeGraph( "PMT1",         "colliX",                 "pol4",     -2.0,  2.0     );   // 3
  gr->makeGraph( "Fcup",         "PMT1"                                               );   // 4

  gr->printGraphs();

  //make multigraphs - use graph names or indices
  gr->makeMultiGraph("All PVs vs Time","PV23004_v_Time", "colliX_v_Time", "BigScaler_v_Time");    //name version
  //gr->makeMultiGraph("All PVs vs Time",0,1,2);                                                  //index version
  //gr->multiCanvas[0]->SetFillColor(406);         //Give them coloured background for mark them different from single graphs.

  
  //Set the period of the readback (seconds - integer)
  gr->setPeriod(3);

  //Set a PV which will be adjusted during the scan. The default is time, which will keep scanning until stopped.
  //If this is not 0 (=time) the start,stop,step size need to be specified. The time interval is specified by scanPeriod.
  gr->setScan("colliX",-4.0,4.0,0.1);
   
  //stop it clogging up the console with all the PV readback numbers
  gr->setVerbosity(0);

  //(defaults to 1, meaning ask for confirmation before starting scan).
  gr->setConfirmScan(0);
  
  gr->makeControlGUI(GR_BIGGUI);         //bring up the GUI, if required.

  //start the scan
  //gr->startScanning();
}

