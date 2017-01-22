program seqDCHVwaveforms

option -c;
option -r;

string prefix = "B_DET_DC_HV";
string suffixi = "imon";
string suffixv = "vmon";

// update period (seconds): 
int delay=5;

int nsfwires=8;
int ngwires=2;
string sfwires[8]={"01-08","09-16","17-24","25-32","33-48","49-64","65-80","81-112"};
string gwires[2]={"01-32","33-112"};

int wfLength=0;

string msg; assign msg to "B_DET_DC_HV:wfmsg";

float s1r1l1iwf[18]; assign s1r1l1iwf to "B_DET_DC_HV_SEC1_R1_SL1:imonwf";
float s1r1l2iwf[18]; assign s1r1l2iwf to "B_DET_DC_HV_SEC1_R1_SL2:imonwf";
float s1r2l3iwf[18]; assign s1r2l3iwf to "B_DET_DC_HV_SEC1_R2_SL3:imonwf";
float s1r2l4iwf[18]; assign s1r2l4iwf to "B_DET_DC_HV_SEC1_R2_SL4:imonwf";
float s1r3l5iwf[18]; assign s1r3l5iwf to "B_DET_DC_HV_SEC1_R3_SL5:imonwf";
float s1r3l6iwf[18]; assign s1r3l6iwf to "B_DET_DC_HV_SEC1_R3_SL6:imonwf";
float s2r1l1iwf[18]; assign s2r1l1iwf to "B_DET_DC_HV_SEC2_R1_SL1:imonwf";
float s2r1l2iwf[18]; assign s2r1l2iwf to "B_DET_DC_HV_SEC2_R1_SL2:imonwf";
float s2r2l3iwf[18]; assign s2r2l3iwf to "B_DET_DC_HV_SEC2_R2_SL3:imonwf";
float s2r2l4iwf[18]; assign s2r2l4iwf to "B_DET_DC_HV_SEC2_R2_SL4:imonwf";
float s2r3l5iwf[18]; assign s2r3l5iwf to "B_DET_DC_HV_SEC2_R3_SL5:imonwf";
float s2r3l6iwf[18]; assign s2r3l6iwf to "B_DET_DC_HV_SEC2_R3_SL6:imonwf";
float s3r1l1iwf[18]; assign s3r1l1iwf to "B_DET_DC_HV_SEC3_R1_SL1:imonwf";
float s3r1l2iwf[18]; assign s3r1l2iwf to "B_DET_DC_HV_SEC3_R1_SL2:imonwf";
float s3r2l3iwf[18]; assign s3r2l3iwf to "B_DET_DC_HV_SEC3_R2_SL3:imonwf";
float s3r2l4iwf[18]; assign s3r2l4iwf to "B_DET_DC_HV_SEC3_R2_SL4:imonwf";
float s3r3l5iwf[18]; assign s3r3l5iwf to "B_DET_DC_HV_SEC3_R3_SL5:imonwf";
float s3r3l6iwf[18]; assign s3r3l6iwf to "B_DET_DC_HV_SEC3_R3_SL6:imonwf";
float s4r1l1iwf[18]; assign s4r1l1iwf to "B_DET_DC_HV_SEC4_R1_SL1:imonwf";
float s4r1l2iwf[18]; assign s4r1l2iwf to "B_DET_DC_HV_SEC4_R1_SL2:imonwf";
float s4r2l3iwf[18]; assign s4r2l3iwf to "B_DET_DC_HV_SEC4_R2_SL3:imonwf";
float s4r2l4iwf[18]; assign s4r2l4iwf to "B_DET_DC_HV_SEC4_R2_SL4:imonwf";
float s4r3l5iwf[18]; assign s4r3l5iwf to "B_DET_DC_HV_SEC4_R3_SL5:imonwf";
float s4r3l6iwf[18]; assign s4r3l6iwf to "B_DET_DC_HV_SEC4_R3_SL6:imonwf";
float s5r1l1iwf[18]; assign s5r1l1iwf to "B_DET_DC_HV_SEC5_R1_SL1:imonwf";
float s5r1l2iwf[18]; assign s5r1l2iwf to "B_DET_DC_HV_SEC5_R1_SL2:imonwf";
float s5r2l3iwf[18]; assign s5r2l3iwf to "B_DET_DC_HV_SEC5_R2_SL3:imonwf";
float s5r2l4iwf[18]; assign s5r2l4iwf to "B_DET_DC_HV_SEC5_R2_SL4:imonwf";
float s5r3l5iwf[18]; assign s5r3l5iwf to "B_DET_DC_HV_SEC5_R3_SL5:imonwf";
float s5r3l6iwf[18]; assign s5r3l6iwf to "B_DET_DC_HV_SEC5_R3_SL6:imonwf";
float s6r1l1iwf[18]; assign s6r1l1iwf to "B_DET_DC_HV_SEC6_R1_SL1:imonwf";
float s6r1l2iwf[18]; assign s6r1l2iwf to "B_DET_DC_HV_SEC6_R1_SL2:imonwf";
float s6r2l3iwf[18]; assign s6r2l3iwf to "B_DET_DC_HV_SEC6_R2_SL3:imonwf";
float s6r2l4iwf[18]; assign s6r2l4iwf to "B_DET_DC_HV_SEC6_R2_SL4:imonwf";
float s6r3l5iwf[18]; assign s6r3l5iwf to "B_DET_DC_HV_SEC6_R3_SL5:imonwf";
float s6r3l6iwf[18]; assign s6r3l6iwf to "B_DET_DC_HV_SEC6_R3_SL6:imonwf";

