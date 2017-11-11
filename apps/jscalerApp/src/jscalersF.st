program seqJscalersF

// N. Baltzell

option -c;
option -r;

string suffixTrg = "cTrg";
string suffixTdc = "cTdc";
string suffixFadc = "c";
string suffixTrgT = "tTrg";
string suffixTdcT = "tTdc";
string suffixFadcT = "t";

// update period (seconds): 
int delay=1;

// threshold update period (number of scaler updates):
int delayT=30;

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

/*
float wfoEtrgT[NECAL]; assign wfoEtrgT to "B_DET_ECAL_TRG_SEC{S}:t:wf";
float wfiEtrgT[NECAL]; assign wfiEtrgT to {};
float wfoPtrgT[NPCAL]; assign wfoPtrgT to "B_DET_PCAL_TRG_SEC{S}:t:wf";
float wfiPtrgT[NPCAL]; assign wfiPtrgT to {};
float wfoFtrgT[NFTOF]; assign wfoFtrgT to "B_DET_FTOF_TRG_SEC{S}:t:wf";
float wfiFtrgT[NFTOF]; assign wfiFtrgT to {};
float wfoLtrgT[NLTCC]; assign wfoLtrgT to "B_DET_LTCC_TRG_SEC{S}:t:wf";
float wfiLtrgT[NLTCC]; assign wfiLtrgT to {};

float wfoEtdcT[NECAL]; assign wfoEtdcT to "B_DET_ECAL_TDC_SEC{S}:t:wf";
float wfiEtdcT[NECAL]; assign wfiEtdcT to {};
float wfoPtdcT[NPCAL]; assign wfoPtdcT to "B_DET_PCAL_TDC_SEC{S}:t:wf";
float wfiPtdcT[NPCAL]; assign wfiPtdcT to {};
float wfoFtdcT[NFTOF]; assign wfoFtdcT to "B_DET_FTOF_TDC_SEC{S}:t:wf";
float wfiFtdcT[NFTOF]; assign wfiFtdcT to {};
float wfoLtdcT[NLTCC]; assign wfoLtdcT to "B_DET_LTCC_TDC_SEC{S}:t:wf";
float wfiLtdcT[NLTCC]; assign wfiLtdcT to {};

float wfoEfT[NECAL]; assign wfoEfT to "B_DET_ECAL_FADC_SEC{S}:t:wf";
float wfiEfT[NECAL]; assign wfiEfT to {};
float wfoPfT[NPCAL]; assign wfoPfT to "B_DET_PCAL_FADC_SEC{S}:t:wf";
float wfiPfT[NPCAL]; assign wfiPfT to {};
float wfoFfT[NFTOF]; assign wfoFfT to "B_DET_FTOF_FADC_SEC{S}:t:wf";
float wfiFfT[NFTOF]; assign wfiFfT to {};
float wfoLfT[NLTCC]; assign wfoLfT to "B_DET_LTCC_FADC_SEC{S}:t:wf";
float wfiLfT[NLTCC]; assign wfiLfT to {};
*/

int ipanel;
int iside;
int ichan;
int iview;
int ilayer;

