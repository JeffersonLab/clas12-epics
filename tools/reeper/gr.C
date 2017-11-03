//(GRIM)REEPER Implements Macros to Read EPICS Events and Plot Everything in ROOT
//Ken Livingston (kliv@jlab.org) March 2017.
//
//A collection of functions to deal with EPICS scans.
// ... and a simple, optional, GUI based on TButtons
//
//To use this, load the library, then load your own macro to use the library:
// >root grLoad.C myFuncs.C

#include <stdlib.h>
#include "TROOT.h"
#include "TRootCanvas.h"
#include "TCanvas.h"
#include "TColor.h"
#include "TFrame.h"
#include "TGraph.h"
#include "TMultiGraph.h"
#include "TLine.h"
#include "TLatex.h"
#include "TMath.h"
#include "TStyle.h"
#include "Riostream.h"
#include "TRandom.h"
#include "TSystem.h"
#include <TGMsgBox.h>
#include <TH1.h>
#include <TH2.h>
#include <TF1.h>
#include <string.h>
#include <TLegend.h>
#include <TList.h>
#include <TIterator.h>
#include <TImage.h>
#include <TButton.h>
#include <TPaveText.h>
#include <TClass.h>
#include <TClassMenuItem.h>
#include <TGMenu.h>

enum E_GR_PV {Time}; //(Because I want to refer to Time
enum E_GR_LOCAL {GR_SET,GR_READ,GR_WRITE,GR_INIT};
enum E_GR_FIT {GR_NOFIT,GR_FIT,GR_FITRANGE};
enum E_GR_STATUS {GR_STOPPED,GR_STARTED,GR_PAUSED};
enum E_GR_AUTO {GR_AUTO,GR_MANUAL,GR_TOGGLE};
enum E_GR_GUI {GR_NOGUI,GR_SMALLGUI,GR_BIGGUI};

const char*  defaultFormats[]  = {"gif","root","pdf","C",NULL}; //default formats for saving canvases
const char   defaultOutdir[]   = "./epics_gr";                  //default dir
const char*  onOffList[]       = {"#bullet",""};

class GrimReeper : public TObject{
private:

public:
  //  GrimReeper(const char* myname="gr" );
  GrimReeper();
  virtual ~GrimReeper(){};
  void init();
  int  addPV(const char *pvstring);
  void printPVs();
  void PVScanStep();
  void printGraphs();
  void startScanning();
  void stopScanning();
  void pauseScanning();
  void resumeScanning();
  void makeGraph(int yPV, int xPV, const char* pvfit = "", double rangemin = 0.0, double rangemax = 0.0 );
  void makeGraph(const char *yPVName, const char *xPVName, const char* pvfit = "", double rangemin = 0.0, double rangemax = 0.0 );
  void updateGraph(int g);
  void drawGraph(int g);
  void drawGraphs();
  void updateMultiGraph(int g);
  void updateMultiGraphs();
  void makeMultiGraph(const char *title, const char *g0, const char *g1=NULL,const char *g2=NULL,const char *g3=NULL,const char *g4=NULL,const char *g5=NULL,const char *g6=NULL,const char *g7=NULL,const char *g8=NULL,const char *g9=NULL);
  void makeMultiGraph(const char *title, int g0, int g1=-1,int g2=-1,int g3=-1,int g4=-1,int g5=-1,int g6=-1,int g7=-1,int g8=-1,int g9=-1);
  void makeMultiGraph(const char *title, int *mg);
  void updateGraphList();
  void updatePvList();
  void updateMultiList();
  void updateGUI();
  void updateStartButton();
  void updatePauseButton();
  void updateStatus();
  void writePV(const char *pv_name, double pv_value);
  void changePeriod(int t);
  void setGraphAuto(int g, int a);
  void setMultiAuto(int g, int a);
  void setAuto(TObject *gr);
  void resetGrim();
  void exitGrim();
  void saveAll();
  void setGuiToggle();
  void toggleGUI();
  void makeControlGUI(int guisize=GR_BIGGUI);
  void waveToArray(const char *pv, double *array, int n,int add=0);
  void waveToTH1D(const char *pv,TH1D *h,int add=0);
  void waveToTH2DRow(const char *pv,TH2D *h, double y,int add=0);
  void setScan(int pvindex,double start, double stop, double step);
  void setScan(const char *pvname,double start, double stop, double step);
  void setPeriod(int period){scanPeriod=period;};
  void setVerbosity(int verbosity){verbose=verbosity;};
  void setConfirmScan(int confirm){confirmScan=confirm;};
  void setUserRead(const char *read){userRead=read;};
  void setUserWrite(const char *write){userWrite=write;};
  void setUserInit(const char *init){userInit=init;};
  void setSaveFormats(const char **formats){saveFormats=(char **)formats;};
  void setSaveDir(const char *dir){outdir=(char *)dir;};
  int  getPoints(){return nPoints;};
  double **getPVData(){return pvData;};
  int confirmDialog(const char *title, char *message, EMsgBoxIcon icon = kMBIconExclamation, Int_t buttons = kMBCancel+kMBOk);
  void setMAXPV(int maxpv){MAXPV=maxpv;};
  void setMAXDATA(int data){MAXDATA=data;};

  //functions for asimulated ioc
  void killSimIOC();
  void writeTestPVs();
  void simIOC(int m=0);

  //All these class data members should really start with "f" to keep in line with ROOT coding convention. Too late!
  //Change any of these before calling adding any PVs, or calling init()
  int MAXPV;                     
  int MAXDATA;     
  int MAXGRAPH;   	
  int MAXMULTI;    
  int MAXADDM;     	
  int MAXCANV;     	
  
  int CANVH;       
  int CANVW;	   
  int GUIH;        
  int GUIW;							
  int MCANVH;							
  int MCANVW;							
  int XPADD;
  int YPADD;
  int verbose;

  const char *REEPER;             //the env variable
  const char *outdir;              //directory for output and saves
  char **saveFormats;              //list of formats to be used for saving graphs etc
  char  **onOff;                   //char strings to represent on and off
  char fitopt[20];                 //options to be passed to fitting
  
  //Arrays to hold all the data
  TString        *pvNames;         //hold the PV names
  double        **pvData;          //pointers to the data arrays
  TGraph        **pvGraph;         //all the graphs
  int            *graphAuto;       //autoscale stuff
  double         *graphXfirst;       
  double         *graphXlast;       
  double         *graphYfirst;       
  double         *graphYlast;       
  double         *multiXfirst;       
  double         *multiXlast;       
  double         *multiYfirst;       
  double         *multiYlast;       
  TCanvas       **grCanvas;        //canvases for each graph 
  TMultiGraph   **pvMultiGraph;    //pointers to all the multigraphs
  int            *multiAuto;       //autoscale flag
  int           **multiIndices;    //hold indices of graphs in multigraphs
  TCanvas       **multiCanvas;     //canvases for each multigraph
  int            *pvGraphX;        //hold the indices of the data sets used for each graph
  int            *pvGraphY;
  TString        *grFits;          //hold fit and ranges for graphs
  double         *grFitMin;
  double         *grFitMax;
  int            *grFitDo;


  TCanvas       *grimCanvas ;   //a main canvas for the controlGUI. 
  TButton       *startButton;
  TButton       *pauseButton;
  TButton       *saveButton;
  TButton       *exitButton;
  TButton       *tIncButton;
  TButton       *tDecButton;
  TButton       *detailsButton;

  
  int nPV;             //no of loaded PVs
  int scanPeriod;      //default to 1s
  int scanTime;        //time counter
  int nPoints;         //no of reads
  int nGraphs;         //no of graphs
  int nCanvas;         //no of canvases
  int nMulti;          //no of mulit graphs
  int nMultiCanvas;    //no of multi canvases
  int refreshRate;     //how often to refresh the graphs (every 2 points default)
  int fitAfter;        //how many points required before trying a fit.
  int confirmScan;     //should ask for confirmation before doing a scan with caput commands.
  int scanStatus; 
  int guiToggle;

  //  char className[20];
  char commandString[128];         //cainfo command
  char getCommandString[256];      //caget command
  char putCommandString[128];      //caput command
  TString returnString;            //general return string
  TLegend *legend;
  
  TTimer  *pvTimer;                //to call the PV read (and possibly write) periodically
  TTimer  *guiTimer;
  
  int   scanPVIndex;               //index of PV to be scanned. Defaults to scanning on time (ie periodic readback only)
  const char *userRead;                  //custom read function called when epics readback is done.
  const char *userWrite;                 //custom write function called at the start of each step.
  const char *userInit;                  //custom init called to do initial positions for user scan
 
  double scanStart;                //defaults for stepping on PV for the scan  
  double scanStop;
  double scanStep;
  double scanVal;                  //current value
  