float s1r1l1i[18]; assign s1r1l1i to {};
float s1r1l2i[18]; assign s1r1l2i to {};
float s1r2l3i[18]; assign s1r2l3i to {};
float s1r2l4i[18]; assign s1r2l4i to {};
float s1r3l5i[18]; assign s1r3l5i to {};
float s1r3l6i[18]; assign s1r3l6i to {};
float s2r1l1i[18]; assign s2r1l1i to {};
float s2r1l2i[18]; assign s2r1l2i to {};
float s2r2l3i[18]; assign s2r2l3i to {};
float s2r2l4i[18]; assign s2r2l4i to {};
float s2r3l5i[18]; assign s2r3l5i to {};
float s2r3l6i[18]; assign s2r3l6i to {};
float s3r1l1i[18]; assign s3r1l1i to {};
float s3r1l2i[18]; assign s3r1l2i to {};
float s3r2l3i[18]; assign s3r2l3i to {};
float s3r2l4i[18]; assign s3r2l4i to {};
float s3r3l5i[18]; assign s3r3l5i to {};
float s3r3l6i[18]; assign s3r3l6i to {};
float s4r1l1i[18]; assign s4r1l1i to {};
float s4r1l2i[18]; assign s4r1l2i to {};
float s4r2l3i[18]; assign s4r2l3i to {};
float s4r2l4i[18]; assign s4r2l4i to {};
float s4r3l5i[18]; assign s4r3l5i to {};
float s4r3l6i[18]; assign s4r3l6i to {};
float s5r1l1i[18]; assign s5r1l1i to {};
float s5r1l2i[18]; assign s5r1l2i to {};
float s5r2l3i[18]; assign s5r2l3i to {};
float s5r2l4i[18]; assign s5r2l4i to {};
float s5r3l5i[18]; assign s5r3l5i to {};
float s5r3l6i[18]; assign s5r3l6i to {};
float s6r1l1i[18]; assign s6r1l1i to {};
float s6r1l2i[18]; assign s6r1l2i to {};
float s6r2l3i[18]; assign s6r2l3i to {};
float s6r2l4i[18]; assign s6r2l4i to {};
float s6r3l5i[18]; assign s6r3l5i to {};
float s6r3l6i[18]; assign s6r3l6i to {};

