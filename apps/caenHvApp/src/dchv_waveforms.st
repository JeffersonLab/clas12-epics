program seqDCHVwaveforms

// N. Baltzell

option -c;

// must be reentrant:
option +r;

string prefix = "B_DET_DC_HV";

int period_seconds = 5;

int nsfwires = 8;
int ngwires = 2;
string sfwires[8] = {"01-08","09-16","17-24","25-32","33-48","49-64","65-80","81-112"};
string gwires[2] = {"01-32","33-112"};

int wfLength = 0;

string msg; assign msg to "B_DET_DC_HV_SEC{S1}{S2}{S3}:{T}wf:msg";

float s1r1l1_wf[18]; assign s1r1l1_wf to "B_DET_DC_HV_SEC{S1}_R1_SL1:{T}wf";
float s1r1l2_wf[18]; assign s1r1l2_wf to "B_DET_DC_HV_SEC{S1}_R1_SL2:{T}wf";
float s1r2l3_wf[18]; assign s1r2l3_wf to "B_DET_DC_HV_SEC{S1}_R2_SL3:{T}wf";
float s1r2l4_wf[18]; assign s1r2l4_wf to "B_DET_DC_HV_SEC{S1}_R2_SL4:{T}wf";
float s1r3l5_wf[18]; assign s1r3l5_wf to "B_DET_DC_HV_SEC{S1}_R3_SL5:{T}wf";
float s1r3l6_wf[18]; assign s1r3l6_wf to "B_DET_DC_HV_SEC{S1}_R3_SL6:{T}wf";
float s2r1l1_wf[18]; assign s2r1l1_wf to "B_DET_DC_HV_SEC{S2}_R1_SL1:{T}wf";
float s2r1l2_wf[18]; assign s2r1l2_wf to "B_DET_DC_HV_SEC{S2}_R1_SL2:{T}wf";
float s2r2l3_wf[18]; assign s2r2l3_wf to "B_DET_DC_HV_SEC{S2}_R2_SL3:{T}wf";
float s2r2l4_wf[18]; assign s2r2l4_wf to "B_DET_DC_HV_SEC{S2}_R2_SL4:{T}wf";
float s2r3l5_wf[18]; assign s2r3l5_wf to "B_DET_DC_HV_SEC{S2}_R3_SL5:{T}wf";
float s2r3l6_wf[18]; assign s2r3l6_wf to "B_DET_DC_HV_SEC{S2}_R3_SL6:{T}wf";
float s3r1l1_wf[18]; assign s3r1l1_wf to "B_DET_DC_HV_SEC{S3}_R1_SL1:{T}wf";
float s3r1l2_wf[18]; assign s3r1l2_wf to "B_DET_DC_HV_SEC{S3}_R1_SL2:{T}wf";
float s3r2l3_wf[18]; assign s3r2l3_wf to "B_DET_DC_HV_SEC{S3}_R2_SL3:{T}wf";
float s3r2l4_wf[18]; assign s3r2l4_wf to "B_DET_DC_HV_SEC{S3}_R2_SL4:{T}wf";
float s3r3l5_wf[18]; assign s3r3l5_wf to "B_DET_DC_HV_SEC{S3}_R3_SL5:{T}wf";
float s3r3l6_wf[18]; assign s3r3l6_wf to "B_DET_DC_HV_SEC{S3}_R3_SL6:{T}wf";

float s1r1l1[18]; assign s1r1l1 to {};
float s1r1l2[18]; assign s1r1l2 to {};
float s1r2l3[18]; assign s1r2l3 to {};
float s1r2l4[18]; assign s1r2l4 to {};
float s1r3l5[18]; assign s1r3l5 to {};
float s1r3l6[18]; assign s1r3l6 to {};
float s2r1l1[18]; assign s2r1l1 to {};
float s2r1l2[18]; assign s2r1l2 to {};
float s2r2l3[18]; assign s2r2l3 to {};
float s2r2l4[18]; assign s2r2l4 to {};
float s2r3l5[18]; assign s2r3l5 to {};
float s2r3l6[18]; assign s2r3l6 to {};
float s3r1l1[18]; assign s3r1l1 to {};
float s3r1l2[18]; assign s3r1l2 to {};
float s3r2l3[18]; assign s3r2l3 to {};
float s3r2l4[18]; assign s3r2l4 to {};
float s3r3l5[18]; assign s3r3l5 to {};
float s3r3l6[18]; assign s3r3l6 to {};

int ii;
int jj;
string stmp;