  int isInit;                      //flag if initialised
  
  //Stuff for the optional GUI
  int        isGUI;                //flag if GUI running
  int        maxlines;
  TPad      *titlepad1;
  TPad      *titlepad2;
  TPad      *titlepad3;
  TPad      *pvpad;
  TPad      *graphpad;
  TPad      *multipad;
  TPad      *buttonpad;
  TPaveText *pvtext;
  TPaveText *graphtext;
  TPaveText *multitext;
  TPaveText *statustext;
  TPaveText *pvlabel;
  TPaveText *graphlabel;
  TPaveText *multilabel;
  TPaveText *statuslabel;
  int         textPixels;  
  int         textLines ;  

  //some variables for a simulated ioc
  int updatePeriod;
  TTimer  *iocTimer;               //to push values to the simIOC
  TRandom *klrand;
  int testTime;                    //time counter for simIOC
  int mode;
  double AMO_SCALERS[100];

  ClassDef(GrimReeper, 0)
};

//This needs to be a global to allow the very crude way of using buttons!
GrimReeper *GR;

GrimReeper::GrimReeper(){
  MAXPV    = 50;          //Max no of PVs				
  MAXDATA  = 10000;       //Max no of data points per PV		
  MAXGRAPH = 100;         //Max no of graphs to draw			
  MAXMULTI = 20;          //Max no of canvases to mults to draw	
  MAXADDM  = 10;          //Max no of graphs to add to a multigraph	
  MAXCANV  = 20;          //Max no of canvases to use			
  
  CANVH    = 600;         //come canvas dimensions			
  CANVW    = 800;							
  GUIH     = 900;	
  GUIW     = 820;							
  MCANVH   = 500;							
  MCANVW   = 500;							
  XPADD    = 10;
  YPADD    = 40;                                                      
  
  scanPeriod  = 1;         //default to 1s
  verbose     = 1;         //default to verbose

  userRead      = NULL;    //custom read function called when epics readback is done.
  userWrite     = NULL;    //custom write function called at the start of each step.
  userInit      = NULL;    //custom write function called at the start of each step.
  
  scanStart    = 0.0;       //defaults for stepping on PV for the scan  
  scanStop     = 0.0;
  scanStep     = 0.0;
  scanVal      = 0.0;

  isInit       = 0;         //flag if initialised

  //Stuff for the optional GUI
  isGUI              = 0;      //flag if GUI running
  maxlines           = 20;
  textPixels         = 10;  
  textLines          = 20;

  sprintf(fitopt,"");
  
  outdir                   = (char *)defaultOutdir;
  saveFormats              = (char **)defaultFormats;
  onOff                    = (char **)onOffList;
  scanPVIndex              = Time;

  pvTimer                  = NULL;
  guiTimer                 = NULL;
  iocTimer                 = NULL;
  klrand                   = NULL;

  //init of simulation data;
  updatePeriod  = 1;
  testTime    = 0;             //time counter for simIOC
  mode = 0;

  
  //sprintf(className,"%s",myname);
  REEPER = gSystem->Getenv("REEPER");
  GR=(GrimReeper *)this;  //to make the finctions available as button methods (gr->Exit() etc)
}


void GrimReeper::init(){                       // initialise
  char namestring[128];
  char titlestring[128];
  char timerfunc[128];
  
 
  pvNames       = new TString[MAXPV];
  pvData        = new double*[MAXPV];          //pointers to the data arrays
  pvGraph       = new TGraph*[MAXGRAPH];       //all the graphs
  grCanvas      = new TCanvas*[MAXGRAPH];      //canvases for each graph 
  pvMultiGraph  = new TMultiGraph*[MAXMULTI];  //pointers to all the multigraphs
  multiIndices  = new int*[MAXMULTI];
  for(int n=0;n<MAXMULTI;n++){
    multiIndices[n]= new int[MAXADDM];         //hold indices of graphs in multigraphs
  }
  multiCanvas   = new TCanvas*[MAXGRAPH];      //canvases for each multigraph
  pvGraphX      = new int[MAXGRAPH];           //hold the indices of the data sets used for each graph
  pvGraphY      = new int[MAXGRAPH];
  grFits        = new TString[MAXGRAPH];       //hold fit and ranges for graphs
  grFitMin      = new double [MAXGRAPH];
  grFitMax      = new double[MAXGRAPH];
  grFitDo       = new int[MAXGRAPH];
  graphAuto     = new int[MAXGRAPH];
  multiAuto     = new int[MAXMULTI];
  graphXfirst   = new double[MAXGRAPH];
  graphXlast    = new double[MAXGRAPH];
  graphYfirst   = new double[MAXGRAPH];
  graphYlast    = new double[MAXGRAPH];
  multiXfirst   = new double[MAXMULTI];
  multiXlast    = new double[MAXMULTI];
  multiYfirst   = new double[MAXMULTI];
  multiYlast    = new double[MAXMULTI];
  
  pvNames[0]    = "Time";                      //the zeroth "PV" is always time 
  pvData[0]     = new Double_t[MAXDATA];       //create an array for it

  nPV         = 1;             //no of loaded PVs
  scanTime    = 0;             //time counter
  nPoints     = 0;             //no of reads
  nGraphs     = 0;             //no of graphs
  nCanvas     = 0;             //no of canvases
  nMulti      = 0;             //no of mulit graphs
  nMultiCanvas= 0;             //no of multi canvases
  refreshRate = 2;             //how often to refresh the graphs (every 2 points default)
  fitAfter    = 10;            //how many points required before trying a fit.
  confirmScan = 1;             //should ask for confirmation before doing a scan with caput commands.
  scanStatus  = GR_STOPPED; 
  guiToggle   = 0;

  //  sprintf(timerfunc,"%s->PVScanStep()",className);
  pvTimer       = new TTimer("GR->PVScanStep()",1000*scanPeriod);   //create timer with the default time

  gStyle->SetMarkerSize(1.5);                              //set dome default styles
  gStyle->SetMarkerStyle(20);

  
  fprintf(stdout, "\nInitialised\n\n");
  isInit     = 1;                                          //flag that init was called
}

int GrimReeper::addPV(const char *pvstring){               //Add a PV to the list for plotting

  char pvname[128];
  char checkString[128];
  char comString[128];
  char namestring[128];
  char titlestring[128];
  char conststring[128];

  if(!isInit) init();                                      //call init if required
  
  sscanf(pvstring, "%s", pvname);                          //scan into new string to strip any whitespace
  sprintf(checkString,"cainfo %s | grep State:",pvname);  //print the cainfo command to figure if the channel exists
  returnString = gSystem->GetFromPipe(checkString);        //capture the result from the command
  if(strstr(returnString.Data(),"never")){                 //return -1 if pv not found from chan access
    fprintf(stdout,"WARNING, PV not found: %s\n",pvname);
    return -1;
  }
  pvNames[nPV] = pvname;                                   //save the name
  pvData[nPV]  = new Double_t[MAXDATA];                    //create an array for it
  for(int p = 0;p<nPoints;p++){                            //if PV added after there are already points done, retro fill with zeros
    pvData[nPV][p]=0.0;
  }
  
  nPV++;                                                  //increment the no of PVs

  fprintf(stdout,"PV added to list: %s\n",pvname);
  if (nPV<=1) return 0;                                   //must be PVs other than "time"
  
  sprintf(getCommandString,"caget -t");                   //init the command to read them all
  for(int n=1;n<nPV;n++){                                 //add all the PVs to the string
    strcat(getCommandString," ");
    strcat(getCommandString,pvNames[n].Data());
  }
  strcat(getCommandString," | awk '{printf\"%s \",$1}'");

  if(isGUI==GR_BIGGUI)updatePvList();                     //if full GUI, update the pvlist
  return 0;
}

void GrimReeper::printPVs(){                  //print the current list with indices
  fprintf(stdout,"\nFull list of PVs is:\n");
  fprintf(stdout,"Index   %-50s\n","PV name (can be used as index)");
  fprintf(stdout,"%2d\t%-50s\t%s\n",0,"Time (Time(s) is local pv, always present)","n/a");
  for(int n=1;n<nPV;n++){
    fprintf(stdout,"%2d\t%-50s\n",n,pvNames[n].Data());
  }
  fprintf(stdout,"\n");
  fprintf(stdout,"The caget command is:\n");
  fprintf(stdout,"%s\n\n",getCommandString);
}  

