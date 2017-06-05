program seq_v450waveform

option -c;
option -r;

// update period (seconds): 
int delay=5;

string prefix = "B_SVT_TEMP";

#define NREGIONS 3
#define NSLOTS 9
#define FIRSTSLOT 2
//#define NTEMPS 132
#define NTEMPS 84

int nChansPerSlot[NSLOTS]={16,16,16,16,16,4,16,16,16};
int nModulesPerRegion[NREGIONS]={10,14,18};
//int nModulesPerRegion[NREGIONS]={10,14,18,24};

float wfo[NTEMPS]; assign wfo to "B_SVT_TEMP:wf";
float wfi[NTEMPS]; assign wfi to {};

int wfLength=0;

string msg; assign msg to "B_SVT_TEMP:wfmsg";

int ii;
int jj;
int kk;
int ll;
int slot;
string stmp;

ss seq_v450waveform {

  state start
  {   
    when ()
    { 
      printf("** start state **************************\n");
      sprintf(msg,"INIT - Assigning PVs");
      pvPut(msg);
      kk=0;
      ll=0;
      slot=FIRSTSLOT;
      for (ii=0; ii<NREGIONS; ii++)
      {
        for (jj=0; jj<nModulesPerRegion[ii]; jj++)
        {
          sprintf(stmp,"%s_R%dS%dT_Slot%d",prefix,ii+1,jj+1,slot);
          pvAssign(wfi[kk++],stmp); ll++;
          sprintf(stmp,"%s_R%dS%dB_Slot%d",prefix,ii+1,jj+1,slot);
          pvAssign(wfi[kk++],stmp); ll++;
          if (ll>=nChansPerSlot[slot-FIRSTSLOT]) 
          {
            slot++;
            ll=0;
          }
        }
      }
      wfLength = kk;
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
      for (ii=0; ii<wfLength; ii++) pvGet(wfi[ii]);
      for (ii=0; ii<wfLength; ii++) wfo[ii]=wfi[ii];
      pvPut(wfo);
      epicsThreadSleep(delay);
    } state run
  }

}


