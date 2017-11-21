program seq_mpodwaveform

// N. Baltzell

option -c;
option -r;

// update period (seconds): 
int delay=5;

string prefix = "B_SVT_HV";
string vsuff = ":outputMeasSenseV";
string isuff = ":outputMeasCurrent";

#define NREGIONS 3
#define NCHANS 84

int nModulesPerRegion[NREGIONS]={10,14,18};
int slotsPerRegion[NREGIONS][4]={ {7,8,9,10}, {9,10,0,0}, {8,9,10,0} };
int nChansPerSlot[NREGIONS][4]={ {16,4,0,0}, {16,12,0,0}, {16,16,4,0} };

// when SVT had 4 regions:
//#define NCHANS 132
//int nModulesPerRegion[NREGIONS]={10,14,18,24};
//int slotsPerRegion[NREGIONS][4]={ {7,8,9,10}, {9,10,0,0}, {8,9,10,0} };
//int nChansPerSlot[NREGIONS][4]={ {16,4,0,0}, {16,12,0,0}, {16,16,4,0} };

float wfvo[NCHANS]; assign wfvo to "B_SVT_HV_V:wf";
float wfio[NCHANS]; assign wfio to "B_SVT_HV_I:wf";
float wfvi[NCHANS]; assign wfvi to {};
float wfii[NCHANS]; assign wfii to {};

string msg; assign msg to "B_SVT_HV:wfmsg";

string stmp;

int ii;
int jj;
int kk;
int iSlot;
int nChanSlot;
int slot;
int wfLength;

ss seq_mpodwaveform {

  state start
  {   
    when ()
    { 
      printf("** start state **************************\n");
      sprintf(msg,"INIT - Assigning PVs");
      pvPut(msg);
      wfLength=0;
      kk=0;
      for (ii=0; ii<NREGIONS; ii++)
      {
        iSlot=0;
        nChanSlot=0;
        for (jj=0; jj<nModulesPerRegion[ii]; jj++)
        {
          slot = slotsPerRegion[ii][iSlot];
          sprintf(stmp,"%s_R%dS%dT_Slot%d%s",prefix,ii+1,jj+1,slot,isuff);
          pvAssign(wfii[kk],stmp);
          sprintf(stmp,"%s_R%dS%dT_Slot%d%s",prefix,ii+1,jj+1,slot,vsuff);
          pvAssign(wfvi[kk++],stmp);
          sprintf(stmp,"%s_R%dS%dB_Slot%d%s",prefix,ii+1,jj+1,slot,isuff);
          pvAssign(wfii[kk],stmp);
          sprintf(stmp,"%s_R%dS%dB_Slot%d%s",prefix,ii+1,jj+1,slot,vsuff);
          pvAssign(wfvi[kk++],stmp);
          nChanSlot+=2;
          if (nChanSlot >= nChansPerSlot[ii][iSlot])
          {
            iSlot++;
            nChanSlot=0;
          }
        }
      }
      wfLength=kk;
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
      printf("\nmpodwaveform:  Waiting for PVs (%d/%d)\n\n",pvConnectCount(),pvChannelCount());
      sprintf(msg,"ERROR - Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
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
    when () {
      for (ii=0; ii<wfLength; ii++)
      {
        pvGet(wfii[ii]); wfio[ii]=wfii[ii];
        pvGet(wfvi[ii]); wfvo[ii]=wfvi[ii];
      }
      pvPut(wfvo);
      pvPut(wfio);

      epicsThreadSleep(2);
    } state run
  }
  
}