void GrimReeper::printGraphs(){                  //print the current list with indices
  fprintf(stdout,"\nFull list of Graphs is:\n");
  fprintf(stdout,"Index\t%-50s\tFit    \tFitRange           \tnPoints\n","Graph Name (can be used as index)");
  for(int n=0;n<nGraphs;n++){
    if(grFitDo[n] == GR_FITRANGE){
      fprintf(stdout,"%-2d\t%-50s%10s\t%5.2lf - %5.2lf\t\t%2d\n",n,grCanvas[n]->GetName(),grFits[n].Data(), grFitMin[n], grFitMax[n], pvGraph[n]->GetN());
    }
    else{
      fprintf(stdout,"%-2d\t%-50s%10s\t\t\t\t%2d\n",n,grCanvas[n]->GetName(),grFits[n].Data(), pvGraph[n]->GetN());      
    }
  }
  fprintf(stdout,"\n");
}


void GrimReeper::PVScanStep(){  //This is called by the timer
  char command[128];
  char warning[500];
  int ret;
  char *data, *eptr;
  int n = 1;
  
  if(verbose)fprintf(stdout,"Doing step number %d: ", nPoints);
  
  pvData[Time][nPoints] = (double)scanTime;           //save the time as pv0
  scanTime += scanPeriod;                                //increment the timer

  if(verbose)fprintf(stdout,"%s\n",getCommandString);
  returnString = gSystem->GetFromPipe(getCommandString); //read
  if(verbose)fprintf(stdout,"%s\n",returnString.Data());  

  data=(char *)returnString.Data();
  do {                                      //loop over in this old fashioned way
    pvData[n][nPoints]=strtod(data, &eptr);
    if(verbose)fprintf(stdout,"%-50s\t%g\n",pvNames[n].Data(),pvData[n][nPoints]);
    data = eptr;
    n++;
  } while ((*eptr)&&(n<nPV));

  if(userRead){
    gROOT->ProcessLine(userRead);
  }
  nPoints++;
  if(isGUI)updateStatus();
  
  if(nPoints>=MAXDATA){
    stopScanning();
    sprintf(warning,"The limit of %d sets of readings has been reached.", MAXDATA);
    confirmDialog("Message from the GRIM REEPER",warning,kMBIconStop,kMBOk);
    updateStartButton();
    updatePauseButton();
    return;
  }
  
  //if it's writing a PV, do the next step
  if(scanPVIndex){
    scanVal+=scanStep;
    if(scanVal<=scanStop){
      sprintf(command,"caput -t %s %g > /dev/null", pvNames[scanPVIndex].Data(), scanVal);    //go to the next position
      gSystem->Exec(command);
    }
    else{
      scanVal-=scanStep;
      stopScanning();
    }
  }
  if(userWrite){
    gROOT->ProcessLine(userWrite);
  }
  
  if((nPoints%refreshRate==0)||(nPoints==1)) drawGraphs(); //try updating 
}


void GrimReeper::startScanning(){
  char command[128];
  char warning[500];
  int ret;

  if(scanStatus==GR_STARTED){
    fprintf(stdout,"WARNING: The scan is already started\n");
    return;  //If it's already started return
  }

  if(scanStatus==GR_STOPPED){

    if(nPoints>0){      
      sprintf(warning,"WARNING. This will clear all graphs and restart any scans.\nSave first if you need to.\n"); //make a big string
      
      fprintf(stdout,"%s",warning);  //print on stdout, and open confim dialogue
      ret=confirmDialog("Message from the GRIM REEPER",warning,kMBIconExclamation,kMBCancel+kMBOk);
      
      if(ret!=kMBOk) return;         //Don't start unless OK
      else resetGrim();
    }
    
    if(scanPVIndex){     //if time is not the control variable, init the control variable before starting scan
      if(confirmScan){   //if cautious, ask for confirmation
	sprintf(warning,"SCANNING: About to start scan which will cause values to be written to a PV as follows:\n"); //make a big string
	sprintf(warning,"%sPV name:    %s\n",warning,pvNames[scanPVIndex].Data());
	sprintf(warning,"%sStart:      %g\n",warning,scanStart);
	sprintf(warning,"%sStop:       %g\n",warning,scanStop);
	sprintf(warning,"%sStep:       %g\n",warning,scanStep);
	sprintf(warning,"%sPeriod(s):  %d    ( = time to wait between steps)\n",warning,scanPeriod);
	sprintf(warning,"%sARE YOU REALLY SURE YOU WANT TO DO THIS ? \n",warning);
	
	fprintf(stdout,"%s",warning);  //print on stdout, and open confim dialogue
	ret=confirmDialog("Message from the GRIM REEPER",warning,kMBIconExclamation,kMBCancel+kMBOk);
      
	if(ret!=kMBOk) return;         //Don't start unless OK
      }
      
      //    sprintf(command,"caput -t %s %g > /dev/null", pvNames[scanPVIndex].Data(), scanStart); //go to the starting poition
      sprintf(command,"caput %s %g", pvNames[scanPVIndex].Data(), scanStart); //go to the starting poition
      gSystem->Exec(command);
      
      scanVal=scanStart;             //save this for the next steps
    }

    if(userWrite){                   //The user has some proceedure to write EPICS. Warn the user!
      if(confirmScan){   //if cautious, ask for confirmation
	sprintf(warning,"WARNING form the GRIM REEPER\n");                //make a big string
	sprintf(warning,"%sIt looks like you are about to write to EPICS PVs with your own custom procedure\n",warning);
	sprintf(warning,"%sARE YOU REALLY SURE YOU WANT TO DO THIS ? \n",warning);
	fprintf(stdout,"%s",warning);  //print on stdout, and open confim dialogue
	ret=confirmDialog("Message from the GRIM REEPER",warning,kMBIconExclamation,kMBDismiss+kMBOk);
	if(ret!=kMBOk) return;         //Don't start unless OK
      }
      if(userInit){     //if init function, call before starting
	gROOT->ProcessLine(userInit);
      }
    }
  }
  pvTimer->Start(scanPeriod*1000);   //start the timer which calls the scan step function
  scanStatus = GR_STARTED;
  if(isGUI)updateGUI();
}


void GrimReeper::stopScanning(){
  if(pvTimer){
    pvTimer->Stop();
    fprintf(stdout,"\nStopped any scans\n");
    scanStatus = GR_STOPPED;
    if(isGUI)updateGUI();
  }
}
void GrimReeper::pauseScanning(){
  if(pvTimer){
    pvTimer->Stop();
    fprintf(stdout,"\nPaused any scans\n");
    scanStatus = GR_PAUSED;
    if(isGUI)updateGUI();
  }
}
void GrimReeper::resumeScanning(){
  if(pvTimer){
    pvTimer->Start();
    fprintf(stdout,"\nResumed any scans\n");
    scanStatus = GR_STARTED;
    if(isGUI)updateGUI();
  }
}

void GrimReeper::makeGraph(const char *yPVName, const char *xPVName, const char* pvfit, double rangemin, double rangemax) {
  int x=-1,y=-1;
  for(int n=0;n<nPV;n++){
    if(!strcmp(yPVName,pvNames[n].Data()))y=n;
    if(!strcmp(xPVName,pvNames[n].Data()))x=n;
  }
  if((x!=y)&&(y>=0)&&(y<nPV)&&(x>=0)&&(x<nPV)){
    makeGraph(y,x,pvfit,rangemin,rangemax);
  }
  else{
    fprintf(stderr,"ERROR: plotting %s vs %s is not possible. Available PVs are:",yPVName,xPVName);
    printPVs();
    fprintf(stderr,"Select 2 different sets from the above list");
  }
}
  

