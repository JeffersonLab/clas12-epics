int updatePeriod  = 1;
TTimer  *iocTimer;               //to push values to the simIOC
TRandom *klrand;
int testTime    = 0;             //time counter for simIOC
int mode = 0;
double AMO_SCALERS[100];

void killSimIOC();
void writeTestPVs();

void simIOC(int m=0){     //run up the test IOC
  mode = m;
  killSimIOC();           //kill the running one you forgot about
  gSystem->Exec("xterm -e softIoc st.cmd_reeper&");
  iocTimer = new TTimer("writeTestPVs()",1000*updatePeriod); //call this function
  iocTimer->Start();
  fprintf(stdout, "\nAttempted to start testIOC in a separate xterm (softIoc,caput etc must be in the PATH)\n\n");
  fprintf(stdout, "The following, correlated, test PVs are being updated every %ds:\n",updatePeriod);
  fprintf(stdout, "PV23004\ncolliX\nPMT1\nFcup\nXsetting\nYsetting\nYsetting\nBigScaler\n");
  fprintf(stdout, "(Names chosen to avoid conflict with real PVs)\n\n");
  fprintf(stdout, "To stop this process type killTestIOC() at the ROOT prompt, or exit in the xterm with the ioc\n\n");
  gSystem->Sleep(1000); //wait 1s before we try to access it
}

void killSimIOC(){
  if(iocTimer)iocTimer->Stop();   //stop the timer and kill the ioc
  gSystem->Exec("kill -9 `ps x | grep soft | grep reeper | grep -v xterm | awk '{print $1;exit}'`");
  fprintf(stdout, "Killed testIOC \n\n");
}


void writeTestPVs(){
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
    //read in the x and x
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

