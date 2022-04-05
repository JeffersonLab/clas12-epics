program srs

// allow sequencer to start before all PVs connected:
option -c;

// make reentrant (required for multiple instances):
option +r;

// run in safe mode:
option +s;

#define NANA 991
#define NHIST 100

#define MESSAGE(MSG) \
    sprintf(msg,#MSG);\
    printf("%s\n",msg);\
    pvPut(msg);

float wf[NANA]; assign wf to "B_HTCC:RGA:anascan:amu:wf";
float wf2[NHIST]; assign wf2 to "B_HTCC:RGA:histscan:amu:wf";
float min; assign min to "B_HTCC:RGA:mass:initial:rbk";
float max; assign max to "B_HTCC:RGA:mass:final:rbk";
string msg; assign msg to "B_HTCC:RGA:seq:status";
int go; assign go to "B_HTCC:RGA:seq:update:axes"; monitor go;
int ii;

ss srs {

  state start {
	  entry {
		  MESSAGE(Initializing...)
	  }
    
	  when (pvConnectCount() < 5) {
		  MESSAGE(Waiting for PVs ...)
		  epicsThreadSleep(1);
	  } state start
	  
	  when () {} state run
  }

  state run {

	entry {
		MESSAGE(Idle)
	}
  
    when (go==1) {
      MESSAGE(Filling axis arrays ...)
      go=0;
      pvPut(go);
      pvGet(min);
      pvGet(max);
      for (ii=0; ii<NANA; ii++) {
          wf[ii] = min + ((float)ii)/(NANA-1)*(max-min);
      }
      for (ii=0; ii<NHIST; ii++) {
          wf2[ii] = min + ((float)ii)/(NHIST-1)*(max-min);
      }
      pvPut(wf);
      pvPut(wf2);
	  MESSAGE(Idle);
    } state run

  }

}