void GrimReeper::makeGraph(int yPV, int xPV, const char* pvfit, double rangemin, double rangemax) {
  char titlestring[128];
  char namestring[128];
  int xcoord,ycoord;
  char conststring[128];
  TClass *cl;
  TList*l;
  TClassMenuItem* mi;  
    
  if((xPV>=nPV)||(yPV>=nPV)||(xPV==yPV)){
    fprintf(stderr,"ERROR: plotting set[%d] vs set[%d] is not possible. Available sets are:",yPV,xPV);
    printPVs();
    fprintf(stderr,"Select 2 different sets from the above list");
    return;
  }
  
  for(int n=0; n<nGraphs; n++){
    if((pvGraphX[n]==xPV)&&(pvGraphY[n]==yPV)){
      fprintf(stderr,"ERROR: a graph of set[%d] vs set[%d] is not possiblealready exists. Available sets are:",yPV,xPV);
      printPVs();
      fprintf(stderr,"Select 2 different sets from the above list");
      return;
    }
  }
  if(nPoints==0){
    pvData[xPV][0]=0.0;pvData[yPV][0]=0.0;         //force 1st point of 0 to allow multigraphs to be made.
  }
  pvGraph[nGraphs] = new TGraph(1,pvData[xPV],pvData[yPV]);
  pvGraph[nGraphs]->SetMarkerColor((6*nGraphs)+50);
  pvGraph[nGraphs]->SetMarkerStyle(nGraphs+20);
  pvGraphX[nGraphs] = xPV;
  pvGraphY[nGraphs] = yPV;

  sprintf(titlestring,"pvGraph[%d]: %s v %s", nGraphs, pvNames[pvGraphY[nGraphs]].Data(),pvNames[pvGraphX[nGraphs]].Data());
  sprintf(namestring,"graph%d_%s_v_%s", nGraphs, pvNames[pvGraphY[nGraphs]].Data(),pvNames[pvGraphX[nGraphs]].Data());

  fprintf(stderr,"%s %s %s\n", titlestring,namestring, pvfit);
  
  pvGraph[nGraphs]->SetTitle(titlestring);
  pvGraph[nGraphs]->SetName(namestring);
      
  //store the fit for the graph
  //fprintf(stderr,"pvfitstr = %s\n",pvfit);
  if(strlen(pvfit)>2){
    grFits[nGraphs].Append(pvfit);
    grFitMin[nGraphs] = rangemin;
    grFitMax[nGraphs] = rangemax;
    if(TMath::Abs(rangemax-rangemin)<0.000001){    //tiny, so don't use fit range
      grFitDo[nGraphs] = GR_FIT;
    }
    else{
      grFitDo[nGraphs] = GR_FITRANGE;
    }
  }
  else{
    grFitDo[nGraphs]=GR_NOFIT;
    grFits[nGraphs].Append(pvfit);
  }

  
  //make a canvas for the graph
  sprintf(titlestring,"%s v %s", pvNames[pvGraphY[nGraphs]].Data(),pvNames[pvGraphX[nGraphs]].Data());
  sprintf(namestring,"Graph%d_%s_v_%s", nGraphs, pvNames[pvGraphY[nGraphs]].Data(),pvNames[pvGraphX[nGraphs]].Data());
  
  xcoord = GUIW + 20 + (XPADD*nGraphs);
  ycoord = 30+YPADD*nGraphs; 

  grCanvas[nGraphs] = new TCanvas(namestring,titlestring,xcoord,ycoord,CANVW,CANVH);

  //as soon as a graph canvas is made, set the context menu to have extra item for toggling autoscaling
  //this adds it to the context menu for all TGraphs

  if(nGraphs==0){
    cl = grCanvas[nGraphs]->IsA();
    cl->SetContextMenuTitle("GrimReeper");
    l  = cl->GetMenuList();
    //l->RemoveAll();
    mi = new TClassMenuItem(TClassMenuItem::kPopupUserFunction,cl,"toggle autoscale","setAuto",GR,"TObject *",0);
    l->AddFirst(mi);
  }
  

  graphAuto[nGraphs]=GR_AUTO;                                        //default to auto scaling
  graphXfirst[nGraphs] = 0.0;
  graphXlast[nGraphs]  = 0.0;
  graphYfirst[nGraphs] = 0.0;
  graphYlast[nGraphs]  = 0.0;
  
  sprintf(namestring,"%s_v_%s", pvNames[pvGraphY[nGraphs]].Data(),pvNames[pvGraphX[nGraphs]].Data());
  fprintf(stdout,"Added graph %s\n",namestring);
  sprintf(conststring,"const int %s = %d;",namestring, nGraphs);  //make a line to define a const for the graph.
  gROOT->ProcessLine(conststring);                                //now PV names can be used as enum array indices
  nGraphs++;

  if(isGUI==GR_BIGGUI){
    updateGraphList();
  }
}

//This gets called from the graph menu, passing the object associated with the menu.
void GrimReeper::setAuto(TObject *gr){
  int g;
  if(strstr(gr->GetName(),"Multi")){
    sscanf(gr->GetName(),"MultiGraph%d",&g);
    setMultiAuto(g,GR_TOGGLE);    
  }

  else{
    sscanf(gr->GetName(),"Graph%d_",&g);
    setGraphAuto(g,GR_TOGGLE);
  }
}

void GrimReeper::setGraphAuto(int g, int a){
  if(a==GR_TOGGLE)graphAuto[g]=!graphAuto[g];
  else graphAuto[g]=a;
  if(isGUI==GR_BIGGUI)updateGraphList();
}

void GrimReeper::setMultiAuto(int g, int a){
  double xf,xl;

  if(a==GR_TOGGLE)multiAuto[g]=!multiAuto[g];
  else multiAuto[g]=a;
  
  if(multiAuto[g]==GR_MANUAL){
    xf = pvMultiGraph[g]->GetXaxis()->GetBinCenter(pvMultiGraph[g]->GetXaxis()->GetFirst());
    xl = pvMultiGraph[g]->GetXaxis()->GetBinCenter(pvMultiGraph[g]->GetXaxis()->GetLast());
    multiXfirst[g]=xf;    
    multiXlast[g]=xl;
  }
  if(isGUI==GR_BIGGUI)updateMultiList();
}

void GrimReeper::updateGraph(int g){
  double xf=0.0,xl=0.0;
  
  if(nPoints==1){          //if its 1st point, replace the dummy 0,0 point with the real one.
    pvGraph[g]->SetPoint(0,pvData[pvGraphX[g]][0],pvData[pvGraphY[g]][0]);
  } 
  if(graphAuto[g]==GR_MANUAL){
    //    xf = pvGraph[g]->GetXaxis()->GetBinLowEdge(pvGraph[g]->GetXaxis()->GetFirst());
    //    xl = pvGraph[g]->GetXaxis()->GetBinUpEdge(pvGraph[g]->GetXaxis()->GetLast());
    xf = pvGraph[g]->GetXaxis()->GetBinCenter(pvGraph[g]->GetXaxis()->GetFirst());
    xl = pvGraph[g]->GetXaxis()->GetBinCenter(pvGraph[g]->GetXaxis()->GetLast());
    graphXfirst[g]=xf;    
    graphXlast[g]=xl;
    //    if((TMath::Abs((xf-graphXfirst[g])/graphXfirst[g]))>0.2)graphXfirst[g]=xf;
    //    if((TMath::Abs((xl-graphXlast[g])/graphXlast[g]))>0.2)graphXlast[g]=xl;
    graphYfirst[g]=pvGraph[g]->GetHistogram()->GetMinimum();
    graphYlast[g]=pvGraph[g]->GetHistogram()->GetMaximum();
    
  }
  if(nPoints>pvGraph[g]->GetN()){
    for(int p=pvGraph[g]->GetN();p<nPoints;p++){
      pvGraph[g]->SetPoint(p,pvData[pvGraphX[g]][p],pvData[pvGraphY[g]][p]);
    }
  }
  if(graphAuto[g]==GR_MANUAL) pvGraph[g]->GetXaxis()->SetRangeUser(xf,xl);
  
}


void GrimReeper::drawGraphs(){
  double xf,xl;

  for(int m=0;m<nMulti;m++){   //store the ranges of the multigraphs before updating graphs
    if(multiAuto[m]==GR_MANUAL){
      xf = pvMultiGraph[m]->GetXaxis()->GetBinCenter(pvMultiGraph[m]->GetXaxis()->GetFirst());
      xl = pvMultiGraph[m]->GetXaxis()->GetBinCenter(pvMultiGraph[m]->GetXaxis()->GetLast());
      multiXfirst[m]=xf;    
      multiXlast[m]=xl;
    }
  }

  for(int g=0;g<nGraphs;g++){
    drawGraph(g);
  }
  updateMultiGraphs();
}

void GrimReeper::drawGraph(int g){
  char fopt[10];
  char dopt[10]="AP";

  
  if(!nPoints){
    fprintf(stdout, "ERROR: No data accumulated yet. Be patient. Or did you forget to start scanning?\n");
    return;
  }
  updateGraph(g);
  grCanvas[g]->cd();

  if((grFitDo[g]==GR_NOFIT)&&(strlen(grFits[g].Data())>0)){
    strcat(dopt,grFits[g].Data());
  }
  if(graphAuto[g]==GR_MANUAL){
    //pvGraph[g]->GetXaxis()->SetRangeUser(graphXfirst[g],graphXlast[g]);
    pvGraph[g]->GetHistogram()->SetMinimum(graphYfirst[g]);
    pvGraph[g]->GetHistogram()->SetMaximum(graphYlast[g]);
    
  }
  else{
    pvGraph[g]->GetXaxis()->SetRange(0.0,0.0);
    pvGraph[g]->GetYaxis()->UnZoom();
  }
  pvGraph[g]->Draw(dopt);
  if(pvGraphX[g]==Time)pvGraph[g]->GetHistogram()->GetXaxis()->SetTitle("Time (s)");
  else pvGraph[g]->GetHistogram()->GetXaxis()->SetTitle(pvNames[pvGraphX[g]].Data());
  ((TRootCanvas*)grCanvas[g]->GetCanvasImp())->DontCallClose(); //don't allow closing the graph canvas
  pvGraph[g]->Draw(dopt);
 
  
  if((grFitDo[g])&&(nPoints>10)){                               //only apply fits after 10 points
    sprintf(fopt,"q%s",fitopt);
    if(grFitDo[g]==GR_FIT){
      pvGraph[g]->Fit(grFits[g].Data(),fopt);
    }
    else{
      sprintf(fopt,"q%sR",fitopt);
      pvGraph[g]->Fit(grFits[g].Data(),fopt,"", grFitMin[g],grFitMax[g]);
    }
  }
  grCanvas[g]->Update();
}

