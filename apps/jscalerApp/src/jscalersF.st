program seqJscalersF

option -c;
option -r;

string suffixTrg = "cTrg";
string suffixTdc = "cTdc";
string suffixFadc = "c";

// update period (seconds): 
int delay=1;

#define NECAL 216
int nchanE=36;
int nviewE=3;
int nlayerE=2;
string viewsE[3]={"U","V","W"};
string layersE[2]={"I","O"};

#define NPCAL 192
int nviewP=3;
string viewsP[3]={"U","V","W"};
int nchansP[3]={68,62,62};

#define NFTOF 180
int npanelF=3;
int nsideF=2;
int nchansF[3]={23,62,5};
string panelsF[3]={"1A","1B","2"};
string sidesF[2]={"L","R"};

#define NLTCC 36
int nchansL=18;
int nsideL=2;
string sidesL[2]={"L","R"};

int wfLengthE=0;
int wfLengthP=0;
int wfLengthF=0;
int wfLengthL=0;

string msg; assign msg to "B_SYS_SEC{S}:wfmsg";

float wfoEtrg[NECAL]; assign wfoEtrg to "B_DET_ECAL_TRG_SEC{S}:wf";
float wfiEtrg[NECAL]; assign wfiEtrg to {};
float wfoPtrg[NPCAL]; assign wfoPtrg to "B_DET_PCAL_TRG_SEC{S}:wf";
float wfiPtrg[NPCAL]; assign wfiPtrg to {};
float wfoFtrg[NFTOF]; assign wfoFtrg to "B_DET_FTOF_TRG_SEC{S}:wf";
float wfiFtrg[NFTOF]; assign wfiFtrg to {};
float wfoLtrg[NLTCC]; assign wfoLtrg to "B_DET_LTCC_TRG_SEC{S}:wf";
float wfiLtrg[NLTCC]; assign wfiLtrg to {};

float wfoEtdc[NECAL]; assign wfoEtdc to "B_DET_ECAL_TDC_SEC{S}:wf";
float wfiEtdc[NECAL]; assign wfiEtdc to {};
float wfoPtdc[NPCAL]; assign wfoPtdc to "B_DET_PCAL_TDC_SEC{S}:wf";
float wfiPtdc[NPCAL]; assign wfiPtdc to {};
float wfoFtdc[NFTOF]; assign wfoFtdc to "B_DET_FTOF_TDC_SEC{S}:wf";
float wfiFtdc[NFTOF]; assign wfiFtdc to {};
float wfoLtdc[NLTCC]; assign wfoLtdc to "B_DET_LTCC_TDC_SEC{S}:wf";
float wfiLtdc[NLTCC]; assign wfiLtdc to {};