int ii;
int nScalerUpdates;
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
          /*
            sprintf(stmp,"B_DET_ECAL_FADC_SEC{S}_%s%s_E%.2d:%s",viewsE[iview],layersE[ilayer],ichan,suffixFadcT);
            pvAssignSubst(wfiEfT[wfLengthE],stmp);
            sprintf(stmp,"B_DET_ECAL_DISC_SEC{S}_%s%s_E%.2d:%s",viewsE[iview],layersE[ilayer],ichan,suffixTrgT);
            pvAssignSubst(wfiEtrgT[wfLengthE],stmp);
            sprintf(stmp,"B_DET_ECAL_DISC_SEC{S}_%s%s_E%.2d:%s",viewsE[iview],layersE[ilayer],ichan,suffixTdcT);
            pvAssignSubst(wfiEtdcT[wfLengthE],stmp);
          */
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
          /*
          sprintf(stmp,"B_DET_PCAL_FADC_SEC{S}_%s_E%.2d:%s",viewsP[iview],ichan,suffixFadcT);
          pvAssignSubst(wfiPfT[wfLengthP],stmp);
          sprintf(stmp,"B_DET_PCAL_DISC_SEC{S}_%s_E%.2d:%s",viewsP[iview],ichan,suffixTrgT);
          pvAssignSubst(wfiPtrgT[wfLengthP],stmp);
          sprintf(stmp,"B_DET_PCAL_DISC_SEC{S}_%s_E%.2d:%s",viewsP[iview],ichan,suffixTdcT);
          pvAssignSubst(wfiPtdcT[wfLengthP],stmp);
          */
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
          /*
            sprintf(stmp,"B_DET_FTOF_FADC_SEC{S}_PANEL%s_%s_E%.2d:%s",panelsF[ipanel],sidesF[iside],ichan,suffixFadcT);
            pvAssignSubst(wfiFfT[wfLengthF],stmp);
            sprintf(stmp,"B_DET_FTOF_DISC_SEC{S}_PANEL%s_%s_E%.2d:%s",panelsF[ipanel],sidesF[iside],ichan,suffixTrgT);
            pvAssignSubst(wfiFtrgT[wfLengthF],stmp);
            sprintf(stmp,"B_DET_FTOF_DISC_SEC{S}_PANEL%s_%s_E%.2d:%s",panelsF[ipanel],sidesF[iside],ichan,suffixTdcT);
            pvAssignSubst(wfiFtdcT[wfLengthF],stmp);
          */
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
          /*
          sprintf(stmp,"B_DET_LTCC_FADC_SEC{S}_%s_E%.2d:%s",sidesL[iside],ichan,suffixFadcT);
          pvAssignSubst(wfiLfT[wfLengthL],stmp);
          sprintf(stmp,"B_DET_LTCC_DISC_SEC{S}_%s_E%.2d:%s",sidesL[iside],ichan,suffixTrgT);
          pvAssignSubst(wfiLtrgT[wfLengthL],stmp);
          sprintf(stmp,"B_DET_LTCC_DISC_SEC{S}_%s_E%.2d:%s",sidesL[iside],ichan,suffixTdcT);
          pvAssignSubst(wfiLtdcT[wfLengthL],stmp);
          */
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
      nScalerUpdates=0;
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

      /*
      if (nScalerUpdates == 0) {
          for (ii=0; ii<wfLengthE; ii++)
          {
              pvGet(wfiEtdcT[ii]); wfoEtdcT[ii]=wfiEtdcT[ii];
              pvGet(wfiEtrgT[ii]); wfoEtrgT[ii]=wfiEtrgT[ii];
              pvGet(wfiEfT[ii]);   wfoEfT[ii]=wfiEfT[ii];
          }
          for (ii=0; ii<wfLengthP; ii++)
          {
              pvGet(wfiPtdcT[ii]); wfoPtdcT[ii]=wfiPtdcT[ii];
              pvGet(wfiPtrgT[ii]); wfoPtrgT[ii]=wfiPtrgT[ii];
              pvGet(wfiPfT[ii]);   wfoPfT[ii]=wfiPfT[ii];
          }
          for (ii=0; ii<wfLengthF; ii++)
          {
              pvGet(wfiFtdcT[ii]); wfoFtdcT[ii]=wfiFtdcT[ii];
              pvGet(wfiFtrgT[ii]); wfoFtrgT[ii]=wfiFtrgT[ii];
              pvGet(wfiFfT[ii]);   wfoFfT[ii]=wfiFfT[ii];
          }
          for (ii=0; ii<wfLengthL; ii++)
          {
              pvGet(wfiLtdcT[ii]); wfoLtdcT[ii]=wfiLtdcT[ii];
              pvGet(wfiLtrgT[ii]); wfoLtrgT[ii]=wfiLtrgT[ii];
              pvGet(wfiLfT[ii]);   wfoLfT[ii]=wfiLfT[ii];
          }
          pvPut(wfoEtdcT);
          pvPut(wfoPtdcT);
          pvPut(wfoFtdcT);
          pvPut(wfoLtdcT);
          pvPut(wfoEtrgT);
          pvPut(wfoPtrgT);
          pvPut(wfoFtrgT);
          pvPut(wfoLtrgT);
          pvPut(wfoEfT);
          pvPut(wfoPfT);
          pvPut(wfoFfT);
          pvPut(wfoLfT);
      }
      */

      nScalerUpdates++;
      if (nScalerUpdates>=delayT) nScalerUpdates=0;

      epicsThreadSleep(delay);

    } state run
  }

}