void GrimReeper::makeMultiGraph(const char *title, const char *g0,const char *g1,const char *g2,const char *g3,const char *g4,const char *g5,const char *g6,const char *g7,const char *g8,const char *g9){
  const char *mc[10];
  mc[0]=g0;mc[1]=g1;mc[2]=g2;mc[3]=g3;mc[4]=g4;mc[5]=g5;mc[6]=g6;mc[7]=g7;mc[8]=g8;mc[9]=g9;
  int mg[10];
  int match=-1;
  int mcount=0;

  for(int n=0;n<10;n++){
    fprintf(stderr,"making multi %d, %s\n",n,mc[n]);
    mg[n]=-1;
  }
  
  int g=0;
  while(mc[g]!=NULL){
    match=-1;
    for(int n=0;n<nGraphs;n++){
      fprintf(stderr, "%d %s %s %d\n",n,mc[g],strstr(pvGraph[n]->GetName(),"_")+1,strcmp(mc[g],strstr(pvGraph[n]->GetName(),"_")+1));
      if(strcmp(mc[g],strstr(pvGraph[n]->GetName(),"_")+1)==0){
	match=n;
	break;
      }
    }
    if(match==-1){
      fprintf(stderr, "Error: makeMultiGraph(\"%s\",....) graph \"%s\" does not exist\n",title,mc[g]);
    }
    else{
      mg[mcount++]=match;
    }
    g++;
  }
  if(mcount>1){
    makeMultiGraph(title,mg);
  }
}


void GrimReeper::makeMultiGraph(const char *title, int g0,int g1,int g2,int g3,int g4,int g5,int g6,int g7,int g8,int g9){
  //This one gets called by hand - allowing up to 10 graphs on the command line
  //Just fills an array and calls the proper version of makeMultiGraph
  int mg[10];
  mg[0]=g0;mg[1]=g1;mg[2]=g2;mg[3]=g3;mg[4]=g4;mg[5]=g5;mg[6]=g6;mg[7]=g7;mg[8]=g8;mg[9]=g9;
  makeMultiGraph(title,mg);
}

void GrimReeper::makeMultiGraph(const char *title,int *mg){

  char namestring[128];
  char titlestring[128];
  int mcount=0;
  
  legend = new TLegend(0.6,0.7,0.90,0.90);                         //Create a legend

  sprintf(titlestring,"pvMultiGraph[%d]: %s",nMulti,title);        //make name and titles
  sprintf(namestring,"MultiGraph%d",nMulti);
	  
  pvMultiGraph[nMulti] = new TMultiGraph(namestring,titlestring);  //new multigraph


  for(int n=0; n<10;  n++){                                        //init the list of indices
    multiIndices[nMulti][n]=-1;
  }
  for(int g=0;g<10;g++){                                           //loop over the requested graphs
    if(mg[g]==-1) break;
    if(!pvGraph[mg[g]]){                                           //check they exist
      fprintf(stdout,"Warning: pvGraph[%d] doesn't exist\n",mg[g]);
    }
    else{
      pvMultiGraph[nMulti]->Add(pvGraph[mg[g]]);                   //add graph, save index and add to legend
      multiIndices[nMulti][mcount++]=mg[g];
      legend->AddEntry(pvGraph[mg[g]],pvNames[pvGraphY[mg[g]]],"pl");
    }
  }

  multiAuto[nMulti]   = GR_AUTO;                                        //default to auto scaling
  multiXfirst[nMulti] = 0.0;
  multiXlast[nMulti]  = 0.0;
  multiYfirst[nMulti] = 0.0;
  multiYlast[nMulti]  = 0.0;

  sprintf(namestring,"MultiGraphCanvas%d",nMulti);                 //name and create canvas
  multiCanvas[nMulti]  = new TCanvas(namestring,titlestring,1250+CANVW+2*XPADD*nMulti,2*YPADD*(nMulti),MCANVW,MCANVH);
  multiCanvas[nMulti]->cd();
  ((TRootCanvas*)multiCanvas[nMulti]->GetCanvasImp())->DontCallClose(); //don't allow closing the graph canvas
  pvMultiGraph[nMulti]->Draw("ap");
  if(pvGraphX[mg[0]]==Time) pvMultiGraph[nMulti]->GetXaxis()->SetTitle("Time (s)"); //If time, give x axis label units of s
  else pvMultiGraph[nMulti]->GetXaxis()->SetTitle(pvNames[pvGraphX[mg[0]]]);        //else just pv name
  
  legend->Draw();           
  
  multiCanvas[nMulti]->Modified();                                 //force the drawing before coloring the canvas
  multiCanvas[nMulti]->Update();                                   //to keep the actual graph white
  multiCanvas[nMulti]->SetFillColor(20+(3*nMulti));
  multiCanvas[nMulti]->Modified();
  multiCanvas[nMulti]->Update();

  nMulti++;
  
  if(isGUI==GR_BIGGUI) updateMultiList();                                     //if there's a GUI update the list. 
}


void GrimReeper::updateMultiGraphs(){
  for(int g=0;g<nMulti;g++){
    updateMultiGraph(g);
  }
} 
void GrimReeper::updateMultiGraph(int m){
  double xmin,xmax,tmin,tmax;
  double ymin,ymax,umin,umax;
  TGraph *g;

  
  TList *l = pvMultiGraph[m]->GetListOfGraphs();
  TIter next(l);
  
  xmin = ((TGraph*)l->First())->GetXaxis()->GetXmin();
  xmax = ((TGraph*)l->First())->GetXaxis()->GetXmax();
  ymin = ((TGraph*)l->First())->GetYaxis()->GetXmin();
  ymax = ((TGraph*)l->First())->GetYaxis()->GetXmax();
  
  while((g=(TGraph*)next())){
    tmin=g->GetXaxis()->GetXmin();
    tmax=g->GetXaxis()->GetXmax();
    umin=g->GetYaxis()->GetXmin();
    umax=g->GetYaxis()->GetXmax();
    if(tmin<xmin)xmin=tmin;
    if(tmax>xmax)xmax=tmax;
    if(umin<ymin)ymin=umin;
    if(umax>ymax)ymax=umax;
  }
  pvMultiGraph[m]->GetXaxis()->SetLimits(xmin,xmax);
  if(multiAuto[m]==GR_AUTO)pvMultiGraph[m]->GetXaxis()->SetRangeUser(xmin,xmax);
  else pvMultiGraph[m]->GetXaxis()->SetRangeUser(multiXfirst[m],multiXlast[m]);
  
  
  
  pvMultiGraph[m]->GetYaxis()->SetLimits(ymin,ymax);
  if(nPoints<10)pvMultiGraph[m]->GetYaxis()->SetRangeUser(ymin,ymax); //autoscale on the basis of the 1st 10 points
  if(multiAuto[m]==GR_AUTO)pvMultiGraph[m]->GetYaxis()->SetRangeUser(ymin,ymax);
  
  multiCanvas[m]->cd();
  gPad->Modified(); 
  multiCanvas[m]->Update();
}
 
void GrimReeper::changePeriod(int t){
  scanPeriod += t;
  if(scanPeriod<1)scanPeriod=1;
  pvTimer->SetTime(1000*scanPeriod);
  if(isGUI)updateGUI();
}