float wfoEf[NECAL]; assign wfoEf to "B_DET_ECAL_FADC_SEC{S}:wf";
float wfiEf[NECAL]; assign wfiEf to {};
float wfoPf[NPCAL]; assign wfoPf to "B_DET_PCAL_FADC_SEC{S}:wf";
float wfiPf[NPCAL]; assign wfiPf to {};
float wfoFf[NFTOF]; assign wfoFf to "B_DET_FTOF_FADC_SEC{S}:wf";
float wfiFf[NFTOF]; assign wfiFf to {};
float wfoLf[NLTCC]; assign wfoLf to "B_DET_LTCC_FADC_SEC{S}:wf";
float wfiLf[NLTCC]; assign wfiLf to {};

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
            sprintf(stmp,"B_DET_ECAL_FADC_SEC{S}_%s%s_E%.2d:%s",viewsE[iview],layersE[ilayer],ichan,suffixFadc);
            pvAssignSubst(wfiEf[wfLengthE],stmp);
            sprintf(stmp,"B_DET_ECAL_DISC_SEC{S}_%s%s_E%.2d:%s",viewsE[iview],layersE[ilayer],ichan,suffixTrg);
            pvAssignSubst(wfiEtrg[wfLengthE],stmp);
            sprintf(stmp,"B_DET_ECAL_DISC_SEC{S}_%s%s_E%.2d:%s",viewsE[iview],layersE[ilayer],ichan,suffixTdc);
            pvAssignSubst(wfiEtdc[wfLengthE],stmp);
            wfLengthE++;
          }
        }
      }
      for (iview=0; iview<nviewP; iview++)
      {
        for (ichan=1; ichan<=nchansP[iview]; ichan++)
        {
          sprintf(stmp,"B_DET_PCAL_FADC_SEC{S}_%s_E%.2d:%s",viewsP[iview],ichan,suffixFadc);
          pvAssignSubst(wfiPf[wfLengthP],stmp);
          sprintf(stmp,"B_DET_PCAL_DISC_SEC{S}_%s_E%.2d:%s",viewsP[iview],ichan,suffixTrg);
          pvAssignSubst(wfiPtrg[wfLengthP],stmp);
          sprintf(stmp,"B_DET_PCAL_DISC_SEC{S}_%s_E%.2d:%s",viewsP[iview],ichan,suffixTdc);
          pvAssignSubst(wfiPtdc[wfLengthP],stmp);
          wfLengthP++;
        }
      }
      for (ipanel=0; ipanel<npanelF; ipanel++)
      {
        for (ichan=1; ichan<=nchansF[ipanel]; ichan++)
        {
          for (iside=0; iside<nsideF; iside++)
          {
            sprintf(stmp,"B_DET_FTOF_FADC_SEC{S}_PANEL%s_%s_E%.2d:%s",panelsF[ipanel],sidesF[iside],ichan,suffixFadc);
            pvAssignSubst(wfiFf[wfLengthF],stmp);
            sprintf(stmp,"B_DET_FTOF_DISC_SEC{S}_PANEL%s_%s_E%.2d:%s",panelsF[ipanel],sidesF[iside],ichan,suffixTrg);
            pvAssignSubst(wfiFtrg[wfLengthF],stmp);
            sprintf(stmp,"B_DET_FTOF_DISC_SEC{S}_PANEL%s_%s_E%.2d:%s",panelsF[ipanel],sidesF[iside],ichan,suffixTdc);
            pvAssignSubst(wfiFtdc[wfLengthF],stmp);
            wfLengthF++;
          }
        }
      }
      for (ichan=1; ichan<=nchansL; ichan++)
      {
        for (iside=0; iside<nsideL; iside++)
        {
          sprintf(stmp,"B_DET_LTCC_FADC_SEC{S}_%s_E%.2d:%s",sidesL[iside],ichan,suffixFadc);
          pvAssignSubst(wfiLf[wfLengthL],stmp);
          sprintf(stmp,"B_DET_LTCC_DISC_SEC{S}_%s_E%.2d:%s",sidesL[iside],ichan,suffixTrg);
          pvAssignSubst(wfiLtrg[wfLengthL],stmp);
          sprintf(stmp,"B_DET_LTCC_DISC_SEC{S}_%s_E%.2d:%s",sidesL[iside],ichan,suffixTdc);
          pvAssignSubst(wfiLtdc[wfLengthL],stmp);
          wfLengthL++;
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
        pvGet(wfiEtdc[ii]); wfoEtdc[ii]=wfiEtdc[ii];
        pvGet(wfiEtrg[ii]); wfoEtrg[ii]=wfiEtrg[ii];
        pvGet(wfiEf[ii]);   wfoEf[ii]=wfiEf[ii];
      }
      for (ii=0; ii<wfLengthP; ii++)
      {
        pvGet(wfiPtdc[ii]); wfoPtdc[ii]=wfiPtdc[ii];
        pvGet(wfiPtrg[ii]); wfoPtrg[ii]=wfiPtrg[ii];
        pvGet(wfiPf[ii]);   wfoPf[ii]=wfiPf[ii];
      }
      for (ii=0; ii<wfLengthF; ii++)
      {
        pvGet(wfiFtdc[ii]); wfoFtdc[ii]=wfiFtdc[ii];
        pvGet(wfiFtrg[ii]); wfoFtrg[ii]=wfiFtrg[ii];
        pvGet(wfiFf[ii]);   wfoFf[ii]=wfiFf[ii];
      }
      for (ii=0; ii<wfLengthL; ii++)
      {
        pvGet(wfiLtdc[ii]); wfoLtdc[ii]=wfiLtdc[ii];
        pvGet(wfiLtrg[ii]); wfoLtrg[ii]=wfiLtrg[ii];
        pvGet(wfiLf[ii]);   wfoLf[ii]=wfiLf[ii];
      }
      pvPut(wfoEtdc);
      pvPut(wfoPtdc);
      pvPut(wfoFtdc);
      pvPut(wfoLtdc);
      pvPut(wfoEtrg);
      pvPut(wfoPtrg);
      pvPut(wfoFtrg);
      pvPut(wfoLtrg);
      pvPut(wfoEf);
      pvPut(wfoPf);
      pvPut(wfoFf);
      pvPut(wfoLf);
      epicsThreadSleep(delay);
    } state run
  }

}


