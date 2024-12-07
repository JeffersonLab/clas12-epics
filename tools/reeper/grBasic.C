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

  //         PVname                      Index 
  //        "Time"                    // 0     Time is automatically there as PV0
  gr->addPV("PV23004");               // 1
  gr->addPV("colliX");                // 2
  gr->addPV("BigScaler");             // 3
  gr->addPV("Fcup");                  // 4
  gr->addPV("PMT1");                  // 5
  gr->addPV("Xsetting");              // 6 
  gr->addPV("Ysetting");              // 7

  //The following are "dummy PVs - these are formulae combinations of those already defined above, where any TF1 string is allowed 
  // There are options for specifying the parameters
  // [n], [n-], [n+] where:
  // [n]  is current value, just read in, (= PVdata[n][nPoint])
  // [n-] is the "diffence" - current value - previous value (= PVdata[n][nPoint]-PVdata[n][nPoint-1])
  // [n+] is the "integral" - summ of all values up to current value (= Sum(PVdata[n][p] for b=0,nPoint))
  // Eg 
  gr->addPV("[5]/[4]");               // 8 PMT1/Fcup             
  gr->addPV("[5]/[0-]");              // 9 PMT - Time difference - ie Scaler rate in Hz               
  gr->addPV("[3+]/[4+]");             //10 BigScaler integral /  Fcup Integral              


  gr->printPVs();

  gr->setGraphsPerCanvas(3);
  
  //make some graphs using makeGraph(char *y, char *x, const char *fit,double min, double max, int canv, int pad),
  //                       makeGraph(int   y, int   x, const char *fit,double min, double max, int canv, int pad),
  //                           where y,x are names or indices of PVs (see above)
  //                           fit is a fit function min,max are fit range)
  //                           canv,pad specify the canvas and pad index. 
  //
  //             y-axis    v     x-axis                  fitfunc     fitrange    canv(0,,,) pad(1,,,,)    
  gr->makeGraph( "PV23004",      "Time",                   "pol3",   0.0, 0.0,   0,         1);            // 0
  gr->makeGraph( "colliX",       "Time",                   "C",      0.0, 0.0,   0,         2);            // 1
  gr->makeGraph( "BigScaler",    "Time",                   "",       0.0, 0.0,   0,         3);            // 2
  gr->makeGraph( "PMT1",         "colliX",                 "pol4",  -2.0, 2.0,   1,         1);            // 3
  gr->makeGraph( "Fcup",         "colliX",                 "",       0.0, 0.0,   1,         2);            // 4
  gr->makeGraph( 8,               2,                       "",       0.0, 0.0,   1,         3);            // 5
  gr->makeGraph( 9,               0,                       "",       0.0, 0.0,   2,         1);            // 6
  gr->makeGraph( 10,              0,                       "",       0.0, 0.0,   2,         2);            // 7

  gr->printGraphs();

  //make multigraphs - use graph names or indices
  gr->makeMultiGraph("All PVs vs Time","PV23004_v_Time", "colliX_v_Time", "BigScaler_v_Time");    //name version
  gr->makeMultiGraph("All PVs vs colliX",3,4,5);    //name version
  //gr->makeMultiGraph("All PVs vs Time",0,1,2);                                                  //index version
  //gr->multiCanvas[0]->SetFillColor(406);         //Give them coloured background for mark them different from single graphs.

  //gr->drawGraphs();
  
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

