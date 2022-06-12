program sums

option -c;
option -r;

// update period (seconds): 
int delay=1;
int itmp;
string stmp;
float summed[32]; assign summed to {};
float rates[32]; assign rates to {};
float ratespre[32]; assign ratespre to {};
float sum; assign sum to "B_DAQ_GTTrigBit:sum";
float sumpre; assign sumpre to "B_DAQ_GTTrigBitPrescaled:sum";

ss sums {

  state start { 
    when () { 
      printf("** sums:  start state **************************\n");
      for (itmp=0; itmp<32; itmp++) {
          sprintf(stmp,"B_DAQ:TriggerFlag:%.2d:sum",itmp);
          pvAssign(summed[itmp],stmp);
          sprintf(stmp,"B_DAQ_GTTrigBit:%d",itmp);
          pvAssign(rates[itmp],stmp);
          sprintf(stmp,"B_DAQ:trig1ts_TRIGGERBITS:%d",itmp);
          pvAssign(ratespre[itmp],stmp);
      }
    } state init
  }

  state init {
    entry {
      printf("** sums:  init state ****************************\n");
    }
    when (pvConnectCount() < pvChannelCount()) {
      printf("Waiting for PVs (%d/%d)\n",pvConnectCount(),pvChannelCount());
      epicsThreadSleep(2);
    } state init
    when () {} state run
  }

  state run {
    entry {
      printf("** sums:  run state ****************************\n");
    }

    when (pvConnectCount() < pvChannelCount()) {} state init

    when () {
        sum=0;
        sumpre=0;
        for (itmp=0; itmp<32; itmp++) {
            pvGet(summed[itmp]);
            if (summed[itmp] != 0) { 
                pvGet(rates[itmp]);
                sum += rates[itmp];
                pvGet(ratespre[itmp]);
                sumpre += ratespre[itmp];
            }
        }
        pvPut(sum);
        pvPut(sumpre);
      
      epicsThreadSleep(delay);
    } state run
  }

}


