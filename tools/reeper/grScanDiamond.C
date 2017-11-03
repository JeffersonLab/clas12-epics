// Demo script 
// Part of the (GRIM)REEPER package
// (GRIM REEPER Implements Macros to) Read EPICS Events and Plot Everything in ROOT

// This script shows how to use a custom read and write function to do a 2d scan.
// It aims to demostrate several features, which would, in general, not all be used together!
// 1. Carries out a 2d scan in xSetting,ySetting by writing to these with caput commands.
// 2. Reads back the actual values of xSetting,ySetting and also BigScaler after each step, and makes time graphs
// 3. Makes a 2D hist of x,y,BigScaler
// 4. Demonstrates how to use the (GRIM)REEPER functions to read waveforms:
//    into an array, a TH1D, and a slice of a TH2D 


//Some essential globals
GrimReeper* gr       = NULL;  //The GrimReeper class
int      p           = 0;     //number of points
double **pvdata      = NULL;  //All the acquired data
void myFunc(int mode = 0);        //custom user function defined below


double yOffset=-2.0;
double xOffset=-75.0;
double ystepSize=4.0/10.0;
double xstepSize=5.0/10.0;
double xpos,ypos;


void grScanDiamond(){

  //make the main class object
  gr = new GrimReeper();
  
  gr->CANVW=400; //make the default canvases a bit smaller. Some parameters are accessible without set Functions
  gr->CANVH=400;
  
  //gr->simIOC(2); // mode 2 means xy scan the simulation

  //Add all the PVs to be readback - in addition to setting x,y in the scan with caput, we read the actual values back. 
  //Time is compuslory as PV0         // 0
  gr->addPV("BEAM:GONI:X");           // 1 
  gr->addPV("BEAM:GONI:Y");           // 2 
  gr->addPV("GEN:MON:MaxTaggRate");   // 3 

  //make some graphs using makeGraph(int y,int x, const char *fit,double min, double max),
  //                       where y,x are indices of PVs (see above, fit is a fit function min,max are fit range)
  //                       A single letter is for fit is passed as a draw option "C" or "L" normally.
  //
  //                       Axes can be referred to by their PVname or index (see addPV() above).
  //
  //             y-axis       v        x-axis            fitfunc     fitrange
  gr->makeGraph("BEAM:GONI:X",         "Time",           "L"                    );   // 0
  gr->makeGraph("BEAM:GONI:Y",         "Time",           "L"                    );   // 1
  gr->makeGraph("GEN:MON:MaxTaggRate", "Time",           "C"                    );   // 2

  gr->setPeriod(8);                    //Set the period of the readback (seconds - integer)
  gr->setVerbosity(0);                 //stop it clogging up the console with all the PV readback numbers
  gr->setConfirmScan(1);               //(defaults to 1, meaning ask for confirmation before starting scan).

  myFunc(GR_SET);                     //Call myFunc() to do the init part this is the specialised part. 
  
  //make a gui - or you could do it all from the command line
  gr->makeControlGUI(GR_SMALLGUI);
  
  //gr->startScanning();               //start the scan directly instead of clicking the button on the GUI.
  
}


//  This section relates to the customised user functions /////////////////////////////////////////////////////
//  Variables to be accessed by the user definedby calls to these read and write functions need to be globals. 
//  They will be initialised by myfunc(GR_SET) below.

TH2D    *xyPlot       = NULL;   
TCanvas *xycanv       = NULL;


void myFunc(int mode){
  double xstep       = 0.0;
  double ystep       = 0.0;
  double val;
  char   command[100];
  
  //fprintf(stderr,"ran myRead(%d)\n",mode);
  
  p = gr->getPoints();          //get the number of points read.
  
  switch (mode) {
    
  case GR_SET:                 //only called once to set u pmy func
    
    pvdata = gr->getPVData();   //get the address of the array with all the data points
    
    
    xycanv = new TCanvas("xycanv","xycanv",200,800,500,500); //make canvas and don't allow closing
    ((TRootCanvas*)xycanv->GetCanvasImp())->DontCallClose(); 
    xycanv->cd();
    xyPlot = new TH2D("xyPlot","LadderOR vs xy;Xsetting(mm);Ysetting)(mm)",10,xOffset,xOffset+5.0,10,yOffset,yOffset+4.0);
    xyPlot->Draw("col");
    
    //These 2 lines set up the (GRIM)REEPER to call myFunc() to read and write as appropriate.
    gr->setUserRead("myFunc(1)");
    gr->setUserWrite("myFunc(2)");
    gr->setUserInit("myFunc(3)");
    

    break;
    
  case GR_READ: //Called during a scan, after reading the PVs.
    //fprintf(stderr,"ran myRead(2)\n");
    
    //write the current BigScaler value into the appropriate x,y bin.
    //need to use the indices of the PVs to access pvtata. Xsetting, Ysetting,BigScaler = 1,2,3
    xyPlot->SetBinContent(xyPlot->FindBin(pvdata[1][p]+0.5*xstepSize,pvdata[2][p]+0.5*ystepSize),pvdata[3][p]);
    xycanv->Modified();xycanv->Update();
    
    break;
    
  case GR_WRITE: //called during a scan after reading pvs (and before waiting Period time)  
    //fprintf(stderr,"ran myRead(2)\n");
    if(p<100){
      ystep=int(p/10);xstep=p%10;
      xpos=xOffset+(xstep*xstepSize);
      ypos=yOffset+(ystep*ystepSize);
      
      //fprintf(stderr,"%lf    %lf  \n",xpos,ypos);
      gr->writePV("BEAM:GONI:X",xpos);
      gr->writePV("BEAM:GONI:Y",ypos);
      
    }
    
    else gr->stopScanning();
    break;
    
  case GR_INIT: //Called during a scan, after reading the PVs.
    //fprintf(stderr,"%lf    %lf  \n",xpos,ypos);
    gr->writePV("BEAM:GONI:X",xoffset);
    gr->writePV("BEAM:GONI:Y",yoffset);
    fprintf(stderr,"Step 0 - Waiting 10s to get to initial position\n");
    gSystem->Sleep(10000);
    break;
    
  
  default:
    break;
  }
}

