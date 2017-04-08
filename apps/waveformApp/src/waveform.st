/*
   waveform.st

   Read list of PV names from a file, fill their values in a waveform,
   preserving ordering.  Allow for arbitrary number of PVs, limited by
   MAXLEN below and waveform record's .NELM, truncating if greater.

   {P}{R}wf       = waveform of PV values
   {P}{R}wfnames  = waveform of PV names
   {P}{R}period   = waveform update period in seconds
   {P}{R}filename = name of file from which to read PV names
   {P}{R}wflen    = number of PV names read from file
   {P}{R}msg      = sequencer status message
*/

program waveform

option -c;
option +r;

#ifdef VXWORKS
%%#include <vxWorks.h>
%%#include <ioLib.h>
int file
#else
%%FILE* file;
#endif

#define MAXLEN  100000
float wfIn[MAXLEN];     assign wfIn to {};

#define NPVSTATIC 7
float wfOut[MAXLEN];    assign wfOut    to "{P}{R}wf";
float wfDelay;          assign wfDelay  to "{P}{R}period";
string wfNames[MAXLEN]; assign wfNames  to "{P}{R}wfnames";
string msg;             assign msg      to "{P}{R}msg";
string filename;        assign filename to "{P}{R}filename";
int wfLen;              assign wfLen    to "{P}{R}wflen";
int wfRecLen;           assign wfRecLen to "{P}{R}wf.NELM";

monitor wfDelay;

int ii;
int nPVs;
int isTruncated;
string stmp;
string stub;
string prefix;

ss waveform {

  state start {

    entry {
      wfLen=0;
      isTruncated=0;
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
      sprintf(msg,"Assigning PVs");
      pvPut(msg);
      pvPut(wfLen);
      pvGet(filename);
      pvGet(wfRecLen);
      if (wfRecLen > MAXLEN) {
        printf("\n%s - WARNING:  %swf.NELM is greater than sequencer's MAXLEN\n",stub,prefix);
      }
      printf("\n%s - Opening file:  %s\n",stub,filename);
#ifdef VXWORKS
			file = open(filename,O_RDONLY);
#else
      file = fopen(filename,"r");
#endif
      if (!file) {
        sprintf(msg,"Error Reading %s",filename);
        pvPut(msg);
        printf("\n%s - %s\n",stub,msg);
      }
      else {
        while ((fscanf(file,"%s",stmp))==1) {
          if (wfLen >= wfRecLen) {
            sprintf(msg,"#PVs > NELM.  Truncating.");
            pvPut(msg);
            printf("\n%s - %s\n",stub,msg);
            isTruncated=1;
            break;
          }
          else if (wfLen >= MAXLEN) {
            sprintf(msg,"#PVs > MAXLEN.  Truncating.");
            pvPut(msg);
            printf("\n%s - %s\n",stub,msg);
            isTruncated=1;
            break;
          }
          pvAssign(wfIn[wfLen],stmp);
          pvMonitor(wfIn[wfLen]);
          sprintf(wfNames[wfLen],"%s",stmp);
          wfLen++;
        }
        fclose(file);
      }
      pvPut(wfLen);
      pvPut(wfNames);
      nPVs += wfLen;
    } state wait

  }

  state wait {

    when (wfLen <= 0) {
      sprintf(msg,"Zero PVs Read from %s",filename);
      pvPut(msg);
      printf("\n%s - %s - EXITING SEQUENCER\n",stub,msg);
    } exit
    
    when (pvConnectCount() < nPVs) {
      sprintf(msg,"Waiting for PVs (%d/%d)",pvConnectCount(),nPVs);
      pvPut(msg);
      printf("\n%s - %s\n",stub,msg);
      epicsThreadSleep(1);
    } state wait
    
    when () {} state run
  }
 

  state run {
  
    entry { 
      if (isTruncated) sprintf(msg,"OK - Running Truncated");
      else             sprintf(msg,"OK - Running");
      pvPut(msg);
      printf("\n%s - %s\n",stub,msg);
    }

    when (pvConnectCount() < nPVs) {} state wait

    when (delay(wfDelay)) {
      for (ii=0; ii<wfLen; ii++) wfOut[ii]=wfIn[ii];
      pvPut(wfOut);
    } state run

  }

}


