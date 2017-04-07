program waveform

option -c;
option +r;

#define MAXWFLEN  100000
float wfIn[MAXWFLEN];     assign wfIn to {};

#define NPVSTATIC 6
float wfDelay;            assign wfDelay  to "{P}{R}period";
int wfLength;             assign wfLength to "{P}{R}wflen";
string msg;               assign msg      to "{P}{R}wfmsg";
string filename;          assign filename to "{P}{R}filename";
string wfNames[MAXWFLEN]; assign wfNames  to "{P}{R}wfnames";
float wfOut[MAXWFLEN];    assign wfOut    to "{P}{R}wf";

int ii;
string stmp;

ss waveform {

  state start
  {

    entry { printf("** start state **************************\n"); }

    when (pvConnectCount() < NPVSTATIC) 
    {
      printf("Waiting for Static PVs (%d/%d)\n",pvConnectCount(),NPVSTATIC);
      sprintf(msg,"Waiting for Static PVs (%d/%d)",pvConnectCount(),NPVSTATIC);
      pvPut(msg);
      epicsThreadSleep(2);
    } state start
    
    when ()
    {
      sprintf(msg,"Assigning PVs");
      pvPut(msg);
      wfLength=0;
      pvPut(wfLength);
      pvGet(filename);
      fprintf(stderr,"\n\nOpening file:  %s\n\n",filename);
      FILE* fd = fopen(filename,"r");
      if (fd)
      {
        while ((fscanf(fd,"%s",stmp))==1) {
          if (wfLength>=MAXWFLEN)
          {
            fprintf(stderr,"\n\nToo Many PVs\n\n");
            sprintf(msg,"TOO MANY PVs");
            pvPut(msg);
            break;
          }
          pvAssign(wfIn[wfLength],stmp);
          pvMonitor(wfIn[wfLength]);
          sprintf(wfNames[wfLength],"%s",stmp);
          wfLength++;
        }
        pvPut(filename);
        pvPut(wfLength);
        pvPut(wfNames);
      }
    } state init

  }

  state init
  {
    entry { printf("** init state ****************************\n"); }

    when (wfLength==0) {} state start
    
    when (pvConnectCount() < NPVSTATIC+wfLength)
    {
      printf("Waiting for PVs (%d/%d)\n",pvConnectCount(),pvChannelCount());
      sprintf(msg,"ERROR - Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
      pvPut(msg);
      epicsThreadSleep(2);
    } state init
    
    when () {} state run

  }
  
  state run
  {
    entry { 
      printf("** run state ****************************\n");
      sprintf(msg,"OK - Running");
      pvPut(msg);
    }

    when (pvConnectCount() < NPVSTATIC+wfLength) {} state init

    when (delay(wfDelay))
    {
      for (ii=0; ii<wfLength; ii++) wfOut[ii]=wfIn[ii];
      pvPut(wfOut);
      pvGet(wfDelay);
    } state run

  }

}


