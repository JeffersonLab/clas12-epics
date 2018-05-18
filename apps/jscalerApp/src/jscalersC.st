program seqJscalersC

// N. Baltzell

option -c;
option -r;

string suffix = "c1";

// update period (seconds): 
int delay=1;

int nchanC=48;
int nsideC=2;
string sidesC[2]={"U","D"};

int nchanH=4;
int nsideH=2;
string sidesH[2]={"L","R"};

int wfLengthC=0;
int wfLengthH=0;

string msg; assign msg to "B_SYS_FADC_CENTRAL:wfmsg";

float wfoC[96]; assign wfoC to "B_DET_CTOF_FADC:wf";
float wfiC[96]; assign wfiC to {};

float wfoH[48]; assign wfoH to "B_DET_HTCC_FADC:wf";
float wfiH[48]; assign wfiH to {};

int isec;
int iside;
int ichan;

int ii;
string stmp;

ss seqJscalersC {

  state start
  {   
    when ()
    { 
      printf("** start state **************************\n");
      sprintf(msg,"INIT - Assigning PVs");
      pvPut(msg);
      wfLengthC=0;
      wfLengthH=0;
      for (iside=0; iside<nsideC; iside++)
      {
        for (ichan=1; ichan<=nchanC; ichan++)
        {
            sprintf(stmp,"B_DET_CTOF_FADC_%s%.2d:%s",sidesC[iside],ichan,suffix);
            pvAssignSubst(wfiC[wfLengthC++],stmp);
        }
      }
      for (isec=1; isec<=6; isec++)
      {
        for (ichan=1; ichan<=nchanH; ichan++)
        {
          for (iside=0; iside<nsideH; iside++)
          {
            sprintf(stmp,"B_DET_HTCC_FADC_SEC%d_%s%d:%s",isec,sidesH[iside],ichan,suffix);
            pvAssignSubst(wfiH[wfLengthH++],stmp);
          }
        }
      }
    } state init
  }

  state init
  {
    entry
    {
      printf("** init state ****************************\n");
    }
    when (pvConnectCount() < pvChannelCount())
    {
      printf("Waiting for PVs (%d/%d)\n",pvConnectCount(),pvChannelCount());
      sprintf(msg,"ERROR - Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
      pvPut(msg);
      pvPut(msg);
      epicsThreadSleep(2);
    } state init
    when () {} state run
  }

  state run
  {
    entry
    {
      printf("** run state ****************************\n");
      sprintf(msg,"OK - Running");
      pvPut(msg);
    }

    when (pvConnectCount() < pvChannelCount()) {} state init

    when ()
    {
      for (ii=0; ii<wfLengthC; ii++)
      {
        pvGet(wfiC[ii]);
        wfoC[ii]=wfiC[ii];
      }
      for (ii=0; ii<wfLengthH; ii++)
      {
        pvGet(wfiH[ii]);
        wfoH[ii]=wfiH[ii];
      }
      pvPut(wfoC);
      pvPut(wfoH);
      epicsThreadSleep(delay);
    } state run
  }

}