ss seqDCHVwaveforms {

  state start
  {   
    when ()
    { 
      printf("** start state **************************\n");
      sprintf(msg,"Assigning PVs ...");
      pvPut(msg);

      jj=0;

      for (ii=0; ii<nsfwires; ii++)
      {
        sprintf(stmp,"%s_SEC{S1}_R1_SL1_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s1r1l1[jj],stmp);
        sprintf(stmp,"%s_SEC{S1}_R1_SL2_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s1r1l2[jj],stmp);
        sprintf(stmp,"%s_SEC{S1}_R2_SL3_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s1r2l3[jj],stmp);
        sprintf(stmp,"%s_SEC{S1}_R2_SL4_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s1r2l4[jj],stmp);
        sprintf(stmp,"%s_SEC{S1}_R3_SL5_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s1r3l5[jj],stmp);
        sprintf(stmp,"%s_SEC{S1}_R3_SL6_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s1r3l6[jj],stmp);

        sprintf(stmp,"%s_SEC{S2}_R1_SL1_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s2r1l1[jj],stmp);
        sprintf(stmp,"%s_SEC{S2}_R1_SL2_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s2r1l2[jj],stmp);
        sprintf(stmp,"%s_SEC{S2}_R2_SL3_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s2r2l3[jj],stmp);
        sprintf(stmp,"%s_SEC{S2}_R2_SL4_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s2r2l4[jj],stmp);
        sprintf(stmp,"%s_SEC{S2}_R3_SL5_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s2r3l5[jj],stmp);
        sprintf(stmp,"%s_SEC{S2}_R3_SL6_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s2r3l6[jj],stmp);

        sprintf(stmp,"%s_SEC{S3}_R1_SL1_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s3r1l1[jj],stmp);
        sprintf(stmp,"%s_SEC{S3}_R1_SL2_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s3r1l2[jj],stmp);
        sprintf(stmp,"%s_SEC{S3}_R2_SL3_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s3r2l3[jj],stmp);
        sprintf(stmp,"%s_SEC{S3}_R2_SL4_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s3r2l4[jj],stmp);
        sprintf(stmp,"%s_SEC{S3}_R3_SL5_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s3r3l5[jj],stmp);
        sprintf(stmp,"%s_SEC{S3}_R3_SL6_S%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s3r3l6[jj],stmp);

        jj++;
      }

      for (ii=0; ii<nsfwires; ii++)
      {
        sprintf(stmp,"%s_SEC{S1}_R1_SL1_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s1r1l1[jj],stmp);
        sprintf(stmp,"%s_SEC{S1}_R1_SL2_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s1r1l2[jj],stmp);
        sprintf(stmp,"%s_SEC{S1}_R2_SL3_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s1r2l3[jj],stmp);
        sprintf(stmp,"%s_SEC{S1}_R2_SL4_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s1r2l4[jj],stmp);
        sprintf(stmp,"%s_SEC{S1}_R3_SL5_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s1r3l5[jj],stmp);
        sprintf(stmp,"%s_SEC{S1}_R3_SL6_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s1r3l6[jj],stmp);

        sprintf(stmp,"%s_SEC{S2}_R1_SL1_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s2r1l1[jj],stmp);
        sprintf(stmp,"%s_SEC{S2}_R1_SL2_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s2r1l2[jj],stmp);
        sprintf(stmp,"%s_SEC{S2}_R2_SL3_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s2r2l3[jj],stmp);
        sprintf(stmp,"%s_SEC{S2}_R2_SL4_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s2r2l4[jj],stmp);
        sprintf(stmp,"%s_SEC{S2}_R3_SL5_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s2r3l5[jj],stmp);
        sprintf(stmp,"%s_SEC{S2}_R3_SL6_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s2r3l6[jj],stmp);

        sprintf(stmp,"%s_SEC{S3}_R1_SL1_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s3r1l1[jj],stmp);
        sprintf(stmp,"%s_SEC{S3}_R1_SL2_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s3r1l2[jj],stmp);
        sprintf(stmp,"%s_SEC{S3}_R2_SL3_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s3r2l3[jj],stmp);
        sprintf(stmp,"%s_SEC{S3}_R2_SL4_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s3r2l4[jj],stmp);
        sprintf(stmp,"%s_SEC{S3}_R3_SL5_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s3r3l5[jj],stmp);
        sprintf(stmp,"%s_SEC{S3}_R3_SL6_F%s:{T}",prefix,sfwires[ii]);
        pvAssignSubst(s3r3l6[jj],stmp);

        jj++;
      }

      for (ii=0; ii<ngwires; ii++)
      {
        sprintf(stmp,"%s_SEC{S1}_R1_SL1_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s1r1l1[jj],stmp);
        sprintf(stmp,"%s_SEC{S1}_R1_SL2_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s1r1l2[jj],stmp);
        sprintf(stmp,"%s_SEC{S1}_R2_SL3_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s1r2l3[jj],stmp);
        sprintf(stmp,"%s_SEC{S1}_R2_SL4_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s1r2l4[jj],stmp);
        sprintf(stmp,"%s_SEC{S1}_R3_SL5_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s1r3l5[jj],stmp);
        sprintf(stmp,"%s_SEC{S1}_R3_SL6_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s1r3l6[jj],stmp);

        sprintf(stmp,"%s_SEC{S2}_R1_SL1_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s2r1l1[jj],stmp);
        sprintf(stmp,"%s_SEC{S2}_R1_SL2_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s2r1l2[jj],stmp);
        sprintf(stmp,"%s_SEC{S2}_R2_SL3_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s2r2l3[jj],stmp);
        sprintf(stmp,"%s_SEC{S2}_R2_SL4_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s2r2l4[jj],stmp);
        sprintf(stmp,"%s_SEC{S2}_R3_SL5_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s2r3l5[jj],stmp);
        sprintf(stmp,"%s_SEC{S2}_R3_SL6_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s2r3l6[jj],stmp);

        sprintf(stmp,"%s_SEC{S3}_R1_SL1_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s3r1l1[jj],stmp);
        sprintf(stmp,"%s_SEC{S3}_R1_SL2_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s3r1l2[jj],stmp);
        sprintf(stmp,"%s_SEC{S3}_R2_SL3_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s3r2l3[jj],stmp);
        sprintf(stmp,"%s_SEC{S3}_R2_SL4_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s3r2l4[jj],stmp);
        sprintf(stmp,"%s_SEC{S3}_R3_SL5_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s3r3l5[jj],stmp);
        sprintf(stmp,"%s_SEC{S3}_R3_SL6_G%s:{T}",prefix,gwires[ii]);
        pvAssignSubst(s3r3l6[jj],stmp);

        jj++;
      }

      wfLength = jj;

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
      sprintf(msg,"Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
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
      sprintf(msg,"Running");
      pvPut(msg);
    }

    when (pvConnectCount() < pvChannelCount()) {} state init

    when ()
    {
      for (ii=0; ii<wfLength; ii++)
      {
        pvGet(s1r1l1[ii]);
        pvGet(s1r1l2[ii]);
        pvGet(s1r2l3[ii]);
        pvGet(s1r2l4[ii]);
        pvGet(s1r3l5[ii]);
        pvGet(s1r3l6[ii]);
        pvGet(s2r1l1[ii]);
        pvGet(s2r1l2[ii]);
        pvGet(s2r2l3[ii]);
        pvGet(s2r2l4[ii]);
        pvGet(s2r3l5[ii]);
        pvGet(s2r3l6[ii]);
        pvGet(s3r1l1[ii]);
        pvGet(s3r1l2[ii]);
        pvGet(s3r2l3[ii]);
        pvGet(s3r2l4[ii]);
        pvGet(s3r3l5[ii]);
        pvGet(s3r3l6[ii]);

        s1r1l1_wf[ii] = s1r1l1[ii];
        s1r1l2_wf[ii] = s1r1l2[ii];
        s1r2l3_wf[ii] = s1r2l3[ii];
        s1r2l4_wf[ii] = s1r2l4[ii];
        s1r3l5_wf[ii] = s1r3l5[ii];
        s1r3l6_wf[ii] = s1r3l6[ii];
        s2r1l1_wf[ii] = s2r1l1[ii];
        s2r1l2_wf[ii] = s2r1l2[ii];
        s2r2l3_wf[ii] = s2r2l3[ii];
        s2r2l4_wf[ii] = s2r2l4[ii];
        s2r3l5_wf[ii] = s2r3l5[ii];
        s2r3l6_wf[ii] = s2r3l6[ii];
        s3r1l1_wf[ii] = s3r1l1[ii];
        s3r1l2_wf[ii] = s3r1l2[ii];
        s3r2l3_wf[ii] = s3r2l3[ii];
        s3r2l4_wf[ii] = s3r2l4[ii];
        s3r3l5_wf[ii] = s3r3l5[ii];
        s3r3l6_wf[ii] = s3r3l6[ii];
      }

      pvPut(s1r1l1_wf);
      pvPut(s1r1l2_wf);
      pvPut(s1r2l3_wf);
      pvPut(s1r2l4_wf);
      pvPut(s1r3l5_wf);
      pvPut(s1r3l6_wf);
      pvPut(s2r1l1_wf);
      pvPut(s2r1l2_wf);
      pvPut(s2r2l3_wf);
      pvPut(s2r2l4_wf);
      pvPut(s2r3l5_wf);
      pvPut(s2r3l6_wf);
      pvPut(s3r1l1_wf);
      pvPut(s3r1l2_wf);
      pvPut(s3r2l3_wf);
      pvPut(s3r2l4_wf);
      pvPut(s3r3l5_wf);
      pvPut(s3r3l6_wf);

      epicsThreadSleep(period_seconds);

    } state run
  }

}


