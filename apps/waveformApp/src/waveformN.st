program waveformN

// allow sequencer to start before all PVs connected:
option -c;

// make reentrant (required for multiple instances):
option +r;

// run in safe mode:
option +s;

#ifdef VXWORKS
%%#include <vxWorks.h>
%%#include <ioLib.h>
int inFile
#else
%%FILE* inFile;
#endif

#define MAXWF 10

#define MAXLEN  10000
float wfIn0[MAXLEN];     assign wfIn0 to {};
float wfIn1[MAXLEN];     assign wfIn1 to {};
float wfIn2[MAXLEN];     assign wfIn2 to {};
float wfIn3[MAXLEN];     assign wfIn3 to {};
float wfIn4[MAXLEN];     assign wfIn4 to {};
float wfIn5[MAXLEN];     assign wfIn5 to {};
float wfIn6[MAXLEN];     assign wfIn6 to {};
float wfIn7[MAXLEN];     assign wfIn7 to {};
float wfIn8[MAXLEN];     assign wfIn8 to {};
float wfIn9[MAXLEN];     assign wfIn9 to {};

float wfOut0[MAXLEN];    assign wfOut0 to {};
float wfOut1[MAXLEN];    assign wfOut1 to {};
float wfOut2[MAXLEN];    assign wfOut2 to {};
float wfOut3[MAXLEN];    assign wfOut3 to {};
float wfOut4[MAXLEN];    assign wfOut4 to {};
float wfOut5[MAXLEN];    assign wfOut5 to {};
float wfOut6[MAXLEN];    assign wfOut6 to {};
float wfOut7[MAXLEN];    assign wfOut7 to {};
float wfOut8[MAXLEN];    assign wfOut8 to {};
float wfOut9[MAXLEN];    assign wfOut9 to {};

string wfNames0[MAXLEN]; assign wfNames0 to {};
string wfNames1[MAXLEN]; assign wfNames1 to {};
string wfNames2[MAXLEN]; assign wfNames2 to {};
string wfNames3[MAXLEN]; assign wfNames3 to {};
string wfNames4[MAXLEN]; assign wfNames4 to {};
string wfNames5[MAXLEN]; assign wfNames5 to {};
string wfNames6[MAXLEN]; assign wfNames6 to {};
string wfNames7[MAXLEN]; assign wfNames7 to {};
string wfNames8[MAXLEN]; assign wfNames8 to {};
string wfNames9[MAXLEN]; assign wfNames9 to {};

int wfLen[MAXWF];    assign wfLen    to {};
int wfRecLen[MAXWF]; assign wfRecLen to {};

#define NPVSTATIC 4
float wfDelay;          assign wfDelay  to "{P}{R}period";
string msg;             assign msg      to "{P}{R}msg";
string filename;        assign filename to "{P}{R}filename";
int doSleep;            assign doSleep  to "{P}{R}sleep";

monitor wfDelay;
monitor doSleep;

int nWF;
int ii;
int nPVs;
int fatalError;
string stmp;
string stub;
string prefix;
string stmp2;

ss waveformN {

  state start {

    entry {
      for (ii=0; ii<MAXWF; ii++) wfLen[ii]=0;
      nPVs=NPVSTATIC;
      sprintf(stub,"seq waveform(%s%s)",macValueGet("P"),macValueGet("R"));
      sprintf(prefix,"%s%s",macValueGet("P"),macValueGet("R"));
    }
    
    when (pvConnectCount() < nPVs) {
      printf("\n%s - Waiting for Static PVs (%d/%d)\n",stub,pvConnectCount(),nPVs);
      sprintf(msg,"Waiting for Static PVs (%d/%d)",pvConnectCount(),nPVs);
      pvPut(msg);
      epicsThreadSleep(1);
    } state start
    
    when () {} state init
  
  }

  state init {

    when () {
      nWF=0;
      fatalError=0;
      sprintf(msg,"Assigning PVs");
      pvPut(msg);
      pvGet(filename);
      //pvArrayPut(wfLen);
      //pvGet(wfRecLen);
      //if (wfRecLen > MAXLEN) {
      //  printf("%s - WARNING:  %swf.NELM is greater than sequencer's MAXLEN\n",stub,prefix);
      //}
      sprintf(msg,"Opening file:  %s",filename);
      printf("%s - %s\n",stub,msg);
      pvPut(msg);
#ifdef VXWORKS
      inFile = open(filename,O_RDONLY);
#else
      inFile = fopen(filename,"r");
#endif
      if (!inFile) {
        sprintf(msg,"Error Reading %s",filename);
        pvPut(msg);
        printf("%s - %s\n",stub,msg);
        fatalError=1;
      }
      else {
        while ((fscanf(inFile,"%s",stmp))==1) {

          // ignore blank lines:
          if (strcmp(stmp,"")==0) continue;


          // if line starts with '#', then it's a new waveform
          if (stmp[0]=='#') {
              if (sscanf(stmp,"#%s",stmp2)!=1) {
                  sprintf(msg,"Error Reading %s",filename);
                  pvPut(msg);
                  printf("%s - %s\n",stub,msg);
                  fatalError=1;
                  break;
              }
              pvAssign(wfOut0,stmp2);
              nWF++;
          }


          else printf("%s\n",stmp);
          if (wfLen[nWF] >= wfRecLen[nWF]) {
            sprintf(msg,"ABORT:  #PVs > NELM.");
            pvPut(msg);
            printf("%s - %s\n",stub,msg);
            fatalError=1;
            break;
          }
          else if (wfLen[nWF] >= MAXLEN) {
            sprintf(msg,"ABORT:  #PVs > MAXLEN.");
            pvPut(msg);
            printf("%s - %s\n",stub,msg);
            fatalError=1;
            break;
          }
          //pvAssign(wfIn[wfLen],stmp);
          //pvMonitor(wfIn[wfLen]);
          //sprintf(wfNames[wfLen],"%s",stmp);
          //wfLen++;
        }
        fclose(inFile);
      }
      //pvArrayPut(wfLen);
      //pvArrayPut(wfNames);
      nPVs += wfLen[nWF];
    } state wait

  }

  state wait {

    when (fatalError) {} exit

    when (wfLen <= 0) {
      sprintf(msg,"Zero PVs Read from %s",filename);
      pvPut(msg);
      printf("%s - %s - EXITING SEQUENCER\n",stub,msg);
    } exit
    
    when (pvConnectCount() < nPVs) {
      sprintf(msg,"Waiting for PVs (%d/%d)",pvConnectCount(),nPVs);
      pvPut(msg);
      printf("%s - %s\n",stub,msg);
      epicsThreadSleep(1);
    } state wait
    
    when () {} state run
  }
 

  state run {
  
    entry { 
      sprintf(msg,"OK - Running");
      pvPut(msg);
      printf("%s - %s\n",stub,msg);
    }

    when (pvConnectCount() < nPVs) {} state wait

    when (doSleep || delay(wfDelay)) {
      if (doSleep) epicsThreadSleep(wfDelay);
      //for (ii=0; ii<wfLen; ii++) wfOut[ii]=wfIn[ii];
      //pvPut(wfOut);
    } state run

  }

}