void GrimReeper::saveAll(){  //save data in column format and save canvases in some sort of format

  FILE *fp;
  char filename[100];
  char command[100];
  char warning[500];
  int ret;
  
  TString date = gSystem->GetFromPipe("date '+%d_%m_%y-%H_%M'");   //get date for timestamping files

    
  sprintf(filename,"%s/gr_save_%s.txt",outdir,date.Data());  

  sprintf(warning,"Save all data.\n"); //make a big string
  sprintf(warning,"%sAll PV data will be saved in columns in file: %s \n",warning,filename);
  sprintf(warning,"%sand graph canvases as %s/<graphname>_%s.<formats>  \n",warning,outdir,date.Data());
    
  fprintf(stdout,"%s",warning);  //print on stdout, and open confim dialogue
  ret=confirmDialog("Message from the GRIM REEPER",warning,kMBIconQuestion,kMBCancel+kMBOk);
  if(ret!=kMBOk) return;         //Don't startsave unless OK
  
  sprintf(command,"mkdir -p %s",outdir);                      //make the output directory if it doesn't exist
  gSystem->Exec(command);
  fp = fopen(filename,"w");
  for(int n=0;n<nPV;n++){                                     //write the pv infor as #comments at top of file
    fprintf(fp,"# PV%d = %s\n",n,pvNames[n].Data());
  }
  fprintf(fp,"#step");                                        //write column headers as #comment
  for(int n=0;n<nPV;n++){
    fprintf(fp,"\t\tPV%d",n);
  }
  fprintf(fp,"\n");
  for(int p=0;p<nPoints;p++){
    fprintf(fp,"%d",p);
    for(int n=0;n<nPV;n++){
      fprintf(fp,"\t%8.4lf",pvData[n][p]);
    }
    fprintf(fp,"\n");
  }
  fclose(fp);


  for(int g=0;g<nGraphs;g++){
    int f=0;
    while(saveFormats[f]){
      sprintf(filename,"%s/%s_%s.%s",outdir,grCanvas[g]->GetName(),date.Data(),saveFormats[f]);
      fprintf(stderr,"Saving %s\n",filename);
      grCanvas[g]->SaveAs(filename);
      f++;
    }
  }
	      
}

void GrimReeper::resetGrim(){
  nPoints = 0; //reset npoints
  scanTime=0.0;
  for(int g=0;g<nGraphs;g++){
    pvGraph[g]->Set(1);
    pvGraph[g]->SetPoint(0,0.0,0.0);
    if(pvGraph[g]->GetListOfFunctions()->First()) delete pvGraph[g]->GetListOfFunctions()->First();
  }
  if(isGUI)updateGUI();
}


int GrimReeper::confirmDialog(const char *title, char *message, EMsgBoxIcon icon, Int_t buttons){
  TGMsgBox *box;
  int ret=0;
  //get confirmation from dialog box if isGUI, otherwise from root CINT.
  if(isGUI){
    box = new TGMsgBox(gClient->GetRoot(),0,title, message,icon,buttons,&ret,0,0);
  }
  else{
    fprintf(stderr,"** %s **\n",title); 
    if(buttons==kMBOk){                      //no confirm reqd
      fprintf(stderr,"%s\n",message); 
    }
    else{
      fprintf(stderr,"%s (y/n)?",message);     //a fudge to allow CINT to get response from the command line (return 4 if OK, since kMBOk = 4).
      sscanf((gSystem->GetFromPipe("read p;echo $p|awk '{if($1==\"y\"){print 4}else{print 0}}'")).Data(),"%d",&ret);
    }
  }
  return ret;
}

void GrimReeper::exitGrim(){
  killSimIOC();
  exit(0);
}

void GrimReeper::setScan(int pvindex,double start, double stop, double step){
  scanPVIndex = pvindex;
  scanStart   = start;
  scanStop    = stop;
  scanStep    = step;
  fprintf(stdout,"Scanning %s, %lg ---> %lg, step = %lg\n\n",pvNames[scanPVIndex].Data(),scanStart,scanStop,scanStep);
}

void GrimReeper::setScan(const char *pvname,double start, double stop, double step){
  scanPVIndex = Time;
  for(int n=1;n<nPV;n++){
    if(!strcmp(pvname,pvNames[n].Data()))scanPVIndex=n;
  }
  if(scanPVIndex==Time){
    fprintf(stderr,"ERROR: setScan(\"%s\" .....)  PVName \"%s\" is wrong, or has not been added with addPV(\"%s\")\n\n",pvname,pvname,pvname);
    return;
  }
  scanStart = start;
  scanStop  = stop;
  scanStep  = step;
  fprintf(stdout,"Scanning %s, %lg ---> %lg, step = %lg\n\n",pvNames[scanPVIndex].Data(),scanStart,scanStop,scanStep);
}

//Functions for the optional GUI
//A simple GUI with only TButtons. However, added functions are on the ContextMenus (RH Mouse button)

