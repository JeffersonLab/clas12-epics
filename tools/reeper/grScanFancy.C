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

enum {MY_SET,MY_INIT,MY_READ,MY_WRITE,MY_END};

//Some essential globals
GrimReeper* gr       = NULL;  //The GrimReeper class
int      p           = 0;     //number of points
double **pvdata      = NULL;  //All the acquired data
void myFunc(int mode = 0);    //custom user function defined below

void grScanFancy(){

  //make the main class object
  gr = new GrimReeper();
  
  gr->CANVW=600; //make the default canvases a bit smaller. Some parameters are accessible without set Functions
  gr->CANVH=400;
  gr->setGraphsPerCanvas(3);

  gr->simIOC(2); // mode 2 means xy scan in the simulation

  //Add all the PVs to be readback - in addition to setting x,y in the scan with caput, we read the actual values back. 
  //Time is compuslory as PV0         // 0
  gr->addPV("Xsetting");              // 1 
  gr->addPV("Ysetting");              // 2 
  gr->addPV("BigScaler");             // 3 

  //make some graphs using makeGraph(char *y, char *x, const char *fit,double min, double max, int canv, int pad),
  //                       makeGraph(int   y, int   x, const char *fit,double min, double max, int canv, int pad),
  //                           where y,x are names or indices of PVs (see above)
  //                           fit is a fit function min,max are fit range (
  //                           canv,pad specify the canvas and pad index. 
  //
  //             y-axis    v     x-axis              fitfunc     fitrange    canv(0,,,) pad(1,,,,)    
  gr->makeGraph("Xsetting",        "Time",           "L",        0.0, 0.0,   0,         1);          // 0
  gr->makeGraph("Ysetting",        "Time",           "L",        0.0, 0.0,   0,         2);          // 1
  gr->makeGraph("BigScaler",       "Time",           "C",        0.0, 0.0,   0,         3);          // 2
  gr->makeGraph("BigScaler",       "Xsetting",       "pol3",    -2.0, 2.0,   1,         1);          // 3
  gr->makeGraph("BigScaler",       "Ysetting",       "pol3",     0.0, 0.0,   1,         2);          // 4

  
  //gr->makeMultiGraph("Position vs Time","Xsetting_v_Time","Ysetting_v_Time");
  
 
  gr->setPeriod(1);                    //Set the period of the readback (seconds - integer)
  gr->setVerbosity(0);                 //stop it clogging up the console with all the PV readback numbers
  gr->setConfirmScan(0);               //(defaults to 1, meaning ask for confirmation before starting scan).


  myFunc(MY_SET);                      //Call myFunc() to do the init part this is the specialised part. 
  
  //make a gui - or you could do it all from the command line
  gr->makeControlGUI(GR_SMALLGUI);

  //gr->startScanning();               //start the scan directly instead of clicking the button on the GUI.
  
}


//  This section relates to the customised user functions /////////////////////////////////////////////////////
//  Variables to be accessed by the user definedby calls to these read and write functions need to be globals. 
//  They will be initialised by myfunc(GR_INIT) below.



TH1D    *currentSlice = NULL;    //make global hists and canvases to be filled by myfunc()
TH2D    *xyPlot       = NULL;   
TH2D    *timeSlices   = NULL;   
TCanvas *slicecanv    = NULL;
TCanvas *xycanv       = NULL;
TCanvas *timecanv     = NULL;
double   dArray[100];           //an array to hold the waveform

void myFunc(int mode){
  double xstep       = 0.0;
  double ystep       = 0.0;
  double val;
  char   command[100];
  char thisfunc[100];

  //fprintf(stderr,"ran myRead(%d)\n",mode);
  
  p = gr->getPoints();          //get the number of points read.
  
  switch (mode) {
    
  case MY_SET:                 //only called once to set up my func
    
    fprintf(stdout,"called myFunc(MY_SET)\n");

    pvdata = gr->getPVData();   //get the address of the array with all the data points

    slicecanv = new TCanvas("slicecanv","slicecanv",1200,800,500,500); //make canvas and don't allow closing
    ((TRootCanvas*)slicecanv->GetCanvasImp())->DontCallClose(); 
    slicecanv->cd();
    currentSlice = new TH1D("currentSlice","currentSlice",100,0,100);
    currentSlice->Draw();

    xycanv = new TCanvas("xycanv","xycanv",200,800,500,500); //make canvas and don't allow closing
    ((TRootCanvas*)xycanv->GetCanvasImp())->DontCallClose(); 
    xycanv->cd();
    xyPlot = new TH2D("xyPlot","BigScaler vs xy;Xsetting(mm);Ysetting)(mm)",10,0,10,10,0,10);
    xyPlot->Draw("col");
    
    timecanv = new TCanvas("timecanv","timecanv",700,800,500,500);
    ((TRootCanvas*)timecanv->GetCanvasImp())->DontCallClose(); 
    timecanv->cd();
    timeSlices = new TH2D("timeSlices","timeSlices",100,0,100,20,0,20);
    timeSlices->Draw("col");
    
    //These  lines set up the (GRIM)REEPER to call myFunc() to init, read, write, end as required.
    gr->setUserInit("myFunc(1)");    //=myFunc(MY_INIT)
    gr->setUserRead("myFunc(2)");    //=myFunc(MY_READ)
    gr->setUserWrite("myFunc(3)");   //=myFunc(MY_WRITE)
    gr->setUserEnd("myFunc(4)");     //=myFunc(MY_END)

    break;
    
  case MY_INIT:
    gr->writePV("Xsetting",0);
    gr->writePV("Ysetting",0);
    fprintf(stdout,"Moving to initial x,y positions ... waiting 5s\n");
    gSystem->Sleep(5000);
    break;
    
  case MY_READ: //Called during a scan, after reading the PVs.
    //fprintf(stderr,"ran myRead(2)\n");
    gr->waveToArray("AMO_SCALERS",dArray,100);
    //now do something with that array if you like!
    
    //write the current BigScaler value into the appropriate x,y bin.
    //need to use the indices of the PVs to access pvtata. Xsetting, Ysetting,BigScaler = 1,2,3
    xyPlot->SetBinContent(xyPlot->FindBin(pvdata[1][p],pvdata[2][p]),pvdata[3][p]);
    xycanv->Modified();xycanv->Update();
    
    gr->waveToTH1D("AMO_SCALERS",currentSlice);       //waveform into TH1D.
    slicecanv->Modified();slicecanv->Update();
    
    gr->waveToTH2DRow("AMO_SCALERS",timeSlices,p%20); //waveform into row of TH2D. After point 20 go back to row zero  again
    timecanv->Modified();timecanv->Update();
    break;
    
  case MY_WRITE: //called during a scan after reading pvs (and before waiting Period time)  
    if(p<100){
      ystep=int(p/10);xstep=p%10;
      gr->writePV("Xsetting",xstep);
      gr->writePV("Ysetting",ystep);
	//sprintf(command,"caput -t Xsetting %g > /dev/null", xstep);
	//gSystem->Exec(command);
	//sprintf(command,"caput -t Ysetting %g > /dev/null", ystep);
	//gSystem->Exec(command);
    }
    
    else gr->stopScanning();
    break;

  case MY_END:
    //do something here just to demonstrate
    xyPlot->Scale(0.1);
    xycanv->Modified();xycanv->Update();
    break;
    
  default:
    break;
  }
}
