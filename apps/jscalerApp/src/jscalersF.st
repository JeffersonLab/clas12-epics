program seqJscalersF

option -c;
option -r;

string suffix = "c3";

// update period (seconds): 
int delay=1;

int nchanE=36;
int nviewE=3;
int nlayerE=2;
string viewsE[3]={"U","V","W"};
string layersE[2]={"I","O"};

int nviewP=3;
string viewsP[3]={"U","V","W"};
int nchansP[3]={68,62,62};

int npanelF=3;
int nsideF=2;
int nchansF[3]={23,62,5};
string panelsF[3]={"1A","1B","2"};
string sidesF[2]={"L","R"};

int nchansL=18;
int nsideL=2;
string sidesL[2]={"L","R"};

int wfLengthE=0;
int wfLengthP=0;
int wfLengthF=0;
int wfLengthL=0;

string msg; assign msg to "B_SYS_SEC{S}:wfmsg";

float wfoE[216]; assign wfoE to "B_DET_ECAL_DISC_SEC{S}:wf";
float wfiE[216]; assign wfiE to {};
float wfoP[192]; assign wfoP to "B_DET_PCAL_DISC_SEC{S}:wf";
float wfiP[192]; assign wfiP to {};
float wfoF[180]; assign wfoF to "B_DET_FTOF_DISC_SEC{S}:wf";
float wfiF[180]; assign wfiF to {};
float wfoL[36]; assign wfoL to "B_DET_LTCC_DISC_SEC{S}:wf";
float wfiL[36]; assign wfiL to {};

//float wfoE[216]; assign wfoE to "B_DET_ECAL_FADC_SEC{S}:wf";
//float wfiE[216]; assign wfiE to {};
//float wfoP[192]; assign wfoP to "B_DET_PCAL_FADC_SEC{S}:wf";
//float wfiP[192]; assign wfiP to {};
//float wfoF[180]; assign wfoF to "B_DET_FTOF_FADC_SEC{S}:wf";
//float wfiF[180]; assign wfiF to {};
//float wfoL[36]; assign wfoL to "B_DET_LTCC_FADC_SEC{S}:wf";
//float wfiL[36]; assign wfiL to {};

int ipanel;
int iside;
int ichan;
int iview;
int ilayer;

int ii;
string stmp;

ss seqJscalersF {

  state start
  {   
    when ()
    { 
      printf("** start state **************************\n");
      sprintf(msg,"INIT - Assigning PVs");
      pvPut(msg);
      wfLengthE=0;
      wfLengthF=0;
      wfLengthP=0;
      wfLengthL=0;
      for (iview=0; iview<nviewE; iview++)
      {
        for (ilayer=0; ilayer<nlayerE; ilayer++)
        {
          for (ichan=1; ichan<=nchanE; ichan++)
          {
            sprintf(stmp,"B_DET_ECAL_DISC_SEC{S}_%s%s_E%.2d:%s",viewsE[iview],layersE[ilayer],ichan,suffix);
            pvAssignSubst(wfiE[wfLengthE++],stmp);
          }
        }
      }
      for (iview=0; iview<nviewP; iview++)
      {
        for (ichan=1; ichan<=nchansP[iview]; ichan++)
        {
          sprintf(stmp,"B_DET_PCAL_DISC_SEC{S}_%s_E%.2d:%s",viewsP[iview],ichan,suffix);
          pvAssignSubst(wfiP[wfLengthP++],stmp);
        }
      }
      for (ipanel=0; ipanel<npanelF; ipanel++)
      {
        for (ichan=1; ichan<=nchansF[ipanel]; ichan++)
        {
          for (iside=0; iside<nsideF; iside++)
          {
            sprintf(stmp,"B_DET_FTOF_DISC_SEC{S}_PANEL%s_%s_E%.2d:%s",panelsF[ipanel],sidesF[iside],ichan,suffix);
            pvAssignSubst(wfiF[wfLengthF++],stmp);
          }
        }
      }
      for (ichan=1; ichan<=nchansL; ichan++)
      {
        for (iside=0; iside<nsideL; iside++)
        {
          sprintf(stmp,"B_DET_LTCC_DISC_SEC{S}_%s_E%.2d:%s",sidesL[iside],ichan,suffix);
          pvAssignSubst(wfiL[wfLengthL++],stmp);
        }
      }

      printf("%d %d %d %d\n",wfLengthE,wfLengthP,wfLengthF,wfLengthL);

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
      for (ii=0; ii<wfLengthE; ii++)
      {
        pvGet(wfiE[ii]);
        wfoE[ii]=wfiE[ii];
      }
      for (ii=0; ii<wfLengthP; ii++)
      {
        pvGet(wfiP[ii]);
        wfoP[ii]=wfiP[ii];
      }
      for (ii=0; ii<wfLengthF; ii++)
      {
        pvGet(wfiF[ii]);
        wfoF[ii]=wfiF[ii];
      }
      for (ii=0; ii<wfLengthL; ii++)
      {
        pvGet(wfiL[ii]);
        wfoL[ii]=wfiL[ii];
      }
      pvPut(wfoE);
      pvPut(wfoP);
      pvPut(wfoF);
      pvPut(wfoL);
      epicsThreadSleep(delay);
    } state run
  }

}