void GrimReeper::makeControlGUI(int guisize){
  char string[200];
  char method[200];
  TClass *cl;
  TList*l;
  TClassMenuItem* mi;  
  
  
  if(!guiTimer) guiTimer = new TTimer("GR->toggleGUI()",200); //create timer
  guiTimer->Start();

  
  gStyle->SetPadBorderMode(1);
  gStyle->SetPadBorderSize(2);
  //if(!grimCanvas){
  if(1){
    if(guisize==GR_SMALLGUI){
      grimCanvas = new TCanvas("grimCanvas","grimCanvas",  10,    10, GUIW, 0.45*GUIH);
      ((TRootCanvas*)grimCanvas->GetCanvasImp())->DontCallClose(); //don't allow closing the canvas
      
      titlepad1   = new TPad(  "titlepad1", "titlepad1",    0,   0.33,  0.2, 1.0,  0);titlepad1->Draw(); 
      titlepad2   = new TPad(  "titlepad2", "titlepad2",   0.2,  0.33,  0.8, 1.0,  0);titlepad2->Draw(); 
      titlepad3   = new TPad(  "titlepad3", "titlepad3",   0.8,  0.33,  1.0, 1.0,  0);titlepad3->Draw(); 
      buttonpad   = new TPad(  "buttonpad", "buttonpad",     0,  0.0, 1.0,  0.33, 0);buttonpad->SetFillColor(30);buttonpad->Draw(); 
    }
    else{
      grimCanvas = new TCanvas("grimCanvas","grimCanvas",  10,    10, GUIW, GUIH);
      ((TRootCanvas*)grimCanvas->GetCanvasImp())->DontCallClose(); //don't allow closing the canvas

      titlepad1   = new TPad(  "titlepad1", "titlepad1",    0,   0.7,  0.2, 1.0,  0);titlepad1->Draw(); 
      titlepad2   = new TPad(  "titlepad2", "titlepad2",   0.2,  0.7,  0.8, 1.0,  0);titlepad2->Draw(); 
      titlepad3   = new TPad(  "titlepad3", "titlepad3",   0.8,  0.7,  1.0, 1.0,  0);titlepad3->Draw(); 
      buttonpad   = new TPad(  "buttonpad", "buttonpad",     0,  0.55, 1.0, 0.7,  0);buttonpad->SetFillColor(30);buttonpad->Draw(); 
      pvpad       = new TPad(  "pvpad",     "pvpad",         0,  0.15, 0.3, 0.55, 0);pvpad->SetFillColor(30);pvpad->Draw(); 
      graphpad    = new TPad(  "graphpad",  "graphpad",    0.3,  0.15, 1.0, 0.55, 0);graphpad->SetFillColor(30);graphpad->Draw(); 
      multipad    = new TPad(  "multipad",  "multipad",      0,  0.00, 1.0, 0.15, 0);multipad->SetFillColor(30);multipad->Draw(); 
    }
    titlepad1->cd();
    
    sprintf(string,"%s/Grim_Reaper.png",REEPER);
    TImage *img1 = TImage::Open(string);
    img1->Draw();
    img1->SetConstRatio(kTRUE);
    img1->SetEditable(kTRUE);
    titlepad1->SetEditable(kFALSE);

    titlepad2->cd();
    sprintf(string,"%s/welcome2.png",REEPER);
    TImage *img2 = TImage::Open(string);
    img2->Draw();
    img2->SetConstRatio(kFALSE);
    img2->SetEditable(kTRUE);
    titlepad2->SetEditable(kFALSE);
    
    titlepad3->cd();
    sprintf(string,"%s/EPICS_Logo-192x192.png",REEPER);
    TImage *img3 = TImage::Open(string);
    img3->Draw();
    img3->SetConstRatio(kTRUE);
    img3->SetEditable(kTRUE);
    titlepad3->SetEditable(kFALSE);


    if(nGraphs > textLines) textLines = nGraphs;
    if(nPV > textLines)     textLines = nPV;
    textPixels = (GUIH*0.4*0.87)/textLines;

    buttonpad->SetFillColor(30);
    buttonpad->SetBorderMode(1);
    buttonpad->cd();

    //sprintf(method,"%s->startScanning()",className);
    startButton = new TButton("Start","GR->startScanning()",0.02,0.75,0.15,0.9);
    startButton->Draw();
    updateStartButton();

    buttonpad->cd();
    //sprintf(method,"%s->pauseScanning()",className);
    pauseButton = new TButton("Pause","GR->pauseScanning()",0.02,0.60,0.15,0.75);
    pauseButton->Draw();
    updatePauseButton();

    buttonpad->cd();
    //sprintf(method,"%s->saveAll()",className);
    saveButton = new TButton("Save","GR->saveAll()",0.02,0.45,0.15,0.60);
    saveButton->Draw();

    buttonpad->cd();
    //sprintf(method,"%s->exitGrim()",className);
    exitButton = new TButton("Exit","GR->exitGrim()",0.02,0.3,0.15,0.45);
    exitButton->Draw();

    buttonpad->cd();
    //sprintf(method,"%s->setGuiToggle()",className);
    detailsButton = new TButton("Detail (show/hide)","GR->setGuiToggle()",0.02,0.05,0.15,0.2);
    detailsButton->Draw();

    //sprintf(method,"%s->changePeriod(-1)",className);
    tDecButton = new TButton("<","GR->changePeriod(-1)",0.36,0.6,0.39,0.72); 
    tDecButton->SetBorderMode(0);tDecButton->SetBorderSize(0);tDecButton->Draw();
    //sprintf(method,"%s->changePeriod(1)",className);
    tIncButton = new TButton(">","GR->changePeriod(1)",0.39,0.6,0.42,0.72); 
    tIncButton->SetBorderMode(0);tIncButton->SetBorderSize(0);tIncButton->Draw();
    
    statuslabel=new TPaveText(0.18,0.1,0.36,0.9,"NB");
    statuslabel->SetTextFont(103);
    statuslabel->SetFillColor(30);
    statuslabel->SetTextAlign(32);
    statuslabel->SetTextSize(textPixels);
    statuslabel->AddText("nPoints:");
    statuslabel->AddText("Period(s):");
    statuslabel->AddText("Scanning:");
    statuslabel->AddText("Read func:");
    statuslabel->AddText("Write func:");
    statuslabel->Draw();

    statustext=new TPaveText(0.42,0.1,0.98,0.9,"NB");
    statustext->SetTextFont(83);
    statustext->SetFillColor(30);
    statustext->SetTextAlign(12);
    statustext->SetTextSize(textPixels);
    statustext->Draw();
    buttonpad->SetEditable(kFALSE);

    updateStatus();

    if(guisize==GR_BIGGUI){
      //pv info pad
      pvpad->cd();
      //if(nPV>maxlines)maxlines=nPV;
      
      pvlabel=new TPaveText(0.02,0.90,0.98,0.98,"NB");
      pvlabel->SetTextFont(103);
      pvlabel->SetFillColor(30);
      pvlabel->SetTextAlign(12);
      pvlabel->SetTextSize(textPixels);
      pvlabel->AddText("   PV");
      pvlabel->Draw();

      pvtext=new TPaveText(0.02,0.02,0.98,0.89,"NB");
      pvtext->SetFillColor(30);
      pvtext->SetTextFont(83);
      pvtext->SetTextAlign(12);
      pvtext->SetTextSize(textPixels);
      updatePvList();

      //graph info pad
      graphpad->cd();
      graphlabel=new TPaveText(0.02,0.90,0.90,0.98,"NB");
      graphlabel->SetTextFont(103);
      graphlabel->SetFillColor(30);
      graphlabel->SetTextAlign(12);
      graphlabel->SetTextSize(textPixels);
      graphlabel->AddText("   Graph                              yPV,xPV   Autoscale");
      graphlabel->Draw();

      graphtext=new TPaveText(0.02,0.02,0.90,0.89,"NB");
      graphtext->SetFillColor(30);
      graphtext->SetTextFont(83);
      graphtext->SetTextAlign(12);
      graphtext->SetTextSize(textPixels);
      //graphtext->AddText("");
      updateGraphList();

      //multi info pad
      multipad->cd();
      multilabel=new TPaveText(0.00,0.78,0.986,0.96,"NB");
      multilabel->SetTextFont(103);
      multilabel->SetFillColor(30);
      multilabel->SetTextAlign(12);
      multilabel->SetTextSize(textPixels);
      multilabel->AddText("  Multi name                            Graph indices                         Autoscale");
      multilabel->Draw();

      multitext=new TPaveText(0.00,0.04,0.986,0.76,"NB");
      multitext->SetFillColor(30);
      multitext->SetTextFont(83);
      multitext->SetTextAlign(12);
      multitext->SetTextSize(textPixels);
      updateMultiList();
    }
    

    //as soon as pads are made, set the TTextLabel context menu to have extra items for addPV, makeGraph and makeMultiGraph
    cl = statustext->IsA();
    cl->SetContextMenuTitle("GrimReeper");
    l  = cl->GetMenuList();
    l->RemoveAll();
    //mi = new TClassMenuItem(TClassMenuItem::kPopupUserFunction,cl,"Make new multigraph","GR->makeMultiGraph",0,"char *title, int, int, int, int, int, int, int, int, int, int");
    mi = new TClassMenuItem(TClassMenuItem::kPopupUserFunction,cl,"Make new multigraph","makeMultiGraph",GR,"char *title, int, int, int, int, int, int, int, int, int, int");
    l->AddFirst(mi);
    mi = new TClassMenuItem(TClassMenuItem::kPopupUserFunction,cl,"Make new graph","makeGraph",GR,"int, int, const char*, double, rangemax");
    l->AddFirst(mi);
    mi = new TClassMenuItem(TClassMenuItem::kPopupUserFunction,cl,"Add new PV","addPV",GR,"char *");
    l->AddFirst(mi);
    
    grimCanvas->cd();

    //
    
    isGUI = guisize;
    guiToggle = 0;
    
    //add a special popup menu to the toolbar with some info
    TRootCanvas *imp = (TRootCanvas*)grimCanvas->GetCanvasImp();
    TGMenuBar *bar = imp->GetMenuBar();
    TGPopupMenu *popup = bar->AddPopup("GrimReeper");
    popup->AddEntry("Use the Contex Menu (RH mouse) to access the extra Grim Reeper functions:", 1);
    popup->AddEntry("AddPV(), makeGraph(), makeMultiGraph() functions from the text area below", 1);
    popup->AddEntry("Autoscaling() from any of the graph Canvases", 1);
    popup->AddSeparator();
    popup->AddEntry("See manual at http://somewhere.soon.com", 1);
    bar->MapSubwindows();
    bar->Layout();
    
  }
}
void GrimReeper::updatePvList(){
  char string[100];
  //pv info pad
  pvpad->SetEditable(kTRUE);
  pvpad->cd();
  pvtext->Clear();
  for(int n=0;n<maxlines;n++){
    if(n<nPV)sprintf(string,"%2d %s",n,pvNames[n].Data());
    else sprintf(string,"");
    pvtext->AddText(string);
  }
  pvtext->Draw();
  pvpad->SetEditable(kFALSE);
}

void GrimReeper::updateGraphList(){
  char string[100];
  char fstring[100];
  //graph info pad
  graphpad->SetEditable(kTRUE);
  graphpad->cd();
  graphtext->Clear();
  for(int n=0;n<textLines;n++){
    if(n<nGraphs){
      sprintf(string,"%2d %-33s    %d,%d        %s",n,strstr(grCanvas[n]->GetName(),"_")+1,pvGraphY[n],pvGraphX[n],onOff[graphAuto[n]]);
    }
    else{
      sprintf(string,"");
    }
    graphtext->AddText(string);
  }
  graphtext->Draw();
  graphpad->SetEditable(kFALSE);
  if(nGraphs>maxlines){
    maxlines=nGraphs;
    updatePvList();    //to keep the spacing the same in both boxes.
  }
}

void GrimReeper::updateMultiList(){
  char string[100];
  char multistring[50]="";
  int l=0;
  
  //multi info pad
  multipad->SetEditable(kTRUE);
  multipad->cd();
  multitext->Clear();
  if(nMulti){
    for(int n=0;n<(int)(maxlines/4);n++){
      if(n<nMulti){
	sprintf(multistring,"");
	l=0;
	while(multiIndices[n][l]!=-1){
	  if(l>0)strcat(multistring,",");
	  sprintf(multistring,"%s%d",multistring,multiIndices[n][l]);
	  l++;
	}
	sprintf(string,"%d %-38s%-42s%s",n,strstr(multiCanvas[n]->GetTitle(),":")+2,multistring,onOff[multiAuto[n]]);
      }
      else sprintf(string,"");
      multitext->AddText(string);
    }
    multitext->Draw();
  }
  multipad->SetEditable(kFALSE);
  grimCanvas->cd();
  multipad->Update();
  grimCanvas->Update();
}

void GrimReeper::updateGUI(){
  
  updateStatus();
  updateStartButton();
  updatePauseButton();
  if(isGUI==GR_BIGGUI){
    if(nGraphs > textLines) textLines = nGraphs;
    if(nPV > textLines)     textLines = nPV;
    textPixels = (GUIH*0.4*0.87)/textLines;
  }
}