float s1r1l1vwf[18]; assign s1r1l1vwf to "B_DET_DC_HV_SEC1_R1_SL1:vmonwf";
float s1r1l2vwf[18]; assign s1r1l2vwf to "B_DET_DC_HV_SEC1_R1_SL2:vmonwf";
float s1r2l3vwf[18]; assign s1r2l3vwf to "B_DET_DC_HV_SEC1_R2_SL3:vmonwf";
float s1r2l4vwf[18]; assign s1r2l4vwf to "B_DET_DC_HV_SEC1_R2_SL4:vmonwf";
float s1r3l5vwf[18]; assign s1r3l5vwf to "B_DET_DC_HV_SEC1_R3_SL5:vmonwf";
float s1r3l6vwf[18]; assign s1r3l6vwf to "B_DET_DC_HV_SEC1_R3_SL6:vmonwf";
float s2r1l1vwf[18]; assign s2r1l1vwf to "B_DET_DC_HV_SEC2_R1_SL1:vmonwf";
float s2r1l2vwf[18]; assign s2r1l2vwf to "B_DET_DC_HV_SEC2_R1_SL2:vmonwf";
float s2r2l3vwf[18]; assign s2r2l3vwf to "B_DET_DC_HV_SEC2_R2_SL3:vmonwf";
float s2r2l4vwf[18]; assign s2r2l4vwf to "B_DET_DC_HV_SEC2_R2_SL4:vmonwf";
float s2r3l5vwf[18]; assign s2r3l5vwf to "B_DET_DC_HV_SEC2_R3_SL5:vmonwf";
float s2r3l6vwf[18]; assign s2r3l6vwf to "B_DET_DC_HV_SEC2_R3_SL6:vmonwf";
float s3r1l1vwf[18]; assign s3r1l1vwf to "B_DET_DC_HV_SEC3_R1_SL1:vmonwf";
float s3r1l2vwf[18]; assign s3r1l2vwf to "B_DET_DC_HV_SEC3_R1_SL2:vmonwf";
float s3r2l3vwf[18]; assign s3r2l3vwf to "B_DET_DC_HV_SEC3_R2_SL3:vmonwf";
float s3r2l4vwf[18]; assign s3r2l4vwf to "B_DET_DC_HV_SEC3_R2_SL4:vmonwf";
float s3r3l5vwf[18]; assign s3r3l5vwf to "B_DET_DC_HV_SEC3_R3_SL5:vmonwf";
float s3r3l6vwf[18]; assign s3r3l6vwf to "B_DET_DC_HV_SEC3_R3_SL6:vmonwf";
float s4r1l1vwf[18]; assign s4r1l1vwf to "B_DET_DC_HV_SEC4_R1_SL1:vmonwf";
float s4r1l2vwf[18]; assign s4r1l2vwf to "B_DET_DC_HV_SEC4_R1_SL2:vmonwf";
float s4r2l3vwf[18]; assign s4r2l3vwf to "B_DET_DC_HV_SEC4_R2_SL3:vmonwf";
float s4r2l4vwf[18]; assign s4r2l4vwf to "B_DET_DC_HV_SEC4_R2_SL4:vmonwf";
float s4r3l5vwf[18]; assign s4r3l5vwf to "B_DET_DC_HV_SEC4_R3_SL5:vmonwf";
float s4r3l6vwf[18]; assign s4r3l6vwf to "B_DET_DC_HV_SEC4_R3_SL6:vmonwf";
float s5r1l1vwf[18]; assign s5r1l1vwf to "B_DET_DC_HV_SEC5_R1_SL1:vmonwf";
float s5r1l2vwf[18]; assign s5r1l2vwf to "B_DET_DC_HV_SEC5_R1_SL2:vmonwf";
float s5r2l3vwf[18]; assign s5r2l3vwf to "B_DET_DC_HV_SEC5_R2_SL3:vmonwf";
float s5r2l4vwf[18]; assign s5r2l4vwf to "B_DET_DC_HV_SEC5_R2_SL4:vmonwf";
float s5r3l5vwf[18]; assign s5r3l5vwf to "B_DET_DC_HV_SEC5_R3_SL5:vmonwf";
float s5r3l6vwf[18]; assign s5r3l6vwf to "B_DET_DC_HV_SEC5_R3_SL6:vmonwf";
float s6r1l1vwf[18]; assign s6r1l1vwf to "B_DET_DC_HV_SEC6_R1_SL1:vmonwf";
float s6r1l2vwf[18]; assign s6r1l2vwf to "B_DET_DC_HV_SEC6_R1_SL2:vmonwf";
float s6r2l3vwf[18]; assign s6r2l3vwf to "B_DET_DC_HV_SEC6_R2_SL3:vmonwf";
float s6r2l4vwf[18]; assign s6r2l4vwf to "B_DET_DC_HV_SEC6_R2_SL4:vmonwf";
float s6r3l5vwf[18]; assign s6r3l5vwf to "B_DET_DC_HV_SEC6_R3_SL5:vmonwf";
float s6r3l6vwf[18]; assign s6r3l6vwf to "B_DET_DC_HV_SEC6_R3_SL6:vmonwf";

float s1r1l1v[18]; assign s1r1l1v to {};
float s1r1l2v[18]; assign s1r1l2v to {};
float s1r2l3v[18]; assign s1r2l3v to {};
float s1r2l4v[18]; assign s1r2l4v to {};
float s1r3l5v[18]; assign s1r3l5v to {};
float s1r3l6v[18]; assign s1r3l6v to {};
float s2r1l1v[18]; assign s2r1l1v to {};
float s2r1l2v[18]; assign s2r1l2v to {};
float s2r2l3v[18]; assign s2r2l3v to {};
float s2r2l4v[18]; assign s2r2l4v to {};
float s2r3l5v[18]; assign s2r3l5v to {};
float s2r3l6v[18]; assign s2r3l6v to {};
float s3r1l1v[18]; assign s3r1l1v to {};
float s3r1l2v[18]; assign s3r1l2v to {};
float s3r2l3v[18]; assign s3r2l3v to {};
float s3r2l4v[18]; assign s3r2l4v to {};
float s3r3l5v[18]; assign s3r3l5v to {};
float s3r3l6v[18]; assign s3r3l6v to {};
float s4r1l1v[18]; assign s4r1l1v to {};
float s4r1l2v[18]; assign s4r1l2v to {};
float s4r2l3v[18]; assign s4r2l3v to {};
float s4r2l4v[18]; assign s4r2l4v to {};
float s4r3l5v[18]; assign s4r3l5v to {};
float s4r3l6v[18]; assign s4r3l6v to {};
float s5r1l1v[18]; assign s5r1l1v to {};
float s5r1l2v[18]; assign s5r1l2v to {};
float s5r2l3v[18]; assign s5r2l3v to {};
float s5r2l4v[18]; assign s5r2l4v to {};
float s5r3l5v[18]; assign s5r3l5v to {};
float s5r3l6v[18]; assign s5r3l6v to {};
float s6r1l1v[18]; assign s6r1l1v to {};
float s6r1l2v[18]; assign s6r1l2v to {};
float s6r2l3v[18]; assign s6r2l3v to {};
float s6r2l4v[18]; assign s6r2l4v to {};
float s6r3l5v[18]; assign s6r3l5v to {};
float s6r3l6v[18]; assign s6r3l6v to {};

