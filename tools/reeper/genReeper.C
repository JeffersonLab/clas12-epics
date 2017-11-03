//This takes a list of PVs and some arguments and makes graphs.
//Part of the GRIM REEPER package
//Ken Livingston (kliv@jlab.org) March 2017. 

//If you're reading this, you should probably be using the command shell one liner: genReeper.sh
//try ./genReeper.sh -h
//
//Args for genReeper() are:
//npv:      no of PVs
//pvstring: string with pvnames separated by whitespace
//period:   time between succesive PV read/writes
//sim:      0/1 Set to 1 to use simulated data.
//gui:      0/1 Set to 0 run with no gui and no prompt/confirm for scanning with caput.
//scan:     set to scan on the 1st PV in pvlist. should be comma separated string - "start,stop,step"

void genReeper(int npv, const char* pvstring, int period=2, int sim=0, int gui = 1, const char* scan="", const char* dir=""){

  char star[4]="%*s";
  char format[100]="";                    //format string for scanning PV names from pvstring
  char nofit[]="";
  char pvname[100];                        //temp string for pvnames
  char *fit[50];
  int fitpv[10];
  double min[10],max[10];
  int timemg[10]  = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
  int pvmg[10]    = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
  int ntmg=0;
  int npvmg=0;
  char extrapv[100];
  int extraPV=0;
  char inBracket[100];
  char *b1,*b2;
  int mode=0;
  char hashtag[4];
  char hashpv[4];
  
  GrimReeper* gr = new GrimReeper();

  gr->setPeriod(period);                   //set the scan period                   
  
  if(strlen(scan)>0){                      //scan!="" indicates that 1st PV is to be used as x-axis for additional graphs of all PVs
    extraPV=1;
  }
  if(strlen(scan)>1){                      //scan>"1" indicates that an scan is in progress with caputs to PV1
    mode=1;
  }

  if(sim){                                 //If running in test mode, start the simulation and softIOC 
    gr->simIOC(mode);                      //start the simulation
  }
  
  if(strlen(dir)>0){
      gr->setOutputDir(dir);
    }
    
  for(int n=1;n<=npv;n++){                 //for all PVs
    fit[n]=nofit;                          //default, no fit or range
    fitpv[n]=-1;                           //default, no fit or range
    min[n]=0.0;
    max[n]=0.0;
    
    strcpy(format,"");                                       //make the format string to scan the PV (eg %*s%*s%s)
    for(int s=1;s<n;s++)strcat(format,"%*s");
    strcat(format,"%s");
    sscanf(pvstring,format,pvname);                          //Scan in the PV from the space separated list, pvstring="pv1 pv2 ..."
                                                             //see if it has a fit in the brackets
                                                             //eg myepicspv::pol3,2.0,6.3         
    if((b1=strstr(pvname,"::"))){                            //find the position of the ::
      fit[n]=new char[strlen(b1+1)];                         //make a string
      strcpy(fit[n],b1+2);                                   //copy to it
      strcpy(b1,"");                                         //terminate pvname at the :
      if((b2=strstr(fit[n],","))){                           //look for a ","
	if((sscanf(b2+1,"%lg,%lg",&min[n],&max[n]))!=2){     //if we don't scan 2 doubles
	  min[n]=0.0;                                        //set range to zero
	  max[n]=0.0;
	}
	sprintf(b2,"");                                      //terminate at the 1st ","
      }
      fitpv[n]=0;                                            //apply the fit to PV0 (= Time)
    }
    else if((b1=strstr(pvname,"##"))){                       //find the position of the ##
      fit[n]=new char[strlen(b1+1)];                         //make a string
      strcpy(fit[n],b1+2);                                   //copy to it
      strcpy(b1,"");                                         //terminate pvname at the :
      if((b2=strstr(fit[n],","))){                           //look for a ","
	if(sscanf(b2+1,"%lg,%lg",&min[n],&max[n])!=2){       //if we don't scan 2 doubles
	  min[n]=0.0;                                        //set range to zero
	  max[n]=0.0;
	}
	sprintf(b2,"");                                      //terminate at the 1st ","
      }
      if(extraPV)fitpv[n]=1;                                 //apply the fit to PV1 it extraPV plots are being done
      else fitpv[n]=0;
    }
        
    
    gr->addPV(pvname);                     //add the PV to the list
    
    if((n==1)&&(extraPV)){                 //save the 1st PV in the list if  needed for extra graphs
      sprintf(extrapv,"%s",pvname);
    }    
  }
  
  
  if(strlen(scan)>2){                      //if scanning, get the scan parameters and set scanPV as 1st in list.
    sscanf(scan,"%lg,%lg,%lg",&gr->scanStart,&gr->scanStop,&gr->scanStep);
    gr->setScan(1,gr->scanStart,gr->scanStop,gr->scanStep);                                                  
  }
  gr->printPVs();                              //print all the pv details
  
  
  for(int n=1;n<gr->nPV;n++){                  //make a set of graphs of all PVs vs Time(index=0).
    if(fitpv[n]==0){
      gr->makeGraph(n,Time,fit[n],min[n],max[n]);
    }
    else{
      gr->makeGraph(n,Time); 
    }
    timemg[ntmg++]=gr->nGraphs-1;               //add each to list for TIME multigraph
  }
  
  if(extraPV){                              //if set, also make all graphs vs 1st PV
    for(int n=2;n<gr->nPV;n++){
      if(fitpv[n]==1){
	gr->makeGraph(n,1,fit[n],min[n],max[n]);
      }
      else{
	gr->makeGraph(n,1);
      }
      pvmg[npvmg++]=gr->nGraphs-1;             //add to list for extraPV multigraph
    }
    sprintf(pvname,"All PVs vs %s", extrapv);    
  }
  gr->printGraphs();                       //print all the pv details

  gr->setVerbosity(0);                     //stop it clogging up the console with all the PV readback numbers

  if(gui){                                 //make gui if required
    gr->makeControlGUI(gui);
  }
  else{                                    //otherwise quiet
    gr->confirmScan = 0;
  }
  
  if(gr->nPV>2){
    gr->makeMultiGraph("All PVs vs Time",timemg);  //make multigraph
    gr->multiCanvas[0]->SetFillColor(406);         //Give them coloured background for mark them different from single graphs.
    if(extraPV&&(gr->nPV>3)){                      //if there's an extrPV set, do the same the the extraPV multigraph
      gr->makeMultiGraph(pvname,pvmg);
      gr->multiCanvas[1]->SetFillColor(422);
    }
  }

  gr->startScanning();                             //start the scan

}