void GrimReeper::updateStartButton(){
  buttonpad->cd();
  if((scanStatus==GR_STARTED)||(scanStatus==GR_PAUSED)){
    startButton->SetMethod("GR->stopScanning()");
    startButton->SetTitle("Stop");
    startButton->SetFillColor(kRed);
    startButton->Draw();
  }
  else{
    startButton->SetMethod("GR->startScanning()");
    startButton->SetTitle("Start");
    startButton->SetFillColor(kGreen);
    startButton->Draw();
  }
  buttonpad->Modified();
  startButton->Modified();
  startButton->Update();
}

void GrimReeper::updatePauseButton(){
  buttonpad->cd();
  if(scanStatus==GR_STARTED){
    pauseButton->SetMethod("GR->pauseScanning()");
    pauseButton->SetTitle("Pause");
    pauseButton->SetFillColor(50);
    pauseButton->Draw();
  }
  else if (scanStatus==GR_PAUSED){
    pauseButton->SetMethod("GR->resumeScanning()");
    pauseButton->SetTitle("Resume");
    pauseButton->SetFillColor(5);
    pauseButton->Draw();
  }
  else{
    pauseButton->SetMethod("");
    pauseButton->SetTitle("pause");
    pauseButton->SetFillColor(19);
    pauseButton->Draw();
  }
  pauseButton->Modified();
  pauseButton->Update();
}

void GrimReeper::updateStatus(){
  buttonpad->cd();
  char string[100];
  statustext->Clear();
  sprintf(string,"%-6d", nPoints);
  statustext->AddText(string);
  sprintf(string,"%-6d", scanPeriod);
  statustext->AddText(string);
  if(scanPVIndex){
    sprintf(string,"%s (%5.2f-%5.2f,step %4.2f) %5.2f", pvNames[scanPVIndex].Data(),scanStart,scanStop,scanStep,scanVal );
  }
  else{
    sprintf(string,"------ ");
  }
  statustext->AddText(string);
  if(userRead==NULL){
    sprintf(string,"------ ");
  }
  else{
    sprintf(string,"%s",userRead);
  }
  statustext->AddText(string);
  
  if(userWrite==NULL){
    sprintf(string,"------ ");
  }
  else{
    sprintf(string,"%s",userWrite);
  }
  statustext->AddText(string);
  
  buttonpad->Modified();
  buttonpad->Update();
  grimCanvas->cd();
  buttonpad->Update();
}

void GrimReeper::setGuiToggle(){
  guiToggle=1;
}

void GrimReeper::toggleGUI(){
  if(!guiToggle) return;
  
  int newsize=0;
  if(isGUI==GR_BIGGUI) newsize=GR_SMALLGUI;
  else if (isGUI==GR_SMALLGUI) newsize=GR_BIGGUI;  
  makeControlGUI(newsize);
}

//Some functions to read waveforms into doubles.

//get a waveform into an array of doubles, 
void GrimReeper::waveToArray(const char *pv, double *array, int n, int add ){
  int cnt = 0;
  char command[200];
  TString response;
  char *data, *eptr;
  int elem;
  
  sprintf(command,"caget -t %s",pv);        //caget to read waveform:  "n a1 a2 .......an"
  response = gSystem->GetFromPipe(command);
  data=(char *)response.Data();
  
  elem=strtod(data, &eptr);                 //read the no of elements in the waveform
  data=eptr;
  
  do {                                      //loop over in this old fashioned way
    if(add){
      array[cnt++]+=strtod(data, &eptr);
    }
    else{
      array[cnt++]=strtod(data, &eptr);
    }
    data = eptr;
  } while ((*eptr)&&(cnt<n));
}

//get the waveform directly into a TH1D 
void GrimReeper::waveToTH1D(const char *pv,TH1D *h, int add){
  waveToArray(pv, h->GetArray()+1,h->GetNbinsX(),add);
}

//get the waveform directly into a row of a TH2D
void GrimReeper::waveToTH2DRow(const char *pv,TH2D *h, double y, int add){
  h->Fill(h->GetXaxis()->GetBinCenter(0),y); //seem to need something to force it to realise it's modified
  //fprintf(stderr,"%d\n",h->GetYaxis()->FindBin(y)*(h->GetNbinsX()+2));
  waveToArray(pv, h->GetArray()+h->GetYaxis()->FindBin(y)*(h->GetNbinsX()+2)+1,h->GetNbinsX(),add);
}

void GrimReeper::simIOC(int m){     //run up the test IOC
  char command[200];
  mode = m;
  killSimIOC();         //kill the running one you forgot about
  sprintf(command,"xterm -e \"cd %s;softIoc st.cmd_reeper\"&",REEPER);
  gSystem->Exec(command);
  iocTimer = new TTimer("GR->writeTestPVs()",1000*updatePeriod); //call this function
  iocTimer->Start();
  fprintf(stdout, "\nAttempted to start testIOC in a separate xterm (softIoc,caput etc must be in the PATH)\n\n");
  fprintf(stdout, "The following, correlated, test PVs are being updated every %ds:\n",updatePeriod);
  fprintf(stdout, "PV23004\ncolliX\nPMT1\nFcup\nXsetting\nYsetting\nYsetting\nBigScaler\n");
  fprintf(stdout, "(Names chosen to avoid conflict with real PVs)\n\n");
  fprintf(stdout, "To stop this process type killTestIOC() at the ROOT prompt, or exit in the xterm with the ioc\n\n");
  gSystem->Sleep(2000); //wait 2s before we try to access it
}

void GrimReeper::killSimIOC(){
  if(iocTimer)iocTimer->Stop();   //stop the timer and kill the ioc
  gSystem->Exec("kill -9 `ps x | grep soft | grep reeper | grep -v xterm | awk '{print $1;exit}'`");
  fprintf(stdout, "Killed testIOC \n\n");
}


void GrimReeper::writeTestPVs(){
  static double PV23004,colliX,PMT1,Fcup,Xsetting,Ysetting,BigScaler;
  double x;
  char command[1028];
  double amp;
   
  if(!klrand) klrand = new TRandom();

  if(mode==1){   //called this way if scanning
    sscanf((gSystem->GetFromPipe("caget -t colliX")).Data(),"%lg",&colliX);
  }
  else{
    colliX=klrand->Uniform(-4,4);
    //colliX=klrand->Gaus(0.6,1.0);
    sprintf(command,"caput -t colliX %g > /dev/null", colliX);
    gSystem->Exec(command);
  }
  
  if(mode==2){ //xy scan demo mode
    //read in the x and y
    sscanf((gSystem->GetFromPipe("caget -t Xsetting")).Data(),"%lg",&Xsetting);
    sscanf((gSystem->GetFromPipe("caget -t Ysetting")).Data(),"%lg",&Ysetting);
  }
  else{
    Xsetting=4.0+klrand->Uniform(0,4);
    sprintf(command,"caput -t Xsetting %g > /dev/null", Xsetting);
    gSystem->Exec(command);
    Ysetting=3.0+klrand->Uniform(0,3);
    sprintf(command,"caput -t Ysetting %g > /dev/null", Ysetting);
    gSystem->Exec(command);
  }

  
  //full up the sum scalers according to some alorgithm
  amp=TMath::Gaus(Xsetting,4,1.0)*TMath::Gaus(Ysetting,3,1.0);
  sprintf(command,"caput -a -t AMO_SCALERS 100");
  for(int n=0;n<100;n++){
    AMO_SCALERS[n]=amp*klrand->Gaus(1,0.01)/(n+1.0);
    sprintf(command,"%s %lf",command,AMO_SCALERS[n]);
  }
  sprintf(command,"%s > /dev/null", command);
  gSystem->Exec(command);

  sprintf(command,"caput -t BigScaler %g > /dev/null",amp*klrand->Gaus(1,0.01));
  gSystem->Exec(command);
  
  
  PV23004 = klrand->Uniform(100.0,200.0);
  sprintf(command,"caput -t PV23004 %g > /dev/null", PV23004);
  gSystem->Exec(command);
  
  PMT1 = 20000.0*TMath::Gaus(colliX,0.6,1.0);
  //PMT1 *= klrand->Gaus(1,0.1);
  sprintf(command,"caput -t PMT1 %g > /dev/null", PMT1);
  gSystem->Exec(command);
  
  Fcup = 1000.0*TMath::Gaus(colliX,0.6,2.0);
  Fcup *= klrand->Gaus(1,0.01);
  sprintf(command,"caput -t Fcup %g > /dev/null", Fcup);
  gSystem->Exec(command);
  
  testTime++;
}


void GrimReeper::writePV(const char *pv_name, double pv_value){
  char   command[100];
  sprintf(command,"caput -t %s %g > /dev/null", pv_name, pv_value);
  gSystem->Exec(command);
}
