program stage2bits

option -c;
option -r;

// update period (seconds): 
int delay=1;

float i1[8]; assign i1 to "B_DAQ:SSPGT_SEC1_TriggerBits";
float i2[8]; assign i2 to "B_DAQ:SSPGT_SEC2_TriggerBits";
float i3[8]; assign i3 to "B_DAQ:SSPGT_SEC3_TriggerBits";
float i4[8]; assign i4 to "B_DAQ:SSPGT_SEC4_TriggerBits";
float i5[8]; assign i5 to "B_DAQ:SSPGT_SEC5_TriggerBits";
float i6[8]; assign i6 to "B_DAQ:SSPGT_SEC6_TriggerBits";

float o0[6]; assign o0 to "B_DAQ:SSPGT_TrigBit:0";
float o1[6]; assign o1 to "B_DAQ:SSPGT_TrigBit:1";
float o2[6]; assign o2 to "B_DAQ:SSPGT_TrigBit:2";
float o3[6]; assign o3 to "B_DAQ:SSPGT_TrigBit:3";
float o4[6]; assign o4 to "B_DAQ:SSPGT_TrigBit:4";
float o5[6]; assign o5 to "B_DAQ:SSPGT_TrigBit:5";
float o6[6]; assign o6 to "B_DAQ:SSPGT_TrigBit:6";
float o7[6]; assign o7 to "B_DAQ:SSPGT_TrigBit:7";

string msg; assign msg to "B_DAQ:SSPGT_TrigBit:seq:msg";

ss stage2bits {

  state start { 
    when () { 
      printf("** stage2bits:  start state **************************\n");
      pvPut(msg);
    } state init
  }

  state init {
    entry {
      printf("** stage2bits:  init state ****************************\n");
    }
    when (pvConnectCount() < pvChannelCount()) {
      printf("Waiting for PVs (%d/%d)\n",pvConnectCount(),pvChannelCount());
      sprintf(msg,"ERROR - Waiting for PVs (%d/%d)",pvConnectCount(),pvChannelCount());
      pvPut(msg);
      epicsThreadSleep(2);
    } state init
    when () {} state run
  }

  state run {
    entry {
      printf("** stage2bits:  run state ****************************\n");
      sprintf(msg,"OK - Running");
      pvPut(msg);
    }

    when (pvConnectCount() < pvChannelCount()) {} state init

    when () {
      pvGet(i1);
      pvGet(i2);
      pvGet(i3);
      pvGet(i4);
      pvGet(i5);
      pvGet(i6);
	  
      o0[0]=i1[0]; o1[0]=i1[1]; o2[0]=i1[2]; o3[0]=i1[3];
	  o0[1]=i2[0]; o1[1]=i2[1]; o2[1]=i2[2]; o3[1]=i2[3];
	  o0[2]=i3[0]; o1[2]=i3[1]; o2[2]=i3[2]; o3[2]=i3[3];
	  o0[3]=i4[0]; o1[3]=i4[1]; o2[3]=i4[2]; o3[3]=i4[3];
	  o0[4]=i5[0]; o1[4]=i5[1]; o2[4]=i5[2]; o3[4]=i5[3];
	  o0[5]=i6[0]; o1[5]=i6[1]; o2[5]=i6[2]; o3[5]=i6[3];

	  o4[0]=i1[4]; o5[0]=i1[5]; o6[0]=i1[6]; o7[0]=i1[7];
	  o4[1]=i2[4]; o5[1]=i2[5]; o6[1]=i2[6]; o7[1]=i2[7];
	  o4[2]=i3[4]; o5[2]=i3[5]; o6[2]=i3[6]; o7[2]=i3[7];
	  o4[3]=i4[4]; o5[3]=i4[5]; o6[3]=i4[6]; o7[3]=i4[7];
	  o4[4]=i5[4]; o5[4]=i5[5]; o6[4]=i5[6]; o7[4]=i5[7];
	  o4[5]=i6[4]; o5[5]=i6[5]; o6[5]=i6[6]; o7[5]=i6[7];
      
      pvPut(o0);
      pvPut(o1);
      pvPut(o2);
      pvPut(o3);
      pvPut(o4);
      pvPut(o5);
      pvPut(o6);
      pvPut(o7);
      epicsThreadSleep(delay);
    } state run
  }

}