int ii;
int jj;
string stmp;

ss seqDCHVwaveforms {

  state start
  {   
    when ()
    { 
      printf("** start state **************************\n");
      sprintf(msg,"INIT - Assigning PVs");
      pvPut(msg);

      jj=0;

      for (ii=0; ii<nsfwires; ii++)
      {
        sprintf(stmp,"%s_SEC1_R1_SL1_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s1r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC1_R1_SL2_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s1r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC1_R2_SL3_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s1r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC1_R2_SL4_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s1r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC1_R3_SL5_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s1r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC1_R3_SL6_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s1r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC2_R1_SL1_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s2r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC2_R1_SL2_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s2r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC2_R2_SL3_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s2r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC2_R2_SL4_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s2r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC2_R3_SL5_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s2r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC2_R3_SL6_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s2r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC3_R1_SL1_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s3r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC3_R1_SL2_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s3r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC3_R2_SL3_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s3r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC3_R2_SL4_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s3r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC3_R3_SL5_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s3r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC3_R3_SL6_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s3r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC4_R1_SL1_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s4r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC4_R1_SL2_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s4r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC4_R2_SL3_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s4r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC4_R2_SL4_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s4r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC4_R3_SL5_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s4r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC4_R3_SL6_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s4r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC5_R1_SL1_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s5r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC5_R1_SL2_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s5r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC5_R2_SL3_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s5r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC5_R2_SL4_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s5r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC5_R3_SL5_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s5r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC5_R3_SL6_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s5r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC6_R1_SL1_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s6r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC6_R1_SL2_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s6r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC6_R2_SL3_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s6r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC6_R2_SL4_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s6r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC6_R3_SL5_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s6r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC6_R3_SL6_S%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s6r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC1_R1_SL1_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s1r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC1_R1_SL2_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s1r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC1_R2_SL3_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s1r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC1_R2_SL4_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s1r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC1_R3_SL5_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s1r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC1_R3_SL6_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s1r3l6v[jj],stmp);

        sprintf(stmp,"%s_SEC2_R1_SL1_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s2r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC2_R1_SL2_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s2r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC2_R2_SL3_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s2r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC2_R2_SL4_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s2r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC2_R3_SL5_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s2r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC2_R3_SL6_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s2r3l6v[jj],stmp);

        sprintf(stmp,"%s_SEC3_R1_SL1_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s3r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC3_R1_SL2_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s3r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC3_R2_SL3_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s3r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC3_R2_SL4_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s3r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC3_R3_SL5_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s3r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC3_R3_SL6_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s3r3l6v[jj],stmp);

        sprintf(stmp,"%s_SEC4_R1_SL1_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s4r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC4_R1_SL2_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s4r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC4_R2_SL3_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s4r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC4_R2_SL4_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s4r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC4_R3_SL5_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s4r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC4_R3_SL6_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s4r3l6v[jj],stmp);

        sprintf(stmp,"%s_SEC5_R1_SL1_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s5r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC5_R1_SL2_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s5r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC5_R2_SL3_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s5r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC5_R2_SL4_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s5r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC5_R3_SL5_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s5r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC5_R3_SL6_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s5r3l6v[jj],stmp);

        sprintf(stmp,"%s_SEC6_R1_SL1_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s6r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC6_R1_SL2_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s6r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC6_R2_SL3_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s6r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC6_R2_SL4_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s6r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC6_R3_SL5_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s6r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC6_R3_SL6_S%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s6r3l6v[jj],stmp);
        jj++;
      }

      for (ii=0; ii<nsfwires; ii++)
      {
        sprintf(stmp,"%s_SEC1_R1_SL1_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s1r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC1_R1_SL2_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s1r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC1_R2_SL3_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s1r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC1_R2_SL4_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s1r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC1_R3_SL5_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s1r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC1_R3_SL6_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s1r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC2_R1_SL1_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s2r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC2_R1_SL2_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s2r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC2_R2_SL3_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s2r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC2_R2_SL4_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s2r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC2_R3_SL5_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s2r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC2_R3_SL6_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s2r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC3_R1_SL1_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s3r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC3_R1_SL2_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s3r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC3_R2_SL3_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s3r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC3_R2_SL4_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s3r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC3_R3_SL5_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s3r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC3_R3_SL6_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s3r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC4_R1_SL1_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s4r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC4_R1_SL2_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s4r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC4_R2_SL3_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s4r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC4_R2_SL4_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s4r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC4_R3_SL5_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s4r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC4_R3_SL6_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s4r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC5_R1_SL1_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s5r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC5_R1_SL2_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s5r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC5_R2_SL3_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s5r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC5_R2_SL4_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s5r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC5_R3_SL5_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s5r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC5_R3_SL6_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s5r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC6_R1_SL1_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s6r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC6_R1_SL2_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s6r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC6_R2_SL3_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s6r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC6_R2_SL4_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s6r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC6_R3_SL5_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s6r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC6_R3_SL6_F%s:%s",prefix,sfwires[ii],suffixi);
        pvAssign(s6r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC1_R1_SL1_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s1r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC1_R1_SL2_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s1r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC1_R2_SL3_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s1r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC1_R2_SL4_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s1r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC1_R3_SL5_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s1r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC1_R3_SL6_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s1r3l6v[jj],stmp);

        sprintf(stmp,"%s_SEC2_R1_SL1_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s2r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC2_R1_SL2_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s2r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC2_R2_SL3_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s2r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC2_R2_SL4_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s2r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC2_R3_SL5_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s2r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC2_R3_SL6_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s2r3l6v[jj],stmp);

        sprintf(stmp,"%s_SEC3_R1_SL1_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s3r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC3_R1_SL2_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s3r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC3_R2_SL3_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s3r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC3_R2_SL4_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s3r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC3_R3_SL5_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s3r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC3_R3_SL6_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s3r3l6v[jj],stmp);

        sprintf(stmp,"%s_SEC4_R1_SL1_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s4r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC4_R1_SL2_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s4r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC4_R2_SL3_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s4r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC4_R2_SL4_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s4r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC4_R3_SL5_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s4r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC4_R3_SL6_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s4r3l6v[jj],stmp);

        sprintf(stmp,"%s_SEC5_R1_SL1_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s5r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC5_R1_SL2_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s5r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC5_R2_SL3_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s5r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC5_R2_SL4_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s5r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC5_R3_SL5_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s5r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC5_R3_SL6_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s5r3l6v[jj],stmp);

        sprintf(stmp,"%s_SEC6_R1_SL1_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s6r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC6_R1_SL2_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s6r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC6_R2_SL3_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s6r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC6_R2_SL4_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s6r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC6_R3_SL5_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s6r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC6_R3_SL6_F%s:%s",prefix,sfwires[ii],suffixv);
        pvAssign(s6r3l6v[jj],stmp);

        jj++;
      }

      for (ii=0; ii<ngwires; ii++)
      {
        sprintf(stmp,"%s_SEC1_R1_SL1_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s1r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC1_R1_SL2_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s1r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC1_R2_SL3_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s1r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC1_R2_SL4_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s1r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC1_R3_SL5_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s1r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC1_R3_SL6_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s1r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC2_R1_SL1_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s2r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC2_R1_SL2_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s2r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC2_R2_SL3_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s2r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC2_R2_SL4_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s2r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC2_R3_SL5_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s2r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC2_R3_SL6_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s2r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC3_R1_SL1_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s3r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC3_R1_SL2_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s3r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC3_R2_SL3_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s3r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC3_R2_SL4_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s3r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC3_R3_SL5_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s3r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC3_R3_SL6_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s3r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC4_R1_SL1_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s4r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC4_R1_SL2_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s4r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC4_R2_SL3_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s4r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC4_R2_SL4_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s4r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC4_R3_SL5_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s4r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC4_R3_SL6_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s4r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC5_R1_SL1_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s5r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC5_R1_SL2_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s5r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC5_R2_SL3_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s5r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC5_R2_SL4_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s5r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC5_R3_SL5_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s5r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC5_R3_SL6_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s5r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC6_R1_SL1_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s6r1l1i[jj],stmp);
        sprintf(stmp,"%s_SEC6_R1_SL2_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s6r1l2i[jj],stmp);
        sprintf(stmp,"%s_SEC6_R2_SL3_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s6r2l3i[jj],stmp);
        sprintf(stmp,"%s_SEC6_R2_SL4_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s6r2l4i[jj],stmp);
        sprintf(stmp,"%s_SEC6_R3_SL5_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s6r3l5i[jj],stmp);
        sprintf(stmp,"%s_SEC6_R3_SL6_G%s:%s",prefix,gwires[ii],suffixi);
        pvAssign(s6r3l6i[jj],stmp);

        sprintf(stmp,"%s_SEC1_R1_SL1_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s1r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC1_R1_SL2_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s1r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC1_R2_SL3_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s1r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC1_R2_SL4_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s1r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC1_R3_SL5_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s1r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC1_R3_SL6_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s1r3l6v[jj],stmp);

        sprintf(stmp,"%s_SEC2_R1_SL1_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s2r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC2_R1_SL2_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s2r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC2_R2_SL3_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s2r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC2_R2_SL4_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s2r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC2_R3_SL5_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s2r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC2_R3_SL6_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s2r3l6v[jj],stmp);

        sprintf(stmp,"%s_SEC3_R1_SL1_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s3r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC3_R1_SL2_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s3r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC3_R2_SL3_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s3r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC3_R2_SL4_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s3r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC3_R3_SL5_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s3r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC3_R3_SL6_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s3r3l6v[jj],stmp);

        sprintf(stmp,"%s_SEC4_R1_SL1_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s4r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC4_R1_SL2_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s4r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC4_R2_SL3_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s4r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC4_R2_SL4_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s4r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC4_R3_SL5_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s4r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC4_R3_SL6_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s4r3l6v[jj],stmp);

        sprintf(stmp,"%s_SEC5_R1_SL1_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s5r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC5_R1_SL2_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s5r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC5_R2_SL3_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s5r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC5_R2_SL4_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s5r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC5_R3_SL5_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s5r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC5_R3_SL6_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s5r3l6v[jj],stmp);

        sprintf(stmp,"%s_SEC6_R1_SL1_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s6r1l1v[jj],stmp);
        sprintf(stmp,"%s_SEC6_R1_SL2_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s6r1l2v[jj],stmp);
        sprintf(stmp,"%s_SEC6_R2_SL3_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s6r2l3v[jj],stmp);
        sprintf(stmp,"%s_SEC6_R2_SL4_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s6r2l4v[jj],stmp);
        sprintf(stmp,"%s_SEC6_R3_SL5_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s6r3l5v[jj],stmp);
        sprintf(stmp,"%s_SEC6_R3_SL6_G%s:%s",prefix,gwires[ii],suffixv);
        pvAssign(s6r3l6v[jj],stmp);

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
      for (ii=0; ii<wfLength; ii++)
      {
        pvGet(s1r1l1i[ii]);
        pvGet(s1r1l2i[ii]);
        pvGet(s1r2l3i[ii]);
        pvGet(s1r2l4i[ii]);
        pvGet(s1r3l5i[ii]);
        pvGet(s1r3l6i[ii]);
        pvGet(s2r1l1i[ii]);
        pvGet(s2r1l2i[ii]);
        pvGet(s2r2l3i[ii]);
        pvGet(s2r2l4i[ii]);
        pvGet(s2r3l5i[ii]);
        pvGet(s2r3l6i[ii]);
        pvGet(s3r1l1i[ii]);
        pvGet(s3r1l2i[ii]);
        pvGet(s3r2l3i[ii]);
        pvGet(s3r2l4i[ii]);
        pvGet(s3r3l5i[ii]);
        pvGet(s3r3l6i[ii]);
        pvGet(s4r1l1i[ii]);
        pvGet(s4r1l2i[ii]);
        pvGet(s4r2l3i[ii]);
        pvGet(s4r2l4i[ii]);
        pvGet(s4r3l5i[ii]);
        pvGet(s4r3l6i[ii]);
        pvGet(s5r1l1i[ii]);
        pvGet(s5r1l2i[ii]);
        pvGet(s5r2l3i[ii]);
        pvGet(s5r2l4i[ii]);
        pvGet(s5r3l5i[ii]);
        pvGet(s5r3l6i[ii]);
        pvGet(s6r1l1i[ii]);
        pvGet(s6r1l2i[ii]);
        pvGet(s6r2l3i[ii]);
        pvGet(s6r2l4i[ii]);
        pvGet(s6r3l5i[ii]);
        pvGet(s6r3l6i[ii]);

        s1r1l1iwf[ii]=s1r1l1i[ii];
        s1r1l2iwf[ii]=s1r1l2i[ii];
        s1r2l3iwf[ii]=s1r2l3i[ii];
        s1r2l4iwf[ii]=s1r2l4i[ii];
        s1r3l5iwf[ii]=s1r3l5i[ii];
        s1r3l6iwf[ii]=s1r3l6i[ii];
        s2r1l1iwf[ii]=s2r1l1i[ii];
        s2r1l2iwf[ii]=s2r1l2i[ii];
        s2r2l3iwf[ii]=s2r2l3i[ii];
        s2r2l4iwf[ii]=s2r2l4i[ii];
        s2r3l5iwf[ii]=s2r3l5i[ii];
        s2r3l6iwf[ii]=s2r3l6i[ii];
        s3r1l1iwf[ii]=s3r1l1i[ii];
        s3r1l2iwf[ii]=s3r1l2i[ii];
        s3r2l3iwf[ii]=s3r2l3i[ii];
        s3r2l4iwf[ii]=s3r2l4i[ii];
        s3r3l5iwf[ii]=s3r3l5i[ii];
        s3r3l6iwf[ii]=s3r3l6i[ii];
        s4r1l1iwf[ii]=s4r1l1i[ii];
        s4r1l2iwf[ii]=s4r1l2i[ii];
        s4r2l3iwf[ii]=s4r2l3i[ii];
        s4r2l4iwf[ii]=s4r2l4i[ii];
        s4r3l5iwf[ii]=s4r3l5i[ii];
        s4r3l6iwf[ii]=s4r3l6i[ii];
        s5r1l1iwf[ii]=s5r1l1i[ii];
        s5r1l2iwf[ii]=s5r1l2i[ii];
        s5r2l3iwf[ii]=s5r2l3i[ii];
        s5r2l4iwf[ii]=s5r2l4i[ii];
        s5r3l5iwf[ii]=s5r3l5i[ii];
        s5r3l6iwf[ii]=s5r3l6i[ii];
        s6r1l1iwf[ii]=s6r1l1i[ii];
        s6r1l2iwf[ii]=s6r1l2i[ii];
        s6r2l3iwf[ii]=s6r2l3i[ii];
        s6r2l4iwf[ii]=s6r2l4i[ii];
        s6r3l5iwf[ii]=s6r3l5i[ii];
        s6r3l6iwf[ii]=s6r3l6i[ii];
        
        pvGet(s1r1l1v[ii]);
        pvGet(s1r1l2v[ii]);
        pvGet(s1r2l3v[ii]);
        pvGet(s1r2l4v[ii]);
        pvGet(s1r3l5v[ii]);
        pvGet(s1r3l6v[ii]);
        pvGet(s2r1l1v[ii]);
        pvGet(s2r1l2v[ii]);
        pvGet(s2r2l3v[ii]);
        pvGet(s2r2l4v[ii]);
        pvGet(s2r3l5v[ii]);
        pvGet(s2r3l6v[ii]);
        pvGet(s3r1l1v[ii]);
        pvGet(s3r1l2v[ii]);
        pvGet(s3r2l3v[ii]);
        pvGet(s3r2l4v[ii]);
        pvGet(s3r3l5v[ii]);
        pvGet(s3r3l6v[ii]);
        pvGet(s4r1l1v[ii]);
        pvGet(s4r1l2v[ii]);
        pvGet(s4r2l3v[ii]);
        pvGet(s4r2l4v[ii]);
        pvGet(s4r3l5v[ii]);
        pvGet(s4r3l6v[ii]);
        pvGet(s5r1l1v[ii]);
        pvGet(s5r1l2v[ii]);
        pvGet(s5r2l3v[ii]);
        pvGet(s5r2l4v[ii]);
        pvGet(s5r3l5v[ii]);
        pvGet(s5r3l6v[ii]);
        pvGet(s6r1l1v[ii]);
        pvGet(s6r1l2v[ii]);
        pvGet(s6r2l3v[ii]);
        pvGet(s6r2l4v[ii]);
        pvGet(s6r3l5v[ii]);
        pvGet(s6r3l6v[ii]);

        s1r1l1vwf[ii]=s1r1l1v[ii];
        s1r1l2vwf[ii]=s1r1l2v[ii];
        s1r2l3vwf[ii]=s1r2l3v[ii];
        s1r2l4vwf[ii]=s1r2l4v[ii];
        s1r3l5vwf[ii]=s1r3l5v[ii];
        s1r3l6vwf[ii]=s1r3l6v[ii];
        s2r1l1vwf[ii]=s2r1l1v[ii];
        s2r1l2vwf[ii]=s2r1l2v[ii];
        s2r2l3vwf[ii]=s2r2l3v[ii];
        s2r2l4vwf[ii]=s2r2l4v[ii];
        s2r3l5vwf[ii]=s2r3l5v[ii];
        s2r3l6vwf[ii]=s2r3l6v[ii];
        s3r1l1vwf[ii]=s3r1l1v[ii];
        s3r1l2vwf[ii]=s3r1l2v[ii];
        s3r2l3vwf[ii]=s3r2l3v[ii];
        s3r2l4vwf[ii]=s3r2l4v[ii];
        s3r3l5vwf[ii]=s3r3l5v[ii];
        s3r3l6vwf[ii]=s3r3l6v[ii];
        s4r1l1vwf[ii]=s4r1l1v[ii];
        s4r1l2vwf[ii]=s4r1l2v[ii];
        s4r2l3vwf[ii]=s4r2l3v[ii];
        s4r2l4vwf[ii]=s4r2l4v[ii];
        s4r3l5vwf[ii]=s4r3l5v[ii];
        s4r3l6vwf[ii]=s4r3l6v[ii];
        s5r1l1vwf[ii]=s5r1l1v[ii];
        s5r1l2vwf[ii]=s5r1l2v[ii];
        s5r2l3vwf[ii]=s5r2l3v[ii];
        s5r2l4vwf[ii]=s5r2l4v[ii];
        s5r3l5vwf[ii]=s5r3l5v[ii];
        s5r3l6vwf[ii]=s5r3l6v[ii];
        s6r1l1vwf[ii]=s6r1l1v[ii];
        s6r1l2vwf[ii]=s6r1l2v[ii];
        s6r2l3vwf[ii]=s6r2l3v[ii];
        s6r2l4vwf[ii]=s6r2l4v[ii];
        s6r3l5vwf[ii]=s6r3l5v[ii];
        s6r3l6vwf[ii]=s6r3l6v[ii];
      }

      pvPut(s1r1l1iwf);
      pvPut(s1r1l2iwf);
      pvPut(s1r2l3iwf);
      pvPut(s1r2l4iwf);
      pvPut(s1r3l5iwf);
      pvPut(s1r3l6iwf);
      pvPut(s2r1l1iwf);
      pvPut(s2r1l2iwf);
      pvPut(s2r2l3iwf);
      pvPut(s2r2l4iwf);
      pvPut(s2r3l5iwf);
      pvPut(s2r3l6iwf);
      pvPut(s3r1l1iwf);
      pvPut(s3r1l2iwf);
      pvPut(s3r2l3iwf);
      pvPut(s3r2l4iwf);
      pvPut(s3r3l5iwf);
      pvPut(s3r3l6iwf);
      pvPut(s4r1l1iwf);
      pvPut(s4r1l2iwf);
      pvPut(s4r2l3iwf);
      pvPut(s4r2l4iwf);
      pvPut(s4r3l5iwf);
      pvPut(s4r3l6iwf);
      pvPut(s5r1l1iwf);
      pvPut(s5r1l2iwf);
      pvPut(s5r2l3iwf);
      pvPut(s5r2l4iwf);
      pvPut(s5r3l5iwf);
      pvPut(s5r3l6iwf);
      pvPut(s6r1l1iwf);
      pvPut(s6r1l2iwf);
      pvPut(s6r2l3iwf);
      pvPut(s6r2l4iwf);
      pvPut(s6r3l5iwf);
      pvPut(s6r3l6iwf);

      pvPut(s1r1l1vwf);
      pvPut(s1r1l2vwf);
      pvPut(s1r2l3vwf);
      pvPut(s1r2l4vwf);
      pvPut(s1r3l5vwf);
      pvPut(s1r3l6vwf);
      pvPut(s2r1l1vwf);
      pvPut(s2r1l2vwf);
      pvPut(s2r2l3vwf);
      pvPut(s2r2l4vwf);
      pvPut(s2r3l5vwf);
      pvPut(s2r3l6vwf);
      pvPut(s3r1l1vwf);
      pvPut(s3r1l2vwf);
      pvPut(s3r2l3vwf);
      pvPut(s3r2l4vwf);
      pvPut(s3r3l5vwf);
      pvPut(s3r3l6vwf);
      pvPut(s4r1l1vwf);
      pvPut(s4r1l2vwf);
      pvPut(s4r2l3vwf);
      pvPut(s4r2l4vwf);
      pvPut(s4r3l5vwf);
      pvPut(s4r3l6vwf);
      pvPut(s5r1l1vwf);
      pvPut(s5r1l2vwf);
      pvPut(s5r2l3vwf);
      pvPut(s5r2l4vwf);
      pvPut(s5r3l5vwf);
      pvPut(s5r3l6vwf);
      pvPut(s6r1l1vwf);
      pvPut(s6r1l2vwf);
      pvPut(s6r2l3vwf);
      pvPut(s6r2l4vwf);
      pvPut(s6r3l5vwf);
      pvPut(s6r3l6vwf);

      epicsThreadSleep(delay);

    } state run
  }

}


